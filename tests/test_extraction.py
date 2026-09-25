"""Synthetic engineering cases; none are biological evidence."""

from pathlib import Path

import pytest
from langchain_core.language_models.chat_models import BaseChatModel
from langchain_core.messages import AIMessage
from langchain_core.outputs import ChatGeneration, ChatResult
from pydantic import Field

from regkg.config import ModelSpec, read_yaml
from regkg.extraction.assembly import assemble, validate_proposal
from regkg.extraction.assembly_schemas import AssemblyProposal
from regkg.extraction.assembly_tools import SourceTools
from regkg.extraction.frames import FRAME_FIELDS
from regkg.extraction.runtime import Runtime, model_kwargs
from regkg.extraction.schemas import Capability, Finding, FindingReview
from regkg.extraction.validation import EntityResolver, assess
from regkg.provenance import read_json


def source(text="TEAD1 knockdown did not affect CTGF in human lung fibroblasts."):
    return {
        "part_id": "p:1",
        "passage_id": "passage:1",
        "text": text,
        "start": 10,
        "end": 10 + len(text),
        "document_id": "d:1",
        "document_sha256": "docsha",
        "asset_sha256": "assetsha",
        "publication_id": "pub:1",
        "publication_version_id": "v:1",
        "locator": "/p[1]",
        "page": None,
        "kind": "paragraph",
        "order": 1,
        "table_id": None,
        "item_id": None,
        "cells": None,
    }


def finding(**overrides):
    value = dict(
        subject={"name": "TEAD1", "kind": "gene", "species": "Homo sapiens"},
        object={"name": "CTGF", "kind": "gene", "species": "Homo sapiens"},
        relation="REGULATES",
        direction="NO_EFFECT",
        outcome="negative_or_null",
        statement_status="primary_result",
        directness="not_established",
        context={
            "species": "Homo sapiens",
            "tissue": "lung",
            "cell_type": "fibroblast",
            "condition": None,
            "model_system": None,
        },
        assay="knockdown",
        intervention="TEAD1 knockdown",
        experiment_label=None,
        assertion=source()["text"],
        citations=[{"part_id": "p:1", "quote": source()["text"]}],
        quantities=[],
        limitations=[],
    )
    value.update(overrides)
    return Finding.model_validate(value)


def resolver():
    return EntityResolver(
        [
            {
                "source_symbol": n,
                "approved_symbol": n,
                "species": "Homo sapiens",
                "mapping_status": "resolved_approved_symbol",
                "hgnc_id": i,
                "gene_id": i,
                "mapping_source": "synthetic",
                "mapping_version": "test",
            }
            for n, i in [("TEAD1", "HGNC:1"), ("CTGF", "HGNC:2")]
        ],
        "test",
    )


def review(status="SUPPORTED", issues=None):
    return FindingReview(
        source_target_change="NO_EFFECT",
        finding_index=0,
        status=status,
        field_issues=issues or [],
        explanation="Synthetic check",
    )


def bundle(state="READY_FULL_TEXT"):
    return {
        "payload_id": "b:1",
        "publication_id": "pub:1",
        "pmid": "1",
        "document_id": "d:1",
        "canonical_sha256": "docsha",
        "source_asset_sha256": "assetsha",
        "readiness_state": state,
        "readiness_reasons": [],
        "document_parse": {"state": "PARSED"},
        "text_version": "v:1",
    }


def test_negative_is_accepted_and_offsets_are_host_calculated():
    result = assess(finding(), review(), [source()], bundle(), resolver())
    assert result["status"] == "AUTO_ACCEPTED"
    assert result["spans"][0]["start"] == 10
    assert result["finding"]["outcome"] == "negative_or_null"
    assert result["independent_study_id"] is None


@pytest.mark.parametrize(
    "change,expected",
    [
        ({"citations": [{"part_id": "p:1", "quote": "invented source"}]}, "REJECTED"),
        ({"relation": "BINDS", "directness": "direct"}, "REJECTED"),
        ({"statement_status": "speculation"}, "UNCERTAIN"),
        ({"subject": {"name": "TEAD1", "kind": "gene", "species": "Mus musculus"}}, "UNCERTAIN"),
        ({"outcome": "positive"}, "REJECTED"),
    ],
)
def test_disposition_does_not_promote_unsupported_or_unknown_fields(change, expected):
    assert assess(finding(**change), review(), [source()], bundle(), resolver())["status"] == expected


