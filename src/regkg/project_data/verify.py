"""Checks of a project-data artifact: integrity, reconciliation with sources, and invariants.

`table_checks` runs on the staging directory before publication and again from
`regkg verify project-data`, so each rule has one implementation.
"""

from __future__ import annotations

from collections.abc import Callable
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd
import pyarrow as pa
import pyarrow.compute as pc
import pyarrow.parquet as pq

from regkg.config import ProjectConfig
from regkg.models import (
    SCHEMA_VERSION,
    TABLE_SCHEMAS,
    CheckResult,
    DonorStatus,
    MappingStatus,
    ScoreSemanticsStatus,
    StageStatus,
)
from regkg.project_data import identities
from regkg.project_data.io import READ_OPTIONS
from regkg.project_data.niche_expression_signatures import COLUMN_MAP, COUNT_COLUMNS, FLOAT_COLUMNS, effect_mismatch
from regkg.provenance import read_json, sha256_file

ROLE_CHROMLINKER = "chromlinker_scores"
ROLE_EXPRESSION = "pseudobulk_expression"
ROLE_SIGNATURES = "niche_expression_signatures"
ROLE_NEIGHBORHOOD = "neighborhood_composition"


class Checks:
    def __init__(self) -> None:
        self.results: list[CheckResult] = []

    def add(self, name: str, passed: bool, detail: str) -> None:
        self.results.append(CheckResult(name=name, passed=bool(passed), detail=detail))

    def run(self, name: str, check: Callable[[], tuple[bool, str]]) -> None:
        """A check that raises is recorded as failed instead of aborting the remaining checks."""
        try:
            passed, detail = check()
        except Exception as error:  # noqa: BLE001 - reported as a failed check with its message
            passed, detail = False, f"check raised {type(error).__name__}: {error}"
        self.add(name, passed, detail)


def _read(artifact_dir: Path, name: str, columns: list[str] | None = None) -> pa.Table:
    return pq.read_table(artifact_dir / name, columns=columns)


def _all(values: pa.ChunkedArray | pa.Array) -> bool:
    return bool(pc.all(values).as_py()) if len(values) else True


def _unique(table: pa.Table, column: str) -> tuple[bool, str]:
    distinct = pc.count_distinct(table[column]).as_py()
    nulls = table[column].null_count
    return distinct == table.num_rows and nulls == 0, f"{distinct}/{table.num_rows} distinct, {nulls} null"


def _subset(values: pa.ChunkedArray, allowed: pa.ChunkedArray) -> tuple[bool, str]:
    missing = pc.sum(pc.invert(pc.is_in(values.drop_null(), value_set=allowed.combine_chunks()))).as_py() or 0
    return missing == 0, f"{missing} unresolved references"


def _identity_check(stored: list[str], recomputed: list[str]) -> tuple[bool, str]:
    mismatched = sum(a != b for a, b in zip(stored, recomputed, strict=True))
    return mismatched == 0, f"{len(stored)} IDs recomputed from their stored assignments; {mismatched} differ"


def _source(inventory: list[dict[str, Any]], role: str) -> list[dict[str, Any]]:
    return [source for source in inventory if source["role"] == role]


