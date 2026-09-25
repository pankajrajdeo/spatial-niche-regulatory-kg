"""Host-applied observation patches with explicit scope and optimistic concurrency."""

from typing import Literal

from pydantic import Field, create_model

from regkg.extraction.schemas import Citation, StrictRecord
from regkg.provenance import canonical_json, sha256_text

FIELD_DEPENDENCIES = {
    "endpoints": {"subject_id", "object_id", "assertion"},
    "entity_types": {"subject_id", "object_id", "relation", "assertion"},
    "relation": {"relation", "directness", "evidence_classification", "assertion"},
    "measurement": {"measured_variable", "measurement_evidence", "quantities", "assertion"},
    "direction": {"observed_change", "outcome", "evidence_classification", "assertion"},
    "intervention": {"intervention", "comparison", "relation", "directness", "evidence_classification", "assertion"},
    "context": {"context", "assay", "experiment_label", "frame_id"},
    "attribution": {"statement_status", "evidence_classification", "assertion"},
    "directness": {"directness", "evidence_classification"},
    "quantities": {"quantities"},
    "evidence_classification": {"evidence_classification"},
}


def observation_hash(observation):
    return sha256_text(canonical_json(observation.model_dump()))


def patch_contract(observation_type):
    patch = create_model(
        "ObservationPatch",
        __base__=StrictRecord,
        observation_index=(int, Field(ge=0)),
        previous_sha256=(str, ...),
        action=(Literal["replace", "remove"], ...),
        changed_fields=(list[Literal[tuple(observation_type.model_fields)]], Field(max_length=24)),
        replacement=(observation_type | None, ...),
        evidence=(list[Citation], Field(min_length=1, max_length=4)),
        reason=(str, Field(max_length=400)),
    )
    return create_model(
        "TargetedRepairs",
        __base__=StrictRecord,
        patches=(list[patch], Field(max_length=16)),
        additions=(list[observation_type], Field(max_length=16)),
        overflow=(bool, ...),
    )


def repair_scope(snapshot, observations, mentions):
    scope = {}
    for review in (snapshot.get("field_reviews") or {}).get("reviews", []):
        for check in review["checks"]:
            if check["verdict"] != "SUPPORTED":
                scope.setdefault(review["observation_index"], set()).update(FIELD_DEPENDENCIES[check["field"]])
    # Host defects are also explicit correction targets; complete changed observations
    # are reverified, so a shared-frame or endpoint change cannot bypass dependencies.
    for defect in snapshot.get("host_defects", []):
        for failure in defect["failures"]:
            if "quantity" in failure or "cell" in failure:
                scope.setdefault(defect["index"], set()).add("quantities")
            elif "endpoint" in failure:
                scope.setdefault(defect["index"], set()).update(FIELD_DEPENDENCIES["entity_types"])
            elif "frame" in failure:
                scope.setdefault(defect["index"], set()).update({"frame_id", "measured_variable"})
            elif "measurement" in failure:
                scope.setdefault(defect["index"], set()).update(FIELD_DEPENDENCIES["measurement"])
            else:
                scope.setdefault(defect["index"], set()).update({"relation", "evidence_classification", "directness"})
    for assessment in snapshot.get("assessments", []):
        if any("quantity" in f or "cell" in f for f in assessment["failures"]):
            scope.setdefault(assessment["observation_index"], set()).add("quantities")
    critic = snapshot.get("critique") or {}
    for key, check in critic.get("mention_checks", {}).items():
        if check["verdict"] == "SUPPORTED":
            continue
        mid = mentions[int(key.removeprefix("mention_"))]["mention_id"]
        for i, obs in enumerate(observations):
            if mid in {obs.subject_id, obs.object_id}:
                scope.setdefault(i, set()).update(FIELD_DEPENDENCIES["entity_types"])
    for i in scope:
        scope[i].update({"citations", "limitations"})
    return scope


def apply_patches(original, proposed, scope, parts, allow_additions):
    if proposed.overflow:
        raise ValueError("patch_overflow")
    replacements, removed = {}, set()
    for patch in proposed.patches:
        i = patch.observation_index
        if i not in scope or i in replacements or i in removed or not 0 <= i < len(original.observations):
            raise ValueError("patch_outside_scope_or_duplicate")
        before = original.observations[i]
        if patch.previous_sha256 != observation_hash(before):
            raise ValueError("stale_patch")
        if not all(any(p["part_id"] == c.part_id and c.quote in p["text"] for p in parts) for c in patch.evidence):
            raise ValueError("patch_evidence_not_grounded")
        if patch.action == "remove":
            if patch.replacement is not None or patch.changed_fields:
                raise ValueError("invalid_removal_patch")
            removed.add(i)
            continue
        if patch.replacement is None:
            raise ValueError("missing_patch_replacement")
        changed = {k for k, v in before.model_dump().items() if patch.replacement.model_dump()[k] != v}
        if changed != set(patch.changed_fields) or len(patch.changed_fields) != len(changed) or not changed <= scope[i]:
            raise ValueError("patch_changes_unapproved_fields")
        replacements[i] = patch.replacement
    if proposed.additions and not allow_additions:
        raise ValueError("unrequested_additions")
    values = [replacements.get(i, o) for i, o in enumerate(original.observations) if i not in removed]
    values.extend(proposed.additions)
    if len({canonical_json(o.model_dump()) for o in values}) != len(values):
        raise ValueError("duplicate_patch_observations")
    # Revalidate the aggregate (including its output bound) rather than model_copy.
    return type(original).model_validate(
        {**original.model_dump(), "observations": [o.model_dump() for o in values], "missing_mentions": []}
    )


PATCH_PROMPT = (
    "Return only targeted patches for the supplied correction scope, plus explicitly requested missing\n"
    "findings. Never regenerate unaffected observations. Each replacement is one complete observation, but "
    "only\n"
    "listed allowed fields may differ; report the exact changed_fields and copy previous_sha256. Host code "
    "checks\n"
    "all unchanged fields byte-for-byte. Use supplied mention IDs. Corrected mention IDs may replace old "
    "endpoint\n"
    "IDs only within scope. Copy measured_variable exactly from the selected "
    "frame.fields.measured_variable.value;\n"
    "never reuse a frame for a different endpoint/variable/experiment. Removal requires a source-based "
    "reason and evidence; do not remove merely uncertain\n"
    "findings. Each patch needs exact original-source quotes. Do not treat reviewer opinions as source truth.\n"
    "Preserve valid findings, explicit nulls, joint perturbations and unknown metadata. All patched "
    "observations\n"
    "and their dependencies receive full semantic and deterministic verification. No edits to experiment "
    "frames.\n"
)
