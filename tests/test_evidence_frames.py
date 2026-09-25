"""Synthetic regressions for context, patch isolation and finding-level decisions."""

from copy import deepcopy
from pathlib import Path

import pytest

from regkg.extraction.frames import FRAME_FIELDS, FrameAssembly, validate_frames
from regkg.extraction.grounded import contracts, extract_grounded, load_scientific_schema
from regkg.extraction.patches import apply_patches, observation_hash, patch_contract
from regkg.extraction.sources import model_parts
from tests.test_critique_repair import ScriptedRuntime
from tests.test_extraction import bundle, resolver, source
from tests.test_grounded_extraction import observation


def test_frame_quotes_and_unknown_fields_cannot_pass_grounding():
    from pydantic import ValidationError

    citation = {"part_id": "p:1", "quote": source()["text"]}
    good = {"result": citation, "fields": dict.fromkeys(FRAME_FIELDS), "missing_context": ["species not stated"]}
    invented = {
        **good,
        "fields": {**good["fields"], "species": {"value": "human", "evidence": [{**citation, "quote": "invented"}]}},
    }
    assembly = FrameAssembly(frames=[good, invented], context_requests=[], overflow=False)
    valid, invalid = validate_frames(assembly, [source()])
    assert len(valid) == 1 and valid[0]["fields"]["species"] is None
    assert invalid[0]["failures"] == ["frame_quote_not_grounded"]
    with pytest.raises(ValidationError):
        FrameAssembly(
            frames=[{**good, "fields": {**good["fields"], "second_assay": None}}], context_requests=[], overflow=False
        )


def test_model_receives_source_labels_without_mutating_frozen_parts():
    part = {**source(), "item_label": "Figure 4", "item_id": "fig4", "page": 7, "bbox": [1, 2, 3, 4]}
    before = deepcopy(part)
    item = model_parts([part])[0]
    assert item["item_label"] == "Figure 4" and item["page"] == 7 and item["bbox"] == [1, 2, 3, 4]
    assert part == before


def patch_example():
    policy = load_scientific_schema(Path("configs/extraction_schema.yaml"))
    _, schema = contracts(policy, [source()])
    value = observation().model_dump()
    value["frame_id"] = "frame:fixture"
    original = schema(
        observations=[value, {**value, "measured_variable": "other variable"}],
        missing_mentions=[],
        overflow=False,
        missing_context=[],
    )
    corrected = {
        **value,
        "quantities": [
            {
                "part_id": "p:1",
                "cell_ref": None,
                "raw_value": "10",
                "units": None,
                "comparison": None,
                "origin": "author_reported",
            }
        ],
    }
    patch = {
        "observation_index": 0,
        "previous_sha256": observation_hash(original.observations[0]),
        "action": "replace",
        "changed_fields": ["quantities"],
        "replacement": corrected,
        "evidence": [{"part_id": "p:1", "quote": source()["text"]}],
        "reason": "synthetic fixture",
    }
    response = patch_contract(schema.model_fields["observations"].annotation.__args__[0])
    return original, patch, response


def test_patch_preserves_unaffected_observation_and_passed_fields():
    original, patch, schema = patch_example()
    before = original.model_dump()
    revised = apply_patches(
        original, schema(patches=[patch], additions=[], overflow=False), {0: {"quantities"}}, [source()], False
    )
    assert original.model_dump() == before
    assert revised.observations[1] == original.observations[1]
    assert revised.observations[0].model_dump(exclude={"quantities"}) == original.observations[0].model_dump(
        exclude={"quantities"}
    )