def test_reversal_or_missing_context_fails_even_with_valid_quotes():
    assert (
        assess(
            finding(direction="INCREASE"),
            review("UNSUPPORTED", ["reversed direction"]),
            [source()],
            bundle(),
            resolver(),
        )["status"]
        == "REJECTED"
    )
    assert assess(finding(), None, [source()], bundle(), resolver())["status"] == "UNCERTAIN"


def test_complex_never_maps_to_one_human_gene():
    f = finding(subject={"name": "TEAD family", "kind": "family", "species": "Homo sapiens"})
    mapped = resolver().resolve(f.subject)
    assert mapped["kind"] == "family" and "hgnc_id" not in mapped


def test_reported_species_alias_normalizes_without_cross_species_mapping():
    human = finding(subject={"name": "TEAD1", "kind": "gene", "species": "human"})
    mouse = finding(subject={"name": "TEAD1", "kind": "gene", "species": "mouse"})
    assert resolver().resolve(human.subject)["hgnc_id"] == "HGNC:1"
    assert resolver().resolve(mouse.subject)["entity_id"] is None
    a = assess(finding(), review(), [source()], bundle(), resolver())
    b = assess(human, review(), [source()], bundle(), resolver())
    assert a["claim_id"] == b["claim_id"]


def test_invented_table_cell_rejected():
    f = finding(
        quantities=[
            {
                "part_id": "p:1",
                "cell_ref": "fake",
                "raw_value": "TEAD1",
                "units": "x",
                "comparison": "x",
                "origin": "author_reported",
            }
        ]
    )
    assert "table_cell_mismatch" in assess(f, review(), [source()], bundle(), resolver())["failures"]


def test_claim_identity_is_paper_independent_but_evidence_is_not():
    a = assess(finding(), review(), [source()], bundle(), resolver())
    b = assess(finding(), review(), [source()], {**bundle(), "publication_id": "pub:2"}, resolver())
    assert a["claim_id"] == b["claim_id"] and a["finding_id"] != b["finding_id"]


class Registry:
    def __init__(self, parts=None):
        self.parts = parts or [source()]
        self.changed = False
        self.manifest_hash = "synthetic"
        self.file_hashes = {"d:1": "synthetic"}

    def paper_parts(self, b):
        return self.parts

    def document(self, doc_id):
        if self.changed:
            raise ValueError("SOURCE_CHANGED")

    def validate_bundle(self, b, require_ready=True):
        return self.parts


def test_tool_scope_and_cache_never_hide_source_changes():
    registry = Registry()
    tools = SourceTools(registry, bundle(), [])
    assert tools.call("read_passages", part_ids=["outside"])["status"] == "DENIED"
    assert tools.call("read_passages", part_ids=["p:1"])["status"] == "OK"
    registry.changed = True
    assert tools.call("read_passages", part_ids=["p:1"])["status"] == "SOURCE_CHANGED"


def test_oversized_tool_result_is_not_seen_or_silently_truncated():
    tools = SourceTools(Registry([source("x" * 7000)]), bundle(), [])
    assert tools.call("read_passages", part_ids=["p:1"])["status"] == "LIMIT_REACHED"
    assert "p:1" not in tools.seen


def test_table_numeric_filter_requires_reviewed_units_and_keeps_zero():
    row = {
        **source("A | 0"),
        "table_id": "t:1",
        "kind": "table_row",
        "cells": [{"col_start": 0, "text": "A", "header": "gene"}, {"col_start": 1, "text": "0", "header": "value"}],
    }
    tools = SourceTools(Registry([row]), bundle(), [])
    args = {"table_id": "t:1", "column_ids": ["1"], "filters": [{"column_id": "1", "op": "ge", "values": ["0"]}]}
    assert tools.call("read_table_rows", **args)["status"] == "UNSUPPORTED"
    tools = SourceTools(
        Registry([row]),
        bundle(),
        [],
        meaning_reviews={"t:1": {"1": {"numeric": True, "units": "synthetic units", "scale": "linear"}}},
    )
    result = tools.call("read_table_rows", **args)
    assert result["parts"][0]["cells"][1]["text"] == "0"
    assert tools.call("read_table_rows", **args, row_ids=["p:1"])["status"] == "INVALID_ARGUMENT"


def test_agent_bypass_and_blocked_sources_use_no_model():
    assert assemble(Registry(), bundle(), "", None, None, {})["status"] == "BYPASSED_READY"
    assert assemble(Registry(), bundle("NEEDS_ASSET"), "", None, None, {})["status"] == "BLOCKED_SOURCE"


