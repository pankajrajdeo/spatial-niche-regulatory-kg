"""P3 behavioral checks with mocked transports and tiny synthetic documents (engineering only)."""

from __future__ import annotations

import json
import sys
import types
from pathlib import Path

import httpx
import numpy as np
import pytest

from regkg.config import BundleConfig, EmbeddingSection, RetrievalConfig, resolve_model_settings
from regkg.literature import embeddings as emb
from regkg.literature.fetch import fetch_full_text, fetch_pubmed_record, parse_work_id
from regkg.literature.http import NcbiSettings, NotFound, SourceClient, SourceError
from regkg.literature.parse import ParseError, parse_bioc, parse_jats, parse_pubmed_abstract
from regkg.literature.passages import ALIGN_EXACT, ALIGN_UNALIGNED, pubtator_mentions
from regkg.literature.publications import normalize_doi, resolve_publications, select_corpus, selection_features
from regkg.literature.retrieval import BM25Okapi, QueryTerms, assemble_bundles, rank_passages, tokenize
from regkg.literature.search import (
    STATUS_EMPTY,
    STATUS_FAILED,
    STATUS_PARTIAL,
    STATUS_SUCCESS,
    QuerySpec,
    SourceRecord,
    search_papers,
    translate_query,
    validate_limit,
)
from regkg.literature.xml import UnsafeXMLError, parse_xml

SPEC = QuerySpec("query:1", ["TEAD1", "TEF-1"], ["NTM"], ["ChIP"])
EFETCH = b"""<?xml version="1.0"?>
<!DOCTYPE PubmedArticleSet PUBLIC "-//NLM//DTD PubMedArticle//EN" "https://dtd.nlm.nih.gov/ncbi/pubmed/out/pubmed_250101.dtd">
<PubmedArticleSet><PubmedArticle><MedlineCitation><PMID>111</PMID><Article><Journal><Title>J</Title>
<JournalIssue><PubDate><Year>2020</Year></PubDate></JournalIssue></Journal>
<ArticleTitle>TEAD1 in alveolar cells</ArticleTitle><Abstract><AbstractText Label="RESULTS">TEAD1 did not
bind the NTM promoter.</AbstractText></Abstract><PublicationTypeList><PublicationType>Journal Article</PublicationType>
</PublicationTypeList></Article></MedlineCitation><PubmedData><ArticleIdList><ArticleId IdType="pubmed">111</ArticleId>
<ArticleId IdType="pmc">PMC9</ArticleId><ArticleId IdType="doi">10.1/ABC</ArticleId></ArticleIdList></PubmedData>
</PubmedArticle></PubmedArticleSet>"""
EPMC_RESULT = {
    "hitCount": 2,
    "resultList": {
        "result": [
            {
                "id": "111",
                "source": "MED",
                "pmid": "111",
                "pmcid": "PMC9",
                "doi": "https://doi.org/10.1/abc",
                "title": "T",
                "isOpenAccess": "Y",
                "inPMC": "Y",
            },
            {
                "id": "PPR1",
                "source": "PPR",
                "doi": "10.1/preprint",
                "title": "TEAD1 in alveolar cells",
                "pubTypeList": {"pubType": ["Preprint"]},
            },
        ]
    },
}


def client(tmp_path: Path, handler, retries: int = 1, api_key: str | None = "dummy-key") -> SourceClient:
    return SourceClient(
        tmp_path / "cache",
        NcbiSettings("tool", "me@example.invalid", api_key),
        timeout_seconds=1,
        max_retries=retries,
        transport=httpx.MockTransport(handler),
    )