@pytest.mark.parametrize("defect", ["stale", "unapproved", "invented_quote", "duplicate", "unrequested_addition"])
def test_invalid_patches_do_not_mutate_original(defect):
    original, patch, schema = patch_example()
    before = original.model_dump()
    additions = []
    if defect == "stale":
        patch["previous_sha256"] = "stale"
    elif defect == "unapproved":
        patch["replacement"]["observed_change"] = "INCREASE"
        patch["changed_fields"].append("observed_change")
    elif defect == "invented_quote":
        patch["evidence"][0]["quote"] = "fabricated"
    elif defect == "unrequested_addition":
        additions = [original.observations[1]]
    patches = [patch, patch] if defect == "duplicate" else [patch]
    with pytest.raises(ValueError):
        apply_patches(
            original,
            schema(patches=patches, additions=additions, overflow=False),
            {0: {"quantities"}},
            [source()],
            False,
        )
    assert original.model_dump() == before


def extract(runtime):
    return extract_grounded(
        [source()],
        bundle(),
        {},
        load_scientific_schema(Path("configs/extraction_schema.yaml")),
        runtime,
        {"extractor": "fixture", "verifier": "fixture"},
        resolver(),
    )


def test_unrelated_mention_issue_does_not_downgrade_supported_finding():
    class Runtime(ScriptedRuntime):
        def structured(self, model, schema, system, payload, role):
            result = super().structured(model, schema, system, payload, role)
            if role.endswith("source_critique"):
                # A missing unused mention affects coverage, not either endpoint.
                result["parsed"]["missing_mentions"] = [
                    {
                        "surface": "cells",
                        "kind": "cell_type",
                        "part_id": "p:1",
                        "anchor": source()["text"],
                        "species": None,
                        "species_evidence": None,
                    }
                ]
            return result

    records, outcome = extract(Runtime("valid"))
    assert records[0]["status"] == "AUTO_ACCEPTED"
    assert outcome["coverage_status"] == "INCOMPLETE"


def test_endpoint_problem_still_blocks_that_finding():
    class Runtime(ScriptedRuntime):
        def structured(self, model, schema, system, payload, role):
            result = super().structured(model, schema, system, payload, role)
            if role.endswith("source_critique"):
                result["parsed"]["mention_checks"]["mention_0"] = {
                    "verdict": "INSUFFICIENT_CONTEXT",
                    "reason": "ambiguous endpoint",
                }
            if role == "grounded:semantic_repair":
                return {"status": "FAILED", "parsed": None}
            return result

    records, outcome = extract(Runtime("valid"))
    assert records[0]["status"] == "UNCERTAIN"
    assert "endpoint_mention_unresolved" in records[0]["uncertainties"]


def test_context_is_recovered_before_mentions_and_relation_extraction():
    from regkg.extraction.frames import FrameAssembly

    calls = []
    extra = {**source("Explicitly linked synthetic context."), "part_id": "p:2"}

    class Runtime(ScriptedRuntime):
        def structured(self, model, schema, system, payload, role):
            calls.append(role)
            if role == "grounded:recovered_experiment_frames":
                role = "grounded:experiment_frames"
            result = super().structured(model, schema, system, payload, role)
            if schema is FrameAssembly and len(payload["parts"]) == 1:
                result["parsed"]["context_requests"] = [
                    {"evidence": {"part_id": "p:1", "quote": source()["text"]}, "question": "Read linked context"}
                ]
            if role == "grounded:mentions":
                assert len(payload["parts"]) == 2
            return result

    def recover(parent, requests):
        calls.append("recover")
        return {"bundle": {**parent, "payload_id": "child"}, "parts": [source(), extra], "annotations": {}}

    records, outcome = extract_grounded(
        [source()],
        bundle(),
        {},
        load_scientific_schema(Path("configs/extraction_schema.yaml")),
        Runtime("valid"),
        {"extractor": "fixture", "verifier": "fixture"},
        resolver(),
        recover,
    )
    assert calls.index("recover") < calls.index("grounded:mentions") < calls.index("grounded:observations")
    assert outcome["bundle_id"] == bundle()["payload_id"]
    assert records[0]["status"] == "AUTO_ACCEPTED"


