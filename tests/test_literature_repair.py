"""Regression tests for P3 review findings R1-R4 (synthetic fixtures; engineering only)."""

from __future__ import annotations

import json
import sys
import types
from pathlib import Path

import httpx
import pandas as pd
import pytest
import yaml

from regkg.config import BundleConfig, EmbeddingSection, RetrievalConfig
from regkg.literature import embeddings as emb
from regkg.literature import parse as parse_module
from regkg.literature.http import NcbiSettings, SourceClient
from regkg.literature.parse import parse_bioc, parse_jats
from regkg.literature.passages import (
    ALIGN_EXTERNAL_MISMATCH,
    CONFLICTING,
    CONSISTENT,
    HINT_ONLY,
    candidate_name_mentions,
    pubtator_mentions,
    reconcile,
)
from regkg.literature.retrieval import BM25Okapi, QueryTerms, assemble_bundles, rank_passages, tokenize
from regkg.literature.verify import embedding_contract_check, readiness_problems
from regkg.models import StageStatus

TEXT = b"""<article><front><article-meta><title-group><article-title>TEAD1 study</article-title></title-group>
</article-meta></front><body><sec><title>Results</title><p>TEAD1 binds the promoter.</p></sec></body></article>"""
HUMAN = {"7003": "HGNC:11714", "10413": "HGNC:16262"}


def tf_mentions(document, identifier: str | None, text: str = "TEAD1", offset: int = 0):
    annotation = {
        "id": "a",
        "text": text,
        "infons": {"type": "Gene", "identifier": identifier},
        "locations": [{"offset": offset, "length": 5}],
    }
    pubtator = {"passages": [{"offset": 0, "text": "TEAD1 study", "annotations": [annotation]}]} if identifier else {}
    names = candidate_name_mentions(document, {"HGNC:11714": ["TEAD1"]})
    records = reconcile(names + pubtator_mentions(document, pubtator, HUMAN))
    title = [m for m in records if m.start == 0]
    return next(m for m in title if m.source == "exact_candidate_name"), [m for m in title if m.source == "pubtator"]


# --- R1: candidate-name hits vs species-qualified entity identity --------------------------------


def test_mouse_identifier_conflicts_with_human_candidate_name():
    name, (source,) = tf_mentions(parse_jats("p:x", TEXT), "21676")  # NCBI Gene 21676 is mouse Tead1
    assert name.hgnc_id is None and name.species_taxon is None and name.candidate_hgnc_id == "HGNC:11714"
    assert name.identity_status == CONFLICTING and name.linked_mention_ids == [source.mention_id]
    assert source.hgnc_id is None and source.resolution == "unresolved_non_human_or_unmapped"
    assert source.external_identifier == "21676"  # raw ID kept; never mapped onto the human ortholog


def test_name_hit_without_source_identifier_stays_species_unknown():
    name, sources = tf_mentions(parse_jats("p:x", TEXT), None)
    assert sources == [] and name.identity_status == HINT_ONLY
    assert name.hgnc_id is None and name.resolution == "candidate_name_match_species_unknown"


def test_consistent_human_identifier_resolves_only_through_the_source():
    name, (source,) = tf_mentions(parse_jats("p:x", TEXT), "7003")
    assert source.hgnc_id == "HGNC:11714" and source.species_taxon == "9606"
    assert name.identity_status == CONSISTENT and name.hgnc_id is None  # identity lives on the source record


@pytest.mark.parametrize("identifier", ["7003;21676", "10413"])  # ambiguous IDs; a different human gene
def test_conflicting_same_span_identifiers_are_exposed(identifier):
    name, (source,) = tf_mentions(parse_jats("p:x", TEXT), identifier)
    assert name.identity_status == CONFLICTING
    assert source.hgnc_id in (None, "HGNC:16262")


