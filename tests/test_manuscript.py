"""Manuscript-scope candidate extension (P2.11-P2.13) on the synthetic project (engineering only).

The synthetic AT1 lineage has ChromLinker contexts in both conditions; the synthetic fibroblast
lineage has Control signatures and expression but no Control niche ChromLinker contexts, like
the real KRT5-/KRT17+ and fibroblast cases.
"""

from __future__ import annotations

import json
from pathlib import Path

import httpx
import pandas as pd
import pytest
import yaml

from regkg.analysis.manuscript import (
    ROLE_PRIMARY,
    ROLE_SIGNATURE_ONLY,
    run_manuscript_candidates,
    verify_manuscript_artifact,
)
from regkg.analysis.queue import TYPE_CONTEXT, next_pending, schedule_queries
from regkg.analysis.stage import CandidateStageError, run_candidates
from regkg.config import ConfigError, load_manuscript_scope, load_project_config
from regkg.models import StageStatus
from regkg.project_data.ingest import run_ingest
from tests.test_candidates import QUEUE, configure, seed_resources

FIBRO = "Activated_Fibrotic_FBs"
TF_A, TF_B, GENE1 = "HGNC:10", "HGNC:11", "HGNC:12"


def scope(lineages: list[dict], batch_size: int = 4) -> dict:
    return {
        "schema_version": 1,
        "scope_version": "test-scope-1",
        "source": "synthetic",
        "lineages": lineages,
        "expected": {
            "primary_comparisons": sum(len(x["primary_conditions"]) for x in lineages),
            "lineage_tf_memberships": sum(len(x["tf_seeds"]) for x in lineages),
            "unique_named_tfs": len({s for x in lineages for s in x["tf_seeds"]}),
        },
        "schedule": {"rule_version": "test-schedule", "batch_size": batch_size},
    }


def lineage(cell_type: str, seeds: list[str], conditions: list[str], context: list[str]) -> dict:
    return {
        "cell_type": cell_type,
        "tf_seeds": seeds,
        "primary_conditions": conditions,
        "context_terms": context,
        "draft_interpretation": "synthetic claim to assess",
    }


# AT1 seeds and context terms equal the synthetic baseline's; TF_B and GENE1 are fibroblast-only
# seeds. GENE1 has no prior regulon and no ChromLinker rows: a sparse seed.
DEFAULT = [
    lineage("AT1", ["TF_A"], ["Control", "IPF"], QUEUE.context_terms),
    lineage(FIBRO, ["TF_A", "TF_B", "GENE1"], ["IPF"], ["lung", "fibroblast"]),
]


def setup(synthetic_project: Path, lineages=DEFAULT, **kwargs):
    root = synthetic_project.parents[1]
    loaded = load_project_config(synthetic_project, repo_root=root)
    ingest = run_ingest(loaded)
    seed_resources(root)
    path = root / "configs" / "manuscript_scope.yaml"
    path.write_text(yaml.safe_dump(scope(lineages, **kwargs)))
    configs = root / "configs"
    return loaded, ingest.ingest_key, path, configs / "ranking.yaml", configs / "literature.yaml"


def read(outcome, name: str) -> pd.DataFrame:
    return pd.read_parquet(outcome.artifact_dir / name)


