"""Behavioral checks of project-data ingestion on synthetic inputs (engineering only)."""

from __future__ import annotations

import json
import re
from pathlib import Path

import pandas as pd
import pytest

from regkg.config import load_project_config
from regkg.models import TABLE_SCHEMAS, StageStatus
from regkg.project_data.contexts import parse_context_label
from regkg.project_data.ingest import IngestError, run_ingest
from regkg.project_data.io import SourceDataError
from regkg.project_data.verify import verify_artifact
from tests.conftest import CHROMLINKER_CONTEXTS, CHROMLINKER_ROWS, EXPRESSION_CONTEXTS, EXPRESSION_GENES


def ingest(config_path: Path):
    return run_ingest(load_project_config(config_path, repo_root=config_path.parents[1]))


def table(outcome, name: str) -> pd.DataFrame:
    return pd.read_parquet(outcome.artifact_dir / name)


def edit(path: Path, old: str, new: str) -> None:
    text = path.read_text(encoding="utf-8")
    assert old in text
    path.write_text(text.replace(old, new, 1), encoding="utf-8")


@pytest.mark.parametrize(
    ("label", "condition", "cell_type", "niche"),
    [
        ("IPF.Activated_Fibrotic_FBs_niche_2", "IPF", "Activated_Fibrotic_FBs", "niche_2"),
        ("Control.AT2", "Control", "AT2", None),
        ("IPF.Proliferating_NK_NKT", "IPF", "Proliferating_NK_NKT", None),
        ("IPF.KRT5neg_KRT17pos_niche_10", "IPF", "KRT5neg_KRT17pos", "niche_10"),
        ("IPF.Odd_niche_label", "IPF", "Odd_niche_label", None),  # suffix is not niche_<integer>
        ("IPF.Type.with.dots", "IPF", "Type.with.dots", None),  # only the first period splits
    ],
)
def test_context_labels_split_at_first_period_and_anchored_niche_suffix(label, condition, cell_type, niche):
    parsed = parse_context_label(label)
    assert (parsed.condition_raw, parsed.cell_type_raw, parsed.niche_label) == (condition, cell_type, niche)


@pytest.mark.parametrize("label", ["AT1_niche_1", ".AT1", "IPF."])
def test_context_label_without_condition_is_rejected(label):
    with pytest.raises(SourceDataError):
        parse_context_label(label)


def test_ingest_preserves_every_value_and_verifies(synthetic_project):
    outcome = ingest(synthetic_project)
    assert outcome.status is StageStatus.SUCCEEDED
    results = verify_artifact(outcome.artifact_dir, synthetic_project.parents[1])
    assert [r for r in results if not r.passed] == []

    chromlinker = table(outcome, "chromlinker_observations.parquet")
    assert len(chromlinker) == len(CHROMLINKER_ROWS) * len(CHROMLINKER_CONTEXTS)
    expected_zeros = sum(value == 0 for _, _, values in CHROMLINKER_ROWS for value in values)
    assert (chromlinker["raw_score"] == 0).sum() == expected_zeros  # zeros kept, not filtered
    assert set(chromlinker["score_semantics_status"]) == {"unconfirmed"}
    assert len(table(outcome, "expression_observations.parquet")) == len(EXPRESSION_GENES) * len(EXPRESSION_CONTEXTS)
    manifest = json.loads((outcome.artifact_dir / "manifest.json").read_text())
    assert manifest["input_mode"] == "fixture"


def test_niche_identity_is_shared_across_conditions_and_null_for_non_niche(synthetic_project):
    outcome = ingest(synthetic_project)
    contexts = table(outcome, "contexts.parquet").set_index("context_label_raw")
    assert contexts.loc["Control.AT1_niche_1", "niche_state_id"] == contexts.loc["IPF.AT1_niche_1", "niche_state_id"]
    assert (
        contexts.loc["Control.AT1_niche_1", "niche_state_id"] != contexts.loc["Control.AT1_niche_2", "niche_state_id"]
    )
    assert contexts.loc["Control.AT1_niche_1", "context_id"] != contexts.loc["IPF.AT1_niche_1", "context_id"]
    assert pd.isna(contexts.loc["Control.AT2", "niche_state_id"])
    # Two focal types x two niches; Control/IPF must not double the count.
    assert len(table(outcome, "niche_states.parquet")) == 4

    biological = table(outcome, "biological_contexts.parquet").set_index(["cell_type", "condition"])
    assert pd.isna(biological.loc[("AT1", "Control"), "disease"])
    assert biological.loc[("AT1", "Control"), "disease_status"] == "not_specified"

    expression = table(outcome, "expression_observations.parquet")
    at2 = expression[expression["context_label_raw"] == "Control.AT2"]
    assert at2["niche_state_id"].isna().all()


