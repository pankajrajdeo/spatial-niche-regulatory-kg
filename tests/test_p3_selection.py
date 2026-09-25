"""Synthetic checks for source selection, strict grounding, and version deduplication."""

import json

import pytest

from regkg.literature.parse import parse_jats
from regkg.workflows.p3_selection import (
    candidate_passages,
    main_text,
    source_bundle,
    verified_versions,
    verify_parts,
)


def document(body=True):
    inner = (
        '<body><sec sec-type="results"><title>Results</title>'
        "<p>A new regulator changed epithelial differentiation.</p></sec></body>"
        if body
        else ""
    )
    return parse_jats(
        "publication:synthetic",
        (
            "<article><front><article-meta><abstract><p>A synthetic abstract.</p></abstract></article-meta></front>"
            + inner
            + "</article>"
        ).encode(),
    )


def record():
    return {
        "publication_id": "publication:synthetic",
        "pmid": "123",
        "questions": {"AT1": {"decision": "include_for_extraction"}},
    }


def test_front_matter_jats_cannot_become_full_text():
    doc = document(False)
    assert not main_text(doc)
    b = source_bundle(doc, {"document_id": "doc:synthetic", "state": "PARSED"}, doc.passages[0], record(), [])
    assert b["readiness_state"] == "NEEDS_ASSET"


def test_new_regulator_is_not_dropped_by_exact_seed_gate():
    doc = document()
    anchors = candidate_passages(doc, set(), True)
    assert any(p.section_type == "results" for p in anchors)
    assert candidate_passages(doc, set(), False) == []


def test_partial_source_and_corrupted_quote_are_rejected():
    doc = document()
    anchor = next(p for p in doc.passages if p.section_type == "results" and p.kind == "paragraph")
    b = source_bundle(doc, {"document_id": "doc:synthetic", "state": "PARTIAL"}, anchor, record(), [])
    assert b["readiness_state"] == "NEEDS_PARSE_REPAIR"
    b["parts"][0]["text"] = "An invented claim."
    with pytest.raises(ValueError, match="Source mismatch"):
        verify_parts(b, doc)


def test_version_deduplication_requires_published_doi(tmp_path):
    directory = tmp_path / "p3-final-acquisition"
    directory.mkdir()
    payload = {
        "publication_id": "preprint:1",
        "doi": "10.1/preprint",
        "source": "https://api.biorxiv.org/details",
        "response": {"collection": [{"title": "Identical title", "published": "NA"}]},
    }
    path = directory / "one-biorxiv.json"
    path.write_text(json.dumps(payload))
    audits = {
        "journal:1": {"publication_id": "journal:1", "pmid": "123", "doi": "10.1/JOURNAL", "title": "Identical title"}
    }
    assert verified_versions(tmp_path, audits) == {}
    payload["response"]["collection"][0]["published"] = "10.1/journal"
    path.write_text(json.dumps(payload))
    assert verified_versions(tmp_path, audits)["preprint:1"]["canonical_publication_id"] == "journal:1"


def test_docling_records_the_configured_table_model_tag(tmp_path, monkeypatch):
    from pathlib import Path

    from regkg.literature.files import docling_assets

    monkeypatch.setattr(Path, "home", lambda: tmp_path)
    hub = tmp_path / ".cache/huggingface/hub"
    ref = hub / "models--docling-project--docling-models/refs/v2.3.0"
    ref.parent.mkdir(parents=True)
    ref.write_text("verified-table-revision")
    assets = docling_assets()
    assert assets["models"]["docling-project/docling-models"] == "verified-table-revision"