def test_manuscript_stage_covers_cases_isolates_lineages_and_replays(synthetic_project, monkeypatch):
    loaded, ingest_key, scope_path, ranking, literature = setup(synthetic_project)
    monkeypatch.setattr(httpx, "get", lambda *a, **k: pytest.fail("network access attempted"))
    args = (loaded, ingest_key, scope_path, ranking, literature)
    first = run_manuscript_candidates(*args)
    assert first.status is StageStatus.SUCCEEDED and first.network_requests == 0
    assert [r for r in verify_manuscript_artifact(first.artifact_dir, loaded.repo_root) if not r.passed] == []

    comparisons = read(first, "comparisons.parquet")
    primary = comparisons[comparisons["comparison_role"] == ROLE_PRIMARY]
    assert sorted(zip(primary["cell_type"], primary["condition"], strict=True)) == [
        ("AT1", "Control"),
        ("AT1", "IPF"),
        (FIBRO, "IPF"),
    ]
    # The fibroblast Control signature is kept as observation-only; no context is invented for it.
    (control,) = comparisons[comparisons["comparison_role"] == ROLE_SIGNATURE_ONLY].itertuples(index=False)
    assert (control.cell_type, control.condition, control.regulatory_context_status) == (
        FIBRO,
        "Control",
        "none_supplied",
    )
    assert pd.isna(control.chromlinker_case_context_label) and pd.isna(control.chromlinker_reference_context_label)
    candidates = read(first, "candidates.parquet")
    assert control.comparison_id not in set(candidates["comparison_id"])
    assert control.comparison_id not in set(read(first, "concordance.parquet")["comparison_id"])

    # Shared TF: one gene identity, separate nomination contexts per comparison and lineage.
    memberships = read(first, "lineage_tf_memberships.parquet")
    assert len(memberships) == 4 and memberships["tf_hgnc_id"].nunique() == 3
    shared = memberships[memberships["tf_hgnc_id"] == TF_A]
    assert sorted(shared["cell_type"]) == ["AT1", FIBRO] and shared["tf_gene_id"].nunique() == 1
    tf_a = candidates[candidates["tf_hgnc_id"] == TF_A]
    assert len(tf_a) == 3 and tf_a["candidate_id"].is_unique

    # Isolation: fibroblast-only seeds never carry a seed reason in AT1 comparisons.
    at1 = candidates[candidates["cell_type"] == "AT1"]
    at1_seeded = set(at1.loc[at1["reasons"].map(lambda r: "manuscript_seed" in r), "tf_hgnc_id"])
    assert at1_seeded == {TF_A}
    assert {TF_B, GENE1} <= set(candidates.loc[candidates["cell_type"] == FIBRO, "tf_hgnc_id"])

    # Sparse seed: no prior regulon, no ChromLinker rows, no targets -> kept, with a TF-only query.
    gene1 = candidates[(candidates["tf_hgnc_id"] == GENE1) & (candidates["cell_type"] == FIBRO)].iloc[0]
    assert not gene1["in_prior"] and not gene1["tf_in_chromlinker"] and pd.isna(gene1["ulm_score"])
    assert {"tf_absent_from_prior", "tf_absent_from_chromlinker"} <= set(gene1["missing_component_reasons"])
    targets, queue = read(first, "candidate_targets.parquet"), read(first, "retrieval_queue.parquet")
    assert gene1["candidate_id"] not in set(targets["candidate_id"])
    gene1_queries = queue[(queue["tf_hgnc_id"] == GENE1) & (queue["cell_type"] == FIBRO)]
    assert set(gene1_queries["query_type"]) == {TYPE_CONTEXT}

    # Lineage-scoped queries: the same TF gets separate rows with its own lineage context terms.
    contexts = queue[(queue["tf_hgnc_id"] == TF_A) & (queue["query_type"] == TYPE_CONTEXT)]
    assert sorted(contexts["cell_type"]) == ["AT1", FIBRO] and contexts["query_id"].is_unique
    qualifiers = {r.cell_type: json.loads(r.terms_json)["qualifiers"] for r in contexts.itertuples(index=False)}
    assert qualifiers == {"AT1": QUEUE.context_terms, FIBRO: ["lung", "fibroblast"]}
    owner = dict(zip(candidates["candidate_id"], candidates["cell_type"], strict=True))
    assert all({owner[c] for c in r.candidate_ids} == {r.cell_type} for r in queue.itertuples(index=False))

    manifest = json.loads((first.artifact_dir / "manuscript_manifest.json").read_text())
    assert manifest["observed"]["primary_comparisons"] == 3 and manifest["status"] == "pending_lead_review"
    assert manifest["named_tfs_in_several_lineages"] == {TF_A: {"symbol": "TF_A", "lineages": ["AT1", FIBRO]}}

    before = {p.name: p.read_bytes() for p in first.artifact_dir.iterdir()}
    replay = run_manuscript_candidates(*args)
    assert replay.status is StageStatus.REUSED and replay.candidate_key == first.candidate_key
    assert replay.network_requests == 0
    assert {p.name: p.read_bytes() for p in first.artifact_dir.iterdir()} == before