def test_unreported_neighbor_category_is_not_zero_filled(synthetic_project):
    outcome = ingest(synthetic_project)
    profiles = table(outcome, "neighborhood_profiles.parquet")
    fibroblast = profiles[profiles["focal_cell_type"] == "Activated_Fibrotic_FBs"]
    assert "Proliferating_NK_NKT" not in set(fibroblast["neighbor_cell_type_raw"])
    at1 = profiles[profiles["focal_cell_type"] == "AT1"]
    measured_zero = at1[(at1["niche_label"] == "niche_2") & (at1["neighbor_cell_type_raw"] == "Proliferating_NK_NKT")]
    assert measured_zero["mean_neighbor_count"].tolist() == [0.0]  # a supplied zero stays a measured zero
    assert (profiles["neighbor_fraction"] == profiles["mean_neighbor_count"] / 25).all()
    report = json.loads((outcome.artifact_dir / "join_report.json").read_text())
    unreported = {n["focal_cell_type"]: n["unreported_categories"] for n in report["neighborhoods"]}
    assert unreported == {"AT1": [], "Activated_Fibrotic_FBs": ["Proliferating_NK_NKT"]}


def test_gene_symbols_are_exact_species_qualified_and_unresolved(synthetic_project):
    outcome = ingest(synthetic_project)
    genes = table(outcome, "genes.parquet").set_index("source_symbol")
    assert "NA" in genes.index  # a symbol named NA is not read as missing
    assert genes.loc["MATR3-1", "gene_id"] != genes.loc["MATR3.1", "gene_id"]  # suffix variants not merged
    assert genes.loc["MATR3.1", "suffix_variant_base_symbol"] == "MATR3"
    assert not genes.loc["SIG_ONLY", "in_expression"] and genes.loc["SIG_ONLY", "in_niche_signatures"]
    assert set(genes["mapping_status"]) == {"unresolved_external_id"}
    assert genes[["hgnc_id", "ensembl_gene_id", "ncbi_gene_id"]].isna().all().all()
    assert genes.loc["TF_A", "is_tf"] and pd.isna(genes.loc["GENE1", "is_tf"])  # unknown, not False
    report = json.loads((outcome.artifact_dir / "join_report.json").read_text())
    assert report["genes"]["unmatched"]["signatures_not_in_expression"]["examples"] == ["MATR3.1", "SIG_ONLY"]


def test_signature_units_effect_and_sampling(synthetic_project):
    outcome = ingest(synthetic_project)
    signatures = table(outcome, "niche_expression_signatures.parquet")
    assert signatures["pct_expr_niche1"].between(0, 1).all()
    assert set(signatures["effect_definition"]) == {"mean log-normalized expression, Niche 2 minus Niche 1"}
    at1 = signatures[signatures["cell_type_raw"] == "AT1"]
    niche_states = table(outcome, "niche_states.parquet").set_index(["focal_cell_type", "niche_label"])
    assert set(at1["case_niche_state_id"]) == {niche_states.loc[("AT1", "niche_2"), "niche_state_id"]}
    assert set(at1["reference_niche_state_id"]) == {niche_states.loc[("AT1", "niche_1"), "niche_state_id"]}
    coverage = table(outcome, "sampling_coverage.parquet")
    assert coverage["n_donors"].isna().all() and set(coverage["donor_status"]) == {"not_supplied"}
    case = coverage[
        (coverage["cell_type"] == "AT1") & (coverage["condition"] == "IPF") & (coverage["role_in_comparison"] == "case")
    ]
    assert case["n_cells"].tolist() == [9]


def test_no_inferential_statistics_columns_exist():
    forbidden = ("p_value", "pvalue", "fdr", "q_value", "log2", "significan", "rank", "deg")
    columns = [name for schema in TABLE_SCHEMAS.values() for name in schema.names]
    assert not [c for c in columns if any(term in c.lower() for term in forbidden)]


