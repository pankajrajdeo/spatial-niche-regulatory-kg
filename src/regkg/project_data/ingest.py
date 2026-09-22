"""Project-data ingestion: audit every supplied quantitative input and publish one artifact."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import pandas as pd

import regkg
from regkg.config import LoadedProjectConfig, ProjectConfig
from regkg.identifiers import build_gene_table
from regkg.models import (
    BIOLOGICAL_CONTEXTS,
    CELL_TYPES,
    CONTEXTS,
    GENES,
    NEIGHBORHOOD_PROFILES,
    NICHE_EXPRESSION_SIGNATURES,
    NICHE_STATES,
    SAMPLING_COVERAGE,
    SCHEMA_VERSION,
    CheckResult,
    SourceFile,
    StageStatus,
)
from regkg.project_data.chromlinker import read_chromlinker_layout, write_chromlinker_observations
from regkg.project_data.contexts import build_registry
from regkg.project_data.expression import read_expression_layout, write_expression_observations
from regkg.project_data.io import NumericStats, read_header, write_parquet
from regkg.project_data.neighborhood import neighborhood_long, read_neighborhood
from regkg.project_data.niche_expression_signatures import (
    COLUMN_MAP,
    FLOAT_COLUMNS,
    KEY_COLUMNS,
    read_signatures,
    sampling_coverage,
    signature_table,
    validate_signatures,
)
from regkg.project_data.report import render_audit
from regkg.project_data.verify import (
    ROLE_CHROMLINKER,
    ROLE_EXPRESSION,
    ROLE_NEIGHBORHOOD,
    ROLE_SIGNATURES,
    published_integrity,
    table_checks,
)
from regkg.provenance import (
    canonical_json,
    code_fingerprint,
    describe_outputs,
    discard_directory,
    git_revision,
    new_execution_id,
    publish_directory,
    read_json,
    sha256_file,
    sha256_text,
    software_versions,
    stable_id,
    staging_directory,
    utc_now,
    write_json,
)

STAGE = "project_data_ingest"
# Files whose content changes the ingest result; config.py only loads configuration, which is
# fingerprinted separately from its resolved values.
INGEST_CODE_PATHS = ["provenance.py", "models.py", "identifiers.py", "project_data"]
# Settings that change performance or location but not the scientific content of the artifact.
NON_RESULT_CONFIG_FIELDS = {"ingest_chunk_rows", "data_root"}
SOFTWARE = ["pandas", "pyarrow", "numpy", "pydantic", "PyYAML", "python-dotenv"]
EXAMPLE_LIMIT = 20


class IngestError(RuntimeError):
    """Ingestion failed; no artifact was published by this attempt."""


@dataclass(frozen=True)
class Source:
    role: str
    path: Path
    relative: str
    delimiter: str
    sha256: str
    focal_cell_type: str | None = None

    @property
    def source_id(self) -> str:
        return stable_id("source", {"role": self.role, "sha256": self.sha256})


@dataclass
class IngestOutcome:
    status: StageStatus
    ingest_key: str
    artifact_dir: Path
    execution_id: str
    row_counts: dict[str, int] = field(default_factory=dict)
    checks: list[CheckResult] = field(default_factory=list)


def collect_sources(loaded: LoadedProjectConfig) -> list[Source]:
    config = loaded.config

    def source(role: str, relative: Path, delimiter: str, focal: str | None = None) -> Source:
        path = loaded.resolve(relative)
        if not path.is_file():
            raise IngestError(f"source file not found for {role}: {relative}")
        try:
            display = path.resolve().relative_to(loaded.repo_root).as_posix()
        except ValueError:
            display = path.as_posix()
        return Source(role, path, display, delimiter, sha256_file(path), focal)

    sources = [
        source(ROLE_CHROMLINKER, config.chromlinker.path, config.chromlinker.delimiter),
        source(ROLE_EXPRESSION, config.expression.path, config.expression.delimiter),
        source(ROLE_SIGNATURES, config.niche_expression_signatures.path, config.niche_expression_signatures.delimiter),
    ]
    for definition in config.niche_definitions:
        sources.append(
            source(ROLE_NEIGHBORHOOD, definition.neighborhood_path, definition.delimiter, definition.focal_cell_type)
        )
    return sources


def result_config(config: ProjectConfig) -> dict[str, Any]:
    return config.model_dump(mode="json", exclude=NON_RESULT_CONFIG_FIELDS)


def compute_ingest_key(config: ProjectConfig, sources: list[Source], code_hash: str) -> str:
    identity = {
        "stage": STAGE,
        "schema_version": SCHEMA_VERSION,
        "sources": sorted([s.role, s.focal_cell_type or "", s.sha256] for s in sources),
        "config": result_config(config),
        "code": code_hash,
    }
    return f"ingest-{sha256_text(canonical_json(identity))[:16]}"


def run_ingest(loaded: LoadedProjectConfig) -> IngestOutcome:
    """Reuse a verified identical artifact or build, check, and atomically publish a new one."""
    execution_id = new_execution_id("ingest")
    started = utc_now()
    runs_dir = loaded.data_root / "runs" / execution_id
    record: dict[str, Any] = {
        "stage": STAGE,
        "execution_id": execution_id,
        "started_at": started,
        "input_mode": loaded.config.input_mode.value,
        "config_path": _display_path(loaded.config_path, loaded.repo_root),
    }
    try:
        sources = collect_sources(loaded)
        code_hash = code_fingerprint(Path(regkg.__file__).parent, INGEST_CODE_PATHS)
        key = compute_ingest_key(loaded.config, sources, code_hash)
        record["ingest_key"] = key
        final = loaded.data_root / "processed" / key
        if final.exists():
            integrity = published_integrity(final)
            failed = [check for check in integrity if not check.passed]
            if failed:
                raise IngestError(
                    f"existing artifact {key} failed integrity checks and will not be replaced: "
                    + "; ".join(f"{c.name}: {c.detail}" for c in failed)
                )
            outcome = IngestOutcome(StageStatus.REUSED, key, final, execution_id, _row_counts(final), integrity)
        else:
            staging = staging_directory(final, execution_id)
            try:
                row_counts = build_artifact(loaded, sources, key, code_hash, staging, execution_id, started)
                publish_directory(staging, final)
            except BaseException:
                discard_directory(staging)
                raise
            outcome = IngestOutcome(StageStatus.SUCCEEDED, key, final, execution_id, row_counts)
    except Exception as error:
        record.update(status=StageStatus.FAILED.value, ended_at=utc_now(), error=f"{type(error).__name__}: {error}")
        write_json(runs_dir / "execution.json", record)
        raise
    record.update(status=outcome.status.value, ended_at=utc_now(), artifact=_display_path(final, loaded.repo_root))
    write_json(runs_dir / "execution.json", record)
    return outcome


def _display_path(path: Path, root: Path) -> str:
    try:
        return path.resolve().relative_to(root).as_posix()
    except ValueError:
        return path.as_posix()


def _row_counts(artifact_dir: Path) -> dict[str, int]:
    manifest = read_json(artifact_dir / "manifest.json")
    return {output["path"]: output["rows"] for output in manifest["outputs"] if output["rows"] is not None}


def _source_file(
    source: Source,
    columns: list[str],
    n_rows: int,
    key_columns: list[str],
    stats: NumericStats | None,
    fmt: str,
) -> SourceFile:
    return SourceFile(
        source_id=source.source_id,
        role=source.role,
        path=source.relative,
        sha256=source.sha256,
        bytes=source.path.stat().st_size,
        format=fmt,
        delimiter=source.delimiter,
        n_data_rows=n_rows,
        n_columns=len(columns),
        columns=columns,
        key_columns=key_columns,
        duplicate_key_count=0,  # duplicates abort ingestion before this record is written
        nonfinite_value_count=stats.nonfinite if stats else 0,
        numeric_min=stats.minimum if stats else None,
        numeric_max=stats.maximum if stats else None,
        zero_value_count=stats.zeros if stats else None,
    )


def _examples(values: set[str]) -> dict[str, Any]:
    return {"count": len(values), "examples": sorted(values)[:EXAMPLE_LIMIT]}


def build_artifact(
    loaded: LoadedProjectConfig,
    sources: list[Source],
    key: str,
    code_hash: str,
    out: Path,
    execution_id: str,
    started: str,
) -> dict[str, int]:
    config = loaded.config
    by_role = {s.role: s for s in sources if s.role != ROLE_NEIGHBORHOOD}
    neighborhood_sources = {s.focal_cell_type: s for s in sources if s.role == ROLE_NEIGHBORHOOD}
    chromlinker_source, expression_source = by_role[ROLE_CHROMLINKER], by_role[ROLE_EXPRESSION]
    signature_source = by_role[ROLE_SIGNATURES]

    chromlinker = read_chromlinker_layout(chromlinker_source.path, config.chromlinker)
    expression = read_expression_layout(expression_source.path, config.expression)
    signatures_raw = read_signatures(signature_source.path, signature_source.delimiter)
    validate_signatures(signatures_raw, config, signature_source.relative)
    neighborhoods = {
        definition.focal_cell_type: read_neighborhood(
            neighborhood_sources[definition.focal_cell_type].path, definition, config.tolerances.neighborhood_row_sum
        )
        for definition in config.niche_definitions
    }

    signature_groups = set(zip(signatures_raw["cell_type_raw"], signatures_raw["condition"], strict=True))
    registry = build_registry(
        config,
        niche_labels_by_focal_type={focal: table.niche_labels for focal, table in neighborhoods.items()},
        neighborhood_source_ids={focal: s.source_id for focal, s in neighborhood_sources.items()},
        neighbor_categories={c for table in neighborhoods.values() for c in table.neighbor_categories},
        expression_labels=expression.context_labels,
        chromlinker_labels=chromlinker.context_labels,
        signature_groups=signature_groups,
    )
    signature_genes = set(signatures_raw["gene_symbol_raw"])
    genes = build_gene_table(
        config.dataset.species,
        config.dataset.ncbi_taxon_id,
        chromlinker.tfs,
        chromlinker.targets,
        expression.genes,
        signature_genes,
    )
    gene_ids = dict(zip(genes["source_symbol"], genes["gene_id"], strict=True))

    rows: dict[str, int] = {}
    rows["genes.parquet"] = write_parquet(genes, GENES, out / "genes.parquet")
    rows["cell_types.parquet"] = write_parquet(registry.cell_types, CELL_TYPES, out / "cell_types.parquet")
    rows["niche_states.parquet"] = write_parquet(registry.niche_states, NICHE_STATES, out / "niche_states.parquet")
    rows["biological_contexts.parquet"] = write_parquet(
        registry.biological_contexts, BIOLOGICAL_CONTEXTS, out / "biological_contexts.parquet"
    )
    rows["contexts.parquet"] = write_parquet(registry.contexts, CONTEXTS, out / "contexts.parquet")

    neighborhood_frames = [
        neighborhood_long(
            table,
            neighborhood_sources[focal].source_id,
            registry.niche_state_ids,
            registry.definition_run_ids[focal],
            registry.cell_type_ids,
        )
        for focal, table in sorted(neighborhoods.items())
    ]
    rows["neighborhood_profiles.parquet"] = write_parquet(
        pd.concat(neighborhood_frames, ignore_index=True), NEIGHBORHOOD_PROFILES, out / "neighborhood_profiles.parquet"
    )

    signatures = signature_table(
        signatures_raw,
        signature_source.source_id,
        registry.dataset_id,
        registry.cell_type_ids,
        registry.context_ids,
        registry.niche_state_ids,
        gene_ids,
    )
    rows["niche_expression_signatures.parquet"] = write_parquet(
        signatures, NICHE_EXPRESSION_SIGNATURES, out / "niche_expression_signatures.parquet"
    )
    rows["sampling_coverage.parquet"] = write_parquet(
        sampling_coverage(signatures), SAMPLING_COVERAGE, out / "sampling_coverage.parquet"
    )

    lookup = registry.label_lookup()
    chromlinker_stats = write_chromlinker_observations(
        chromlinker_source.path,
        config.chromlinker,
        chromlinker,
        chromlinker_source.source_id,
        lookup,
        gene_ids,
        out / "chromlinker_observations.parquet",
        config.ingest_chunk_rows,
    )
    rows["chromlinker_observations.parquet"] = chromlinker_stats.values
    expression_stats = write_expression_observations(
        expression_source.path,
        config.expression,
        expression,
        expression_source.source_id,
        lookup,
        gene_ids,
        out / "expression_observations.parquet",
        config.ingest_chunk_rows,
    )
    rows["expression_observations.parquet"] = expression_stats.values

    signature_stats = NumericStats()
    signature_stats.update(signatures_raw[[COLUMN_MAP[column] for column in FLOAT_COLUMNS]])
    inventory = [
        _source_file(
            chromlinker_source,
            [config.chromlinker.tf_column, config.chromlinker.target_column, *chromlinker.context_labels],
            chromlinker.n_rows,
            [config.chromlinker.tf_column, config.chromlinker.target_column],
            chromlinker_stats,
            "csv",
        ),
        _source_file(
            expression_source,
            [config.expression.gene_column, *expression.context_labels],
            expression.n_rows,
            [config.expression.gene_column],
            expression_stats,
            "tsv",
        ),
        _source_file(
            signature_source,
            read_header(signature_source.path, signature_source.delimiter),
            len(signatures_raw),
            KEY_COLUMNS,
            signature_stats,
            "tsv",
        ),
    ]
    for focal, table in sorted(neighborhoods.items()):
        stats = NumericStats()
        stats.update(table.wide[table.neighbor_categories])
        inventory.append(
            _source_file(
                neighborhood_sources[focal],
                [table.definition.niche_column, *table.neighbor_categories],
                len(table.wide),
                [table.definition.niche_column],
                stats,
                "tsv",
            )
        )
    inventory_record = {
        "dataset_id": registry.dataset_id,
        "dataset_name": config.dataset.name,
        "sources": [source.model_dump(mode="json") for source in inventory],
    }
    write_json(out / "source_inventory.json", inventory_record)

    join_report = build_join_report(
        config, registry, genes, chromlinker, expression, signatures, neighborhoods, chromlinker_stats
    )
    write_json(out / "join_report.json", join_report)
    (out / "source_audit.md").write_text(render_audit(inventory_record, join_report, rows), encoding="utf-8")

    checks = table_checks(out, config)
    failed = [check for check in checks if not check.passed]
    if failed:
        raise IngestError("pre-publication checks failed: " + "; ".join(f"{c.name}: {c.detail}" for c in failed))

    manifest = {
        "stage": STAGE,
        "schema_version": SCHEMA_VERSION,
        "ingest_key": key,
        "status": StageStatus.SUCCEEDED.value,
        "execution_id": execution_id,
        "started_at": started,
        "ended_at": utc_now(),
        "input_mode": config.input_mode.value,
        "dataset": {"dataset_id": registry.dataset_id, "name": config.dataset.name},
        "inputs": [
            {
                "source_id": s.source_id,
                "role": s.role,
                "path": s.relative,
                "sha256": s.sha256,
                "focal_cell_type": s.focal_cell_type,
            }
            for s in sources
        ],
        "config": {
            "path": _display_path(loaded.config_path, loaded.repo_root),
            "fingerprint": sha256_text(canonical_json(result_config(config))),
            "resolved": config.model_dump(mode="json"),
        },
        "code": {"fingerprint": code_hash, "paths": INGEST_CODE_PATHS, "git": git_revision(loaded.repo_root)},
        "software": software_versions(SOFTWARE),
        "checks": [check.model_dump() for check in checks],
        "outputs": describe_outputs(out, rows),
        "error": None,
    }
    write_json(out / "manifest.json", manifest)
    return rows


def build_join_report(config, registry, genes, chromlinker, expression, signatures, neighborhoods, chromlinker_stats):
    tf_set, target_set, expr_set = chromlinker.tfs, chromlinker.targets, expression.genes
    signature_set = set(signatures["gene_symbol_raw"])
    contexts = registry.contexts
    niche_contexts = contexts[contexts["niche_label"].notna()]

    scope = config.at1_scope.cell_type
    scope_labels = [label for label in chromlinker.context_labels if registry.labels[label].cell_type_raw == scope]
    scope_values = sum(chromlinker_stats.values_by_column[label] for label in scope_labels)
    scope_nonzero = sum(chromlinker_stats.nonzero_by_column[label] for label in scope_labels)

    expression_labels, chromlinker_labels = set(expression.context_labels), set(chromlinker.context_labels)
    groups = []
    for group in signatures.drop_duplicates("comparison_id").itertuples(index=False):
        niche_labels = [f"{group.condition}.{group.cell_type_raw}_{n}" for n in ("niche_1", "niche_2")]
        groups.append(
            {
                "cell_type": group.cell_type_raw,
                "condition": group.condition,
                "comparison": group.comparison_raw,
                "comparison_id": group.comparison_id,
                "n_genes": int((signatures["comparison_id"] == group.comparison_id).sum()),
                "n_cells_niche1": int(group.n_cells_niche1),
                "n_cells_niche2": int(group.n_cells_niche2),
                "expression_has_both_niche_contexts": all(label in expression_labels for label in niche_labels),
                "chromlinker_has_both_niche_contexts": all(label in chromlinker_labels for label in niche_labels),
            }
        )

    all_categories = sorted({c for table in neighborhoods.values() for c in table.neighbor_categories})
    variants = genes[genes["suffix_variant_base_symbol"].notna()]
    return {
        "contexts": {
            "expression_labels": len(expression.context_labels),
            "chromlinker_labels": len(chromlinker.context_labels),
            "chromlinker_labels_absent_from_expression": sorted(chromlinker_labels - expression_labels),
            "expression_labels_absent_from_chromlinker": sorted(expression_labels - chromlinker_labels),
            "niche_specific_labels": {
                "expression": int(niche_contexts["in_expression"].sum()),
                "chromlinker": int(niche_contexts["in_chromlinker"].sum()),
            },
            "niche_labels_absent_from_chromlinker": sorted(
                niche_contexts.loc[~niche_contexts["in_chromlinker"], "context_label_raw"]
            ),
            "biological_contexts": len(registry.biological_contexts),
            "cell_types": len(registry.cell_types),
            "niche_states": len(registry.niche_states),
            "definition_runs": len(registry.definition_run_ids),
            "unobserved_configured_cell_types": registry.unobserved_configured_cell_types,
        },
        "scope_chromlinker": {
            "cell_type": scope,
            "contexts": scope_labels,
            "values": scope_values,
            "nonzero_values": scope_nonzero,
            "note": "arithmetic count only; nonzero is not an edge-validity rule while score semantics are unconfirmed",
        },
        "signature_groups": groups,
        "genes": {
            "total_source_symbols": len(genes),
            "chromlinker_tfs": len(tf_set),
            "chromlinker_targets": len(target_set),
            "chromlinker_tfs_also_targets": len(tf_set & target_set),
            "expression": len(expr_set),
            "niche_signatures": len(signature_set),
            "unmatched": {
                "chromlinker_tfs_not_in_expression": _examples(tf_set - expr_set),
                "chromlinker_targets_not_in_expression": _examples(target_set - expr_set),
                "chromlinker_tfs_not_in_signatures": _examples(tf_set - signature_set),
                "chromlinker_targets_not_in_signatures": _examples(target_set - signature_set),
                "signatures_not_in_expression": _examples(signature_set - expr_set),
                "expression_not_in_signatures": _examples(expr_set - signature_set),
            },
            "suffix_variant_diagnostic": {
                "note": (
                    "symbol resembles a make-unique copy of another symbol in the same source; not merged or resolved"
                ),
                "count": len(variants),
                "symbols": dict(zip(variants["source_symbol"], variants["suffix_variant_base_symbol"], strict=True)),
            },
            "external_id_status": genes["mapping_status"].value_counts().to_dict(),
        },
        "neighborhoods": [
            {
                "focal_cell_type": focal,
                "k_neighbors": table.definition.k_neighbors,
                "clustering_resolution": table.definition.clustering_resolution,
                "niche_labels": table.niche_labels,
                "reported_categories": len(table.neighbor_categories),
                "unreported_categories": sorted(set(all_categories) - set(table.neighbor_categories)),
                "row_sums": [float(v) for v in table.wide[table.neighbor_categories].sum(axis=1)],
            }
            for focal, table in sorted(neighborhoods.items())
        ],
        "scope_tf_seeds": {
            seed: {
                "in_chromlinker_tf": seed in tf_set,
                "in_expression": seed in expr_set,
                "in_niche_signatures": seed in signature_set,
            }
            for seed in config.at1_scope.tf_seeds
        },
    }