def test_at1_lineage_matches_the_reproducible_baseline(synthetic_project, monkeypatch):
    loaded, ingest_key, scope_path, ranking, literature = setup(synthetic_project)
    monkeypatch.setattr(httpx, "get", lambda *a, **k: pytest.fail("network access attempted"))
    baseline = run_candidates(loaded, ingest_key, "AT1", ranking, literature)
    manuscript = run_manuscript_candidates(loaded, ingest_key, scope_path, ranking, literature)
    old, new = read(baseline, "candidates.parquet"), read(manuscript, "candidates.parquet")
    new = new[new["cell_type"] == "AT1"]
    assert sorted(old["candidate_id"]) == sorted(new["candidate_id"])  # same nomination contexts
    columns = ["candidate_id", "tf_hgnc_id", "ulm_score", "chromlinker_case_observations"]
    pd.testing.assert_frame_equal(
        old[columns].sort_values("candidate_id").reset_index(drop=True),
        new[columns].sort_values("candidate_id").reset_index(drop=True),
    )
    old_queue, new_queue = read(baseline, "retrieval_queue.parquet"), read(manuscript, "retrieval_queue.parquet")
    at1 = new_queue[new_queue["cell_type"] == "AT1"].sort_values("lineage_priority")
    assert at1["query_text"].tolist() == old_queue.sort_values("priority")["query_text"].tolist()


def test_empty_concordance_and_no_targets_keep_seeds_in_every_primary_comparison(synthetic_project, monkeypatch):
    loaded, ingest_key, scope_path, ranking, literature = setup(synthetic_project)
    configure(synthetic_project.parents[1], synthetic_project, {"targets_per_candidate": 0}, {"min_targets": 50})
    monkeypatch.setattr(httpx, "get", lambda *a, **k: pytest.fail("network access attempted"))
    outcome = run_manuscript_candidates(loaded, ingest_key, scope_path, ranking, literature)
    assert [r for r in verify_manuscript_artifact(outcome.artifact_dir, loaded.repo_root) if not r.passed] == []
    candidates, targets = read(outcome, "candidates.parquet"), read(outcome, "candidate_targets.parquet")
    queue, concordance = read(outcome, "retrieval_queue.parquet"), read(outcome, "concordance.parquet")
    assert candidates["is_seed"].all() and candidates["ulm_score"].isna().all()  # no extras, no scores
    assert not concordance["eligible"].any() and len(concordance) > 0  # coverage recorded, not dropped
    assert len(candidates) == 1 + 1 + 3 and targets.empty
    assert set(queue["query_type"]) == {TYPE_CONTEXT}
    memberships = read(outcome, "lineage_tf_memberships.parquet")
    assert memberships["concordance_eligible_comparisons"].map(len).eq(0).all()


def test_primary_comparison_without_supplied_signatures_is_refused(synthetic_project):
    lineages = [*DEFAULT, lineage("AT2", ["TF_A"], ["Control"], ["alveolar type 2"])]
    loaded, ingest_key, scope_path, ranking, literature = setup(synthetic_project, lineages)
    with pytest.raises(CandidateStageError, match="AT2: no signature comparison"):
        run_manuscript_candidates(loaded, ingest_key, scope_path, ranking, literature)
    assert not list((loaded.data_root / "processed").glob("mcandidates-*"))


def test_scope_must_reconcile_with_expected_counts(tmp_path, synthetic_project):
    project = load_project_config(synthetic_project, repo_root=synthetic_project.parents[1]).config
    content = scope(DEFAULT)
    content["expected"]["unique_named_tfs"] = 4
    path = tmp_path / "scope.yaml"
    path.write_text(yaml.safe_dump(content))
    with pytest.raises(ConfigError, match="unique_named_tfs"):
        load_manuscript_scope(path, project)
    content = scope([lineage("Unknown_Cells", ["TF_A"], ["IPF"], ["x"])])
    path.write_text(yaml.safe_dump(content))
    with pytest.raises(ConfigError, match="Unknown_Cells"):
        load_manuscript_scope(path, project)


