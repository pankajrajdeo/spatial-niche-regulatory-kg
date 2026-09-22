"""P2 behavioral checks on tiny synthetic inputs (engineering only; no network, no real resources)."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import httpx
import pandas as pd
import pytest
import yaml

from regkg.analysis import schemas
from regkg.analysis.candidates import (
    REASON_CONCORDANCE,
    REASON_SEED,
    REGULATOR_SCOPE,
    select_candidates,
    select_targets,
)
from regkg.analysis.concordance import PRIMARY_POLICY, ComparisonVector, concordance_table
from regkg.analysis.gene_mapping import resolve_symbol, resolve_symbols, safe_aliases, symbol_index
from regkg.analysis.priors import parse_collectri, ulm_network
from regkg.analysis.queue import STATUS_NOT_SEARCHED, TYPE_ASSAY, TYPE_CONTEXT, build_queue
from regkg.analysis.seed_publications import SeedList, seed_publications
from regkg.config import ConfigError, RetrievalQueueConfig, load_candidate_config, load_project_config
from regkg.models import StageStatus
from regkg.resources import Fetcher, ResourceError, Snapshot, cached_snapshot, store_snapshot

HGNC_COLUMNS = [
    "hgnc_id",
    "symbol",
    "name",
    "locus_group",
    "locus_type",
    "status",
    "alias_symbol",
    "prev_symbol",
    "entrez_id",
    "ensembl_gene_id",
]
QUEUE = RetrievalQueueConfig(
    query_version="test-1",
    max_live_queries=3,
    max_aliases_per_gene=2,
    assay_terms=["ChIP"],
    null_terms=["no effect"],
    context_terms=["lung"],
)


def hgnc_frame(rows: list[tuple[str, str, str, str]]) -> pd.DataFrame:
    """rows: (hgnc_id, approved symbol, alias_symbol pipe list, prev_symbol pipe list)."""
    return pd.DataFrame(
        [
            {
                "hgnc_id": h,
                "symbol": s,
                "name": s,
                "locus_group": "protein-coding gene",
                "locus_type": "gene",
                "status": "Approved",
                "alias_symbol": a,
                "prev_symbol": p,
                "entrez_id": "",
                "ensembl_gene_id": "",
            }
            for h, s, a, p in rows
        ],
        columns=HGNC_COLUMNS,
    )


COMPARISON = pd.DataFrame(
    {
        "comparison_id": ["cmp:1"],
        "condition": ["IPF"],
        "case_niche_state_id": ["niche:2"],
        "reference_niche_state_id": ["niche:1"],
    }
)


def genes_frame(symbols: list[str]) -> pd.DataFrame:
    return pd.DataFrame({"gene_id": [f"gene:{i:03d}" for i in range(len(symbols))], "source_symbol": symbols})


# --- gene mapping ------------------------------------------------------------------------------


def test_mapping_is_exact_unambiguous_and_never_merges_distinct_features():
    hgnc = hgnc_frame(
        [
            ("HGNC:1", "NEW1", "", "OLD1"),  # OLD1 is a previous symbol of NEW1
            ("HGNC:2", "GENEA", "SHARED|UNIQ2", ""),
            ("HGNC:3", "GENEB", "SHARED", ""),  # SHARED alias names two genes: ambiguous
            ("HGNC:4", "GENEC", "ALIASC1|ALIASC2", ""),
        ]
    )
    genes = genes_frame(["NEW1", "OLD1", "SHARED", "UNIQ2", "ALIASC1", "ALIASC2", "genea", "MATR3.1"])
    mapped = resolve_symbols(genes, hgnc, "test").set_index("source_symbol")
    assert mapped.loc["NEW1", "mapping_status"] == "resolved_approved_symbol"
    # OLD1 is a distinct supplied feature claiming NEW1's ID indirectly: rejected, not merged.
    assert mapped.loc["OLD1", "mapping_status"] == "conflict_shared_hgnc_id" and pd.isna(mapped.loc["OLD1", "hgnc_id"])
    assert mapped.loc["SHARED", "mapping_status"] == "ambiguous"
    assert list(mapped.loc["SHARED", "candidate_hgnc_ids"]) == ["HGNC:2", "HGNC:3"]
    assert mapped.loc["UNIQ2", "mapping_status"] == "resolved_alias_symbol"
    assert mapped.loc["UNIQ2", "approved_symbol"] == "GENEA"
    # Two indirect claimants of one ID with no exact holder are both rejected.
    assert set(mapped.loc[["ALIASC1", "ALIASC2"], "mapping_status"]) == {"conflict_shared_hgnc_id"}
    assert mapped.loc["genea", "mapping_status"] == "unresolved"  # no case folding
    assert mapped.loc["MATR3.1", "mapping_status"] == "unresolved"  # no suffix stripping
    assert mapped["gene_id"].tolist() == genes["gene_id"].tolist()  # P1 identities preserved


def test_indirect_names_pool_previous_and_alias_fields():
    hgnc = hgnc_frame(
        [
            ("HGNC:1", "GENEA", "", "OLD"),  # OLD is A's previous symbol ...
            ("HGNC:2", "GENEB", "OLD", ""),  # ... and B's alias: ambiguous, not A
            ("HGNC:3", "GENEC", "BOTH", "BOTH"),  # one ID in both fields: resolves
            ("HGNC:4", "EXACT", "", ""),
            ("HGNC:5", "GENED", "EXACT", "EXACT"),  # an approved symbol beats others' indirect names
        ]
    )
    index = symbol_index(hgnc)
    assert resolve_symbol("OLD", *index) == ("ambiguous", None, "prev_symbol|alias_symbol", ["HGNC:1", "HGNC:2"])
    assert resolve_symbol("BOTH", *index) == (
        "resolved_previous_symbol",
        "HGNC:3",
        "prev_symbol|alias_symbol",
        ["HGNC:3"],
    )
    assert resolve_symbol("EXACT", *index) == ("resolved_approved_symbol", "HGNC:4", "symbol", ["HGNC:4"])
    mapped = resolve_symbols(genes_frame(["OLD", "BOTH", "EXACT"]), hgnc, "test").set_index("source_symbol")
    assert mapped.loc["OLD", "mapping_status"] == "ambiguous" and pd.isna(mapped.loc["OLD", "hgnc_id"])
    assert list(mapped.loc["OLD", "candidate_hgnc_ids"]) == ["HGNC:1", "HGNC:2"]
    assert mapped.loc["BOTH", "hgnc_id"] == "HGNC:3" and mapped.loc["EXACT", "hgnc_id"] == "HGNC:4"


def test_prior_entities_use_the_same_pooled_resolution(tmp_path):
    hgnc = hgnc_frame([("HGNC:1", "TFA", "", ""), ("HGNC:2", "GENEA", "", "OLD"), ("HGNC:3", "GENEB", "OLD", "")])
    priors = parse_collectri(collectri_snapshot(tmp_path, [("TFA", "OLD", 1.0, "CollecTRI:1", "PMID")]), hgnc, [])
    row = priors.iloc[0]
    assert row["target_mapping_status"] == "ambiguous" and pd.isna(row["target_hgnc_id"])
    assert list(row["target_candidate_hgnc_ids"]) == ["HGNC:2", "HGNC:3"]
    frame, net = ulm_network(priors, ["pmid_evidence"])
    assert frame["ulm_exclusion_reason"].tolist() == ["target_not_uniquely_resolved"] and net.empty


def test_safe_aliases_require_uniqueness_length_and_a_digit():
    hgnc = hgnc_frame(
        [
            ("HGNC:1", "TEAD1", "TEF-1|AA|TCF13", ""),
            ("HGNC:2", "KLF5", "BTEB2|CKLF", ""),
            ("HGNC:3", "CKLF", "", ""),
            ("HGNC:4", "OTHER", "TCF13", ""),
        ]
    )
    assert safe_aliases("HGNC:1", hgnc) == ["TEF-1"]  # AA too short; TCF13 shared with OTHER
    assert safe_aliases("HGNC:2", hgnc) == ["BTEB2"]  # CKLF is another gene's approved symbol


# --- CollecTRI prior -----------------------------------------------------------------------------


def collectri_snapshot(tmp_path: Path, rows: list[tuple[str, str, float, str, str]]) -> Snapshot:
    path = tmp_path / "collectri.csv"
    lines = ["source,target,weight,resources,references,sign_decision"]
    lines += [f"{s},{t},{w},CollecTRI;TRRUST_CollecTRI,{r},{d}" for s, t, w, r, d in rows]
    path.write_text("\n".join(lines) + "\n")
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    return Snapshot(
        path,
        {
            "sha256": digest,
            "version": "test",
            "doi": None,
            "license": "cc-by-4.0",
            "retrieved_at": "2026-01-01T00:00:00Z",
        },
        0,
    )


def test_prior_keeps_complexes_unknown_signs_and_contradictions(tmp_path):
    hgnc = hgnc_frame(
        [("HGNC:1", "TFA", "", ""), ("HGNC:2", "T1", "", ""), ("HGNC:3", "T2", "", "OLDT2"), ("HGNC:4", "T3", "", "")]
    )
    snapshot = collectri_snapshot(
        tmp_path,
        [
            ("TFA", "T1", 1.0, "CollecTRI:111", "PMID"),
            ("TFA", "T1", -1.0, "CollecTRI:222", "PMID"),  # contradictory duplicate pair
            ("TFA", "T2", 1.0, "", "default activation"),  # no evidenced sign, no references
            ("TFA", "OLDT2", -1.0, "CollecTRI:333", "PMID"),  # maps onto the same pair as T2
            ("TFA", "T3", -1.0, "CollecTRI:444", "regulon"),
            ("AP1", "T3", 1.0, "CollecTRI:555", "PMID"),
        ],
    )
    priors = parse_collectri(snapshot, hgnc, ["AP1"])
    assert len(priors) == 6  # every supplied row kept
    complex_row = priors[priors["regulator_symbol_raw"] == "AP1"].iloc[0]
    assert complex_row["regulator_type"] == "complex" and pd.isna(complex_row["regulator_hgnc_id"])
    default = priors[priors["sign_basis"] == "default_activation"].iloc[0]
    assert default["sign"] == "unknown" and default["source_weight"] == 1.0 and list(default["pmids"]) == []
    assert priors.loc[priors["target_symbol_raw"] == "T1", "pair_signs_disagree"].all()

    frame, net = ulm_network(priors, ["pmid_evidence", "tf_regulon_majority"])
    reasons = dict(
        zip(
            frame["target_symbol_raw"] + "/" + frame["regulator_symbol_raw"], frame["ulm_exclusion_reason"], strict=True
        )
    )
    assert reasons["T1/TFA"] == "contradictory_signs"
    assert reasons["T2/TFA"] == "sign_basis_not_allowed"
    assert pd.isna(reasons["OLDT2/TFA"])  # the only allowed record for TFA->T2 remains
    assert set(zip(net["source"], net["target"], strict=True)) == {("TFA", "T2"), ("TFA", "T3"), ("AP1", "T3")}
    _, sensitivity = ulm_network(priors, ["pmid_evidence", "tf_regulon_majority", "default_activation"])
    assert reasons_after(sensitivity) == {("TFA", "T3"), ("AP1", "T3")}  # T2 now collides: excluded, not averaged


def reasons_after(net: pd.DataFrame) -> set[tuple[str, str]]:
    return set(zip(net["source"], net["target"], strict=True))


# --- concordance -------------------------------------------------------------------------------


def test_ulm_keeps_zero_effect_genes_and_applies_min_targets():
    genes = [f"G{i}" for i in range(12)]
    values = pd.Series([0.0, 0.0, 1.0, -1.0, 2.0, 0.5, -0.5, 0.0, 1.5, -2.0, 0.3, 0.1], index=genes)
    vector = ComparisonVector("cmp:1", "IPF", "niche:2", "niche:1", values, {})
    net = pd.DataFrame(
        {"source": ["R1"] * 5 + ["R2"] * 4, "target": genes[:5] + genes[5:9], "weight": [1, 1, 1, -1, 1, 1, -1, 1, 1]}
    )
    info = pd.DataFrame(
        {"regulator_type": ["gene", "gene"], "regulator_hgnc_id": ["HGNC:1", "HGNC:2"]}, index=["R1", "R2"]
    )
    table = concordance_table([vector], net, info, 5, PRIMARY_POLICY, "test").set_index("regulator_key")
    # R1's targets include two zero-effect genes; they still count toward coverage.
    assert table.loc["R1", "observed_targets"] == 5 and table.loc["R1", "eligible"]
    assert table.loc["R2", "observed_targets"] == 4 and not table.loc["R2", "eligible"]
    assert pd.isna(table.loc["R2", "ulm_score"]) and pd.isna(table.loc["R2", "concordance_direction"])
    assert table.loc["R1", "concordance_direction"] == ("positive" if table.loc["R1", "ulm_score"] > 0 else "negative")


# --- candidates and targets --------------------------------------------------------------------


def concordance_rows(scores: dict[str, float | None], regulator_type: dict[str, str] | None = None) -> pd.DataFrame:
    rows = []
    for hgnc_id, score in scores.items():
        rows.append(
            {
                "comparison_id": "cmp:1",
                "condition": "IPF",
                "case_niche_state_id": "niche:2",
                "reference_niche_state_id": "niche:1",
                "regulator_key": hgnc_id,
                "regulator_type": (regulator_type or {}).get(hgnc_id, "gene"),
                "regulator_hgnc_id": None if (regulator_type or {}).get(hgnc_id) == "complex" else hgnc_id,
                "prior_universe_targets": 9,
                "observed_targets": 9 if score is not None else 2,
                "eligible": score is not None,
                "ulm_score": score,
                "concordance_direction": None if score is None else "positive" if score > 0 else "negative",
            }
        )
    return pd.DataFrame(rows)


def test_seeds_always_included_and_topk_ties_break_by_hgnc_id():
    concordance = concordance_rows(
        {"HGNC:9": 5.0, "HGNC:3": -5.0, "HGNC:5": 5.0, "HGNC:7": 1.0, "HGNC:1": None, "HGNC:2": 9.0, "AP1": 20.0},
        {"AP1": "complex"},
    )
    seeds = pd.DataFrame({"hgnc_id": ["HGNC:1", "HGNC:2"]})
    selected = select_candidates(COMPARISON, concordance, seeds, 2, "test").set_index("tf_hgnc_id")
    # |score| ties among HGNC:3, :5, :9 resolve by ID; the complex never qualifies.
    assert list(selected.index) == ["HGNC:1", "HGNC:2", "HGNC:3", "HGNC:5"]
    assert list(selected.loc["HGNC:1", "reasons"]) == [REASON_SEED]  # ineligible seed still present
    assert pd.isna(selected.loc["HGNC:1", "ulm_score"])
    assert list(selected.loc["HGNC:2", "reasons"]) == [REASON_SEED, REASON_CONCORDANCE]
    assert list(selected.loc["HGNC:3", "reasons"]) == [REASON_CONCORDANCE]
    assert selected.loc["HGNC:3", "concordance_direction"] == "negative"  # sign kept, not called activity
    again = select_candidates(COMPARISON, concordance.sample(frac=1, random_state=4), seeds, 2, "test")
    assert again.equals(select_candidates(COMPARISON, concordance, seeds, 2, "test"))
    assert set(selected["regulator_scope"]) == {REGULATOR_SCOPE}


def test_targets_are_resolved_route_linked_and_ordered_or_absent():
    mappings = pd.DataFrame(
        {
            "gene_id": ["g:tf", "g:a", "g:b", "g:c", "g:u"],
            "source_symbol": ["TF", "A", "B", "C", "U"],
            "mapping_status": ["resolved_approved_symbol"] * 4 + ["unresolved"],
            "hgnc_id": ["H:0", "H:1", "H:2", "H:3", None],
            "approved_symbol": ["TF", "A", "B", "C", None],
        }
    )
    candidates = pd.DataFrame(
        {"candidate_id": ["c1", "c2"], "comparison_id": ["cmp:1", "cmp:1"], "tf_hgnc_id": ["H:0", "H:9"]}
    )
    evidence = pd.DataFrame({"candidate_id": ["c1", "c2"], "tf_gene_id": ["g:tf", None]})
    priors = pd.DataFrame(
        {
            "regulator_hgnc_id": ["H:0", "H:0"],
            "target_hgnc_id": ["H:1", "H:2"],
            "target_approved_symbol": ["A", "B"],
            "prior_interaction_id": ["p1", "p2"],
            "sign": ["activation", "unknown"],
        }
    )
    chromlinker = pd.DataFrame({"tf_gene_id": ["g:tf", "g:tf"], "target_gene_id": ["g:c", "g:u"]})
    signatures = pd.DataFrame(
        {
            "comparison_id": ["cmp:1"] * 4,
            "gene_id": ["g:a", "g:b", "g:c", "g:u"],
            "effect_niche2_minus_niche1": [0.5, -0.5, 0.2, 9.0],
        }
    )
    targets = select_targets(candidates, evidence, priors, mappings, chromlinker, signatures, 2)
    # Unresolved U is never chosen despite the largest effect; |0.5| tie breaks by gene ID.
    assert targets["target_gene_id"].tolist() == ["g:a", "g:b"]
    assert [list(r) for r in targets["source_routes"]] == [["collectri_prior"], ["collectri_prior"]]
    assert "c2" not in set(targets["candidate_id"])  # no eligible target: none invented

    names = {"H:0": ["TF", "TF-9"], "H:9": ["NOPE"], "H:1": ["A"], "H:2": ["B"]}
    frame = candidates.assign(condition="IPF", reasons=[[REASON_SEED], [REASON_CONCORDANCE]], is_seed=[True, False])
    queue = build_queue(frame, targets, names, QUEUE)
    assert set(queue["search_status"]) == {STATUS_NOT_SEARCHED}
    assert queue["priority"].tolist() == list(range(1, len(queue) + 1))
    # Each TF's first query precedes any second query; the TF without targets gets a TF-only query.
    assert queue.iloc[:2][["tf_hgnc_id", "query_type"]].values.tolist() == [["H:0", TYPE_ASSAY], ["H:9", TYPE_CONTEXT]]
    assert int(queue["in_initial_live_slice"].sum()) == 3
    assert queue["date_restriction"].isna().all()
    assert build_queue(frame, targets, names, QUEUE).equals(queue)


# --- seed publications and resources -----------------------------------------------------------


def test_seed_publications_deduplicate_and_keep_memberships(tmp_path):
    header = "tier,pmid,year,journal,first_author,title,doi,note"
    (tmp_path / "a.csv").write_text(f"{header}\nA,12,2020,J,X,T1,d1,first\nB,34,2021,J,Y,T2,d2,x\n")
    (tmp_path / "b.csv").write_text(f"{header}\nT1,12,2020,J,X,T1,d1,second\nT2,56,2022,K,Z,T3,d3,y\n")
    frame, conflicts = seed_publications(
        [SeedList("a", tmp_path / "a.csv", "a.csv"), SeedList("b", tmp_path / "b.csv", "b.csv")]
    )
    assert frame["pmid"].tolist() == ["12", "34", "56"] and conflicts == []
    shared = frame.set_index("pmid").loc["12"]
    assert list(shared["resources"]) == ["a", "b"]
    assert [json.loads(m["annotations_json"])["note"] for m in shared["memberships"]] == ["first", "second"]
    assert set(frame["evidence_status"]) == {"seed_metadata_not_evidence"}


def test_snapshot_cache_detects_tampering_and_checksum_mismatch(tmp_path):
    fetcher = Fetcher()
    snapshot = store_snapshot(
        tmp_path,
        "f.txt",
        b"payload",
        "https://example.invalid/f",
        fetcher,
        expected_md5_hex=hashlib.md5(b"payload").hexdigest(),
        metadata={},
        response_headers={},
    )
    assert snapshot.provenance["publisher_md5_verified"]
    assert cached_snapshot(tmp_path, "f.txt").network_requests == 0
    (tmp_path / "f.txt").write_bytes(b"changed")
    with pytest.raises(ResourceError, match="no longer matches"):
        cached_snapshot(tmp_path, "f.txt")
    with pytest.raises(ResourceError, match="does not match publisher checksum"):
        store_snapshot(
            tmp_path / "x",
            "g.txt",
            b"payload",
            "u",
            fetcher,
            expected_md5_hex="0" * 32,
            metadata={},
            response_headers={},
        )


def test_fetcher_retries_transient_errors_and_fails_fast_otherwise(monkeypatch):
    responses = iter([httpx.Response(503), httpx.Response(200, content=b"ok")])
    monkeypatch.setattr(httpx, "get", lambda *a, **k: next(responses))
    monkeypatch.setattr("time.sleep", lambda _: None)
    fetcher = Fetcher()
    assert fetcher.get("https://example.invalid").content == b"ok" and fetcher.requests == 2
    monkeypatch.setattr(httpx, "get", lambda *a, **k: httpx.Response(404))
    with pytest.raises(ResourceError, match="HTTP 404"):
        Fetcher().get("https://example.invalid")


# --- end to end on the synthetic P1 project ------------------------------------------------------


def seed_resources(root: Path) -> None:
    """Synthetic HGNC/CollecTRI snapshots placed in the cache so the stage makes no network call."""
    hgnc_dir = root / "data" / "external" / "hgnc" / "hgnc_complete_set_2000-01-01"
    hgnc_dir.mkdir(parents=True)
    hgnc = hgnc_frame(
        [
            ("HGNC:10", "TF_A", "TFA-1", ""),
            ("HGNC:11", "TF_B", "", ""),
            ("HGNC:12", "GENE1", "", ""),
            ("HGNC:13", "MATR3", "", ""),
            ("HGNC:14", "NA", "", ""),
            ("HGNC:15", "SIG_ONLY", "", ""),
        ]
    )
    hgnc.to_csv(hgnc_dir / "hgnc_complete_set_2000-01-01.tsv", sep="\t", index=False)
    rows = [
        ("TF_A", g, w, "CollecTRI:1", "PMID")
        for g, w in [("GENE1", 1.0), ("TF_B", -1.0), ("MATR3", 1.0), ("SIG_ONLY", 1.0), ("TF_A", 1.0)]
    ]
    rows += [("TF_B", "GENE1", 1.0, "", "default activation"), ("AP1", "GENE1", 1.0, "CollecTRI:2", "PMID")]
    collectri_dir = root / "data" / "external" / "collectri" / "zenodo-1"
    collectri_dir.mkdir(parents=True)
    lines = ["source,target,weight,resources,references,sign_decision"]
    lines += [f"{s},{t},{w},CollecTRI,{r},{d}" for s, t, w, r, d in rows]
    (collectri_dir / "CollecTRI_regulons.csv").write_text("\n".join(lines) + "\n")
    for directory, name in ((hgnc_dir, "hgnc_complete_set_2000-01-01.tsv"), (collectri_dir, "CollecTRI_regulons.csv")):
        (directory / "provenance.json").write_text(
            json.dumps(
                {
                    "sha256": hashlib.sha256((directory / name).read_bytes()).hexdigest(),
                    "retrieved_at": "2000-01-01",
                    "publisher_md5_verified": True,
                    "license": "synthetic",
                    "version": "synthetic",
                    "doi": None,
                }
            )
        )
    header = "tier,pmid,year,journal,first_author,title,doi"
    (root / "files" / "seeds_a.csv").write_text(f"{header}\nA,1,2020,J,X,T,d\nA,2,2020,J,X,T2,d2\n")
    (root / "files" / "seeds_b.csv").write_text(f"{header}\nB,2,2020,J,X,T2,d2\n")
    ranking = {
        "schema_version": 1,
        "candidate_generation": {
            "rule_version": "test",
            "cell_types": ["AT1"],
            "resources": {
                "hgnc": {"archive_date": "2000-01-01"},
                "collectri": {
                    "zenodo_record": "1",
                    "filename": "CollecTRI_regulons.csv",
                    "complex_regulators": ["AP1"],
                },
                "seed_publication_lists": {"a": "files/seeds_a.csv", "b": "files/seeds_b.csv"},
                "expected_unique_pmids": 2,
            },
            "concordance": {
                "min_targets": 3,
                "primary_sign_bases": ["pmid_evidence", "tf_regulon_majority"],
                "sensitivity_sign_bases": ["pmid_evidence", "tf_regulon_majority", "default_activation"],
            },
            "extra_tfs_per_comparison": 1,
            "targets_per_candidate": 2,
        },
    }
    (root / "configs" / "ranking.yaml").write_text(yaml.safe_dump(ranking))
    (root / "configs" / "literature.yaml").write_text(
        yaml.safe_dump({"schema_version": 1, "retrieval_queue": QUEUE.model_dump()})
    )


def test_candidate_stage_end_to_end_verifies_and_replays_without_network(synthetic_project, monkeypatch):
    from regkg.analysis.stage import run_candidates
    from regkg.analysis.verify import verify_candidate_artifact
    from regkg.project_data.ingest import run_ingest

    root = synthetic_project.parents[1]
    loaded = load_project_config(synthetic_project, repo_root=root)
    ingest = run_ingest(loaded)
    seed_resources(root)
    monkeypatch.setattr(httpx, "get", lambda *a, **k: pytest.fail("network access attempted"))
    args = (loaded, ingest.ingest_key, "AT1", root / "configs" / "ranking.yaml", root / "configs" / "literature.yaml")

    first = run_candidates(*args)
    assert first.status is StageStatus.SUCCEEDED and first.network_requests == 0
    assert [r for r in verify_candidate_artifact(first.artifact_dir, root) if not r.passed] == []
    candidates = pd.read_parquet(first.artifact_dir / "candidates.parquet")
    assert set(candidates.groupby("comparison_id")["tf_hgnc_id"].agg(set).map(lambda s: "HGNC:10" in s)) == {True}
    assert candidates["connectivity_rank"].isna().all()
    before = {p.name: p.read_bytes() for p in first.artifact_dir.iterdir()}

    second = run_candidates(*args)
    assert second.status is StageStatus.REUSED and second.candidate_key == first.candidate_key
    assert second.network_requests == 0
    assert {p.name: p.read_bytes() for p in first.artifact_dir.iterdir()} == before  # no duplicate or rewrite


def test_candidate_config_rejects_unknown_fields(tmp_path):
    path = tmp_path / "ranking.yaml"
    config = yaml.safe_load(Path("configs/ranking.yaml").read_text())
    config["candidate_generation"]["extra_tfs_per_comparisn"] = 5
    path.write_text(yaml.safe_dump(config))
    with pytest.raises(ConfigError, match="extra_tfs_per_comparisn"):
        load_candidate_config(path)


def configure(root: Path, config_path: Path, candidate_updates: dict, concordance_updates: dict, seeds=None) -> None:
    ranking_path = root / "configs" / "ranking.yaml"
    ranking = yaml.safe_load(ranking_path.read_text())
    ranking["candidate_generation"].update(candidate_updates)
    ranking["candidate_generation"]["concordance"].update(concordance_updates)
    ranking_path.write_text(yaml.safe_dump(ranking))
    if seeds is not None:
        project = yaml.safe_load(config_path.read_text())
        project["at1_scope"]["tf_seeds"] = seeds
        config_path.write_text(yaml.safe_dump(project, sort_keys=False))


@pytest.mark.parametrize(
    ("case", "candidate_updates", "concordance_updates", "seeds"),
    [
        ("no_eligible_regulators", {}, {"min_targets": 50}, None),
        ("empty_primary_network", {}, {"primary_sign_bases": ["tf_regulon_majority"]}, None),
        ("zero_target_limit", {"targets_per_candidate": 0}, {}, None),
        ("seed_without_connectivity_or_targets", {"extra_tfs_per_comparison": 0}, {}, ["GENE1"]),
    ],
)
def test_candidate_stage_empty_result_paths(
    synthetic_project, monkeypatch, case, candidate_updates, concordance_updates, seeds
):
    from regkg.analysis.stage import run_candidates
    from regkg.analysis.verify import verify_candidate_artifact
    from regkg.project_data.ingest import run_ingest

    root = synthetic_project.parents[1]
    ingest = run_ingest(load_project_config(synthetic_project, repo_root=root))
    seed_resources(root)
    configure(root, synthetic_project, candidate_updates, concordance_updates, seeds)
    loaded = load_project_config(synthetic_project, repo_root=root)
    monkeypatch.setattr(httpx, "get", lambda *a, **k: pytest.fail("network access attempted"))
    args = (loaded, ingest.ingest_key, "AT1", root / "configs" / "ranking.yaml", root / "configs" / "literature.yaml")

    first = run_candidates(*args)
    assert first.status is StageStatus.SUCCEEDED
    assert [r for r in verify_candidate_artifact(first.artifact_dir, root) if not r.passed] == []
    read = lambda name: pd.read_parquet(first.artifact_dir / name)  # noqa: E731
    candidates, targets, queue = (
        read("candidates.parquet"),
        read("candidate_targets.parquet"),
        read("retrieval_queue.parquet"),
    )
    concordance, observations = read("concordance.parquet"), read("candidate_chromlinker_observations.parquet")
    comparisons = read("comparisons.parquet")
    seed_ids = {"GENE1": "HGNC:12", "TF_A": "HGNC:10"}
    expected_seeds = {seed_ids[s] for s in (seeds or ["TF_A"])}
    for comparison_id in comparisons["comparison_id"]:  # seeds survive in every comparison object
        rows = candidates[candidates["comparison_id"] == comparison_id]
        assert expected_seeds <= set(rows.loc[rows["is_seed"], "tf_hgnc_id"])
    assert set(candidates["tf_hgnc_id"]) <= set(queue.loc[queue["query_type"] == TYPE_CONTEXT, "tf_hgnc_id"])
    assert set(queue["search_status"]) == {STATUS_NOT_SEARCHED}

    if case in {"no_eligible_regulators", "empty_primary_network"}:
        primary = concordance[concordance["sign_policy"] == PRIMARY_POLICY]
        assert not primary["eligible"].any() and primary["ulm_score"].isna().all()
        assert candidates["ulm_score"].isna().all() and (~candidates["is_seed"]).sum() == 0
        if case == "no_eligible_regulators":
            assert len(primary) > 0  # coverage recorded, not dropped
        else:
            assert primary.empty  # no prior row fabricated
    if case in {"zero_target_limit", "seed_without_connectivity_or_targets"}:
        assert targets.empty and list(targets.columns) == schemas.CANDIDATE_TARGETS.names
        assert set(queue["query_type"]) == {TYPE_CONTEXT}  # TF-only queries, no invented target
    if case == "seed_without_connectivity_or_targets":
        assert observations.empty and list(observations.columns) == schemas.CANDIDATE_CHROMLINKER.names
        assert not candidates["tf_in_chromlinker"].any()
        assert candidates["missing_component_reasons"].map(lambda r: "tf_absent_from_chromlinker" in r).all()
        assert candidates["chromlinker_case_context_label"].notna().all()  # the context exists; the TF lacks rows

    before = {p.name: p.read_bytes() for p in first.artifact_dir.iterdir()}
    second = run_candidates(*args)
    assert second.status is StageStatus.REUSED and second.network_requests == 0
    assert {p.name: p.read_bytes() for p in first.artifact_dir.iterdir()} == before