def test_agent_cannot_select_unseen_or_clear_reviewed_semantics():
    tools = SourceTools(Registry(), bundle(), [source()])
    proposal = AssemblyProposal(
        schema_version="evidence-assembly-1",
        disposition="CONTEXT_PROPOSED",
        selection=[{"part_id": "fake", "role": "anchor"}],
        bindings=[],
        issues=[],
        decision_note="test",
    )
    b = {**bundle("NEEDS_CONTEXT"), "readiness_reasons": ["contrast meaning unknown"]}
    issues, _ = validate_proposal(proposal, tools, b, [source()])
    assert "unseen_or_duplicate_source_parts" in issues and "reviewed_source_blocker" in issues


def test_provider_isolation_and_price_units():
    settings = {"max_output_tokens": 100, "timeout_seconds": 1, "reasoning_effort": "low"}
    env = {
        "LITELLM_BASE_URL": "https://example.org/gateway",
        "LITELLM_API_KEY": "dummy",
        "OPENROUTER_REASONING": "high",
        "OPENROUTER_MAX_PRICE_INPUT": "0.15",
        "OPENROUTER_MAX_PRICE_OUTPUT": "0.50",
        "OPENROUTER_API_KEY": "dummy",
        "GROQ_API_KEY": "dummy",
    }
    llm = model_kwargs(ModelSpec("litellm", "Org/Name:rev"), env, settings)
    assert llm["model"] == "Org/Name:rev" and llm["base_url"] == env["LITELLM_BASE_URL"]
    assert "extra_body" not in llm and llm["reasoning_effort"] == "low"
    groq = model_kwargs(ModelSpec("groq", "name"), env, settings)
    assert "extra_body" not in groq and "reasoning_effort" not in groq
    router = model_kwargs(ModelSpec("openrouter", "name"), env, settings)
    assert router["extra_body"]["provider"]["max_price"] == {"prompt": 0.15, "completion": 0.5}


class Chat:
    def __init__(self):
        self.calls = 0

    def with_structured_output(self, schema, **kwargs):
        assert kwargs == {"method": "json_schema", "include_raw": True, "strict": True}
        return self

    def invoke(self, messages, config):
        self.calls += 1
        return {
            "parsed": Capability(echoed_text="ok"),
            "parsing_error": None,
            "raw": AIMessage(
                content='{"echoed_text":"ok"}',
                usage_metadata={"input_tokens": 12, "output_tokens": 6, "total_tokens": 18},
            ),
        }


def test_structured_replay_and_shared_budget_survive_restart(tmp_path):
    settings = read_yaml(Path("configs/extraction.yaml"))["runtime"]
    settings["max_calls"] = 1
    runtime = Runtime(tmp_path, settings, {"provider": "synthetic"})
    chat = Chat()
    first = runtime.structured(chat, Capability, "test", {}, "extractor")
    assert first["status"] == "SUCCEEDED"
    resumed = Runtime(tmp_path, settings, {"provider": "synthetic"})
    assert resumed.structured(chat, Capability, "test", {}, "extractor")["cached"]
    assert resumed.structured(chat, Capability, "other", {}, "verifier")["status"].startswith("LIMIT:")
    assert chat.calls == 1 and read_json(tmp_path / "budget.json")["used"]["calls"] == 1


def test_explicit_failed_retry_keeps_prior_reservation_and_success_cache(tmp_path):
    settings = read_yaml(Path("configs/extraction.yaml"))["runtime"]
    settings["attempts_per_call"] = 1

    class Failed(Chat):
        def invoke(self, *args, **kwargs):
            raise TimeoutError("synthetic timeout")

    first = Runtime(tmp_path, settings, {"provider": "synthetic"})
    assert first.structured(Failed(), Capability, "test", {}, "extractor")["status"] == "FAILED"
    resumed = Runtime(tmp_path, settings, {"provider": "synthetic"}, retry_failed=True)
    result = resumed.structured(Chat(), Capability, "test", {}, "extractor")
    assert result["status"] == "SUCCEEDED" and len(result["attempts"]) == 2
    assert resumed.budget.used["calls"] == 2 and resumed.budget.unknown_token_calls == 1


class ScriptedModel(BaseChatModel):
    replies: list[AIMessage]
    index: int = 0
    bound_names: list[str] = Field(default_factory=list)

    @property
    def _llm_type(self):
        return "synthetic-tool-fixture"

    def bind_tools(self, tools, **kwargs):
        self.bound_names = [t.get("function", {}).get("name") if isinstance(t, dict) else t.name for t in tools]
        return self

    def _generate(self, messages, stop=None, run_manager=None, **kwargs):
        reply = self.replies[self.index]
        self.index += 1
        return ChatResult(generations=[ChatGeneration(message=reply)])


