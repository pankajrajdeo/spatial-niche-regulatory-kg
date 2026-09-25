"""Bounded source-coverage criticism; decisions remain subject to host validation."""

from typing import Literal

from pydantic import Field, create_model

from regkg.extraction.schemas import Citation, StrictRecord


class MentionCheck(StrictRecord):
    verdict: Literal["SUPPORTED", "UNSUPPORTED", "INSUFFICIENT_CONTEXT"]
    reason: str = Field(max_length=220)


class FactCoverage(StrictRecord):
    disposition: Literal["CAPTURED", "MISSING", "OUTSIDE_SCHEMA", "INSUFFICIENT_CONTEXT"]
    observation_indices: list[int] = Field(max_length=16)
    reason: str = Field(max_length=220)


class ContextRequest(StrictRecord):
    evidence: Citation = Field(description="Exact anchor quote exposing a specific missing source reference/context.")
    question: str = Field(
        max_length=300, description="Specific missing caption/header/methods context; not a request to invent a result."
    )


def critique_contract(mention_count, fact_count, mention_type):
    mention_checks = create_model(
        "MentionChecks",
        __base__=StrictRecord,
        **{f"mention_{i}": (MentionCheck, ...) for i in range(mention_count)},
    )
    fact_checks = create_model(
        "FactChecks",
        __base__=StrictRecord,
        **{f"fact_{i}": (FactCoverage, ...) for i in range(fact_count)},
    )
    return create_model(
        "SourceCritique",
        __base__=StrictRecord,
        mention_checks=(mention_checks, ...),
        fact_checks=(fact_checks, ...),
        missing_mentions=(
            list[mention_type],
            Field(
                max_length=12,
                description="Source-grounded missing or corrected mentions; preserve exact spans and types.",
            ),
        ),
        context_requests=(list[ContextRequest], Field(max_length=3)),
        overflow=(bool, ...),
    )


def critique_issues(critique, mentions, observations, source_read, parts, reviews):
    if critique is None:
        return ["critique_failed"]
    issues = []
    if critique.overflow:
        issues.append("critique_overflow")
    if critique.missing_mentions:
        issues.append("missing_or_mistyped_mentions")
    if critique.context_requests:
        issues.append("source_context_requested")
    for key, decision in critique.mention_checks.model_dump().items():
        if decision["verdict"] != "SUPPORTED":
            issues.append(f"{key}:{decision['verdict']}")
    for key, decision in critique.fact_checks.model_dump().items():
        index = int(key.removeprefix("fact_"))
        fact = source_read.facts[index]
        if not any(p["part_id"] == fact.evidence.part_id and fact.evidence.quote in p["text"] for p in parts):
            issues.append(f"{key}:invalid_source_quote")
        indices = decision["observation_indices"]
        if decision["disposition"] == "CAPTURED":
            if not indices or len(indices) != len(set(indices)) or any(not 0 <= i < len(observations) for i in indices):
                issues.append(f"{key}:invalid_coverage_indices")
            elif any(
                not any(r.observation_index == i and r.source_fact_index == index for r in reviews) for i in indices
            ):
                issues.append(f"{key}:coverage_verification_disagrees")
        elif indices:
            issues.append(f"{key}:unexpected_coverage_indices")
        if decision["disposition"] in {"MISSING", "INSUFFICIENT_CONTEXT"}:
            issues.append(f"{key}:{decision['disposition']}")
    for request in critique.context_requests:
        if not any(p["part_id"] == request.evidence.part_id and request.evidence.quote in p["text"] for p in parts):
            issues.append("context_request_not_source_grounded")
    return sorted(set(issues))


def compact_field_reviews(field_reviews):
    reviews = []
    for review in (field_reviews or {}).get("reviews", []):
        reviews.append(
            {
                **review,
                "checks": [c for c in review["checks"] if c["verdict"] != "SUPPORTED"],
            }
        )
    return {"reviews": reviews}


def repair_feedback(snapshot, mentions=None):
    """Send actionable defects once; keep the complete audit in the saved outcome."""
    critic = dict(snapshot["critique"] or {})
    critic["mention_checks"] = {
        key: value for key, value in critic.get("mention_checks", {}).items() if value["verdict"] != "SUPPORTED"
    }
    if mentions is not None:
        # Critic slots refer to the original inventory, not the shorter corrected one.
        for key, value in critic["mention_checks"].items():
            mention = mentions[int(key.removeprefix("mention_"))]
            critic["mention_checks"][key] = {
                **value,
                "original_mention": {k: mention[k] for k in ("mention_id", "surface", "kind", "part_id", "species")},
            }
    critic["fact_checks"] = {
        key: value for key, value in critic.get("fact_checks", {}).items() if value["disposition"] != "CAPTURED"
    }
    return {**snapshot, "field_reviews": compact_field_reviews(snapshot.get("field_reviews")), "critique": critic}


CRITIQUE_PROMPT = """Audit the original source, every inventory mention, and coverage of every independently read fact.
Check each mention's span, semantic type, qualifiers and source-supported species, even if no relation uses it.
Suggest corrected/missing mentions explicitly; never turn a joint group into separate individual effects.
For each mistyped but eligible mention, supply its exact corrected mention in missing_mentions; a reason
alone does not replace the inventory entry. Use the local assay to distinguish a protein target from a
transcript or genotype. PubTator's Gene label and another occurrence do not override local molecular form.
For each fact, mark CAPTURED only when an observation represents the SAME endpoints, experiment and variable;
otherwise mark MISSING, OUTSIDE_SCHEMA with a specific schema reason, or INSUFFICIENT_CONTEXT.
An empty extraction still needs this full audit. Reread the source for omitted unconnected entities as well.
Missing assay/species detail need not erase a real finding: keep it with unknown metadata. Request source
context only for an identifiable reference/legend/header needed to interpret the result. Source absence
cannot be repaired by biological background knowledge. Inspect host defects and field reviews, not model
confidence. Never invent facts or change the schema. Set overflow if the bounded response is incomplete.
"""

REPAIR_PROMPT = """Repair the proposed extraction once using original source, the source-only reading, critic,
and deterministic defects. Return the complete revised observation set under the same schema. Correct
unsupported fields, add source-supported omitted findings, and remove only source-unsupported/out-of-scope
claims. Preserve valid unchanged findings, explicit nulls, joint perturbations and unknown context.
Preserve fields that already passed unless the original source specifically contradicts them. Fix only
identified defects and source-supported omissions; do not rewrite every evidence label as a fallback.
Critic mention slots refer to original_mention identities, never positions in the revised inventory.
An unclassified primary result keeps evidence_type null; CURATED_LITERATURE does not mean extracted
from a publication. Qualitative changes need no numeric quantity; prose/caption cell_ref is always null.
Select endpoints only from the supplied validated inventory. Do not invent new IDs or use outside knowledge.
Do not treat the critic as truth: every amendment requires original source evidence. Repaired output will
receive fresh criticism and verification; neither agreement nor confident wording establishes correctness.
"""