def routes(pubmed_count: int = 1, epmc=None, epmc_status: int = 200, pubmed_fail: bool = False):
    seen = []

    def handler(request: httpx.Request) -> httpx.Response:
        seen.append(request)
        if request.url.host == "eutils.ncbi.nlm.nih.gov":
            if pubmed_fail:
                raise httpx.ConnectTimeout("timeout", request=request)
            if request.url.path.endswith("esearch.fcgi"):
                ids = ["111"] if pubmed_count else []
                return httpx.Response(200, json={"esearchresult": {"count": str(pubmed_count), "idlist": ids}})
            return httpx.Response(200, content=EFETCH)
        if request.url.host == "www.ebi.ac.uk":
            if epmc_status != 200:
                return httpx.Response(epmc_status)
            return httpx.Response(200, json=epmc if epmc is not None else EPMC_RESULT)
        return httpx.Response(404)

    return handler, seen


# --- reference adaptation, limits, and source outcomes ----------------------------------------


def test_search_imports_no_agent_reranker_or_model_sdk():
    import subprocess

    code = (
        "import sys, regkg.literature.search, regkg.literature.fetch; "
        "print([m for m in sys.modules if m.split('.')[0] in "
        "{'lungchat','langchain_core','aiohttp','torch','sentence_transformers','langchain_ollama'}])"
    )
    assert (
        subprocess.run([sys.executable, "-c", code], capture_output=True, text=True, check=True).stdout.strip() == "[]"
    )


@pytest.mark.parametrize("value", [0, 11, -1])
def test_result_limits_are_validated_in_the_core(value):
    with pytest.raises(ValueError, match="between 1 and 10"):
        validate_limit(value)


def test_identifier_parsing_retained_from_reference():
    assert parse_work_id("pmid:123") == ("pmid", "123")
    assert parse_work_id("PMC45") == ("pmcid", "PMC45")
    assert parse_work_id("doi:https://doi.org/10.1/AbC") == ("doi", "10.1/abc")
    with pytest.raises(ValueError):
        parse_work_id("title:something")


def test_query_translation_is_source_specific():
    assert translate_query(SPEC, "pubmed") == '("TEAD1"[tiab] OR "TEF-1"[tiab]) AND ("NTM"[tiab]) AND ("ChIP"[tiab])'
    assert translate_query(SPEC, "europepmc") == '("TEAD1" OR "TEF-1") AND ("NTM") AND ("ChIP")'


def test_successful_search_keeps_both_sources_and_key_only_goes_to_eutils(tmp_path):
    handler, seen = routes()
    result = search_papers(SPEC, client(tmp_path, handler), ["pubmed", "europepmc"], 10)
    assert result.status == STATUS_SUCCESS and result.warnings == []
    assert {r.source for r in result.records} == {"pubmed", "europepmc"}
    for request in seen:
        has_key = "api_key" in request.url.params or "email" in request.url.params
        assert has_key == (request.url.host == "eutils.ncbi.nlm.nih.gov")


def test_genuine_zero_results_is_empty_not_failed(tmp_path):
    handler, _ = routes(pubmed_count=0, epmc={"hitCount": 0, "resultList": {"result": []}})
    result = search_papers(SPEC, client(tmp_path, handler), ["pubmed", "europepmc"], 10)
    assert result.status == STATUS_EMPTY and result.records == [] and result.warnings == []


def test_one_source_failure_keeps_surviving_results_and_warning(tmp_path, monkeypatch):
    monkeypatch.setattr("time.sleep", lambda _: None)
    handler, _ = routes(epmc_status=503)
    sources = client(tmp_path, handler)
    result = search_papers(SPEC, sources, ["pubmed", "europepmc"], 10)
    assert result.status == STATUS_PARTIAL and {r.source for r in result.records} == {"pubmed"}
    assert result.warnings == ["Europe PMC was unavailable; coverage may be reduced."]
    failed = [r for r in sources.records if r.outcome == "failed"]
    assert failed[0].attempts == 2 and failed[0].error_kind == "server_error"  # 1 retry