def test_annotation_disagreeing_with_its_own_offsets_attaches_nothing():
    annotation = {
        "id": "a",
        "text": "TEAD1",
        "infons": {"type": "Gene", "identifier": "7003"},
        "locations": [{"offset": 6, "length": 5}],
    }  # the source slice there is "study"
    pubtator = {"passages": [{"offset": 0, "text": "TEAD1 study", "annotations": [annotation]}]}
    (source,) = pubtator_mentions(parse_jats("p:x", TEXT), pubtator, HUMAN)
    assert source.alignment == ALIGN_EXTERNAL_MISMATCH and source.start is None and source.hgnc_id is None
    assert source.identity_status == "not_attached" and source.external_offset == 6


# --- R2: table structure and conservative context ------------------------------------------------


def table_article(thead: str, body: str, foot: str = "") -> bytes:
    return (
        f"<article><front><article-meta><title-group><article-title>T</article-title></title-group>"
        f"</article-meta></front><body><sec><title>R</title><table-wrap id='t1'><label>Table 1</label>"
        f"<caption><p>TEAD1 targets</p></caption><table>{thead}<tbody>{body}</tbody></table>{foot}"
        f"</table-wrap></sec></body></article>"
    ).encode()


def test_spanned_multirow_headers_associate_each_value_with_its_column():
    xml = table_article(
        "<thead><tr><th rowspan='2'>Gene</th><th colspan='2'>Treatment</th></tr>"
        "<tr><th>Control</th><th>IPF</th></tr></thead>",
        "<tr><td>TEAD1</td><td>1</td><td>3</td></tr>",
    )
    row = next(p for p in parse_jats("p:x", xml).passages if p.kind == "table_row")
    assert row.table_structure == "header_grid_expanded"
    assert [(c["text"], c["header"]) for c in row.cells] == [
        ("TEAD1", "Gene"),
        ("1", "Treatment / Control"),
        ("3", "Treatment / IPF"),
    ]


def test_body_rowspan_is_carried_and_marked():
    xml = table_article(
        "<thead><tr><th>Gene</th><th>Value</th></tr></thead>",
        "<tr><td rowspan='2'>TEAD1</td><td>1</td></tr><tr><td>2</td></tr>",
    )
    rows = [p for p in parse_jats("p:x", xml).passages if p.kind == "table_row"]
    assert rows[1].text == "2"  # source text is the row's own cells
    assert rows[1].cells[0] == {
        "text": "TEAD1",
        "col_start": 0,
        "col_span": 1,
        "carried_from_rowspan": True,
        "header": "Gene",
    }


def test_unsupported_layout_produces_no_header_association():
    xml = table_article(
        "<thead><tr><th>Gene</th><th>Value</th></tr></thead>", "<tr><td>TEAD1</td><td>1</td><td>extra</td></tr>"
    )
    row = next(p for p in parse_jats("p:x", xml).passages if p.kind == "table_row")
    assert row.table_structure.startswith("unsupported_layout:") and row.cells is None and row.table_header is None


def bundles_for(document, query_terms, max_chars=6000, max_passages=3):
    passages = document.passages
    bm25 = BM25Okapi([tokenize(p.text) for p in passages])
    query = QueryTerms("q", 1, "H:1", query_terms, None, [], ["x"], ["c"])
    hits = {
        "q": rank_passages(
            query,
            passages,
            ["p:x"] * len(passages),
            bm25,
            None,
            RetrievalConfig(hits_per_query=20, rrf_k=60, bm25_k1=1.5, bm25_b=0.75),
        )
    }
    config = BundleConfig(
        max_bundles=20, max_passages=max_passages, max_chars=max_chars, max_per_paper=20, max_per_candidate_tf=20
    )
    return assemble_bundles([query], hits, {"p:x": document}, {p.passage_id: p for p in passages}, config)[0]


def row_bundle(bundles):
    return next(b for b in bundles if any(p["is_anchor"] and p["kind"] == "table_row" for p in b.passages))


def test_table_row_without_header_is_not_extraction_ready():
    bundle = row_bundle(
        bundles_for(parse_jats("p:x", table_article("", "<tr><td>TEAD1</td><td>1</td></tr>")), ["TEAD1"])
    )
    assert not bundle.extraction_ready and "table_header_unavailable:no_header" in bundle.incomplete_reasons