def agent_reply(name, args):
    return AIMessage(
        content="",
        tool_calls=[{"id": "call_fixture", "name": name, "args": args}],
        usage_metadata={"input_tokens": 10, "output_tokens": 10, "total_tokens": 20},
    )


def test_create_agent_real_sdk_tools_proposal_and_zero_call_replay(tmp_path):
    settings = read_yaml(Path("configs/extraction.yaml"))
    # Byte-bound token accounting includes all six schemas and accumulated tool history.
    limits = {**settings["assembly"], "max_input_tokens": 24000}
    runtime = Runtime(tmp_path, settings["runtime"], {"provider": "synthetic"})
    p = {**source(), "table_id": "table:1"}
    legend = {
        **source("Synthetic experiment legend"),
        "part_id": "p:2",
        "passage_id": "passage:2",
        "table_id": "table:1",
        "kind": "table_caption",
    }
    registry = Registry([p, legend])
    registry.validate_bundle = lambda b, require_ready=True: [p]
    proposal = {
        "schema_version": "evidence-assembly-1",
        "disposition": "CONTEXT_PROPOSED",
        "selection": [{"part_id": "p:1", "role": "anchor"}, {"part_id": "p:2", "role": "legend"}],
        "bindings": [],
        "issues": [],
        "decision_note": "synthetic original-source selection",
    }
    model = ScriptedModel(
        replies=[agent_reply("read_passages", {"part_ids": ["p:2"]}), agent_reply("AssemblyProposal", proposal)]
    )
    result = assemble(registry, bundle("NEEDS_CONTEXT"), "synthetic question", model, runtime, limits)
    assert result["status"] == "BUNDLE_VALIDATED", result
    assert result["calls"] == 2 and result["tool_calls"] == 2
    replay = assemble(registry, bundle("NEEDS_CONTEXT"), "synthetic question", model, runtime, limits)
    assert replay["cached"] and model.index == 2


def test_agent_reserves_parallel_tool_calls_before_any_dispatch(tmp_path):
    settings = read_yaml(Path("configs/extraction.yaml"))
    limits = {**settings["assembly"], "max_input_tokens": 24000, "max_tool_calls": 1}
    runtime = Runtime(tmp_path, settings["runtime"], {"provider": "synthetic"})
    reply = AIMessage(
        content="",
        tool_calls=[{"id": str(i), "name": "read_passages", "args": {"part_ids": ["p:1"]}} for i in range(2)],
    )
    model = ScriptedModel(replies=[reply])
    result = assemble(Registry(), bundle("NEEDS_CONTEXT"), "synthetic question", model, runtime, limits)
    assert result["stopping_condition"] == "ASSEMBLY_TOOL_LIMIT", result
    ledgers = list((tmp_path / "assembly").rglob("ledger.json"))
    assert not any("tool" in e for e in read_json(ledgers[0])["events"])


def test_litellm_sdk_sends_strict_schema_to_exact_proxy_path():
    import json

    import httpx
    from langchain_openai import ChatOpenAI

    captured = []

    def respond(request):
        captured.append(request)
        return httpx.Response(
            200,
            json={
                "id": "fixture",
                "object": "chat.completion",
                "created": 0,
                "model": "Org/Deployment:rev",
                "choices": [
                    {
                        "index": 0,
                        "finish_reason": "stop",
                        "message": {"role": "assistant", "content": '{"echoed_text":"fixture"}'},
                    }
                ],
                "usage": {"prompt_tokens": 10, "completion_tokens": 5, "total_tokens": 15},
            },
        )

    settings = {"max_output_tokens": 100, "timeout_seconds": 1, "reasoning_effort": "low"}
    env = {
        "LITELLM_BASE_URL": "https://example.org/proxy",
        "LITELLM_API_KEY": "fixture-only",
        "OPENROUTER_REASONING": "high",
    }
    with httpx.Client(transport=httpx.MockTransport(respond)) as client:
        chat = ChatOpenAI(**model_kwargs(ModelSpec("litellm", "Org/Deployment:rev"), env, settings), http_client=client)
        result = chat.with_structured_output(Capability, method="json_schema", strict=True).invoke("fixture")
    assert result.echoed_text == "fixture"
    assert str(captured[0].url) == "https://example.org/proxy/chat/completions"
    payload = json.loads(captured[0].content)
    assert payload["response_format"]["json_schema"]["strict"] is True
    assert "provider" not in payload and "reasoning" not in payload
    assert captured[0].headers["Authorization"] == "Bearer fixture-only"


