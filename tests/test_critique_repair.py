"""End-to-end synthetic repair behavior; no scientific accuracy claims."""

from pathlib import Path

import pytest

from regkg.extraction.context_repair import recover_context
from regkg.extraction.critique import ContextRequest
from regkg.extraction.frames import FRAME_FIELDS
from regkg.extraction.grounded import REVIEW_FIELDS, extract_grounded, load_scientific_schema
from tests.test_extraction import bundle, finding, resolver, source


def mention(name):
    return dict(
        surface=name,
        kind="gene",
        part_id="p:1",
        anchor=source()["text"],
        species="Homo sapiens",
        species_evidence={"part_id": "p:1", "quote": source()["text"]},
    )


def observation(inventory):
    ids = {m["surface"]: m["mention_id"] for m in inventory}
    value = finding().model_dump(exclude={"subject", "object", "direction"})
    value.update(
        subject_id=ids["TEAD1"],
        object_id=ids["CTGF"],
        measured_variable="CTGF expression",
        measurement_evidence={"part_id": "p:1", "quote": source()["text"]},
        observed_change="NO_EFFECT",
        comparison="control",
        evidence_classification=dict(
            evidence_type="TF_PERTURBATION",
            directness="FUNCTIONAL",
            experimental_outcome="NO_DETECTED_EFFECT",
            statement_status="NEGATED",
            measured_or_inferred="measured",
            regulatory_direction="UNKNOWN",
        ),
    )
    return value


class ScriptedRuntime:
    def __init__(self, mode):
        self.mode, self.calls = mode, []

    def structured(self, model, schema, system, payload, role):
        self.calls.append(role)
        stage = role.removeprefix("grounded:")
        if stage in {"experiment_frames", "amend_experiment_frames"}:
            data = {
                "frames": []
                if self.mode == "empty"
                else [
                    {
                        "result": {"part_id": "p:1", "quote": source()["text"]},
                        "fields": {
                            **dict.fromkeys(FRAME_FIELDS),
                            "measured_variable": {
                                "value": "CTGF expression",
                                "evidence": [{"part_id": "p:1", "quote": source()["text"]}],
                            },
                        },
                        "missing_context": [],
                    }
                ],
                "context_requests": [],
                "overflow": False,
            }
        elif stage == "mentions":
            names = ["TEAD1"] if self.mode == "missing_mention" else ["TEAD1", "CTGF"]
            data = {"mentions": [mention(n) for n in names], "overflow": False}
        elif stage == "observations":
            rows = []
            if self.mode not in {"missing", "missing_mention", "empty"}:
                rows = [observation(payload["inventory"])]
                rows[0]["frame_id"] = payload["evidence_frames"][0]["frame_id"]
                if self.mode in {"quantity", "bad_repair", "repair_extra_mentions"}:
                    rows[0]["quantities"] = [
                        {
                            "part_id": "p:1",
                            "cell_ref": None,
                            "raw_value": "999",
                            "units": None,
                            "comparison": None,
                            "origin": "author_reported",
                        }
                    ]
            data = {"observations": rows, "missing_mentions": [], "overflow": False, "missing_context": []}
        elif stage == "semantic_repair":
            row = observation(payload["inventory"])
            row["frame_id"] = payload["evidence_frames"][0]["frame_id"]
            if self.mode == "bad_repair":
                row["observed_change"] = "INCREASE"
                row["outcome"] = "positive"
                row["evidence_classification"]["experimental_outcome"] = "INCREASE"
            patches = []
            for target in payload["correction_scope"]:
                patches.append(
                    {
                        "observation_index": target["observation_index"],
                        "previous_sha256": target["previous_sha256"],
                        "action": "replace",
                        "changed_fields": [k for k, v in target["observation"].items() if row[k] != v],
                        "replacement": row,
                        "evidence": [{"part_id": "p:1", "quote": source()["text"]}],
                        "reason": "synthetic quantity correction",
                    }
                )
            data = {"patches": patches, "additions": [row] if payload["allow_additions"] else [], "overflow": False}
        elif stage == "blind_source_read":
            assert set(payload) == {"publication_id", "pmid", "parts"}
            data = {
                "facts": []
                if self.mode == "empty"
                else [
                    {
                        "subject_surface": "TEAD1",
                        "object_surface": "CTGF",
                        "measured_variable": "CTGF expression",
                        "observed_change": "NO_EFFECT",
                        "intervention": "TEAD1 knockdown",
                        "evidence": {"part_id": "p:1", "quote": source()["text"]},
                    }
                ],
                "overflow": False,
            }
        elif stage in {"field_verification", "repair_field_verification"}:
            data = {
                f"observation_{i}": {
                    "source_fact_index": 0,
                    "source_target_change": "NO_EFFECT",
                    "checks": {name: {"verdict": "SUPPORTED", "reason": "synthetic"} for name in REVIEW_FIELDS},
                }
                for i in range(len(payload["observations"]))
            }
        elif stage in {"source_critique", "repair_source_critique"}:
            if self.mode == "critic_failure":
                return {"status": "FAILED", "parsed": None, "cached": False}
            has_observation = bool(payload["observations"])
            data = {
                "mention_checks": {
                    f"mention_{i}": {"verdict": "SUPPORTED", "reason": "synthetic"}
                    for i in range(len(payload["inventory"]))
                },
                "fact_checks": {
                    f"fact_{i}": {
                        "disposition": "CAPTURED" if has_observation else "MISSING",
                        "observation_indices": [0] if has_observation else [],
                        "reason": "synthetic",
                    }
                    for i in range(len(payload["independent_source_read"]["facts"]))
                },
                "missing_mentions": [mention("CTGF")]
                if self.mode == "missing_mention" and stage == "source_critique"
                else [],
                "context_requests": [],
                "overflow": False,
            }
        else:
            raise AssertionError(stage)
        parsed = schema.model_validate(data).model_dump()
        return {"status": "SUCCEEDED", "parsed": parsed, "cached": False, "input_sha256": stage}


