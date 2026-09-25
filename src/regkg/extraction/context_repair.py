"""Route critic requests to the existing bounded, read-only source assembly agent."""

from regkg.extraction.assembly import assemble
from regkg.extraction.sources import pubtator_context
from regkg.provenance import canonical_json


def recover_context(registry, bundle, requests, model, runtime, limits, repair_id=None):
    anchors = registry.validate_bundle(bundle)
    if not requests or any(
        not any(p["part_id"] == q.evidence.part_id and q.evidence.quote in p["text"] for p in anchors) for q in requests
    ):
        return {"status": "CONTEXT_REQUEST_NOT_GROUNDED"}
    # Keep all original source/parse flags. Only a validated ready bundle can enter here.
    investigation = {**bundle, "readiness_state": "NEEDS_CONTEXT", "critic_parent_payload_id": bundle["payload_id"]}
    # Existing P3 source links can justify a referenced caption; shared paper identity cannot.
    reasons = list(bundle.get("readiness_reasons", []))
    for candidate in registry.bundles.values():
        if (
            candidate["publication_id"] == bundle["publication_id"]
            and candidate.get("anchor_passage_id")
            and candidate.get("anchor_passage_id") == bundle.get("anchor_passage_id")
        ):
            reasons.extend(
                r
                for r in candidate.get("readiness_reasons", [])
                if r.startswith("context_not_included:referenced_figure_caption:")
            )
    investigation["readiness_reasons"] = sorted(set(reasons))
    result = assemble(
        registry,
        investigation,
        "Resolve only these source-grounded context questions, retaining every original anchor: "
        + canonical_json([q.model_dump() for q in requests]),
        model,
        runtime,
        limits,
        repair_id=repair_id,
    )
    child = result.get("bundle")
    if not child:
        return result
    parts = registry.validate_bundle(child)
    original_ids = {p["part_id"] for p in anchors}
    child_ids = {p["part_id"] for p in parts}
    if not original_ids < child_ids:
        return {**result, "status": "CONTEXT_MUST_ADD_WITHOUT_DROPPING_ANCHORS", "bundle": None}
    return {**result, "parts": parts, "annotations": pubtator_context(registry, parts)}