def test_flattened_bioc_table_is_flagged_and_not_extraction_ready():
    bioc = {
        "passages": [
            {"offset": 0, "text": "TEAD1 paper", "infons": {"section_type": "TITLE", "type": "front"}},
            {"offset": 20, "text": "TEAD1 1 3", "infons": {"section_type": "TABLE", "type": "table", "id": "t1"}},
        ]
    }
    document = parse_bioc("p:x", json.dumps(bioc).encode())
    row = next(p for p in document.passages if p.kind == "table_row")
    assert row.table_structure == "flattened_bioc_no_cell_structure" and row.cells is None
    bundle = row_bundle(bundles_for(document, ["TEAD1"]))
    assert not bundle.extraction_ready
    assert "table_header_unavailable:flattened_bioc_no_cell_structure" in bundle.incomplete_reasons


def test_qualifying_footnote_that_does_not_fit_marks_the_bundle_incomplete():
    xml = table_article(
        "<thead><tr><th>Gene</th><th>Value</th></tr></thead>",
        "<tr><td>TEAD1</td><td>1</td></tr>",
        "<table-wrap-foot><p>" + "Values are means of n = 3 donors; " * 20 + "</p></table-wrap-foot>",
    )
    bundle = row_bundle(bundles_for(parse_jats("p:x", xml), ["TEAD1"], max_chars=200))
    assert not bundle.extraction_ready
    assert any(r.startswith("context_not_included:table_footnote") for r in bundle.incomplete_reasons)
    assert all(len(p["text"]) <= 200 for p in bundle.passages)  # nothing truncated


def test_verification_rejects_false_completeness():
    document = parse_jats("p:x", table_article("", "<tr><td>TEAD1</td><td>1</td></tr>"))
    bundle = row_bundle(bundles_for(document, ["TEAD1"])).to_json()
    passages = pd.DataFrame([{**p.__dict__, "publication_id": "p:x"} for p in document.passages])
    assert readiness_problems([bundle], passages) == 0
    forged = {**bundle, "extraction_ready": True, "incomplete_reasons": []}
    assert readiness_problems([forged], passages) >= 1


# --- R3: content in artifact and record identity -------------------------------------------------


def test_passage_identity_changes_with_canonical_text_or_rule(monkeypatch):
    before = parse_jats("p:x", TEXT).passages[1].passage_id
    changed = parse_jats("p:x", TEXT.replace(b"binds", b"occupies")).passages[1]
    assert changed.passage_id != before and changed.locator == parse_jats("p:x", TEXT).passages[1].locator
    monkeypatch.setattr(parse_module, "TEXT_RULE", "ws-collapse-nfc-block-space-4")
    assert parse_jats("p:x", TEXT).passages[1].passage_id != before


def synthetic_chain(synthetic_project):
    from regkg.analysis.stage import run_candidates
    from regkg.config import load_project_config
    from regkg.project_data.ingest import run_ingest
    from tests.test_candidates import seed_resources

    root = synthetic_project.parents[1]
    loaded = load_project_config(synthetic_project, repo_root=root)
    ingest = run_ingest(loaded)
    seed_resources(root)
    literature = root / "configs" / "literature.yaml"
    base = yaml.safe_load(Path("configs/literature.yaml").read_text())
    config = yaml.safe_load(literature.read_text())
    config.update({k: base[k] for k in ("search", "fetch", "retrieval", "bundles", "embeddings")})
    config["retrieval_queue"]["max_live_queries"] = 2
    literature.write_text(yaml.safe_dump(config))
    candidates = run_candidates(loaded, ingest.ingest_key, "AT1", root / "configs" / "ranking.yaml", literature)
    return loaded, candidates.candidate_key, literature