def table_checks(artifact_dir: Path, config: ProjectConfig) -> list[CheckResult]:
    checks = Checks()
    inventory = read_json(artifact_dir / "source_inventory.json")["sources"]
    tolerances = config.tolerances

    for name, schema in TABLE_SCHEMAS.items():
        checks.run(
            f"schema:{name}",
            lambda name=name, schema=schema: (
                pq.read_schema(artifact_dir / name).remove_metadata().equals(schema),
                "matches the declared Arrow schema",
            ),
        )

    genes = _read(artifact_dir, "genes.parquet")
    cell_types = _read(artifact_dir, "cell_types.parquet")
    niche_states = _read(artifact_dir, "niche_states.parquet")
    biological = _read(artifact_dir, "biological_contexts.parquet")
    contexts = _read(artifact_dir, "contexts.parquet")
    for name, table, column in (
        ("genes", genes, "gene_id"),
        ("cell_types", cell_types, "cell_type_id"),
        ("niche_states", niche_states, "niche_state_id"),
        ("biological_contexts", biological, "context_id"),
        ("contexts", contexts, "context_label_raw"),
    ):
        checks.run(f"unique:{name}.{column}", lambda t=table, c=column: _unique(t, c))

    # Gene identity boundary: no invented external IDs; TF status only where the source states it.
    def gene_boundary() -> tuple[bool, str]:
        status_ok = _all(pc.equal(genes["mapping_status"], MappingStatus.UNRESOLVED_EXTERNAL_ID.value))
        external = sum(genes[c].null_count for c in ("approved_symbol", "hgnc_id", "ensembl_gene_id", "ncbi_gene_id"))
        external_ok = external == 4 * genes.num_rows
        tf = genes.to_pandas()[["is_tf", "in_chromlinker_tf"]]
        tf_ok = bool(
            (tf["is_tf"].isna() | tf["in_chromlinker_tf"]).all() and tf.loc[tf["in_chromlinker_tf"], "is_tf"].all()
        )
        return (
            status_ok and external_ok and tf_ok,
            f"{genes.num_rows} genes unresolved; is_tf from ChromLinker TF column only",
        )

    checks.run("genes:unresolved_external_ids", gene_boundary)

    # Niche identity is condition-pooled: one state per (focal type, niche label) and the same
    # state for Control and IPF observations.
    def niche_identity() -> tuple[bool, str]:
        expected = len(config.niche_definitions) * 2
        frame = contexts.to_pandas()
        niche_rows = frame[frame["niche_label"].notna()]
        per_niche = niche_rows.groupby(["cell_type_raw", "niche_label"])["niche_state_id"].nunique()
        null_ok = bool((frame["niche_label"].isna() == frame["niche_state_id"].isna()).all())
        states = niche_states.to_pandas()
        unique_pairs = not states.duplicated(["focal_cell_type", "niche_label"]).any()
        shared = niche_rows.groupby("niche_state_id")["condition_raw"].nunique()
        return (
            niche_states.num_rows == expected and bool((per_niche == 1).all()) and null_ok and unique_pairs,
            f"{niche_states.num_rows} niche states (expected {expected}); "
            f"{int((shared > 1).sum())} shared by >1 condition; non-niche labels have null niche",
        )

    checks.run("niches:condition_pooled_identity", niche_identity)

    # Each semantic ID must equal the identity rule applied to the fields stored beside it.
    def context_identity() -> tuple[bool, str]:
        rows = biological.to_pylist()
        return _identity_check(
            [row["context_id"] for row in rows],
            [
                identities.context_id(
                    row["dataset_id"],
                    row["species"],
                    row["tissue"],
                    row["cell_type_id"],
                    row["condition"],
                    row["disease"],
                    row["model_system"],
                )
                for row in rows
            ],
        )

    def niche_definition_identity() -> tuple[bool, str]:
        rows = niche_states.to_pylist()
        runs = [
            identities.definition_run_id(
                row["dataset_id"],
                row["focal_cell_type"],
                row["k_neighbors"],
                row["clustering_resolution"],
                row["conditions_used_for_clustering"],
                row["definition_method"],
                row["neighborhood_source_id"],
            )
            for row in rows
        ]
        states = [
            identities.niche_state_id(row["dataset_id"], run, row["focal_cell_type_id"], row["niche_label"])
            for row, run in zip(rows, runs, strict=True)
        ]
        return _identity_check(
            [row["definition_run_id"] for row in rows] + [row["niche_state_id"] for row in rows], runs + states
        )

    checks.run("identity:biological_contexts", context_identity)
    checks.run("identity:niche_states", niche_definition_identity)

    def context_overlap() -> tuple[bool, str]:
        frame = contexts.to_pandas()
        missing = frame[frame["in_chromlinker"] & ~frame["in_expression"]]["context_label_raw"].tolist()
        return (
            not missing,
            f"{int(frame['in_chromlinker'].sum())} ChromLinker labels; absent from expression: {missing}",
        )

    checks.run("contexts:chromlinker_in_expression", context_overlap)

    def references(table: pa.Table, columns: dict[str, pa.ChunkedArray]) -> tuple[bool, str]:
        details, ok = [], True
        for column, allowed in columns.items():
            passed, detail = _subset(table[column], allowed)
            ok &= passed
            details.append(f"{column}: {detail}")
        return ok, "; ".join(details)

    def observation_checks(
        name: str, role: str, value_column: str, id_columns: int, gene_columns: list[str]
    ) -> pa.Table:
        source = _source(inventory, role)[0]
        table = _read(artifact_dir, name)
        n_contexts = source["n_columns"] - id_columns
        expected = source["n_data_rows"] * n_contexts
        checks.add(
            f"rows:{name}",
            table.num_rows == expected,
            f"{table.num_rows} rows = {source['n_data_rows']} source rows x {n_contexts} contexts "
            f"(expected {expected})",
        )
        checks.run(f"unique:{name}.observation_id", lambda: _unique(table, "observation_id"))
        values = table[value_column]
        finite = _all(pc.is_finite(values)) and values.null_count == 0
        zeros = pc.sum(pc.equal(values, 0.0)).as_py() or 0
        checks.add(
            f"values:{name}.zeros_preserved",
            finite and zeros == source["zero_value_count"],
            f"{zeros} zero values (source {source['zero_value_count']}); all finite: {finite}",
        )
        checks.run(
            f"refs:{name}",
            lambda: references(
                table,
                {
                    **{column: genes["gene_id"] for column in gene_columns},
                    "context_id": biological["context_id"],
                    "niche_state_id": niche_states["niche_state_id"],
                    "cell_type_id": cell_types["cell_type_id"],
                },
            ),
        )

        def niche_membership() -> tuple[bool, str]:
            pairs = table.group_by(["context_label_raw", "niche_state_id"]).aggregate([]).to_pylist()
            expected_map = dict(
                zip(contexts["context_label_raw"].to_pylist(), contexts["niche_state_id"].to_pylist(), strict=True)
            )
            labels = [pair["context_label_raw"] for pair in pairs]
            consistent = len(set(labels)) == len(labels) and all(
                pair["niche_state_id"] == expected_map[pair["context_label_raw"]] for pair in pairs
            )
            return consistent, f"{len(pairs)} labels; each maps to its context's niche state or null"

        checks.run(f"niches:{name}.membership", niche_membership)

        def observation_identity() -> tuple[bool, str]:
            columns = {
                c: table[c].to_pylist()
                for c in ["source_id", *gene_columns, "context_label_raw", "context_id", "niche_state_id"]
            }
            genes_ = [columns[c] for c in gene_columns]
            if role == ROLE_CHROMLINKER:
                recomputed = [
                    identities.chromlinker_observation_id(*values)
                    for values in zip(
                        columns["source_id"],
                        *genes_,
                        columns["context_label_raw"],
                        columns["context_id"],
                        columns["niche_state_id"],
                        strict=True,
                    )
                ]
            else:
                recomputed = [
                    identities.expression_observation_id(*values)
                    for values in zip(
                        columns["source_id"],
                        *genes_,
                        columns["context_label_raw"],
                        columns["context_id"],
                        columns["niche_state_id"],
                        strict=True,
                    )
                ]
            return _identity_check(table["observation_id"].to_pylist(), recomputed)

        checks.run(f"identity:{name}", observation_identity)
        return table

    chromlinker = observation_checks(
        "chromlinker_observations.parquet", ROLE_CHROMLINKER, "raw_score", 2, ["tf_gene_id", "target_gene_id"]
    )
    checks.add(
        "chromlinker:score_semantics_unconfirmed",
        _all(pc.equal(chromlinker["score_semantics_status"], ScoreSemanticsStatus.UNCONFIRMED.value)),
        "every observation keeps score_semantics_status=unconfirmed; no rank or aggregate columns exist",
    )
    del chromlinker
    expression = observation_checks("expression_observations.parquet", ROLE_EXPRESSION, "value", 1, ["gene_id"])
    checks.add(
        "expression:nonnegative_cptt",
        _all(pc.greater_equal(expression["value"], 0.0)),
        "CPTT values are nonnegative and unmodified",
    )
    del expression

    signatures = _read(artifact_dir, "niche_expression_signatures.parquet").to_pandas()
    source = _source(inventory, ROLE_SIGNATURES)[0]
    checks.add(
        "rows:niche_expression_signatures.parquet",
        len(signatures) == source["n_data_rows"],
        f"{len(signatures)} rows (source {source['n_data_rows']})",
    )
    checks.run(
        "unique:niche_expression_signatures.signature_row_id",
        lambda: (
            signatures["signature_row_id"].is_unique and not signatures.duplicated(["comparison_id", "gene_id"]).any(),
            f"{signatures['signature_row_id'].nunique()} distinct rows; (comparison, gene) unique",
        ),
    )

    def signature_values() -> tuple[bool, str]:
        mismatch = effect_mismatch(
            signatures["mean_expr_niche1"].to_numpy(),
            signatures["mean_expr_niche2"].to_numpy(),
            signatures["effect_niche2_minus_niche1"].to_numpy(),
            tolerances.signature_effect_abs,
            tolerances.signature_effect_rel,
        )
        fractions = signatures[["pct_expr_niche1", "pct_expr_niche2"]].to_numpy()
        counts = signatures[["n_cells_niche1", "n_cells_niche2"]].to_numpy()
        residual = np.abs(
            signatures["effect_niche2_minus_niche1"] - (signatures["mean_expr_niche2"] - signatures["mean_expr_niche1"])
        ).max()
        ok = not mismatch.any() and ((fractions >= 0) & (fractions <= 1)).all() and (counts >= 0).all()
        return ok, f"effect = niche2 - niche1 (max residual {residual:.3g}); fractions in [0,1]; counts >= 0"

    checks.run("signatures:effect_units", signature_values)

    def signature_groups() -> tuple[bool, str]:
        per_group = signatures.groupby("comparison_id")[["n_cells_niche1", "n_cells_niche2"]].nunique()
        expected = {(d.focal_cell_type, c) for d in config.niche_definitions for c in config.dataset.conditions}
        observed = set(zip(signatures["cell_type_raw"], signatures["condition"], strict=True))
        return (
            bool((per_group == 1).all().all()) and observed == expected,
            f"{signatures['comparison_id'].nunique()} comparisons; cell counts constant within each; "
            f"missing groups {sorted(expected - observed)}",
        )

    checks.run("signatures:groups_and_cell_counts", signature_groups)

    def signature_identity() -> tuple[bool, str]:
        groups = signatures.drop_duplicates("comparison_id")
        comparisons = [
            identities.comparison_id(
                config_dataset_id,
                row.cell_type_id,
                row.condition,
                row.context_id,
                row.case_niche_state_id,
                row.reference_niche_state_id,
            )
            for row in groups.itertuples(index=False)
        ]
        rows = [
            identities.signature_row_id(s, c, g)
            for s, c, g in zip(signatures["source_id"], signatures["comparison_id"], signatures["gene_id"], strict=True)
        ]
        return _identity_check(
            groups["comparison_id"].tolist() + signatures["signature_row_id"].tolist(), comparisons + rows
        )

    config_dataset_id = cell_types["dataset_id"][0].as_py()
    checks.run("identity:niche_expression_signatures.parquet", signature_identity)
    checks.run(
        "refs:niche_expression_signatures.parquet",
        lambda: references(
            pa.Table.from_pandas(signatures),
            {
                "gene_id": genes["gene_id"],
                "context_id": biological["context_id"],
                "case_niche_state_id": niche_states["niche_state_id"],
                "reference_niche_state_id": niche_states["niche_state_id"],
            },
        ),
    )

    def sampling() -> tuple[bool, str]:
        frame = _read(artifact_dir, "sampling_coverage.parquet").to_pandas()
        donors_null = frame["n_donors"].isna().all() and (frame["donor_status"] == DonorStatus.NOT_SUPPLIED.value).all()
        groups = signatures.drop_duplicates("comparison_id").set_index("comparison_id")
        counts_ok = all(
            row.n_cells
            == groups.loc[row.comparison_id, "n_cells_niche2" if row.role_in_comparison == "case" else "n_cells_niche1"]
            for row in frame.itertuples()
        )
        return (
            bool(donors_null) and counts_ok and len(frame) == 2 * len(groups),
            f"{len(frame)} niche groups; cell counts match signatures; donor counts null (not supplied)",
        )

    checks.run("sampling:donors_unknown", sampling)

    def neighborhood() -> tuple[bool, str]:
        frame = _read(artifact_dir, "neighborhood_profiles.parquet").to_pandas()
        sources = _source(inventory, ROLE_NEIGHBORHOOD)
        expected = sum(s["n_data_rows"] * (s["n_columns"] - 1) for s in sources)
        sums = frame.groupby("profile_id").agg(total=("mean_neighbor_count", "sum"), k=("k_neighbors", "first"))
        sums_ok = bool((np.abs(sums["total"] - sums["k"]) <= tolerances.neighborhood_row_sum).all())
        fraction_ok = bool(
            np.allclose(
                frame["neighbor_fraction"], frame["mean_neighbor_count"] / frame["k_neighbors"], rtol=0, atol=1e-15
            )
        )
        unique = not frame.duplicated(["profile_id", "neighbor_cell_type_raw"]).any() and frame["entry_id"].is_unique
        refs = frame["neighbor_cell_type_id"].isin(cell_types["cell_type_id"].to_pylist()).all()
        states = frame["niche_state_id"].isin(niche_states["niche_state_id"].to_pylist()).all()
        return (
            len(frame) == expected and sums_ok and fraction_ok and unique and bool(refs) and bool(states),
            f"{len(frame)} reported entries (expected {expected}) in {len(sums)} profiles; counts sum to k; "
            "fraction = count / k; unreported categories have no rows",
        )

    checks.run("neighborhood:profiles", neighborhood)
    return checks.results