@pytest.mark.parametrize(
    ("relative", "old", "new", "message"),
    [
        ("files/signatures.tsv", "\t0.05\t", "\t0.06\t", "effect != mean_niche_2 - mean_niche_1"),
        ("files/signatures.tsv", "\t0.2\t60\t", "\t1.2\t60\t", "fraction in [0, 1]"),
        ("files/signatures.tsv", "\t60\t7\t", "\t60.5\t7\t", "nonnegative integers"),
        ("files/signatures.tsv", "\t60\t7\t", "\t61\t7\t", "cell counts vary"),
        ("files/signatures.tsv", "niche_2_vs_niche_1", "niche_1_vs_niche_2", "unsupported comparisons"),
        ("files/chromlinker.csv", "TF_B,NA,", "TF_A,GENE1,", "share a TF/target pair"),
        ("files/pseudobulk.txt", "\nNA\t", "\nGENE1\t", "duplicated gene rows"),
        ("files/pseudobulk.txt", "gene\tControl.AT1_niche_1", "gene\tControl.AT1_niche_2", "duplicate column names"),
        ("files/chromlinker.csv", ",Control.AT2", ",IPF.AT2_niche_1", "absent from the configured neighborhood"),
        ("files/chromlinker.csv", "0.05\n", "nan\n", "non-numeric, blank, or NaN"),
        ("files/chromlinker.csv", "0.05\n", "inf\n", "non-finite"),
        ("files/pseudobulk.txt", "\t0.0\n", "\t\n", "non-numeric, blank, or NaN"),
    ],
)
def test_invalid_inputs_fail_without_publishing(synthetic_project, relative, old, new, message):
    root = synthetic_project.parents[1]
    edit(root / relative, old, new)
    with pytest.raises((SourceDataError, IngestError), match=re.escape(message)):
        ingest(synthetic_project)
    processed = root / "data" / "processed"
    assert [p.name for p in processed.iterdir() if p.name != ".staging"] == []
    assert list((processed / ".staging").iterdir()) == []
    records = [json.loads(p.read_text()) for p in (root / "data" / "runs").glob("*/execution.json")]
    assert [r["status"] for r in records] == ["FAILED"]


def test_duplicate_signature_key_is_reported_not_dropped(synthetic_project):
    path = synthetic_project.parents[1] / "files" / "signatures.tsv"
    lines = path.read_text().splitlines()
    path.write_text("\n".join([*lines, lines[1]]) + "\n")
    with pytest.raises(SourceDataError, match="2 rows share a signature key"):
        ingest(synthetic_project)


def test_neighborhood_rows_must_sum_to_k_and_match_filename(synthetic_project):
    root = synthetic_project.parents[1]
    neighborhood = next((root / "files" / "Neighbour_celltypes").glob("AT1_*"))
    edit(neighborhood, "niche_1\t10\t10", "niche_1\t10\t11")
    with pytest.raises(SourceDataError, match="expected 25"):
        ingest(synthetic_project)
    edit(neighborhood, "niche_1\t10\t11", "niche_1\t10\t10")
    edit(synthetic_project, "clustering_resolution: 0.08", "clustering_resolution: 0.09")
    with pytest.raises(SourceDataError, match="filename states"):
        ingest(synthetic_project)


def test_replay_reuses_artifact_and_rebuild_is_identical(synthetic_project, tmp_path):
    first = ingest(synthetic_project)
    second = ingest(synthetic_project)
    assert second.status is StageStatus.REUSED and second.ingest_key == first.ingest_key
    manifest = json.loads((first.artifact_dir / "manifest.json").read_text())
    assert manifest["execution_id"] == first.execution_id  # reuse did not rewrite the artifact

    # An independent rebuild elsewhere reproduces the key and every output byte.
    edit(synthetic_project, "data_root: data", f"data_root: {tmp_path / 'elsewhere'}")
    rebuilt = ingest(synthetic_project)
    assert rebuilt.status is StageStatus.SUCCEEDED and rebuilt.ingest_key == first.ingest_key
    rebuilt_manifest = json.loads((rebuilt.artifact_dir / "manifest.json").read_text())
    assert {o["path"]: o["sha256"] for o in manifest["outputs"]} == {
        o["path"]: o["sha256"] for o in rebuilt_manifest["outputs"]
    }

    # Chunk size changes Parquet row-group layout, never identities, order, or values.
    edit(synthetic_project, "ingest_chunk_rows: 2", "ingest_chunk_rows: 1000")
    edit(synthetic_project, f"data_root: {tmp_path / 'elsewhere'}", f"data_root: {tmp_path / 'chunked'}")
    chunked = ingest(synthetic_project)
    assert chunked.ingest_key == first.ingest_key
    for name in TABLE_SCHEMAS:
        pd.testing.assert_frame_equal(table(first, name), table(chunked, name))


