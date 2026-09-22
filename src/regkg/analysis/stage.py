"""The `regkg candidates` stage: build, check, and atomically publish one candidate artifact."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import pandas as pd
import pyarrow.parquet as pq

import regkg
from regkg.analysis import schemas
from regkg.analysis.candidates import project_evidence, resolve_seeds, select_candidates, select_targets
from regkg.analysis.concordance import (
    COMPARISON_VIEW,
    PRIMARY_POLICY,
    SENSITIVITY_POLICY,
    comparison_vectors,
    concordance_table,
)
from regkg.analysis.gene_mapping import RESOLVED, acquire_hgnc, read_hgnc, resolve_symbols
from regkg.analysis.priors import acquire_collectri, parse_collectri, ulm_network
from regkg.analysis.queue import build_queue, query_names
from regkg.analysis.seed_publications import SeedList, seed_publications
from regkg.analysis.verify import artifact_integrity, table_checks
from regkg.config import (
    CandidateGenerationConfig,
    LoadedProjectConfig,
    RetrievalQueueConfig,
    load_candidate_config,
    load_queue_config,
)
from regkg.models import SCHEMA_VERSION as INGEST_SCHEMA_VERSION
from regkg.models import StageStatus
from regkg.project_data.io import write_parquet
from regkg.project_data.verify import published_integrity
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
    staging_directory,
    utc_now,
    write_json,
)
from regkg.resources import Fetcher

STAGE = "candidates"
CODE_PATHS = ["analysis", "resources.py"]
SOFTWARE = ["decoupler", "pandas", "pyarrow", "numpy", "httpx", "pydantic"]


class CandidateStageError(RuntimeError):
    """Candidate generation failed; this attempt published nothing."""


@dataclass(frozen=True)
class StageInputs:
    loaded: LoadedProjectConfig
    candidate_config: CandidateGenerationConfig
    queue_config: RetrievalQueueConfig
    cell_type: str
    ingest_dir: Path
    hgnc: Any
    collectri: Any
    seed_lists: list[SeedList]
    seed_hashes: dict[str, str]


@dataclass
class CandidateOutcome:
    status: StageStatus
    candidate_key: str
    artifact_dir: Path
    execution_id: str
    network_requests: int
    row_counts: dict[str, int] = field(default_factory=dict)


def _relative(path: Path, root: Path) -> str:
    try:
        return path.resolve().relative_to(root).as_posix()
    except ValueError:
        return path.as_posix()


@dataclass(frozen=True)
class SharedResources:
    ingest_dir: Path
    hgnc: Any
    collectri: Any
    seed_lists: list[SeedList]
    seed_hashes: dict[str, str]


def shared_resources(
    loaded: LoadedProjectConfig, ingest_key: str, candidate_config: CandidateGenerationConfig, fetcher: Fetcher
) -> SharedResources:
    """Accepted ingest artifact plus cached HGNC/CollecTRI snapshots and advisor lists."""
    ingest_dir = loaded.data_root / "processed" / ingest_key
    failed = [c for c in published_integrity(ingest_dir) if not c.passed] if ingest_dir.is_dir() else ["missing"]
    if failed:
        raise CandidateStageError(f"ingest artifact {ingest_key} is missing or failed integrity: {failed}")
    if read_json(ingest_dir / "manifest.json")["schema_version"] != INGEST_SCHEMA_VERSION:
        raise CandidateStageError(f"ingest artifact {ingest_key} has a superseded schema version")
    external = loaded.data_root / "external"
    resources = candidate_config.resources
    hgnc = acquire_hgnc(external, resources.hgnc.archive_date, fetcher)
    collectri = acquire_collectri(external, resources.collectri.zenodo_record, resources.collectri.filename, fetcher)
    seed_lists = [
        SeedList(name, loaded.resolve(path), _relative(loaded.resolve(path), loaded.repo_root))
        for name, path in sorted(resources.seed_publication_lists.items())
    ]
    return SharedResources(
        ingest_dir, hgnc, collectri, seed_lists, {seed.relative: sha256_file(seed.path) for seed in seed_lists}
    )


def prepare_inputs(
    loaded: LoadedProjectConfig, ingest_key: str, cell_type: str, ranking: Path, literature: Path, fetcher: Fetcher
) -> StageInputs:
    candidate_config, queue_config = load_candidate_config(ranking), load_queue_config(literature)
    if cell_type not in candidate_config.cell_types or cell_type != loaded.config.at1_scope.cell_type:
        raise CandidateStageError(f"cell type {cell_type!r} is not configured for candidate generation")
    shared = shared_resources(loaded, ingest_key, candidate_config, fetcher)
    return StageInputs(
        loaded,
        candidate_config,
        queue_config,
        cell_type,
        shared.ingest_dir,
        shared.hgnc,
        shared.collectri,
        shared.seed_lists,
        shared.seed_hashes,
    )


def candidate_key(inputs: StageInputs, code_hash: str, decoupler_version: str | None) -> str:
    identity = {
        "stage": STAGE,
        "schema_version": schemas.CANDIDATE_SCHEMA_VERSION,
        "ingest_key": inputs.ingest_dir.name,
        "cell_type": inputs.cell_type,
        "tf_seeds": inputs.loaded.config.at1_scope.tf_seeds,
        "hgnc_sha256": inputs.hgnc.provenance["sha256"],
        "collectri_sha256": inputs.collectri.provenance["sha256"],
        "seed_lists": inputs.seed_hashes,
        "candidate_config": inputs.candidate_config.model_dump(mode="json"),
        "queue_config": inputs.queue_config.model_dump(mode="json"),
        "code": code_hash,
        "decoupler": decoupler_version,
    }
    return f"candidates-{sha256_text(canonical_json(identity))[:16]}"


def run_candidates(
    loaded: LoadedProjectConfig, ingest_key: str, cell_type: str, ranking: Path, literature: Path
) -> CandidateOutcome:
    def plan(fetcher: Fetcher, execution_id: str, started: str):
        inputs = prepare_inputs(loaded, ingest_key, cell_type, ranking, literature, fetcher)
        versions = software_versions(SOFTWARE)
        code_hash = code_fingerprint(Path(regkg.__file__).parent, CODE_PATHS)
        key = candidate_key(inputs, code_hash, versions["decoupler"])

        def build(staging: Path) -> dict[str, int]:
            return build_artifact(inputs, key, code_hash, versions, staging, execution_id, started, fetcher)

        return key, build

    return execute_stage(loaded, "candidates", {"ingest_key": ingest_key, "cell_type": cell_type}, plan)


def execute_stage(
    loaded: LoadedProjectConfig,
    name: str,
    context: dict[str, Any],
    plan,
    schema_version: str = schemas.CANDIDATE_SCHEMA_VERSION,
) -> CandidateOutcome:
    """Record one execution; publish `plan(...) -> (key, build)` atomically or reuse a verified artifact."""
    execution_id = new_execution_id(name)
    fetcher = Fetcher()
    record: dict[str, Any] = {"stage": name, "execution_id": execution_id, "started_at": utc_now(), **context}
    runs = loaded.data_root / "runs" / execution_id
    try:
        key, build = plan(fetcher, execution_id, record["started_at"])
        record["candidate_key"] = key
        final = loaded.data_root / "processed" / key
        if final.exists():
            integrity = artifact_integrity(final, schema_version)
            failed = [c for c in integrity if not c.passed]
            if failed:
                raise CandidateStageError(
                    f"existing artifact {key} failed integrity and will not be replaced: {failed}"
                )
            manifest = read_json(final / "manifest.json")
            rows = {o["path"]: o["rows"] for o in manifest["outputs"] if o["rows"] is not None}
            outcome = CandidateOutcome(StageStatus.REUSED, key, final, execution_id, fetcher.requests, rows)
        else:
            staging = staging_directory(final, execution_id)
            try:
                rows = build(staging)
                publish_directory(staging, final)
            except BaseException:
                discard_directory(staging)
                raise
            outcome = CandidateOutcome(StageStatus.SUCCEEDED, key, final, execution_id, fetcher.requests, rows)
    except Exception as error:
        record.update(
            status=StageStatus.FAILED.value,
            ended_at=utc_now(),
            network_requests=fetcher.requests,
            error=f"{type(error).__name__}: {error}",
        )
        write_json(runs / "execution.json", record)
        raise
    record.update(
        status=outcome.status.value,
        ended_at=utc_now(),
        network_requests=fetcher.requests,
        artifact=_relative(final, loaded.repo_root),
    )
    write_json(runs / "execution.json", record)
    return outcome


def build_artifact(
    inputs: StageInputs,
    key: str,
    code_hash: str,
    versions: dict[str, str | None],
    out: Path,
    execution_id: str,
    started: str,
    fetcher: Fetcher,
) -> dict[str, int]:
    config, queue_config = inputs.candidate_config, inputs.queue_config
    ingest = inputs.ingest_dir
    shared = shared_tables(inputs, config)
    hgnc, genes, mappings = shared.hgnc, shared.genes, shared.mappings
    publications, publication_conflicts = shared.publications, shared.publication_conflicts
    parsed, priors, sensitivity_frame = shared.parsed, shared.priors, shared.sensitivity

    signatures = pd.read_parquet(ingest / "niche_expression_signatures.parquet")
    vectors = comparison_vectors(signatures, mappings, inputs.cell_type)
    if not vectors:
        raise CandidateStageError(f"no niche-expression comparisons for {inputs.cell_type}")
    gene_of_symbol = mappings[mappings["mapping_status"].isin(RESOLVED)].set_index("approved_symbol")["gene_id"]
    effect_definition = signatures["effect_definition"].iloc[0]
    comparisons = pd.DataFrame(
        [
            {
                "comparison_id": v.comparison_id,
                "cell_type": inputs.cell_type,
                "condition": v.condition,
                "case_niche_state_id": v.case_niche_state_id,
                "reference_niche_state_id": v.reference_niche_state_id,
                "comparison_view": COMPARISON_VIEW,
                "effect_definition": effect_definition,
                **v.coverage,
            }
            for v in vectors
        ]
    )
    vector_rows = pd.concat(
        [
            pd.DataFrame(
                {
                    "comparison_id": v.comparison_id,
                    "approved_symbol": v.values.index,
                    "gene_id": v.values.index.map(gene_of_symbol),
                    "effect_niche2_minus_niche1": v.values.to_numpy(),
                }
            )
            for v in vectors
        ],
        ignore_index=True,
    )

    concordance = both_policies(vectors, shared, config, versions["decoupler"])
    primary = concordance[concordance["sign_policy"] == PRIMARY_POLICY]

    seeds = resolve_seeds(inputs.loaded.config.at1_scope.tf_seeds, mappings)
    selected = select_candidates(comparisons, primary, seeds, config.extra_tfs_per_comparison, config.rule_version)

    resolved = mappings[mappings["mapping_status"].isin(RESOLVED)]
    tf_genes = sorted(resolved.loc[resolved["hgnc_id"].isin(selected["tf_hgnc_id"]), "gene_id"])
    chromlinker = pq.read_table(
        ingest / "chromlinker_observations.parquet", filters=[("tf_gene_id", "in", tf_genes)]
    ).to_pandas()
    expression = pq.read_table(
        ingest / "expression_observations.parquet", filters=[("gene_id", "in", tf_genes)]
    ).to_pandas()
    contexts = pd.read_parquet(ingest / "contexts.parquet")
    evidence, candidate_observations = project_evidence(
        selected, mappings, contexts, chromlinker, expression, signatures
    )
    candidates = selected.merge(evidence, on="candidate_id", how="left", validate="one_to_one")
    targets = select_targets(
        selected, evidence, priors, mappings, chromlinker, signatures, config.targets_per_candidate
    )

    names = query_names(
        set(selected["tf_hgnc_id"]) | set(targets.get("target_hgnc_id", [])), hgnc, queue_config.max_aliases_per_gene
    )
    queue = build_queue(selected, targets, names, queue_config)

    rows = {}
    for name, frame in (
        ("gene_mappings.parquet", mappings),
        ("seed_publications.parquet", publications),
        ("prior_interactions.parquet", priors),
        ("comparisons.parquet", comparisons),
        ("comparison_vectors.parquet", vector_rows),
        ("concordance.parquet", concordance),
        ("candidates.parquet", candidates),
        ("candidate_chromlinker_observations.parquet", candidate_observations),
        ("candidate_targets.parquet", targets),
        ("retrieval_queue.parquet", queue),
    ):
        rows[name] = write_parquet(frame[schemas.TABLE_SCHEMAS[name].names], schemas.TABLE_SCHEMAS[name], out / name)

    resources = resource_record(inputs, inputs.loaded, fetcher)
    write_json(out / "resources.json", resources)
    coverage = coverage_report(
        mappings,
        genes,
        parsed,
        priors,
        sensitivity_frame,
        comparisons,
        concordance,
        candidates,
        targets,
        queue,
        publications,
        publication_conflicts,
        queue_config,
    )
    write_json(out / "coverage_report.json", coverage)

    checks = table_checks(
        out,
        inputs.ingest_dir,
        inputs.loaded.repo_root,
        config,
        queue_config,
        inputs.loaded.config.at1_scope.tf_seeds,
        inputs.hgnc.path,
    )
    failed = [c for c in checks if not c.passed]
    if failed:
        raise CandidateStageError(
            "pre-publication checks failed: " + "; ".join(f"{c.name}: {c.detail}" for c in failed)
        )
    manifest = {
        "stage": STAGE,
        "schema_version": schemas.CANDIDATE_SCHEMA_VERSION,
        "candidate_key": key,
        "status": StageStatus.SUCCEEDED.value,
        "execution_id": execution_id,
        "started_at": started,
        "ended_at": utc_now(),
        "input_mode": inputs.loaded.config.input_mode.value,
        "cell_type": inputs.cell_type,
        "inputs": {"ingest_key": inputs.ingest_dir.name, "resources": resources},
        "config": {
            "candidate_generation": config.model_dump(mode="json"),
            "retrieval_queue": queue_config.model_dump(mode="json"),
            "tf_seeds": inputs.loaded.config.at1_scope.tf_seeds,
        },
        "code": {"fingerprint": code_hash, "paths": CODE_PATHS, "git": git_revision(inputs.loaded.repo_root)},
        "software": versions,
        "checks": [c.model_dump() for c in checks],
        "outputs": describe_outputs(out, rows),
        "error": None,
    }
    write_json(out / "manifest.json", manifest)
    return rows


@dataclass(frozen=True)
class SharedTables:
    hgnc: pd.DataFrame
    genes: pd.DataFrame
    mappings: pd.DataFrame
    publications: pd.DataFrame
    publication_conflicts: Any
    parsed: pd.DataFrame
    priors: pd.DataFrame
    primary_net: pd.DataFrame
    sensitivity: pd.DataFrame
    sensitivity_net: pd.DataFrame


def shared_tables(resources, config: CandidateGenerationConfig) -> SharedTables:
    """Gene mapping, advisor metadata, and CollecTRI networks: identical for every scope."""
    hgnc = read_hgnc(resources.hgnc.path)
    genes = pd.read_parquet(resources.ingest_dir / "genes.parquet")
    mappings = resolve_symbols(genes, hgnc, config.resources.hgnc.archive_date)
    publications, conflicts = seed_publications(resources.seed_lists)
    parsed = parse_collectri(resources.collectri, hgnc, config.resources.collectri.complex_regulators)
    priors, primary_net = ulm_network(parsed, config.concordance.primary_sign_bases)
    sensitivity, sensitivity_net = ulm_network(parsed, config.concordance.sensitivity_sign_bases)
    return SharedTables(
        hgnc, genes, mappings, publications, conflicts, parsed, priors, primary_net, sensitivity, sensitivity_net
    )


def both_policies(vectors, shared: SharedTables, config: CandidateGenerationConfig, decoupler_version) -> pd.DataFrame:
    tmin = config.concordance.min_targets
    return pd.concat(
        [
            concordance_table(
                vectors, shared.primary_net, regulator_info(shared.priors), tmin, PRIMARY_POLICY, decoupler_version
            ),
            concordance_table(
                vectors,
                shared.sensitivity_net,
                regulator_info(shared.sensitivity),
                tmin,
                SENSITIVITY_POLICY,
                decoupler_version,
            ),
        ],
        ignore_index=True,
    )


def resource_record(resources, loaded: LoadedProjectConfig, fetcher: Fetcher) -> dict[str, Any]:
    return {
        "hgnc": {**resources.hgnc.provenance, "path": _relative(resources.hgnc.path, loaded.repo_root)},
        "collectri": {**resources.collectri.provenance, "path": _relative(resources.collectri.path, loaded.repo_root)},
        "seed_publication_lists": resources.seed_hashes,
        "network_requests_this_execution": fetcher.requests,
    }


def regulator_info(frame: pd.DataFrame) -> pd.DataFrame:
    return frame.drop_duplicates("regulator_key").dropna(subset=["regulator_key"]).set_index("regulator_key")


def coverage_report(
    mappings,
    genes,
    parsed,
    priors,
    sensitivity,
    comparisons,
    concordance,
    candidates,
    targets,
    queue,
    publications,
    publication_conflicts,
    queue_config,
) -> dict[str, Any]:
    def counts(series: pd.Series) -> dict[str, int]:
        return {str(k): int(v) for k, v in series.value_counts(dropna=False).sort_index().items()}

    by_source = {
        name: counts(mappings.loc[mappings["gene_id"].isin(genes.loc[genes[flag], "gene_id"]), "mapping_status"])
        for name, flag in (
            ("chromlinker_tf", "in_chromlinker_tf"),
            ("chromlinker_target", "in_chromlinker_target"),
            ("expression", "in_expression"),
            ("niche_signatures", "in_niche_signatures"),
        )
    }
    per_comparison = []
    for comparison in comparisons.itertuples(index=False):
        rows = candidates[candidates["comparison_id"] == comparison.comparison_id]
        per_comparison.append(
            {
                "comparison_id": comparison.comparison_id,
                "condition": comparison.condition,
                "candidates": len(rows),
                "seeds": int(rows["is_seed"].sum()),
                "concordance_extras": int((~rows["is_seed"]).sum()),
                "seeds_also_top_concordance": int(
                    rows.apply(lambda r: r["is_seed"] and len(r["reasons"]) > 1, axis=1).sum()
                ),
                "eligible_regulators_primary": int(
                    concordance[
                        (concordance["comparison_id"] == comparison.comparison_id)
                        & (concordance["sign_policy"] == PRIMARY_POLICY)
                    ]["eligible"].sum()
                ),
                "candidates_with_targets": int(
                    targets[targets["comparison_id"] == comparison.comparison_id]["candidate_id"].nunique()
                ),
            }
        )
    return {
        "gene_mapping": {
            "total_local_genes": len(mappings),
            "status": counts(mappings["mapping_status"]),
            "by_source_role": by_source,
            "ambiguous": mappings.loc[
                mappings["mapping_status"] == "ambiguous", ["source_symbol", "candidate_hgnc_ids"]
            ]
            .assign(candidate_hgnc_ids=lambda f: f["candidate_hgnc_ids"].map(list))
            .to_dict("records"),
            "conflicts": int((mappings["mapping_status"] == "conflict_shared_hgnc_id").sum()),
            "unresolved_examples": sorted(mappings.loc[mappings["mapping_status"] == "unresolved", "source_symbol"])[
                :25
            ],
        },
        "prior": {
            "records": len(parsed),
            "regulators": int(parsed["regulator_symbol_raw"].nunique()),
            "complex_records": counts(parsed.loc[parsed["regulator_type"] == "complex", "regulator_symbol_raw"]),
            "sign": counts(parsed["sign"]),
            "sign_basis": counts(parsed["sign_basis"]),
            "records_without_references": int(
                (parsed["pmids"].map(len) + parsed["other_references"].map(len) == 0).sum()
            ),
            "pairs_with_multiple_records": int((parsed["pair_record_count"] > 1).sum()),
            "pairs_with_contradictory_signs": int(parsed["pair_signs_disagree"].sum()),
            "target_mapping_status": counts(parsed["target_mapping_status"]),
            "primary_ulm_exclusions": counts(priors["ulm_exclusion_reason"].fillna("used")),
            "sensitivity_ulm_exclusions": counts(sensitivity["ulm_exclusion_reason"].fillna("used")),
        },
        "comparisons": comparisons.to_dict("records"),
        "candidates_per_comparison": per_comparison,
        "unique_candidate_tfs": int(candidates["tf_hgnc_id"].nunique()),
        "queue": {
            "queries": len(queue),
            "by_type": counts(queue["query_type"]),
            "initial_live_slice": int(queue["in_initial_live_slice"].sum()),
            "tfs_in_initial_slice": int(queue.loc[queue["in_initial_live_slice"], "tf_hgnc_id"].nunique()),
            "search_status": counts(queue["search_status"]),
            "max_live_queries": queue_config.max_live_queries,
        },
        "seed_publications": {
            "unique_pmids": len(publications),
            "memberships": int(publications["memberships"].map(len).sum()),
            "in_multiple_lists": int((publications["resources"].map(len) > 1).sum()),
            "metadata_conflicts": publication_conflicts,
        },
        "notes": [
            "ULM concordance relates signed curated prior weights to a descriptive pooled contrast; "
            "it is not TF activity, causal regulation, or sample-aware DE.",
            "ChromLinker connectivity rank and interpreted delta are unavailable while score semantics "
            "are unconfirmed.",
            "Seed publications are metadata for retrieval, not accepted findings.",
            "Candidate regulators are individual-gene CollecTRI regulators, which include co-regulators and "
            "general transcription factors; a candidate entry or ULM score does not establish DNA binding.",
            f"Primary sign policy '{PRIMARY_POLICY}' is a project analysis choice excluding CollecTRI "
            "default-activation weights; regulon-inferred signs are not edge-specific experimental evidence. "
            f"'{SENSITIVITY_POLICY}' uses all CollecTRI-assigned weights. Small target sets warrant caution.",
        ],
    }
