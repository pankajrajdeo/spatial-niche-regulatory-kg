"""Synthetic checks for lossless labels, span integrity and training/evaluation separation."""

import copy

import pytest
from pydantic import ValidationError

from regkg.extraction.annotations import AnnotationCandidates, annotation_candidates


def inputs():
    part = {"part_id": "p:1", "start": 10, "text": "GeneA", "document_sha256": "fixture"}
    mention = {
        "part_id": "p:1",
        "start": 10,
        "end": 15,
        "surface": "GeneA",
        "kind": "gene",
        "document_id": "d:1",
        "document_sha256": "fixture",
    }
    result = {
        "model": "synthetic-a",
        "outcome": {"publication_id": "pub:1", "bundle_id": "b:1", "mentions": [mention], "status": "NO_RELATION"},
        "records": [],
    }
    return part, result


def test_model_agreement_never_creates_gold_or_negative_training_labels():
    part, first = inputs()
    second = {**copy.deepcopy(first), "model": "synthetic-b"}
    item = annotation_candidates([part], {}, [first, second], "trial:synthetic", "fixture")
    assert item.entity_agreement[0]["model_count"] == 2
    assert not item.training_eligible and item.reserved_for_diagnostics
    assert item.missing_labels == "UNLABELED_NOT_NEGATIVE" and item.relation_negative_labels == []
    assert item.model_outputs == [first, second]
    with pytest.raises(ValidationError):
        AnnotationCandidates.model_validate({**item.model_dump(), "training_eligible": True})


def test_type_disagreements_and_invalid_source_spans_remain_visible():
    part, first = inputs()
    second = {**copy.deepcopy(first), "model": "synthetic-b"}
    second["outcome"]["mentions"][0]["kind"] = "family"
    item = annotation_candidates([part], {}, [first, second], "trial:synthetic", "fixture")
    assert len(item.entity_agreement) == 2
    assert all(m["model_count"] == 1 for m in item.entity_agreement)
    first["outcome"]["mentions"][0]["end"] = 14
    with pytest.raises(ValueError, match="grounded"):
        annotation_candidates([part], {}, [first, second], "trial:synthetic", "fixture")