def published_integrity(artifact_dir: Path) -> list[CheckResult]:
    """Manifest status and output checksums of a published artifact."""
    checks = Checks()
    manifest_path = artifact_dir / "manifest.json"
    if not manifest_path.is_file():
        checks.add("manifest:present", False, f"missing {manifest_path.name}")
        return checks.results
    manifest = read_json(manifest_path)
    checks.add(
        "manifest:status",
        manifest.get("status") == StageStatus.SUCCEEDED.value and manifest.get("schema_version") == SCHEMA_VERSION,
        f"status {manifest.get('status')}, schema {manifest.get('schema_version')}",
    )
    checks.add(
        "manifest:key",
        manifest.get("ingest_key") == artifact_dir.name,
        f"manifest key {manifest.get('ingest_key')} for directory {artifact_dir.name}",
    )
    listed = {output["path"]: output for output in manifest.get("outputs", [])}
    present = {
        p.relative_to(artifact_dir).as_posix()
        for p in artifact_dir.rglob("*")
        if p.is_file() and p.name != "manifest.json"
    }
    changed = [
        path
        for path, output in listed.items()
        if not (artifact_dir / path).is_file() or sha256_file(artifact_dir / path) != output["sha256"]
    ]
    checks.add(
        "manifest:output_checksums",
        not changed and present == set(listed),
        f"{len(listed)} outputs; changed/missing {changed}; unlisted {sorted(present - set(listed))}",
    )
    return checks.results