def test_agent_no_progress_stops_without_resetting_budget(tmp_path):
    settings = read_yaml(Path("configs/extraction.yaml"))
    runtime = Runtime(tmp_path, settings["runtime"], {"provider": "synthetic"})
    model = ScriptedModel(replies=[agent_reply("read_passages", {"part_ids": ["p:1"]}) for _ in range(4)])
    result = assemble(Registry(), bundle("NEEDS_CONTEXT"), "fixture repeat", model, runtime, settings["assembly"])
    assert result["stopping_condition"] == "ASSEMBLY_CALL_OR_PROGRESS_LIMIT", result
    assert model.index <= 3
    again = assemble(Registry(), bundle("NEEDS_CONTEXT"), "fixture repeat", model, runtime, settings["assembly"])
    assert again["cached"] and runtime.budget.used["calls"] == result["calls"]
    changed_question = assemble(
        Registry(), bundle("NEEDS_CONTEXT"), "different question", model, runtime, settings["assembly"]
    )
    assert changed_question["status"] == "INTERRUPTED_REVIEW_REQUIRED"
    assert runtime.budget.used["calls"] == result["calls"]


def test_partial_source_and_unrelated_experiment_cannot_be_assembled():
    anchor = source()
    other = {**source("Unrelated experiment"), "part_id": "p:2", "passage_id": "passage:2"}
    tools = SourceTools(Registry([anchor, other]), bundle(), [anchor])
    tools.call("read_passages", part_ids=["p:2"])
    proposal = AssemblyProposal(
        schema_version="evidence-assembly-1",
        disposition="CONTEXT_PROPOSED",
        selection=[{"part_id": "p:1", "role": "anchor"}, {"part_id": "p:2", "role": "methods"}],
        bindings=[],
        issues=[],
        decision_note="synthetic",
    )
    issues, _ = validate_proposal(proposal, tools, bundle("NEEDS_CONTEXT"), [anchor])
    assert "experiment_link_requires_review" in issues
    b = {**bundle("NEEDS_CONTEXT"), "document_parse": {"state": "PARTIAL"}}
    assert assemble(Registry(), b, "", None, None, {})["status"] == "BLOCKED_SOURCE"