def test_all_sources_failing_is_failed_with_timeout_status(tmp_path, monkeypatch):
    monkeypatch.setattr("time.sleep", lambda _: None)
    handler, _ = routes(epmc_status=500, pubmed_fail=True)
    sources = client(tmp_path, handler, retries=0)
    result = search_papers(SPEC, sources, ["pubmed", "europepmc"], 10)
    assert result.status == STATUS_FAILED and len(result.warnings) == 2
    assert {o.error_kind for o in result.outcomes} == {"timeout", "server_error"}


def test_version_only_europe_pmc_reply_is_a_failure_not_an_empty_result(tmp_path, monkeypatch):
    monkeypatch.setattr("time.sleep", lambda _: None)
    handler, _ = routes(epmc={"version": "6.9"})
    result = search_papers(SPEC, client(tmp_path, handler), ["europepmc"], 10)
    assert result.status == STATUS_FAILED and result.outcomes[0].error_kind == "malformed_response"


def test_cache_serves_successes_and_never_stores_failures_or_credentials(tmp_path, monkeypatch):
    monkeypatch.setattr("time.sleep", lambda _: None)
    handler, seen = routes()
    first = client(tmp_path, handler)
    search_papers(SPEC, first, ["pubmed"], 10)
    before = len(seen)
    second = client(tmp_path, handler)
    search_papers(SPEC, second, ["pubmed"], 10)
    assert len(seen) == before and {r.outcome for r in second.records} == {"cached"}
    assert second.network_requests == {}
    stored = b"".join(p.read_bytes() for p in (tmp_path / "cache").rglob("*") if p.is_file())
    assert b"dummy-key" not in stored and b"me@example.invalid" not in stored
    assert all("api_key" not in r.params and "email" not in r.params for r in second.records)
    failing, _ = routes(epmc_status=503)
    third = client(tmp_path, failing)
    search_papers(SPEC, third, ["europepmc"], 10)
    retry, _ = routes()
    fourth = client(tmp_path, retry)
    assert search_papers(SPEC, fourth, ["europepmc"], 10).status == STATUS_SUCCESS  # failure was not cached


def test_not_found_is_distinct_from_failed_details_request(tmp_path, monkeypatch):
    monkeypatch.setattr("time.sleep", lambda _: None)
    empty = b"<PubmedArticleSet></PubmedArticleSet>"
    ok = client(tmp_path, lambda r: httpx.Response(200, content=empty))
    with pytest.raises(NotFound):
        fetch_pubmed_record(ok, "999")
    broken = client(tmp_path / "b", lambda r: httpx.Response(502), retries=0)
    with pytest.raises(SourceError) as failure:
        fetch_pubmed_record(broken, "999")
    assert not isinstance(failure.value, NotFound) and failure.value.kind == "server_error"
    missing = client(tmp_path / "c", lambda r: httpx.Response(404))
    with pytest.raises(NotFound):
        fetch_full_text(missing, "PMC1")


# --- identity and selection --------------------------------------------------------------------


def test_publication_identity_merges_only_costated_identifiers():
    pubmed = SourceRecord("pubmed", 1, "k", pmid="111", pmcid="PMC9", doi="10.1/ABC", title="TEAD1 in alveolar cells")
    epmc = SourceRecord("europepmc", 1, "k", pmid="111", doi="https://doi.org/10.1/abc", epmc_id="MED:111")
    preprint = SourceRecord(
        "europepmc", 2, "k", doi="10.1/preprint", epmc_id="PPR:PPR1", title="TEAD1 in alveolar cells", is_preprint=True
    )
    clash = SourceRecord("europepmc", 3, "k", pmid="222", doi="10.1/abc", epmc_id="MED:222")
    publications = resolve_publications([("q1", pubmed), ("q2", epmc), ("q1", preprint)])
    merged = next(p for p in publications if p.identifiers.get("pmid") == "111")
    assert merged.identifiers["doi"] == "10.1/abc" and {label for label, _ in merged.records} == {"q1", "q2"}
    assert len(publications) == 2  # same-title preprint is not merged
    conflicted = resolve_publications([("q1", pubmed), ("q3", clash)])
    assert len(conflicted) == 2 and all(p.identity_conflict for p in conflicted)
    assert normalize_doi("DOI:10.1/AbC") == "10.1/abc" and normalize_doi("not-a-doi") is None