def run(mode):
    runtime = ScriptedRuntime(mode)
    records, outcome = extract_grounded(
        [source()],
        bundle(),
        {},
        load_scientific_schema(Path("configs/extraction_schema.yaml")),
        runtime,
        {"extractor": "fixture-extractor", "verifier": "fixture-critic"},
        resolver(),
    )
    return records, outcome, runtime


@pytest.mark.parametrize("mode", ["missing", "missing_mention", "quantity", "repair_extra_mentions"])
def test_automatic_repair_recovers_omissions_and_rechecks_host_defects(mode):
    records, outcome, runtime = run(mode)
    assert len(records) == 1 and records[0]["status"] == "AUTO_ACCEPTED"
    assert records[0]["finding"]["outcome"] == "negative_or_null"
    assert outcome["verification_status"] == "SUCCEEDED"
    assert outcome["repair"]["status"] == "REVERIFIED"
    assert len(outcome["review_history"]) == 2
    assert runtime.calls.count("grounded:semantic_repair") == 1
    assert "grounded:repair_field_verification" in runtime.calls
    assert "grounded:repair_source_critique" in runtime.calls
    if mode == "quantity":
        assert outcome["raw_observations"][0]["quantities"]
        assert not outcome["final_observations"][0]["quantities"]
        assert outcome["review_history"][0]["assessments"][0]["status"] == "REJECTED"


def test_repair_cannot_introduce_an_accepted_direction_error_or_loop():
    records, outcome, runtime = run("bad_repair")
    assert records[0]["status"] == "REJECTED"
    assert outcome["verification_status"] == "UNRESOLVED_CRITIQUE"
    assert runtime.calls.count("grounded:semantic_repair") == 1
    assert outcome["repair"]["patch_failure"] == "patch_changes_unapproved_fields"
    assert "grounded:repair_field_verification" not in runtime.calls


def test_critic_failure_is_not_silently_accepted_or_retried():
    records, outcome, runtime = run("critic_failure")
    assert records[0]["status"] == "UNCERTAIN"
    assert not outcome["repair"]["attempted"]
    assert "critique_failed" in outcome["unresolved_issues"]
    assert runtime.calls.count("grounded:source_critique") == 1


def test_empty_extraction_receives_source_and_entity_coverage_audit():
    records, outcome, runtime = run("empty")
    assert not records and outcome["status"] == "NO_RELATION"
    assert outcome["verification_status"] == "SUCCEEDED"
    assert not outcome["repair"]["attempted"]
    assert runtime.calls[-2:] == ["grounded:blind_source_read", "grounded:source_critique"]