def test_workflow_writes_joinable_findings_and_replays_without_calls(tmp_path, monkeypatch):
    import json
    from types import SimpleNamespace

    import pandas as pd

    from regkg.extraction.grounded import REVIEW_FIELDS
    from regkg.provenance import write_json
    from regkg.workflows import extraction as workflow

    (tmp_path / "configs").mkdir()
    (tmp_path / "configs/extraction.yaml").write_text(Path("configs/extraction.yaml").read_text())
    (tmp_path / "configs/extraction_schema.yaml").write_text(Path("configs/extraction_schema.yaml").read_text())
    (tmp_path / "configs/kg_schema.yaml").write_text(Path("configs/kg_schema.yaml").read_text())
    mappings = []
    for entries in resolver().index.values():
        mappings.extend(entries)
    mapping_path = tmp_path / "data/processed/mcandidates-c278c6625ff7c537/gene_mappings.parquet"
    mapping_path.parent.mkdir(parents=True)
    pd.DataFrame(mappings).to_parquet(mapping_path)
    write_json(tmp_path / "input/extraction_readiness.json", {"manual_article_requests": 1})
    spec = SimpleNamespace(spec=ModelSpec("litellm", "fixture"))
    monkeypatch.setattr(workflow, "load_model_settings", lambda _: SimpleNamespace(extractor=spec, verifier=spec))
    monkeypatch.setattr(workflow, "load_environment", lambda _: {"LITELLM_BASE_URL": "https://example.org"})

    class FrozenFixture(Registry):
        def __init__(self, *args):
            super().__init__()
            self.root = tmp_path
            self.bundles = {"b:1": {**bundle(), "parts": [source()], "lineages": list(workflow.LINEAGES)}}
            self.artifact = tmp_path / "input"

    monkeypatch.setattr(workflow, "SourceRegistry", FrozenFixture)
    monkeypatch.setattr(workflow, "pubtator_context", lambda *args: {"assets": {}, "gene_mentions": []})
    monkeypatch.setattr(workflow, "code_fingerprint", lambda *args: "synthetic-code")
    calls = []

    class FixtureChat:
        def with_structured_output(self, schema, **kwargs):
            self.schema = schema
            return self

        def invoke(self, messages, config):
            calls.append(self.schema["title"])
            payload = json.loads(messages[-1].content)
            if self.schema["title"] == "Capability":
                parsed = {"echoed_text": "source-bound capability check"}
            elif self.schema["title"] == "FrameAssembly":
                parsed = {
                    "frames": [
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
            elif self.schema["title"] == "TypedInventory":
                parsed = {
                    "overflow": False,
                    "mentions": [
                        {
                            "surface": n,
                            "kind": "gene",
                            "part_id": "p:1",
                            "anchor": source()["text"],
                            "species": "Homo sapiens",
                            "species_evidence": {"part_id": "p:1", "quote": source()["text"]},
                        }
                        for n in ["TEAD1", "CTGF"]
                    ],
                }
            elif self.schema["title"] == "TypedObservations":
                ids = {m["surface"]: m["mention_id"] for m in payload["inventory"]}
                obs = finding().model_dump(exclude={"subject", "object", "direction"})
                obs.update(
                    frame_id=payload["evidence_frames"][0]["frame_id"],
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
                parsed = {
                    "observations": [obs],
                    "missing_mentions": [],
                    "overflow": False,
                    "missing_context": [],
                }
            elif self.schema["title"] == "SourceRead":
                parsed = {
                    "overflow": False,
                    "facts": [
                        {
                            "subject_surface": "TEAD1",
                            "object_surface": "CTGF",
                            "measured_variable": "CTGF expression",
                            "observed_change": "NO_EFFECT",
                            "intervention": "TEAD1 knockdown",
                            "evidence": {"part_id": "p:1", "quote": source()["text"]},
                        }
                    ],
                }
            elif self.schema["title"] == "SourceCritique":
                parsed = {
                    "mention_checks": {
                        f"mention_{i}": {"verdict": "SUPPORTED", "reason": "synthetic"}
                        for i in range(len(payload["inventory"]))
                    },
                    "fact_checks": {
                        "fact_0": {
                            "disposition": "CAPTURED",
                            "observation_indices": [0],
                            "reason": "same synthetic null observation",
                        }
                    },
                    "missing_mentions": [],
                    "context_requests": [],
                    "overflow": False,
                }
            else:
                parsed = {
                    "observation_0": {
                        "source_fact_index": 0,
                        "source_target_change": "NO_EFFECT",
                        "checks": {f: {"verdict": "SUPPORTED", "reason": "synthetic"} for f in sorted(REVIEW_FIELDS)},
                    }
                }
            return {
                "parsed": parsed,
                "parsing_error": None,
                "raw": AIMessage(
                    content=json.dumps(parsed),
                    usage_metadata={"input_tokens": 50, "output_tokens": 50, "total_tokens": 100},
                ),
            }

    monkeypatch.setattr(workflow, "build_chat_model", lambda *args: FixtureChat())
    result = workflow.run(tmp_path, "fixture-selection", limit=1, execute=True, input_mode="fixture")
    assert result["dispositions"] == {"AUTO_ACCEPTED": 1}
    out = Path(result["output"])
    accepted = pd.read_parquet(out / "accepted_findings.parquet")
    evidence = pd.read_parquet(out / "evidence_assertions.parquet")
    assert accepted.finding_id.tolist() == evidence.finding_id.tolist()
    assert json.loads(accepted.record_json.iloc[0])["finding"]["outcome"] == "negative_or_null"
    replay = workflow.run(tmp_path, "fixture-selection", limit=1, execute=True, input_mode="fixture")
    assert replay["status"] == "REUSED_VERIFIED" and replay["calls_this_invocation"] == 0
    assert calls == [
        "Capability",
        "FrameAssembly",
        "TypedInventory",
        "TypedObservations",
        "SourceRead",
        "CompleteFieldVerification",
        "SourceCritique",
    ]


def test_pubtator_context_preserves_external_identity_and_rejects_changed_asset(tmp_path):
    import hashlib
    import json
    from types import SimpleNamespace

    from regkg.extraction.sources import pubtator_context

    text = "TEAD1 regulates CTGF."
    part = source(text)
    passage = SimpleNamespace(passage_id=part["passage_id"], text=text, start=10, end=10 + len(text))
    doc = SimpleNamespace(publication_id="pub:1", canonical_text=" " * 10 + text, passages=[passage])
    registry = SimpleNamespace(root=tmp_path, document=lambda _: doc)
    annotation = {
        "passages": [
            {
                "offset": 0,
                "text": text,
                "annotations": [
                    {
                        "id": "a",
                        "infons": {"type": "Gene", "identifier": "7003"},
                        "text": "TEAD1",
                        "locations": [{"offset": 0, "length": 5}],
                    },
                    {
                        "id": "bad",
                        "infons": {"type": "Gene", "identifier": "1490"},
                        "text": "CTGF",
                        "locations": [{"offset": 0, "length": 4}],
                    },
                ],
            }
        ]
    }
    raw = json.dumps(annotation).encode()
    asset = tmp_path / "data/papers/pub_1" / hashlib.sha256(raw).hexdigest() / "pubtator.json"
    asset.parent.mkdir(parents=True)
    asset.write_bytes(raw)
    result = pubtator_context(registry, [part])
    assert len(result["gene_mentions"]) == 1
    hit = result["gene_mentions"][0]
    assert hit["text"] == "TEAD1" and hit["external_identifier"] == "7003"
    assert hit["start"] == 10 and hit["external_offset"] == 0
    assert result["unaligned_document_mentions"] == 1
    assert "species" not in hit
    asset.write_text("{}")
    with pytest.raises(ValueError, match="checksum"):
        pubtator_context(registry, [part])


def test_treatment_or_cell_state_cannot_be_accepted_as_a_regulatory_gene():
    proposed = finding(subject={"name": "T3 therapy", "kind": "cell_state", "species": "Homo sapiens"})
    result = assess(proposed, review(), [source()], bundle(), resolver())
    assert result["status"] == "REJECTED"
    assert "regulatory_relation_requires_regulator_entity" in result["failures"]


def test_native_schema_failure_keeps_raw_response_and_known_usage(tmp_path):
    import json

    import httpx
    from langchain_openai import ChatOpenAI

    from regkg.extraction.schemas import Extraction

    invalid = {"status": "NO_RELATION", "findings": [finding().model_dump()], "missing_context": []}
    raw_text = json.dumps(invalid)

    def respond(request):
        payload = json.loads(request.content)
        assert payload["response_format"]["json_schema"]["strict"] is True
        return httpx.Response(
            200,
            json={
                "id": "fixture",
                "object": "chat.completion",
                "created": 0,
                "model": "fixture",
                "choices": [
                    {"index": 0, "finish_reason": "stop", "message": {"role": "assistant", "content": raw_text}}
                ],
                "usage": {"prompt_tokens": 10, "completion_tokens": 50, "total_tokens": 60},
            },
        )

    settings = {**read_yaml(Path("configs/extraction.yaml"))["runtime"], "attempts_per_call": 1}
    runtime = Runtime(tmp_path, settings, {"mode": "synthetic"})
    with httpx.Client(transport=httpx.MockTransport(respond)) as client:
        model = ChatOpenAI(model="fixture", api_key="fixture-only", http_client=client)
        result = runtime.structured(model, Extraction, "synthetic", {}, "extractor")
    assert result["status"] == "FAILED" and result["parsed"] is None
    assert result["attempts"][0]["content"] == raw_text
    assert result["attempts"][1]["validation_issues"][0]["type"] == "value_error"
    assert runtime.budget.used["input_tokens"] == 10
    assert runtime.budget.used["output_tokens"] == 50
    assert runtime.budget.used["calls"] == 1


def test_named_assembly_repair_preserves_parent_and_replays(tmp_path):
    from regkg.provenance import sha256_file

    settings = read_yaml(Path("configs/extraction.yaml"))
    runtime = Runtime(tmp_path, settings["runtime"], {"provider": "synthetic"})
    model = ScriptedModel(replies=[agent_reply("read_passages", {"part_ids": ["p:1"]}) for _ in range(4)])
    first = assemble(Registry(), bundle("NEEDS_CONTEXT"), "fixture", model, runtime, settings["assembly"])
    parent = next((tmp_path / "assembly/cases").glob("*/ledger.json"))
    parent_sha = sha256_file(parent)
    proposal = {
        "schema_version": "evidence-assembly-1",
        "disposition": "NO_ADDITIONAL_CONTEXT_FOUND",
        "selection": [{"part_id": "p:1", "role": "anchor"}],
        "bindings": [],
        "issues": [],
        "decision_note": "No additional source found; do not fabricate context.",
    }
    repaired_model = ScriptedModel(replies=[agent_reply("AssemblyProposal", proposal)])
    repaired = assemble(
        Registry(),
        bundle("NEEDS_CONTEXT"),
        "fixture",
        repaired_model,
        runtime,
        settings["assembly"],
        repair_id="fixture-repair",
    )
    assert repaired["calls"] == 1
    assert sha256_file(parent) == parent_sha
    assert runtime.budget.used["calls"] == first["calls"] + 1
    replay = assemble(
        Registry(),
        bundle("NEEDS_CONTEXT"),
        "fixture",
        repaired_model,
        runtime,
        settings["assembly"],
        repair_id="fixture-repair",
    )
    assert replay["cached"] and repaired_model.index == 1


def test_completed_direct_calls_do_not_hide_failed_assembly(tmp_path):
    from regkg.workflows.extraction import persist

    summary = persist(tmp_path, [], [{"status": "NO_RELATION"}], {"assembly_result": "FAILED_OR_LIMIT_REACHED"})
    assert summary["status"] == "PARTIAL_WORKFLOW"


@pytest.mark.parametrize("second_valid", [True, False])
def test_agent_schema_repair_is_once_bounded_and_keeps_failed_raw(tmp_path, second_valid):
    settings = read_yaml(Path("configs/extraction.yaml"))
    runtime = Runtime(tmp_path, settings["runtime"], {"provider": "synthetic"})
    valid = {
        "schema_version": "evidence-assembly-1",
        "disposition": "NO_ADDITIONAL_CONTEXT_FOUND",
        "selection": [{"part_id": "p:1", "role": "anchor"}],
        "bindings": [],
        "issues": [],
        "decision_note": "No source available.",
    }
    model = ScriptedModel(
        replies=[agent_reply("AssemblyProposal", {}), agent_reply("AssemblyProposal", valid if second_valid else {})]
    )
    result = assemble(Registry(), bundle("NEEDS_CONTEXT"), "synthetic", model, runtime, settings["assembly"])
    assert result["calls"] == 2 and model.index == 2
    ledger = read_json(next((tmp_path / "assembly/cases").glob("*/ledger.json")))
    assert ledger["in_flight"] is False
    assert len([e for e in ledger["events"] if "model" in e]) == 2
    assert len([e for e in ledger["events"] if "schema_repair" in e]) == 1
    assert (result["status"] == "FAILED_OR_LIMIT_REACHED") is (not second_valid)


def test_independent_target_change_blocks_false_supported_review():
    checked = review().model_copy(update={"source_target_change": "INCREASE"})
    result = assess(finding(), checked, [source()], bundle(), resolver())
    assert result["status"] == "REJECTED"
    assert "source_target_change_disagrees_with_extraction" in result["failures"]


def test_opposing_target_sign_is_rejected_even_when_verifier_agrees():
    quote = "TEAD1 knockout increased CTGF expression in human lung fibroblasts."
    proposed = finding(
        direction="DECREASE",
        outcome="positive",
        intervention="TEAD1 knockout",
        assertion=quote,
        citations=[{"part_id": "p:1", "quote": quote}],
    )
    checked = review().model_copy(update={"source_target_change": "DECREASE"})
    result = assess(proposed, checked, [source(quote)], bundle(), resolver())
    assert result["status"] == "REJECTED"
    assert "target_change_opposes_unambiguous_cited_direction" in result["failures"]


def test_status_label_cannot_stand_in_for_atomic_assertion():
    result = assess(finding(assertion="reported"), review(), [source()], bundle(), resolver())
    assert result["status"] == "REJECTED"
    assert "assertion_is_status_label_not_proposition" in result["failures"]


@pytest.mark.parametrize(
    "cell_ref,units,expected",
    [("p:1:c0", "counts", "AUTO_ACCEPTED"), (None, "counts", "REJECTED"), ("p:1:c0", "invented_units", "UNCERTAIN")],
)
def test_table_zero_requires_cell_and_source_located_units(cell_ref, units, expected):
    part = {
        **source(),
        "kind": "table_row",
        "text": source()["text"] + " 0 counts",
        "cells": [{"col_start": 0, "raw_value": 0, "text": "0"}],
    }
    proposed = finding(
        quantities=[
            {
                "part_id": "p:1",
                "cell_ref": cell_ref,
                "raw_value": "0",
                "units": units,
                "comparison": "knockdown vs control",
                "origin": "author_reported",
            }
        ]
    )
    result = assess(proposed, review(), [part], bundle(), resolver())
    assert result["status"] == expected
    assert result["finding"]["quantities"][0]["raw_value"] == "0"


@pytest.mark.parametrize("reported,proposed", [("-0.5", "0.5"), ("<0.05", "0.05"), ("10", "1"), ("1.05", "1.0")])
def test_prose_quantity_cannot_drop_sign_inequality_or_digits(reported, proposed):
    part = source(source()["text"] + f" The reported value was {reported} counts.")
    f = finding(
        quantities=[
            {
                "part_id": "p:1",
                "cell_ref": None,
                "raw_value": proposed,
                "units": "counts",
                "comparison": "knockdown vs control",
                "origin": "author_reported",
            }
        ]
    )
    assert "quantity_not_source_reported" in assess(f, review(), [part], bundle(), resolver())["failures"]