def test_selection_requires_exact_tf_and_covers_seeds_deterministically():
    lung = SourceRecord("pubmed", 1, "k", pmid="5", title="KLF5 in lung alveolar epithelium", abstract="knockdown")
    other = SourceRecord("pubmed", 2, "k", pmid="4", title="KLF5 and NTM in pig litters", abstract="KLF5")
    none = SourceRecord("pubmed", 3, "k", pmid="3", title="Lung atlas", abstract="no candidate")
    pubs = resolve_publications([("q", lung), ("q", other), ("q", none)])
    features = [
        selection_features(p, {"H:5": ["KLF5"]}, {"H:9": ["NTM"]}, ["lung"], ["knockdown"], set()) for p in pubs
    ]
    assert [f.exclusion_reason for f in features if not f.eligible] == [
        "no_exact_candidate_tf_mention_in_title_or_abstract"
    ]
    pmids = {p.publication_id: p.identifiers["pmid"] for p in pubs}
    chosen = select_corpus(features, pmids, ["H:5"], 1)
    assert pmids[chosen[0][0]] == "5" and chosen[0][1] == "seed_tf_coverage:H:5"  # lung context beats target
    assert select_corpus(list(reversed(features)), pmids, ["H:5"], 2) == select_corpus(features, pmids, ["H:5"], 2)


# --- parsing, XML safety, offsets --------------------------------------------------------------

JATS = b"""<?xml version="1.0"?><article><front><article-meta><title-group><article-title>TEAD1 study</article-title>
</title-group><abstract><p>TEAD1 binds NTM.</p></abstract></article-meta></front><body><sec><title>Results</title>
<p>We found that <italic>TEAD1</italic> did not regulate NTM compared with control.<fig id="f1"><label>Fig. 1</label>
<caption><title>Binding.</title><p>ChIP of TEAD1.</p></caption></fig></p>
<p>These data show TEAD1 occupancy (Fig. 1).</p>
<table-wrap id="t1"><label>Table 1</label><caption><p>Targets</p></caption><table><thead><tr><th>Gene</th>
<th>Effect</th></tr></thead><tbody><tr><td>NTM</td><td>none</td></tr></tbody></table>
<table-wrap-foot><p>n = 3</p></table-wrap-foot>
</table-wrap></sec></body></article>"""


def test_jats_passages_have_exact_offsets_locators_and_spaced_blocks():
    document = parse_jats("publication:x", JATS)
    text = document.canonical_text
    assert all(text[p.start : p.end] == p.text and p.locator.startswith("/article") for p in document.passages)
    kinds = [p.kind for p in document.passages]
    assert kinds == [
        "title",
        "abstract",
        "paragraph",
        "figure_caption",
        "paragraph",
        "table_caption",
        "table_header",
        "table_row",
        "table_footnote",
    ]
    first = document.passages[2].text
    assert "Fig. 1" not in first and first.endswith("compared with control.")  # nested float kept out
    assert document.passages[3].text == "Fig. 1 Binding. ChIP of TEAD1."  # block boundary spaced
    row = document.passages[7]
    assert row.text == "NTM | none" and row.table_header == "Gene | Effect"


def test_xml_with_internal_entities_is_refused_and_external_ones_are_not_resolved(tmp_path):
    bomb = b'<?xml version="1.0"?><!DOCTYPE a [<!ENTITY x "boom">]><a>&x;</a>'
    with pytest.raises(UnsafeXMLError):
        parse_xml(bomb)
    secret = tmp_path / "secret.txt"
    secret.write_text("SECRET")
    external = f'<?xml version="1.0"?><!DOCTYPE a [<!ENTITY e SYSTEM "file://{secret}">]><a>&e;</a>'.encode()
    with pytest.raises(UnsafeXMLError):
        parse_xml(external)


