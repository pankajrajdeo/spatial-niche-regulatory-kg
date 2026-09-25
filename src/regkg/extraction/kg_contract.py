"""Final KG vocabulary and conservative projection of literature observations."""

from pathlib import Path
from typing import Literal

from pydantic import Field, create_model, model_validator

from regkg.config import read_yaml
from regkg.extraction.schemas import StrictRecord
from regkg.provenance import stable_id


class EvidenceField(StrictRecord):
    description: str
    values: list[str]


class KGSchema(StrictRecord):
    version: str
    sources: list[str]
    nodes: dict[str, str]
    relationships: dict[str, list[tuple[str, str]]]
    evidence_fields: dict[str, EvidenceField]
    relative_fields: dict[str, list[str]]
    extraction_boundary: list[str]

    @model_validator(mode="after")
    def endpoints_defined(self):
        for pairs in self.relationships.values():
            if not pairs or any(a not in self.nodes or b not in self.nodes for a, b in pairs):
                raise ValueError("Graph relationship has undefined endpoints")
        if set(self.evidence_fields) != set(EvidenceClassification.model_fields):
            raise ValueError("KG evidence fields differ from the extraction contract")
        return self


class EvidenceClassification(StrictRecord):
    evidence_type: str | None
    directness: str
    experimental_outcome: str
    statement_status: str
    measured_or_inferred: str
    regulatory_direction: str


def load_kg_schema(path: Path) -> KGSchema:
    return KGSchema.model_validate(read_yaml(path))


def evidence_contract(schema: KGSchema):
    fields = {}
    for name, definition in schema.evidence_fields.items():
        choices = Literal[tuple(definition.values)]
        if name == "evidence_type":
            choices = choices | None
        fields[name] = (choices, Field(description=definition.description))
    return create_model("TypedEvidenceClassification", __base__=EvidenceClassification, **fields)


def classification_failures(observation):
    evidence = observation.evidence_classification
    failures = []
    expected = {"INCREASE": "INCREASE", "DECREASE": "DECREASE", "NO_EFFECT": "NO_DETECTED_EFFECT"}
    result = evidence.experimental_outcome
    if result in {"BINDING_DETECTED", "NO_BINDING_DETECTED"}:
        if observation.relation != "BINDS":
            failures.append("binding_outcome_requires_binding_observation")
    elif observation.observed_change in expected and result not in {expected[observation.observed_change], "UNCLEAR"}:
        failures.append("experimental_outcome_disagrees_with_measured_change")
    if observation.relation == "BINDS" and result == "NO_DETECTED_EFFECT":
        failures.append("binding_absence_is_not_expression_null")
    if evidence.directness == "DIRECT" and observation.directness != "direct":
        failures.append("inconsistent_direct_regulatory_mechanism")
    if evidence.regulatory_direction != "UNKNOWN" and observation.relation != "REGULATES":
        failures.append("regulatory_sign_without_regulatory_claim")
    if evidence.evidence_type == "TF_BINDING_PLUS_PERTURBATION":
        # P4 does not yet resolve compatibility/experiment links between separate findings.
        failures.append("combined_evidence_requires_resolved_experiment_links")
    return failures


def project_finding(record, schema_version):
    """Preserve all evidence; only gene-level propositions enter the core claim table."""
    observation = record["observation"]
    classification = observation["evidence_classification"]
    reasons = []
    if record["status"] != "AUTO_ACCEPTED":
        reasons.append("finding_not_accepted")
    for role in ("subject", "object"):
        entity = record[role]
        if entity["kind"] != "gene" or not entity["entity_id"]:
            reasons.append(f"{role}_not_resolved_gene")
    if observation["relation"] not in {
        "REGULATES",
        "PERTURBATION_EFFECT",
        "BINDS",
        "EXPRESSION_ASSOCIATION",
        "MOTIF_ASSOCIATION",
        "PREDICTS",
    }:
        reasons.append("predicate_outside_core_regulatory_claims")
    claim = None
    if not reasons:
        claim = {
            "regulator_id": record["subject"]["entity_id"],
            "target_id": record["object"]["entity_id"],
            "relation": observation["relation"],
            "regulatory_direction": classification["regulatory_direction"],
            "context": observation["context"],
            "intervention": observation["intervention"],
            "comparison": observation["comparison"],
            "measured_variable": observation["measured_variable"],
        }
    assertion = {
        **classification,
        "extraction_status": record["status"],
        "source_attribution": observation["statement_status"],
        "observed_change": observation["observed_change"],
        "source_context": observation["context"],
        "assay": observation["assay"],
        "experiment_label": observation["experiment_label"],
        "experiment_id": None,
        "study_id": None,
        "polarity": None,
        "context_match": None,
        "relative_assessment_status": "REFERENCE_CLAIM_AND_NOMINATION_REQUIRED",
    }
    return {
        "schema_version": schema_version,
        "core_claim_eligible": not reasons,
        "reasons": reasons,
        "claim_id": stable_id("regulatory-claim", claim) if claim else None,
        "claim": claim,
        "evidence": assertion,
    }