def routes(title: str, jats_word: bytes = b"binds"):
    efetch = (
        b"<PubmedArticleSet><PubmedArticle><MedlineCitation><PMID>111</PMID><Article><ArticleTitle>"
        + title.encode()
        + b"</ArticleTitle><Abstract><AbstractText>TF_A in lung.</AbstractText></Abstract>"
        b"</Article></MedlineCitation><PubmedData><ArticleIdList><ArticleId IdType='pmc'>PMC9</ArticleId>"
        b"</ArticleIdList></PubmedData></PubmedArticle></PubmedArticleSet>"
    )

    def handler(request: httpx.Request) -> httpx.Response:
        if request.url.host == "eutils.ncbi.nlm.nih.gov":
            if request.url.path.endswith("esearch.fcgi"):
                return httpx.Response(200, json={"esearchresult": {"count": "1", "idlist": ["111"]}})
            return httpx.Response(200, content=efetch)
        if request.url.path.endswith("fullTextXML"):
            return httpx.Response(200, content=TEXT.replace(b"TEAD1", b"TF_A").replace(b"binds", jats_word))
        if request.url.host == "www.ebi.ac.uk":
            return httpx.Response(
                200,
                json={
                    "hitCount": 1,
                    "resultList": {
                        "result": [
                            {
                                "id": "111",
                                "source": "MED",
                                "pmid": "111",
                                "pmcid": "PMC9",
                                "title": title,
                                "isOpenAccess": "Y",
                            }
                        ]
                    },
                },
            )
        return httpx.Response(200, json={"PubTator3": []})

    return handler


def test_search_and_fetch_identity_follow_response_bytes(synthetic_project, monkeypatch):
    from regkg.workflows import literature as flow

    monkeypatch.setattr("time.sleep", lambda _: None)
    loaded, candidate_key, literature = synthetic_chain(synthetic_project)

    def client(handler, cache: str):
        return SourceClient(
            loaded.data_root / "external" / cache, NcbiSettings("tool"), 1, 1, httpx.MockTransport(handler)
        )

    first = flow.run_search(loaded, candidate_key, 1, literature, client=client(routes("TF_A in lung A"), "c1"))
    same = flow.run_search(loaded, candidate_key, 1, literature, client=client(routes("TF_A in lung A"), "c2"))
    assert same.status is StageStatus.REUSED and same.key == first.key  # same bytes, fetched fresh -> reuse
    before = {p.name: p.read_bytes() for p in first.artifact_dir.iterdir()}
    changed = flow.run_search(loaded, candidate_key, 1, literature, client=client(routes("TF_A in lung B"), "c3"))
    assert changed.status is StageStatus.SUCCEEDED and changed.key != first.key  # same requests, new bytes
    assert {p.name: p.read_bytes() for p in first.artifact_dir.iterdir()} == before  # prior artifact intact

    fetched = flow.run_fetch(loaded, first.key, literature, client=client(routes("TF_A in lung A"), "f1"))
    again = flow.run_fetch(loaded, first.key, literature, client=client(routes("TF_A in lung A"), "f2"))
    assert again.status is StageStatus.REUSED and again.key == fetched.key
    revised = flow.run_fetch(
        loaded, first.key, literature, client=client(routes("TF_A in lung A", jats_word=b"occupies"), "f3")
    )
    assert revised.status is StageStatus.SUCCEEDED and revised.key != fetched.key
    old = {
        p.passage_id
        for p in flow.load_documents(fetched.artifact_dir)[
            next(iter(flow.load_documents(fetched.artifact_dir)))
        ].passages
    }
    new = {p.passage_id for d in flow.load_documents(revised.artifact_dir).values() for p in d.passages}
    assert old != new  # revised canonical text gets new passage identities


# --- R4: embedding contract enforced before encoding ---------------------------------------------


class RecordingOllama:
    calls: list = []

    def __init__(self, **kwargs):
        pass

    def embed_documents(self, texts):
        RecordingOllama.calls.append(texts)
        return [[1.0, 0.0] for _ in texts]

    def embed_query(self, text):
        RecordingOllama.calls.append([text])
        return [1.0, 0.0]