def test_pubmed_abstract_and_bioc_documents():
    document = parse_pubmed_abstract("publication:x", EFETCH)
    assert [p.kind for p in document.passages] == ["title", "abstract"]
    assert document.passages[1].section_path == "Abstract > RESULTS"
    with pytest.raises(ParseError):
        parse_bioc(
            "publication:x",
            json.dumps(
                {"passages": [{"infons": {"section_type": "ABSTRACT", "type": "abstract"}, "text": "x"}]}
            ).encode(),
        )


def test_pubtator_offsets_are_verified_and_kept_when_versions_differ():
    document = parse_jats("publication:x", JATS)
    pubtator = {
        "passages": [
            {
                "offset": 0,
                "text": "TEAD1 study",
                "annotations": [
                    {
                        "id": "1",
                        "text": "TEAD1",
                        "infons": {"type": "Gene", "identifier": "7003"},
                        "locations": [{"offset": 0, "length": 5}],
                    }
                ],
            },
            {
                "offset": 500,
                "text": "A different sentence mentions Tead1 only here.",
                "annotations": [
                    {
                        "id": "2",
                        "text": "Tead1",
                        "infons": {"type": "Gene", "identifier": "21676"},
                        "locations": [{"offset": 530, "length": 5}],
                    }
                ],
            },
        ]
    }
    mentions = pubtator_mentions(document, pubtator, {"7003": "HGNC:11714"})
    human, mouse = mentions
    assert human.alignment == ALIGN_EXACT and document.canonical_text[human.start : human.end] == "TEAD1"
    assert human.hgnc_id == "HGNC:11714"
    assert mouse.alignment == ALIGN_UNALIGNED and mouse.start is None and mouse.external_offset == 530
    assert mouse.hgnc_id is None and mouse.resolution == "unresolved_non_human_or_unmapped"


# --- retrieval, embeddings, bundles ------------------------------------------------------------


def query(**overrides) -> QueryTerms:
    base = dict(
        query_id="q1",
        priority=1,
        tf_hgnc_id="H:1",
        tf_terms=["TEAD1"],
        target_hgnc_id="H:2",
        target_terms=["NTM"],
        qualifiers=["ChIP"],
        candidate_ids=["c1"],
    )
    return QueryTerms(**{**base, **overrides})


def test_empty_corpus_and_no_exact_hits_produce_no_bundles():
    config = RetrievalConfig(hits_per_query=5, rrf_k=60, bm25_k1=1.5, bm25_b=0.75)
    assert rank_passages(query(), [], [], BM25Okapi([[""]]), None, config) == []
    document = parse_jats("publication:x", JATS)
    no_tf = query(tf_terms=["FOXA2"])
    passages = document.passages
    bm25 = BM25Okapi([tokenize(p.text) for p in passages])
    hits = {"q1": rank_passages(no_tf, passages, ["publication:x"] * len(passages), bm25, None, config)}
    bundles, _ = assemble_bundles(
        [no_tf],
        hits,
        {"publication:x": document},
        {p.passage_id: p for p in passages},
        BundleConfig(max_bundles=20, max_passages=3, max_chars=6000, max_per_paper=4, max_per_candidate_tf=4),
    )
    assert bundles == []