def test_changed_source_gets_new_key_and_prior_artifact_is_preserved(synthetic_project):
    first = ingest(synthetic_project)
    before = {p.name: p.read_bytes() for p in first.artifact_dir.iterdir()}
    edit(synthetic_project.parents[1] / "files" / "chromlinker.csv", "0.05\n", "0.07\n")
    second = ingest(synthetic_project)
    assert second.ingest_key != first.ingest_key
    assert {p.name: p.read_bytes() for p in first.artifact_dir.iterdir()} == before


def test_tampered_artifact_fails_verification_and_is_not_reused(synthetic_project):
    outcome = ingest(synthetic_project)
    with (outcome.artifact_dir / "genes.parquet").open("ab") as handle:
        handle.write(b"tampered")
    results = verify_artifact(outcome.artifact_dir, synthetic_project.parents[1])
    assert not next(r for r in results if r.name == "manifest:output_checksums").passed
    with pytest.raises(IngestError, match="will not be replaced"):
        ingest(synthetic_project)


def test_changed_source_file_is_detected_by_verify(synthetic_project):
    outcome = ingest(synthetic_project)
    edit(synthetic_project.parents[1] / "files" / "pseudobulk.txt", "MATR3-1", "MATR3-2")
    results = verify_artifact(outcome.artifact_dir, synthetic_project.parents[1])
    changed = [r for r in results if r.name.startswith("source_unchanged:") and not r.passed]
    assert [r.name for r in changed] == ["source_unchanged:files/pseudobulk.txt"]


# --- Identity regressions from P1 review R1/R2 -------------------------------------------------


def ids_by_label(outcome, name: str) -> dict[str, set[str]]:
    frame = table(outcome, name)
    return frame.groupby("context_label_raw")["observation_id"].agg(set).to_dict()


def comparisons_by_group(outcome) -> dict[tuple[str, str], str]:
    frame = table(outcome, "niche_expression_signatures.parquet").drop_duplicates("comparison_id")
    return {(r.cell_type_raw, r.condition): r.comparison_id for r in frame.itertuples()}


def niche_ids(outcome) -> dict[tuple[str, str], tuple[str, str]]:
    frame = table(outcome, "niche_states.parquet")
    return {(r.focal_cell_type, r.niche_label): (r.definition_run_id, r.niche_state_id) for r in frame.itertuples()}


def measurements(outcome) -> dict[str, list[float]]:
    return {
        "chromlinker": table(outcome, "chromlinker_observations.parquet")["raw_score"].tolist(),
        "expression": table(outcome, "expression_observations.parquet")["value"].tolist(),
        "signature": table(outcome, "niche_expression_signatures.parquet")["effect_niche2_minus_niche1"].tolist(),
    }


def test_revised_niche_definition_renames_only_that_focal_types_identities(synthetic_project):
    root = synthetic_project.parents[1]
    first = ingest(synthetic_project)
    # Still sums to 25, so only the supplied definition content changes (review R1 probe).
    edit(next((root / "files" / "Neighbour_celltypes").glob("AT1_*")), "niche_1\t10\t10\t4\t1", "niche_1\t11\t9\t4\t1")
    second = ingest(synthetic_project)
    assert second.ingest_key != first.ingest_key

    before, after = niche_ids(first), niche_ids(second)
    for niche in ("niche_1", "niche_2"):
        assert after[("AT1", niche)][0] != before[("AT1", niche)][0]  # definition run
        assert after[("AT1", niche)][1] != before[("AT1", niche)][1]  # niche state
        assert after[("Activated_Fibrotic_FBs", niche)] == before[("Activated_Fibrotic_FBs", niche)]
    contexts = table(second, "contexts.parquet").set_index("context_label_raw")
    assert contexts.loc["Control.AT1_niche_1", "niche_state_id"] == contexts.loc["IPF.AT1_niche_1", "niche_state_id"]

    for name in ("expression_observations.parquet", "chromlinker_observations.parquet"):
        old, new = ids_by_label(first, name), ids_by_label(second, name)
        for label in old:
            if "AT1_niche" in label:
                assert old[label].isdisjoint(new[label]), label
            else:  # unrelated niches and non-niche contexts keep their identities
                assert old[label] == new[label], label
    old_cmp, new_cmp = comparisons_by_group(first), comparisons_by_group(second)
    assert all((old_cmp[g] != new_cmp[g]) == (g[0] == "AT1") for g in old_cmp)
    assert table(first, "genes.parquet")["gene_id"].tolist() == table(second, "genes.parquet")["gene_id"].tolist()
    assert measurements(first) == measurements(second)
    assert [r for r in verify_artifact(second.artifact_dir, root) if not r.passed] == []