def test_p4_context_accepts_four_parts_but_keeps_finite_bounds():
    from regkg.extraction.sources import SourceRegistry, bundle_parts

    parts = [{**source(f"Context {i}"), "passage_id": f"s:{i}", "part_id": f"p:{i}"} for i in range(9)]
    registry = object.__new__(SourceRegistry)
    registry.part = lambda doc, passage: next(p for p in parts if p["passage_id"] == passage)
    candidate = {**bundle(), "parts": bundle_parts(parts[:4])}
    assert len(registry.validate_bundle(candidate)) == 4
    with pytest.raises(ValueError, match="P4 context bounds"):
        registry.validate_bundle({**candidate, "parts": bundle_parts(parts)})
    parts[0]["text"] = "x" * 17000
    with pytest.raises(ValueError, match="P4 context bounds"):
        registry.validate_bundle({**candidate, "parts": bundle_parts(parts[:1])})


def test_frame_id_cannot_be_reused_for_another_measurement():
    from regkg.extraction.frames import frame_failures

    obs = observation().model_copy(update={"frame_id": "frame:1", "measured_variable": "cell proportion"})
    frames = {"frame:1": {"fields": {"measured_variable": {"value": "organoid size"}}}}
    assert frame_failures(obs, frames) == ["frame_measurement_mismatch"]
    assert frame_failures(obs.model_copy(update={"measured_variable": "organoid size"}), frames) == []
    assert frame_failures(obs.model_copy(update={"frame_id": "fabricated"}), frames) == ["unknown_evidence_frame"]


def test_batched_review_preserves_global_indices_and_isolates_failed_batch():
    class Runtime(ScriptedRuntime):
        def structured(self, model, schema, system, payload, role):
            if "field_verification_batch_" in role:
                assert len(payload["observations"]) <= 2
                if role.endswith("_batch_1"):
                    return {"status": "FAILED", "parsed": None}
                role = role.split("_batch_")[0]
            result = super().structured(model, schema, system, payload, role)
            if role == "grounded:observations":
                obs = result["parsed"]["observations"][0]
                result["parsed"]["observations"] = [{**obs, "limitations": [f"synthetic record {i}"]} for i in range(3)]
            if role.endswith("source_critique"):
                result["parsed"]["fact_checks"]["fact_0"]["observation_indices"] = [0, 1, 2]
            return result

    records, outcome = extract(Runtime("valid"))
    assert [r["observation_index"] for r in records] == [0, 1, 2]
    assert [r["status"] for r in records] == ["AUTO_ACCEPTED", "AUTO_ACCEPTED", "UNCERTAIN"]
    assert outcome["coverage_status"] == "INCOMPLETE"


def test_rejected_unused_frame_proposal_does_not_taint_final_coverage():
    class Runtime(ScriptedRuntime):
        def structured(self, model, schema, system, payload, role):
            result = super().structured(model, schema, system, payload, role)
            if role == "grounded:experiment_frames":
                bad = deepcopy(result["parsed"]["frames"][0])
                bad["result"]["quote"] = "invented quotation"
                result["parsed"]["frames"].append(bad)
            return result

    records, outcome = extract(Runtime("valid"))
    assert outcome["invalid_frames"]
    assert outcome["coverage_status"] == "COMPLETE"
    assert records[0]["status"] == "AUTO_ACCEPTED"


def test_frame_context_compaction_is_lossless_and_preserves_original():
    from regkg.extraction.frames import compact_frame_context

    quote = {"part_id": "p:1", "quote": source()["text"]}
    original = [
        {
            "frame_id": "f:1",
            "result": quote,
            "fields": {
                "assay": {"value": "qPCR", "evidence": [quote]},
                "measured_variable": {"value": "CTGF expression", "evidence": [quote]},
                "species": None,
            },
        }
    ]
    before = deepcopy(original)
    compact, dictionary = compact_frame_context(original)
    assert len(dictionary) == 1 and original == before
    restored = deepcopy(compact)
    for frame in restored:
        frame["result"] = dictionary[frame.pop("result_ref")]
        for value in frame["fields"].values():
            if value is not None:
                value["evidence"] = [dictionary[k] for k in value.pop("evidence_refs")]
    assert restored == original