def test_bundles_respect_bounds_add_needed_context_and_never_truncate():
    document = parse_jats("publication:x", JATS)
    passages = document.passages
    owners = ["publication:x"] * len(passages)
    bm25 = BM25Okapi([tokenize(p.text) for p in passages])
    config = RetrievalConfig(hits_per_query=10, rrf_k=60, bm25_k1=1.5, bm25_b=0.75)
    dense = np.linspace(0, 1, len(passages))
    hits = {"q1": rank_passages(query(), passages, owners, bm25, dense, config)}
    assert hits["q1"][0].exact_tf and "dense" in hits["q1"][0].reasons
    capped = BundleConfig(max_bundles=2, max_passages=2, max_chars=6000, max_per_paper=4, max_per_candidate_tf=4)
    bundles, _ = assemble_bundles(
        [query()], hits, {"publication:x": document}, {p.passage_id: p for p in passages}, capped
    )
    assert len(bundles) == 2  # run-level cap
    limits = BundleConfig(max_bundles=20, max_passages=2, max_chars=6000, max_per_paper=10, max_per_candidate_tf=10)
    bundles, _ = assemble_bundles(
        [query()], hits, {"publication:x": document}, {p.passage_id: p for p in passages}, limits
    )
    assert all(len(b.passages) <= 2 and b.total_chars <= 6000 for b in bundles)
    by_text = {p.text: p for p in passages}
    back_reference = next(
        b for b in bundles if b.anchor_passage_id == by_text["These data show TEAD1 occupancy (Fig. 1)."].passage_id
    )
    # The preceding passage is the referenced Fig. 1 caption itself: added once, context complete.
    assert back_reference.context_reasons == ["preceding_passage_for_back_reference"]
    assert [p["kind"] for p in back_reference.passages] == ["figure_caption", "paragraph"]
    assert back_reference.extraction_ready and back_reference.incomplete_reasons == []
    row_query = query(query_id="q2", tf_terms=["NTM"], target_terms=[])
    row_hits = {"q2": rank_passages(row_query, passages, owners, bm25, None, config)}
    tables, _ = assemble_bundles(
        [row_query], row_hits, {"publication:x": document}, {p.passage_id: p for p in passages}, limits
    )
    table = next(b for b in tables if b.anchor_passage_id == by_text["NTM | none"].passage_id)
    assert table.context_reasons == ["table_caption"]  # caption is required context and fits ...
    # ... the required footnote does not fit within two passages, so the omission is reported.
    assert not table.extraction_ready and table.incomplete_reasons[0].startswith("context_not_included:table_footnote")
    negated = next(b for b in bundles if any("did not regulate" in p["text"] for p in b.passages))
    assert "negation_cue" in negated.flags and "comparison_cue" in negated.flags
    tiny = BundleConfig(max_bundles=5, max_passages=1, max_chars=10, max_per_paper=4, max_per_candidate_tf=4)
    small, rejected = assemble_bundles(
        [query()], hits, {"publication:x": document}, {p.passage_id: p for p in passages}, tiny
    )
    assert all(b.total_chars <= 10 for b in small) and rejected  # oversized anchors are rejected, not cut


def test_chunking_never_exceeds_the_limit():
    text = "Sentence one is here. " * 200 + "x" * 2500
    chunks = emb.chunk_text(text, 1000)
    assert max(len(c) for c in chunks) <= 1000 and "".join(chunks).replace(" ", "") == text.replace(" ", "")


def test_ollama_wiring_default_and_override_without_network(monkeypatch):
    captured = {}

    class FakeOllama:
        def __init__(self, **kwargs):
            captured.update(kwargs)

    monkeypatch.setitem(sys.modules, "langchain_ollama", types.SimpleNamespace(OllamaEmbeddings=FakeOllama))
    monkeypatch.setattr(
        emb,
        "ollama_model_metadata",
        lambda url, name: {
            "digest": "d",
            "embedding_length": 384,
            "context_length": 1024,
            "tokenizer_model": "bert",
            "special_tokens": 2,
        },
    )
    selector = "ollama:pankajrajdeo/biomed-embeddings-16l-fp16:latest"
    settings = resolve_model_settings({"EMBEDDINGS_ENABLED": "true", "EMBEDDING_MODEL": selector})
    backend = emb.build_embeddings(settings, EmbeddingSection())
    assert captured == {"model": "pankajrajdeo/biomed-embeddings-16l-fp16:latest", "base_url": "http://localhost:11434"}
    override = resolve_model_settings(
        {"EMBEDDINGS_ENABLED": "true", "EMBEDDING_MODEL": selector, "OLLAMA_BASE_URL": "http://10.0.0.2:11434"}
    )
    emb.build_embeddings(override, EmbeddingSection())
    assert captured["base_url"] == "http://10.0.0.2:11434" and backend.identity["digest"] == "d"