def ollama_backend(monkeypatch, context=1024, tokenizer="bert", max_chunk_chars=1000):
    from regkg.config import resolve_model_settings

    RecordingOllama.calls = []
    monkeypatch.setitem(sys.modules, "langchain_ollama", types.SimpleNamespace(OllamaEmbeddings=RecordingOllama))
    monkeypatch.setattr(
        emb,
        "ollama_model_metadata",
        lambda url, name: {
            "digest": "d",
            "embedding_length": 2,
            "context_length": context,
            "tokenizer_model": tokenizer,
            "special_tokens": 2,
        },
    )
    settings = resolve_model_settings({"EMBEDDINGS_ENABLED": "true", "EMBEDDING_MODEL": "ollama:m:latest"})
    return emb.build_embeddings(settings, EmbeddingSection(max_chunk_chars=max_chunk_chars))


def test_oversized_chunk_limit_is_rejected_before_any_request(monkeypatch):
    with pytest.raises(emb.EmbeddingSetupError, match="exceeds the verified bound 1022"):
        ollama_backend(monkeypatch, max_chunk_chars=5000)
    assert RecordingOllama.calls == []


def test_smaller_model_context_tightens_the_bound(monkeypatch):
    with pytest.raises(emb.EmbeddingSetupError, match="verified bound 510"):
        ollama_backend(monkeypatch, context=512, max_chunk_chars=1000)
    assert ollama_backend(monkeypatch, context=512, max_chunk_chars=500).contract.max_input_chars == 500


def test_unverifiable_tokenizer_is_refused(monkeypatch):
    with pytest.raises(emb.EmbeddingSetupError, match="cannot verify"):
        ollama_backend(monkeypatch, tokenizer="gpt2")


def test_oversized_query_and_chunk_are_rejected_not_truncated(monkeypatch, tmp_path):
    backend = ollama_backend(monkeypatch, max_chunk_chars=100)
    store = emb.VectorStore(tmp_path, backend)
    with pytest.raises(emb.EmbeddingInputError):
        store.embed_query("x" * 101, 2)
    with pytest.raises(emb.EmbeddingInputError):
        store.encode(["ok", "y" * 101], 8, 2)
    assert RecordingOllama.calls == []  # rejected before any encoding request


def test_sentence_transformers_contract_and_backend_aware_verification(monkeypatch):
    from regkg.config import resolve_model_settings

    class FakeHF:
        def __init__(self, **kwargs):
            self._client = types.SimpleNamespace(
                max_seq_length=6, tokenizer=lambda text, add_special_tokens: {"input_ids": [0, *text.split(), 0]}
            )

    monkeypatch.setitem(sys.modules, "langchain_huggingface", types.SimpleNamespace(HuggingFaceEmbeddings=FakeHF))
    settings = resolve_model_settings({"EMBEDDINGS_ENABLED": "true", "EMBEDDING_MODEL": "sentence_transformers:O/M"})
    backend = emb.build_embeddings(settings, EmbeddingSection())
    contract = backend.contract
    assert contract.method == "tokenizer_token_count" and contract.check("a b c d") == 6
    with pytest.raises(emb.EmbeddingInputError):
        contract.check("a b c d e")
    record = {
        "dense_status": "ok",
        "selector": backend.selector,
        "identity": backend.identity,
        "encoding_contract": contract.to_record(),
        "largest_input_size": 6,
        "largest_query_size": 4,
        "size_unit": "tokens",
        "vector_dimension": 384,
    }
    ok, detail = embedding_contract_check(record)
    assert ok and "tokenizer_token_count" in detail  # no Ollama metadata required
    assert not embedding_contract_check({**record, "largest_input_size": 7})[0]
    ollama = {
        **record,
        "encoding_contract": {
            **contract.to_record(),
            "method": "wordpiece_char_bound",
            "max_input_chars": 1000,
            "context_tokens": 1024,
            "special_tokens": 2,
        },
        "largest_input_size": 1001,
        "size_unit": "chars",
    }
    assert not embedding_contract_check(ollama)[0]


# --- Residual F1: table identity without XML ids; caption/footnote readiness ---------------------