def test_context_request_requires_original_source_quote_before_any_agent_call():
    class Registry:
        def validate_bundle(self, value):
            return [source()]

    request = ContextRequest(evidence={"part_id": "p:1", "quote": "fabricated context"}, question="fetch legend")
    result = recover_context(Registry(), bundle(), [request], None, None, {})
    assert result == {"status": "CONTEXT_REQUEST_NOT_GROUNDED"}


def test_context_recovery_cannot_drop_original_anchors(monkeypatch):
    from regkg.extraction import context_repair

    anchor = source()
    additional = {**source("synthetic caption"), "part_id": "p:2"}

    class Registry:
        bundles = {}

        def validate_bundle(self, value):
            return value["parts"]

    parent = {**bundle(), "parts": [anchor]}
    request = ContextRequest(evidence={"part_id": "p:1", "quote": anchor["text"]}, question="linked caption")
    proposals = []

    def assemble(registry, investigation, *args, **kwargs):
        proposals.append(investigation)
        return {"status": "BUNDLE_VALIDATED", "bundle": {**parent, "parts": [additional]}}

    monkeypatch.setattr(context_repair, "assemble", assemble)
    result = recover_context(Registry(), parent, [request], None, None, {})
    assert result["bundle"] is None
    assert result["status"] == "CONTEXT_MUST_ADD_WITHOUT_DROPPING_ANCHORS"
    assert proposals[0]["readiness_state"] == "NEEDS_CONTEXT"
    assert parent["readiness_state"] == "READY_FULL_TEXT"


def test_fact_coverage_must_agree_with_independent_field_review():
    from regkg.extraction.critique import critique_contract, critique_issues
    from regkg.extraction.grounded import Mention, SourceRead

    schema = critique_contract(0, 1, Mention)
    critique = schema.model_validate(
        {
            "mention_checks": {},
            "fact_checks": {"fact_0": {"disposition": "CAPTURED", "observation_indices": [0], "reason": "synthetic"}},
            "missing_mentions": [],
            "context_requests": [],
            "overflow": False,
        }
    )
    source_read = SourceRead(
        facts=[
            {
                "subject_surface": "TEAD1",
                "object_surface": "CTGF",
                "measured_variable": "expression",
                "observed_change": "NO_EFFECT",
                "intervention": None,
                "evidence": {"part_id": "p:1", "quote": source()["text"]},
            }
        ],
        overflow=False,
    )
    issues = critique_issues(critique, [], [object()], source_read, [source()], [])
    assert issues == ["fact_0:coverage_verification_disagrees"]


def test_repair_feedback_removes_redundancy_without_dropping_defects():
    from copy import deepcopy

    from regkg.extraction.critique import repair_feedback

    snapshot = {
        "issues": ["field_review_defects"],
        "field_reviews": {
            "reviews": [
                {
                    "observation_index": 0,
                    "checks": [
                        {"field": "relation", "verdict": "SUPPORTED", "reason": "source"},
                        {"field": "direction", "verdict": "UNSUPPORTED", "reason": "reversed"},
                    ],
                }
            ]
        },
        "critique": {
            "mention_checks": {
                "mention_0": {"verdict": "SUPPORTED", "reason": "source"},
                "mention_1": {"verdict": "UNSUPPORTED", "reason": "wrong type"},
            },
            "fact_checks": {"fact_0": {"disposition": "CAPTURED"}, "fact_1": {"disposition": "MISSING"}},
            "missing_mentions": ["synthetic"],
            "context_requests": ["synthetic"],
        },
    }
    original = deepcopy(snapshot)
    compact = repair_feedback(snapshot)
    assert snapshot == original
    assert len(compact["field_reviews"]["reviews"][0]["checks"]) == 1
    assert compact["critique"]["mention_checks"] == {"mention_1": original["critique"]["mention_checks"]["mention_1"]}
    assert compact["critique"]["fact_checks"] == {"fact_1": {"disposition": "MISSING"}}
    assert compact["critique"]["missing_mentions"] == compact["critique"]["context_requests"] == ["synthetic"]