def test_sentence_transformers_wiring_and_missing_extra(monkeypatch):
    captured = {}

    class FakeHF:
        def __init__(self, **kwargs):
            captured.update(kwargs)
            self._client = types.SimpleNamespace(
                max_seq_length=8, tokenizer=lambda text, add_special_tokens: {"input_ids": [0, *text.split(), 0]}
            )

    settings = resolve_model_settings({"EMBEDDINGS_ENABLED": "true", "EMBEDDING_MODEL": "sentence-transformers:Org/M"})
    monkeypatch.setitem(sys.modules, "langchain_huggingface", None)
    with pytest.raises(emb.EmbeddingSetupError, match="embeddings-sentence-transformers"):
        emb.build_embeddings(settings, EmbeddingSection())
    monkeypatch.setitem(sys.modules, "langchain_huggingface", types.SimpleNamespace(HuggingFaceEmbeddings=FakeHF))
    emb.build_embeddings(settings, EmbeddingSection(revision="abc123", device="cpu"))
    assert captured == {
        "model_name": "Org/M",
        "model_kwargs": {"device": "cpu", "revision": "abc123"},
        "encode_kwargs": {"normalize_embeddings": True},
    }
    assert emb.build_embeddings(resolve_model_settings({"EMBEDDINGS_ENABLED": "false"}), EmbeddingSection()) is None


def test_vector_store_caches_and_rejects_bad_vectors(tmp_path):
    class Fake:
        calls = 0

        def embed_documents(self, texts):
            Fake.calls += 1
            return [[1.0, 0.0, 0.0] for _ in texts]

        def embed_query(self, text):
            Fake.calls += 1
            return [0.0, 1.0, 0.0]

    backend = emb.EmbeddingBackend("ollama:m:t", "ollama", "m:t", Fake(), {"selector": "ollama:m:t"})
    store = emb.VectorStore(tmp_path, backend)
    store.encode(["a", "b"], 8, 3)
    store.embed_query("q", 3)
    replay = emb.VectorStore(tmp_path, backend)
    replay.encode(["a", "b"], 8, 3)
    replay.embed_query("q", 3)
    assert Fake.calls == 2 and replay.requests == 0
    with pytest.raises(emb.EmbeddingSetupError, match="dimension"):
        emb.VectorStore(tmp_path / "x", backend).encode(["c"], 8, 384)


# --- full stage chain on the synthetic P1/P2 project ------------------------------------------

SYN_EFETCH = EFETCH.replace(b"TEAD1 in alveolar cells", b"TF_A in lung alveolar cells").replace(
    b"TEAD1 did not\nbind the NTM promoter.", b"TF_A did not bind the GENE1 promoter."
)
SYN_JATS = JATS.replace(b"TEAD1", b"TF_A").replace(b"NTM", b"GENE1")


def synthetic_routes(epmc_down: bool):
    counts = {"eutils": 0, "epmc_search": 0, "epmc_fulltext": 0, "pubtator": 0}

    def handler(request: httpx.Request) -> httpx.Response:
        if request.url.host == "eutils.ncbi.nlm.nih.gov":
            counts["eutils"] += 1
            if request.url.path.endswith("esearch.fcgi"):
                return httpx.Response(200, json={"esearchresult": {"count": "1", "idlist": ["111"]}})
            return httpx.Response(200, content=SYN_EFETCH)
        if request.url.host == "www.ebi.ac.uk" and request.url.path.endswith("fullTextXML"):
            counts["epmc_fulltext"] += 1
            return httpx.Response(200, content=SYN_JATS)
        if request.url.host == "www.ebi.ac.uk":
            counts["epmc_search"] += 1
            if epmc_down:  # Europe PMC search outage; PubMed still answers
                return httpx.Response(503)
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
                                "title": "TF_A in lung alveolar cells",
                                "isOpenAccess": "Y",
                                "inPMC": "Y",
                            }
                        ]
                    },
                },
            )
        counts["pubtator"] += 1
        return httpx.Response(
            200,
            json={
                "PubTator3": [
                    {
                        "pmid": 111,
                        "passages": [
                            {
                                "offset": 0,
                                "text": "TF_A study",
                                "infons": {"section_type": "TITLE", "type": "front"},
                                "annotations": [
                                    {
                                        "id": "1",
                                        "text": "TF_A",
                                        "infons": {"type": "Gene", "identifier": "5555"},
                                        "locations": [{"offset": 0, "length": 4}],
                                    }
                                ],
                            }
                        ],
                    }
                ]
            },
        )

    return handler, counts