def test_changed_biological_context_renames_observations_and_comparisons(synthetic_project):
    first = ingest(synthetic_project)
    edit(synthetic_project, "model_system: primary tissue", "model_system: organoid")  # review R2 probe
    second = ingest(synthetic_project)

    old_contexts = set(table(first, "biological_contexts.parquet")["context_id"])
    assert old_contexts.isdisjoint(table(second, "biological_contexts.parquet")["context_id"])
    for name in ("expression_observations.parquet", "chromlinker_observations.parquet"):
        old_ids = set(table(first, name)["observation_id"])
        assert old_ids.isdisjoint(table(second, name)["observation_id"])
    signatures = ("comparison_id", "signature_row_id")
    for column in signatures:
        old_ids = set(table(first, "niche_expression_signatures.parquet")[column])
        assert old_ids.isdisjoint(table(second, "niche_expression_signatures.parquet")[column])
    # Model system is not part of niche or gene identity; those stay stable.
    assert niche_ids(first) == niche_ids(second)
    assert table(first, "genes.parquet")["gene_id"].tolist() == table(second, "genes.parquet")["gene_id"].tolist()
    assert measurements(first) == measurements(second)


def test_disease_annotation_is_part_of_context_identity(synthetic_project):
    first = ingest(synthetic_project)
    edit(synthetic_project, "disease: idiopathic pulmonary fibrosis", "disease: pulmonary fibrosis, unspecified")
    second = ingest(synthetic_project)
    old, new = (
        ids_by_label(first, "expression_observations.parquet"),
        ids_by_label(second, "expression_observations.parquet"),
    )
    for label in old:
        assert (old[label] == new[label]) == label.startswith("Control."), label
    old_cmp, new_cmp = comparisons_by_group(first), comparisons_by_group(second)
    assert all((old_cmp[g] == new_cmp[g]) == (g[1] == "Control") for g in old_cmp)


def test_non_niche_observation_identity_uses_null_niche(synthetic_project):
    from regkg.project_data.identities import expression_observation_id

    outcome = ingest(synthetic_project)
    row = table(outcome, "expression_observations.parquet").query("context_label_raw == 'Control.AT2'").iloc[0]
    assert pd.isna(row["niche_state_id"])
    assert row["observation_id"] == expression_observation_id(
        row["source_id"], row["gene_id"], row["context_label_raw"], row["context_id"], None
    )


def test_verify_rejects_assignment_changed_under_an_unchanged_id(synthetic_project, tmp_path):
    import shutil

    from regkg.config import load_project_config as load
    from regkg.project_data.verify import table_checks

    outcome = ingest(synthetic_project)
    copy = tmp_path / "tampered"
    shutil.copytree(outcome.artifact_dir, copy)
    frame = table(outcome, "expression_observations.parquet")
    at1 = frame["context_label_raw"] == "Control.AT1_niche_1"
    other = frame.loc[frame["context_label_raw"] == "Control.AT1_niche_2", "niche_state_id"].iloc[0]
    frame.loc[at1, "niche_state_id"] = other  # reassign niche membership but keep observation IDs
    frame.to_parquet(copy / "expression_observations.parquet", index=False)
    config = load(synthetic_project, repo_root=synthetic_project.parents[1]).config
    failed = {r.name for r in table_checks(copy, config) if not r.passed}
    assert "identity:expression_observations.parquet" in failed
