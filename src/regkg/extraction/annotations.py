"""Lossless candidate annotations for later adjudication; never automatic training gold."""

import json
from collections import defaultdict
from typing import Literal

from pydantic import Field

from regkg.extraction.schemas import StrictRecord
from regkg.provenance import canonical_json, stable_id


class AnnotationCandidates(StrictRecord):
    annotation_id: str
    publication_id: str
    bundle_id: str
    trial_id: str
    schema_version: str
    source_parts: list[dict]
    pubtator_candidates: dict
    model_outputs: list[dict]
    entity_agreement: list[dict]
    label_status: Literal["UNREVIEWED_CANDIDATES"] = "UNREVIEWED_CANDIDATES"
    training_eligible: Literal[False] = False
    annotation_scope: Literal["partial_source_bundle"] = "partial_source_bundle"
    missing_labels: Literal["UNLABELED_NOT_NEGATIVE"] = "UNLABELED_NOT_NEGATIVE"
    reserved_for_diagnostics: Literal[True] = True
    relation_negative_labels: list = Field(default_factory=list, max_length=0)
    adjudication: None = None


def annotation_candidates(parts, annotations, results, trial_id, schema_version):
    """Retain both models and all dispositions; exact span/type agreement is descriptive only."""
    if not results:
        raise ValueError("No model results to export")
    publications = {r["outcome"]["publication_id"] for r in results}
    bundles = {r["outcome"]["bundle_id"] for r in results}
    if len(publications) != 1 or len(bundles) != 1:
        raise ValueError("Cannot combine different publications or source bundles")
    if len({r["model"] for r in results}) != len(results):
        raise ValueError("Duplicate model output")
    by_part = {p["part_id"]: p for p in parts}
    votes = defaultdict(set)
    for result in results:
        for mention in result["outcome"].get("mentions", []):
            part = by_part.get(mention["part_id"])
            if part is None:
                raise ValueError("Mention references an absent source part")
            start, end = mention["start"] - part["start"], mention["end"] - part["start"]
            if (
                not 0 <= start < end <= len(part["text"])
                or part["text"][start:end] != mention["surface"]
                or mention["document_sha256"] != part["document_sha256"]
            ):
                raise ValueError("Candidate mention is not grounded in the frozen source")
            identity = canonical_json(
                {k: mention[k] for k in ("document_id", "document_sha256", "start", "end", "surface", "kind")}
            )
            votes[identity].add(result["model"])
    agreement = [
        {**json.loads(identity), "proposed_by": sorted(models), "model_count": len(models)}
        for identity, models in sorted(votes.items())
    ]
    identity = {"trial": trial_id, "bundle": next(iter(bundles)), "models": sorted(r["model"] for r in results)}
    return AnnotationCandidates(
        annotation_id=stable_id("annotation-candidates", identity),
        publication_id=next(iter(publications)),
        bundle_id=next(iter(bundles)),
        trial_id=trial_id,
        schema_version=schema_version,
        source_parts=parts,
        pubtator_candidates=annotations,
        model_outputs=results,
        entity_agreement=agreement,
    )
