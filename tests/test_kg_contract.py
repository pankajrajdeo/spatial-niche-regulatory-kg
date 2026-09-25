"""Synthetic scientific boundary checks; these do not measure extraction accuracy."""

import json
from copy import deepcopy
from pathlib import Path
from types import SimpleNamespace

import pandas as pd
import pytest
from pydantic import ValidationError

from regkg.extraction.kg_contract import (
    classification_failures,
    evidence_contract,
    load_kg_schema,
    project_finding,
)
from regkg.workflows.extraction import persist


def record(kind="gene", relation="PERTURBATION_EFFECT"):
    return {
        "finding_id": f"fixture:{kind}",
        "claim_id": "intermediate:1",
        "publication_id": "pub:1",
        "pmid": "fixture",
        "bundle_id": "bundle:1",
        "status": "AUTO_ACCEPTED",
        "verification": {},
        "subject": {"kind": kind, "entity_id": "fixture:subject"},
        "object": {"kind": "gene", "entity_id": "fixture:target"},
        "spans": [{"quote": "Synthetic null observation"}],
        "proposition": {},
        "observation": {
            "relation": relation,
            "context": {"species": "synthetic", "disease": "disease D"},
            "intervention": "knockdown",
            "comparison": "control",
            "measured_variable": "target transcript",
            "observed_change": "NO_EFFECT",
            "statement_status": "primary_result",
            "assay": None,
            "experiment_label": "Fig. 1",
            "evidence_classification": {
                "evidence_type": "TF_PERTURBATION",
                "directness": "FUNCTIONAL",
                "experimental_outcome": "NO_DETECTED_EFFECT",
                "statement_status": "NEGATED",
                "measured_or_inferred": "measured",
                "regulatory_direction": "UNKNOWN",
            },
        },
    }


def test_final_vocabulary_and_required_evidence_dimensions():
    schema = load_kg_schema(Path("configs/kg_schema.yaml"))
    assert len(schema.nodes) == 20 and len(schema.relationships) == 29
    assert "TF" not in schema.nodes and "REGULATES" not in schema.relationships
    assert ("Passage", "Publication") in schema.relationships["PART_OF"]
    contract = evidence_contract(schema)
    data = record()["observation"]["evidence_classification"]
    contract.model_validate(data)
    with pytest.raises(ValidationError):
        contract.model_validate({**data, "statement_status": "primary_result"})
    with pytest.raises(ValidationError):
        contract.model_validate({k: v for k, v in data.items() if k != "directness"})


@pytest.mark.parametrize("kind", ["gene_group", "family", "complex", "protein", "chemical"])
def test_broad_mentions_are_preserved_without_becoming_single_gene_claims(kind):
    projection = project_finding(record(kind), "synthetic")
    assert projection["claim_id"] is None and not projection["core_claim_eligible"]
    assert projection["evidence"]["experimental_outcome"] == "NO_DETECTED_EFFECT"


def test_null_evidence_does_not_invent_regulatory_sign_support_or_study_identity():
    original = record()
    projection = project_finding(original, "synthetic")
    assert projection["claim"]["regulatory_direction"] == "UNKNOWN"
    assert projection["claim"]["context"]["disease"] == "disease D"
    for name in ["polarity", "context_match", "study_id", "experiment_id"]:
        assert projection["evidence"][name] is None
    different_result = deepcopy(original)
    different_result["observation"]["observed_change"] = "INCREASE"
    different_result["observation"]["evidence_classification"]["experimental_outcome"] = "INCREASE"
    assert project_finding(different_result, "synthetic")["claim_id"] == projection["claim_id"]
    different_result["observation"]["context"]["disease"] = "other disease"
    assert project_finding(different_result, "synthetic")["claim_id"] != projection["claim_id"]


def test_semantic_contradictions_and_unresolved_composite_evidence_fail():
    observation = SimpleNamespace(**record()["observation"])
    observation.directness = "not_established"
    observation.evidence_classification = SimpleNamespace(**observation.evidence_classification)
    evidence = observation.evidence_classification
    evidence.regulatory_direction = "NEGATIVE"
    evidence.experimental_outcome = "DECREASE"
    evidence.evidence_type = "TF_BINDING_PLUS_PERTURBATION"
    failures = classification_failures(observation)
    assert "regulatory_sign_without_regulatory_claim" in failures
    assert "experimental_outcome_disagrees_with_measured_change" in failures
    assert "combined_evidence_requires_resolved_experiment_links" in failures
    observation.relation = "BINDS"
    evidence.experimental_outcome = "NO_DETECTED_EFFECT"
    assert "binding_absence_is_not_expression_null" in classification_failures(observation)


def test_functional_null_response_does_not_imply_a_regulatory_mechanism():
    observation = SimpleNamespace(**record()["observation"])
    observation.directness = "not_established"
    observation.evidence_classification = SimpleNamespace(**observation.evidence_classification)
    assert not classification_failures(observation)
    observation.evidence_classification.directness = "DIRECT"
    assert "inconsistent_direct_regulatory_mechanism" in classification_failures(observation)


def test_persistence_separates_accepted_observations_from_core_regulatory_claims(tmp_path):
    gene, group, legacy = record(), record("gene_group"), record("chemical")
    for item in [gene, group]:
        item["kg_projection"] = project_finding(item, "synthetic")
    summary = persist(tmp_path, [gene, group, legacy], [], {})
    accepted = pd.read_parquet(tmp_path / "accepted_findings.parquet")
    claims = pd.read_parquet(tmp_path / "claims.parquet")
    evidence = pd.read_parquet(tmp_path / "evidence_assertions.parquet")
    assert len(accepted) == len(evidence) == 3
    assert len(claims) == summary["core_regulatory_claims"] == 1
    assert summary["accepted_file_only_findings"] == 2
    assert set(evidence.claim_id.dropna()) == set(claims.claim_id)
    group_row = accepted[accepted.finding_id == "fixture:gene_group"].iloc[0]
    assert pd.isna(group_row.claim_id)
    assert json.loads(group_row.record_json)["observation"]["relation"] == "PERTURBATION_EFFECT"