def test_real_scope_file_states_the_manuscript_cases():
    project = load_project_config(Path("configs/project.yaml")).config
    loaded = load_manuscript_scope(Path("configs/manuscript_scope.yaml"), project)
    seeds = {x.cell_type: (x.tf_seeds, x.primary_conditions) for x in loaded.lineages}
    assert seeds == {
        "AT1": (["TEAD1", "KLF5", "GATA6", "FOXA2", "ETV1"], ["Control", "IPF"]),
        "Alveolar_Macrophages": (["SPI1", "EGR2", "BHLHE41", "TFEC", "IRF8", "CEBPB"], ["Control", "IPF"]),
        "KRT5neg_KRT17pos": (["TEAD1", "KLF5", "RFX2"], ["IPF"]),
        "Activated_Fibrotic_FBs": (["FOSB", "TEAD1"], ["IPF"]),
    }


def queues(sizes: dict[str, int]) -> dict[str, pd.DataFrame]:
    return {
        name: pd.DataFrame({"query_id": [f"{name}{i}" for i in range(n)], "lineage_priority": range(1, n + 1)})
        for name, n in sizes.items()
    }


def test_schedule_rotates_never_starves_and_resumes():
    schedule = schedule_queries(queues({"A": 10, "B": 1, "C": 3}), batch_size=3)
    # Round 1 starts at A, round 2 at B (exhausted, so C), round 3 at C.
    assert schedule["query_id"].tolist()[:7] == ["A0", "B0", "C0", "C1", "A1", "C2", "A2"]
    for _, batch in schedule.groupby("batch_index"):
        start = batch["schedule_position"].min()
        waiting = set(schedule.loc[schedule["schedule_position"] >= start, "cell_type"])
        assert waiting <= set(batch["cell_type"])  # every lineage still waiting gets a slot
    assert schedule.groupby("cell_type")["query_id"].apply(list).to_dict() == {
        "A": [f"A{i}" for i in range(10)],
        "B": ["B0"],
        "C": ["C0", "C1", "C2"],
    }  # each lineage's own order is kept
    # Batches smaller than the number of lineages: rotation still reaches every lineage.
    small = schedule_queries(queues({"A": 5, "B": 5, "C": 5, "D": 5}), batch_size=2)
    first_two = small[small["batch_index"] <= 2]
    assert set(first_two["cell_type"]) == {"A", "B", "C", "D"}
    # Resume after a partially executed batch continues in schedule order.
    done = set(schedule["query_id"].iloc[:4]) - {"B0"}
    resumed = next_pending(schedule, done, 3)
    assert resumed["query_id"].tolist() == ["B0", "A1", "C2"]


def test_verifier_rejects_a_seed_reason_leaked_into_another_lineage(synthetic_project, monkeypatch):
    from regkg.provenance import sha256_file

    loaded, ingest_key, scope_path, ranking, literature = setup(synthetic_project)
    monkeypatch.setattr(httpx, "get", lambda *a, **k: pytest.fail("network access attempted"))
    outcome = run_manuscript_candidates(loaded, ingest_key, scope_path, ranking, literature)
    path = outcome.artifact_dir / "candidates.parquet"
    candidates = pd.read_parquet(path)
    # A fibroblast-only seed (TF_B) relabelled as an AT1 nomination with its seed reason.
    leak = candidates.index[(candidates["cell_type"] == FIBRO) & (candidates["tf_hgnc_id"] == TF_B)][0]
    at1_comparison = candidates.loc[candidates["cell_type"] == "AT1", "comparison_id"].iloc[0]
    candidates.loc[leak, ["cell_type", "comparison_id"]] = ["AT1", at1_comparison]
    candidates.to_parquet(path, index=False)
    manifest = json.loads((outcome.artifact_dir / "manifest.json").read_text())
    for output in manifest["outputs"]:  # simulate a producer bug published with a consistent checksum
        if output["path"] == "candidates.parquet":
            output["sha256"] = sha256_file(path)
    (outcome.artifact_dir / "manifest.json").write_text(json.dumps(manifest))
    failed = {r.name for r in verify_manuscript_artifact(outcome.artifact_dir, loaded.repo_root) if not r.passed}
    assert "candidates:lineage_isolation_and_selection" in failed