def source_integrity(artifact_dir: Path, repo_root: Path) -> list[CheckResult]:
    checks = Checks()
    for source in read_json(artifact_dir / "source_inventory.json")["sources"]:
        path = repo_root / source["path"]
        current = sha256_file(path) if path.is_file() else None
        checks.add(
            f"source_unchanged:{source['path']}",
            current == source["sha256"],
            f"sha256 {source['sha256'][:12]}… {'matches' if current == source['sha256'] else 'CHANGED or missing'}",
        )
    return checks.results


def _exact_floats(texts) -> np.ndarray:
    """Correctly rounded decimal parsing, independent of the pandas converter used at ingest."""
    return np.fromiter((float(text) for text in texts), dtype=np.float64, count=len(texts))


def source_value_checks(artifact_dir: Path, repo_root: Path, config: ProjectConfig) -> list[CheckResult]:
    """Re-read each unchanged source independently and compare every stored value and label exactly."""
    checks = Checks()
    inventory = read_json(artifact_dir / "source_inventory.json")["sources"]
    sources = {s["role"]: s for s in inventory if s["role"] != ROLE_NEIGHBORHOOD}

    def wide(role: str, table_name: str, id_columns: list[str], raw_columns: list[str], value: str):
        source = sources[role]
        frame = pd.read_csv(repo_root / source["path"], sep=source["delimiter"], dtype=str, **READ_OPTIONS)
        contexts = source["columns"][len(id_columns) :]
        stored = _read(artifact_dir, table_name, ["source_row_index", *raw_columns, "context_label_raw", value])
        stored = stored.take(pc.sort_indices(stored, sort_keys=[("source_row_index", "ascending")]))
        expected_values = _exact_floats(frame[contexts].to_numpy(dtype=object).ravel(order="C"))
        same_values = np.array_equal(stored[value].to_numpy(), expected_values)
        same_labels = stored["context_label_raw"].to_pylist() == contexts * len(frame)
        same_symbols = all(
            stored[raw].to_pylist() == np.repeat(frame[column].to_numpy(dtype=object), len(contexts)).tolist()
            for raw, column in zip(raw_columns, id_columns, strict=True)
        )
        return (
            same_values and same_labels and same_symbols,
            f"{len(expected_values)} values, context labels, and symbols identical to an independent source re-read",
        )

    checks.run(
        "source_values:chromlinker_observations.parquet",
        lambda: wide(
            ROLE_CHROMLINKER,
            "chromlinker_observations.parquet",
            [config.chromlinker.tf_column, config.chromlinker.target_column],
            ["tf_symbol_raw", "target_symbol_raw"],
            "raw_score",
        ),
    )
    checks.run(
        "source_values:expression_observations.parquet",
        lambda: wide(
            ROLE_EXPRESSION,
            "expression_observations.parquet",
            [config.expression.gene_column],
            ["gene_symbol_raw"],
            "value",
        ),
    )

    def signatures() -> tuple[bool, str]:
        source = sources[ROLE_SIGNATURES]
        frame = pd.read_csv(repo_root / source["path"], sep=source["delimiter"], dtype=str, **READ_OPTIONS)
        stored = _read(artifact_dir, "niche_expression_signatures.parquet").to_pandas()
        stored = stored.sort_values("source_row_index").reset_index(drop=True)
        mismatched = []
        for raw, normalized in COLUMN_MAP.items():
            if raw in FLOAT_COLUMNS or raw in COUNT_COLUMNS:
                same = np.array_equal(stored[normalized].to_numpy(dtype=np.float64), _exact_floats(frame[raw]))
            else:
                same = stored[normalized].tolist() == frame[raw].tolist()
            if not same:
                mismatched.append(raw)
        return not mismatched and len(stored) == len(
            frame
        ), f"all {len(COLUMN_MAP)} columns identical; mismatched {mismatched}"

    checks.run("source_values:niche_expression_signatures.parquet", signatures)

    def neighborhoods() -> tuple[bool, str]:
        stored = _read(artifact_dir, "neighborhood_profiles.parquet").to_pandas()
        compared = 0
        for definition in config.niche_definitions:
            source = next(
                s
                for s in inventory
                if s["role"] == ROLE_NEIGHBORHOOD and s["path"].endswith(definition.neighborhood_path.name)
            )
            frame = pd.read_csv(repo_root / source["path"], sep=source["delimiter"], dtype=str, **READ_OPTIONS)
            rows = stored[stored["focal_cell_type"] == definition.focal_cell_type]
            for record in frame.to_dict("records"):
                niche = record.pop(definition.niche_column)
                expected = {category: float(value) for category, value in record.items()}
                observed = rows[rows["niche_label"] == niche].set_index("neighbor_cell_type_raw")["mean_neighbor_count"]
                if observed.to_dict() != expected:
                    return False, f"{definition.focal_cell_type} {niche} counts differ from source"
                compared += len(expected)
        return compared == len(stored), f"{compared} neighbor counts identical to source; no extra rows"

    checks.run("source_values:neighborhood_profiles.parquet", neighborhoods)
    return checks.results


def verify_artifact(artifact_dir: Path, repo_root: Path) -> list[CheckResult]:
    results = published_integrity(artifact_dir)
    if not all(result.passed for result in results):
        return results
    manifest = read_json(artifact_dir / "manifest.json")
    config = ProjectConfig.model_validate(manifest["config"]["resolved"])
    sources = source_integrity(artifact_dir, repo_root)
    results += sources + table_checks(artifact_dir, config)
    if all(result.passed for result in sources):
        results += source_value_checks(artifact_dir, repo_root, config)
    return results