def test_all_field_and_source_failures_are_reported_without_validator_overflow():
    from regkg.extraction.grounded import FieldCheck, ObservationReview, SourceRead, review_finding
    from tests.test_grounded_extraction import observation as synthetic_observation

    obs = synthetic_observation()
    source_read = SourceRead(
        facts=[
            {
                "subject_surface": "DrugA",
                "object_surface": "GeneB",
                "measured_variable": "expression",
                "observed_change": "INCREASE",
                "intervention": None,
                "evidence": {"part_id": "p:1", "quote": "invented source"},
            }
        ],
        overflow=False,
    )
    review = ObservationReview(
        observation_index=0,
        source_fact_index=0,
        source_target_change="NO_EFFECT",
        checks=[FieldCheck(field=name, verdict="UNSUPPORTED", reason="synthetic defect") for name in REVIEW_FIELDS],
    )
    result = review_finding(0, obs, [review], source_read, [{"part_id": "p:1", "text": obs.assertion}])
    assert result.status == "UNSUPPORTED" and len(result.field_issues) == len(REVIEW_FIELDS) + 2


def test_repair_cannot_silently_overwrite_conflicting_species():
    from regkg.extraction.grounded import merge_mentions

    original = {"mention_id": "same-source-span", "species": "Homo sapiens", "annotation_issues": []}
    proposed = {**original, "species": "Mus musculus"}
    result = merge_mentions([original], [proposed])
    assert result[0]["species"] is None
    assert "conflicting_mention_species" in result[0]["annotation_issues"]
    assert original["species"] == "Homo sapiens"
    assert merge_mentions(result, [original])[0]["species"] is None


def test_repair_feedback_keeps_original_identity_when_inventory_positions_change():
    from regkg.extraction.critique import repair_feedback

    mentions = [
        {"mention_id": "m:1", "surface": "GeneA", "kind": "gene", "part_id": "p:1", "species": None},
        {"mention_id": "m:2", "surface": "MarkerB", "kind": "gene", "part_id": "p:1", "species": None},
    ]
    snapshot = {
        "critique": {"mention_checks": {"mention_1": {"verdict": "UNSUPPORTED", "reason": "IF target is protein"}}},
        "field_reviews": None,
    }
    feedback = repair_feedback(snapshot, mentions)
    assert feedback["critique"]["mention_checks"]["mention_1"]["original_mention"] == mentions[1]
    assert "original_mention" not in snapshot["critique"]["mention_checks"]["mention_1"]


def test_oversized_critic_feedback_compacts_passed_checks_without_losing_sources():
    from regkg.extraction.critique import compact_field_reviews
    from regkg.extraction.runtime import token_bound

    class RecordingRuntime(ScriptedRuntime):
        settings = {}

        def structured(self, model, schema, system, payload, role):
            if role == "grounded:source_critique":
                self.request = {"system": system, "payload": payload, "schema": schema.model_json_schema()}
            return super().structured(model, schema, system, payload, role)

    def extract(runtime):
        return extract_grounded(
            [source()],
            bundle(),
            {},
            load_scientific_schema(Path("configs/extraction_schema.yaml")),
            runtime,
            {"extractor": "fixture-extractor", "verifier": "fixture-critic"},
            resolver(),
        )

    original = RecordingRuntime("valid")
    extract(original)
    full_request = original.request
    payload = full_request["payload"]
    compact_payload = {
        **payload,
        "field_reviews": compact_field_reviews(payload["field_reviews"]),
        "passed_field_checks_omitted_from_feedback": True,
    }
    limit = token_bound({**full_request, "payload": compact_payload})
    assert limit < token_bound(full_request)
    constrained = RecordingRuntime("valid")
    constrained.settings = {"max_input_tokens": limit}
    records, outcome = extract(constrained)
    assert token_bound(constrained.request) <= limit
    assert constrained.request["payload"]["parts"] == payload["parts"]
    assert constrained.request["payload"]["independent_source_read"] == payload["independent_source_read"]
    assert outcome["traces"]["source_critique"]["feedback_compacted"]
    assert outcome["review_history"][0]["field_reviews"] == payload["field_reviews"]
    assert records[0]["status"] == "AUTO_ACCEPTED"