def idless_tables(caption_1: str = "<caption><p>Candidate targets</p></caption>", foot_1: str = "") -> bytes:
    foot_1 = foot_1 or "Values are indirect associations, not binding measurements."
    return (
        "<article><front><article-meta><title-group><article-title>Lung study</article-title></title-group>"
        "</article-meta></front><body><sec><title>Results</title><p>Expression was profiled.</p>"
        f"<table-wrap><label>Table 1</label>{caption_1}<table><thead><tr><th>Gene</th><th>Value</th></tr></thead>"
        f"<tbody><tr><td>TEAD1</td><td>2</td></tr></tbody></table>"
        f"<table-wrap-foot><p>{foot_1}</p></table-wrap-foot></table-wrap>"
        "<table-wrap><table><thead><tr><th>Gene</th><th>Score</th></tr></thead>"
        "<tbody><tr><td>TEAD1</td><td>5</td></tr></tbody></table>"
        "<table-wrap-foot><p>Scores are from a mouse model.</p></table-wrap-foot></table-wrap>"
        "</sec></body></article>"
    ).encode()


def row_bundles(bundles):
    return [b for b in bundles if any(p["is_anchor"] and p["kind"] == "table_row" for p in b.passages)]


def frame(document):
    return pd.DataFrame([{**p.__dict__, "publication_id": "p:x"} for p in document.passages])


def test_idless_tables_get_distinct_identities_and_keep_their_own_context():
    document = parse_jats("p:x", idless_tables())
    tables = [p for p in document.passages if p.kind.startswith("table_")]
    assert all(p.item_id is None and p.table_id for p in tables)  # no XML id; internal identity instead
    rows = [p for p in tables if p.kind == "table_row"]
    assert len({p.table_id for p in rows}) == 2  # the two id-less tables are never merged
    first, second = row_bundles(bundles_for(document, ["TEAD1"]))
    texts = [p["text"] for p in first.passages]
    assert "Table 1 Candidate targets" in texts
    assert "Values are indirect associations, not binding measurements." in texts
    assert "Scores are from a mouse model." not in texts
    assert first.extraction_ready
    assert "Values are indirect associations, not binding measurements." not in [p["text"] for p in second.passages]
    assert "Scores are from a mouse model." in [p["text"] for p in second.passages]


def test_missing_or_label_only_caption_is_explicitly_incomplete():
    document = parse_jats("p:x", idless_tables(caption_1=""))
    label_only, absent = row_bundles(bundles_for(document, ["TEAD1"]))
    assert not label_only.extraction_ready and "table_caption_missing:label_only" in label_only.incomplete_reasons
    assert not absent.extraction_ready and "table_caption_missing:absent" in absent.incomplete_reasons
    assert readiness_problems([b.to_json() for b in (label_only, absent)], frame(document)) == 0
    forged = {**absent.to_json(), "extraction_ready": True, "incomplete_reasons": []}
    assert readiness_problems([forged], frame(document)) >= 1


def test_idless_required_footnote_that_does_not_fit_is_incomplete():
    document = parse_jats("p:x", idless_tables(foot_1="Values are means of n = 3 donors; " * 20))
    bundle = row_bundles(bundles_for(document, ["TEAD1"], max_chars=200))[0]
    assert not bundle.extraction_ready
    assert any(r.startswith("context_not_included:table_footnote") for r in bundle.incomplete_reasons)


def test_verifier_rejects_ready_idless_bundle_after_qualifying_context_is_removed():
    document = parse_jats("p:x", idless_tables())
    bundle = row_bundles(bundles_for(document, ["TEAD1"]))[0].to_json()
    assert bundle["extraction_ready"] and readiness_problems([bundle], frame(document)) == 0
    stripped = {**bundle, "passages": [p for p in bundle["passages"] if p["kind"] != "table_footnote"]}
    assert readiness_problems([stripped], frame(document)) >= 1


# --- Residual F1/F2 through artifact verification -------------------------------------------------