def test_literature_stages_resume_verify_and_replay(synthetic_project, monkeypatch):
    import yaml

    from regkg.analysis.stage import run_candidates
    from regkg.config import load_project_config
    from regkg.literature.verify import verify_literature
    from regkg.models import StageStatus
    from regkg.project_data.ingest import run_ingest
    from regkg.workflows import literature as flow
    from tests.test_candidates import seed_resources

    monkeypatch.setattr("time.sleep", lambda _: None)
    root = synthetic_project.parents[1]
    loaded = load_project_config(synthetic_project, repo_root=root)
    ingest = run_ingest(loaded)
    seed_resources(root)
    literature = root / "configs" / "literature.yaml"
    base = yaml.safe_load(Path("configs/literature.yaml").read_text())
    config = yaml.safe_load(literature.read_text())
    config.update({k: base[k] for k in ("search", "fetch", "retrieval", "bundles", "embeddings")})
    config["retrieval_queue"]["max_live_queries"] = 3
    literature.write_text(yaml.safe_dump(config))
    candidates = run_candidates(loaded, ingest.ingest_key, "AT1", root / "configs" / "ranking.yaml", literature)

    def sources(handler):
        return SourceClient(
            loaded.data_root / "external" / "literature_cache", NcbiSettings("tool"), 1, 1, httpx.MockTransport(handler)
        )

    down, _ = synthetic_routes(epmc_down=True)
    first = flow.run_search(loaded, candidates.candidate_key, 2, literature, client=sources(down))
    assert first.status is StageStatus.PARTIAL
    assert first.counts["query_status"].get(flow.SEARCHED_PARTIAL, 0) >= 1
    up, counts = synthetic_routes(epmc_down=False)
    second = flow.run_search(loaded, candidates.candidate_key, 2, literature, client=sources(up))
    assert second.status is StageStatus.SUCCEEDED and second.key != first.key
    assert counts["eutils"] == 0 and counts["epmc_search"] >= 1  # only the failed requests were retried

    fetched = flow.run_fetch(loaded, second.key, literature, client=sources(up))
    assert fetched.counts["processing_status"] == {flow.FULL_TEXT_PROCESSED: 1}
    env = {"EMBEDDINGS_ENABLED": "false"}
    retrieved = flow.run_retrieve(loaded, fetched.key, literature, process_env=env)
    assert retrieved.counts["dense_status"] == "disabled" and retrieved.counts["bundles"] >= 1
    results = verify_literature(retrieved.artifact_dir, root, literature)
    assert [r for r in results if not r.passed] == []

    silent, quiet = synthetic_routes(epmc_down=False)
    assert (
        flow.run_search(loaded, candidates.candidate_key, 2, literature, client=sources(silent)).status
        is StageStatus.REUSED
    )
    assert flow.run_fetch(loaded, second.key, literature, client=sources(silent)).status is StageStatus.REUSED
    assert flow.run_retrieve(loaded, fetched.key, literature, process_env=env).status is StageStatus.REUSED
    assert sum(quiet.values()) == 0  # replay made no request to any source