def verification_routes():
    base = routes("TF_A in lung A")
    jats = idless_tables().replace(b"TEAD1", b"TF_A")
    # Annotation text TF_A placed at the offset of "study": a deliberately inconsistent record.
    pubtator = {
        "PubTator3": [
            {
                "pmid": 111,
                "passages": [
                    {
                        "offset": 0,
                        "text": "Lung study",
                        "infons": {"section_type": "TITLE", "type": "front"},
                        "annotations": [
                            {
                                "id": "m1",
                                "text": "TF_A",
                                "infons": {"type": "Gene", "identifier": "5555"},
                                "locations": [{"offset": 5, "length": 4}],
                            }
                        ],
                    }
                ],
            }
        ]
    }

    def handler(request: httpx.Request) -> httpx.Response:
        if request.url.path.endswith("fullTextXML"):
            return httpx.Response(200, content=jats)
        if "biocjson" in request.url.path:
            return httpx.Response(200, json=pubtator)
        return base(request)

    return handler


def republish(directory: Path, name: str) -> None:
    """Simulate a producer bug: a changed output published with a consistent checksum."""
    from regkg.provenance import sha256_file

    manifest = json.loads((directory / "manifest.json").read_text())
    for output in manifest["outputs"]:
        if output["path"] == name:
            output["sha256"] = sha256_file(directory / name)
    (directory / "manifest.json").write_text(json.dumps(manifest))


def test_artifact_verification_accepts_quarantine_and_rejects_forgeries(synthetic_project, monkeypatch):
    from regkg.literature.verify import verify_literature
    from regkg.workflows import literature as flow

    monkeypatch.setattr("time.sleep", lambda _: None)
    loaded, candidate_key, literature = synthetic_chain(synthetic_project)

    def client():
        return SourceClient(
            loaded.data_root / "external" / "cache",
            NcbiSettings("tool"),
            1,
            1,
            httpx.MockTransport(verification_routes()),
        )

    search = flow.run_search(loaded, candidate_key, 1, literature, client=client())
    fetched = flow.run_fetch(loaded, search.key, literature, client=client())
    retrieved = flow.run_retrieve(loaded, fetched.key, literature, process_env={"EMBEDDINGS_ENABLED": "false"})
    mentions = pd.read_parquet(fetched.artifact_dir / "mentions.parquet")
    quarantined = mentions[mentions["alignment"] == ALIGN_EXTERNAL_MISMATCH]
    assert len(quarantined) == 1 and quarantined["external_identifier"].tolist() == ["5555"]
    bundles = [json.loads(line) for line in (retrieved.artifact_dir / "bundles.jsonl").read_text().splitlines()]
    anchors = [b for b in bundles if any(p["is_anchor"] and p["kind"] == "table_row" for p in b["passages"])]
    assert any(b["extraction_ready"] for b in anchors) and any(not b["extraction_ready"] for b in anchors)
    results = verify_literature(retrieved.artifact_dir, loaded.repo_root, literature)
    assert [r for r in results if not r.passed] == []  # the quarantined record is valid

    ready = next(b for b in anchors if b["extraction_ready"])
    forged = [
        {**b, "passages": [p for p in b["passages"] if p["kind"] != "table_footnote"]} if b is ready else b
        for b in bundles
    ]
    (retrieved.artifact_dir / "bundles.jsonl").write_text("".join(json.dumps(b) + "\n" for b in forged))
    republish(retrieved.artifact_dir, "bundles.jsonl")
    failed = {r.name for r in verify_literature(retrieved.artifact_dir, loaded.repo_root, literature) if not r.passed}
    assert "tables:structure_and_bundle_readiness" in failed

    index = quarantined.index[0]
    mentions.loc[index, ["hgnc_id", "resolution", "species_taxon"]] = ["HGNC:1", "resolved_ncbi_gene_human", "9606"]
    mentions.to_parquet(fetched.artifact_dir / "mentions.parquet", index=False)
    republish(fetched.artifact_dir, "mentions.parquet")
    failed = {r.name for r in verify_literature(retrieved.artifact_dir, loaded.repo_root, literature) if not r.passed}
    assert {"fetch:mention_alignment", "mentions:identity_separation_and_conflicts"} <= failed
