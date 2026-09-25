Current authorized P4 context limit: eight selected source parts and 16,000 serialized characters; the earlier three-part payload examples below are historical. Preserve frozen P3 inputs and all source/experiment-link checks. See [current automation](../P4_CRITIQUE_AUTOMATION.md).

# P4 evidence-assembly agent: implementation contract

Design: 2026-09-22. Implementation checkpoint: 2026-09-23. Status: **IMPLEMENTATION/OFFLINE VALIDATION PRESENT; LIVE ACCEPTANCE PENDING**. See [P4 handoff](../handoffs/P4.md) for tested coverage and limitations.
Read with [P3 corpus readiness](P3-corpus-readiness.md),
[file readiness](P3-file-readiness.md), AGENTS.md and plan §10.
This document narrowly supersedes the old blanket ban on a runtime agent.
The 2026-09-23 user assignment now authorizes implementation and bounded validation on the verified available source subset (plan §16); comprehensive expansion remains required afterward.

## 1. Scope and location in the pipeline

One LangChain `create_agent` instance handles one investigation: one publication
version, one evidence question/anchor, and its explicitly linked parsed assets.
The configured model chooses read-only tools to assemble context. No subagents,
Deep Agents harness, arbitrary code/SQL/shell, browsing, downloads, model switching,
Neo4j access, or automatic scientific reanalysis. Tools are ordinary validated
Python functions over the existing local corpus, not new services.

Sequence: P3 frozen source corpus → deterministic retrieval/readiness → direct
extraction for complete bundles OR bounded evidence assembly → host bundle
validation → extractor → verifier → deterministic finding checks → P5 export.
The extractor and verifier remain tool-free. Scientific claims are not agent output.

The P3 checkpoint freezes source files, parser outputs and reviewed dispositions.
It supplies both ready bundles and a separate, explicit investigation queue for
resolvable context questions. An investigation item is NOT an extraction-ready
bundle. Acquisition/parse failures, unknown raw-data analysis requirements and
unresolved source-identity problems still require P3 repair/disposition, not agent
permission to proceed. P4 creates new immutable bundle artifacts referencing the
frozen sources; it never edits a P3 manifest to mark it ready.

Invoke on a concrete missing reference, ambiguous table description, or context
question identified by retrieval/review. A verifier's `INSUFFICIENT_CONTEXT` may
reopen the same investigation within its original limits. A valid `NO_RELATION`,
negative finding, low support score or lack of a desired conclusion is NOT a
retry trigger. Searches include counter-evidence and qualifiers, not just support.

## 2. Host inputs and model-visible inputs

All JSON contracts reject extra fields. IDs are opaque, nonempty application IDs;
the host resolves them against frozen manifests. The model never supplies paths,
credentials, trusted hashes, budget increases, or publication ownership.

The following Pydantic definitions specify the entry/exit types for implementation.
Cross-record invariants below are additional requirements, not implied by type checking.

```python
from typing import Literal
from pydantic import BaseModel, ConfigDict, Field

class StrictRecord(BaseModel):
    model_config = ConfigDict(extra="forbid")

class SourceRef(StrictRecord):
    part_id: str = Field(min_length=1)

class Gap(StrictRecord):
    code: Literal[
        "MISSING_LEGEND", "MISSING_METHODS", "AMBIGUOUS_CONTRAST",
        "AMBIGUOUS_ENTITY_OR_CONTEXT", "CROSS_ASSET_REFERENCE",
        "CONFLICTING_SOURCE_CONTEXT", "VERIFIER_CONTEXT_REQUEST"
    ]
    question: str = Field(min_length=1, max_length=600)
    anchor_part_ids: list[str] = Field(min_length=1, max_length=3)

class InvestigationInput(StrictRecord):
    schema_version: Literal["evidence-assembly-1"]
    investigation_id: str
    source_corpus_key: str
    source_manifest_sha256: str
    publication_id: str
    publication_version_id: str
    parent_bundle_id: str | None
    candidate_ids: list[str] = Field(max_length=100)
    # Associations are routing context, not proof of the source experiment's identity.
    manuscript_lineages: list[str] = Field(max_length=4)
    question: str = Field(min_length=1, max_length=1000)
    anchor_part_ids: list[str] = Field(min_length=1, max_length=3)
    permitted_asset_ids: list[str] = Field(min_length=1)
    gaps: list[Gap] = Field(min_length=1, max_length=8)
    prior_investigation_id: str | None
    human_review_record_ids: list[str] = Field(max_length=20)

class Selection(StrictRecord):
    part_id: str
    role: Literal["anchor", "legend", "methods", "header", "qualifier", "counter_evidence"]

class ContextBinding(StrictRecord):
    field: Literal[
        "species", "cell_type", "tissue", "condition", "intervention", "assay",
        "comparison", "units", "scale", "normalization", "experiment_link",
        "statistic_definition", "reported_sample_structure"
    ]
    value: str | None = Field(max_length=500)
    state: Literal["SOURCE_STATED", "AMBIGUOUS", "UNKNOWN", "CONFLICTING"]
    source_part_ids: list[str] = Field(max_length=3)

class OpenIssue(StrictRecord):
    code: Literal[
        "MISSING_ASSET", "PARSE_REPAIR", "IDENTITY_REVIEW", "MISSING_CONTEXT",
        "AMBIGUOUS_MEANING", "ANALYSIS_REQUIRED", "CONTEXT_TOO_LARGE", "SOURCE_CONFLICT"
    ]
    question: str = Field(min_length=1, max_length=600)
    source_part_ids: list[str] = Field(max_length=3)

class AssemblyProposal(StrictRecord):
    schema_version: Literal["evidence-assembly-1"]
    disposition: Literal[
        "CONTEXT_PROPOSED", "NEEDS_ASSET", "NEEDS_PARSE_REPAIR",
        "NEEDS_HUMAN_REVIEW", "ANALYSIS_REQUIRED", "NO_ADDITIONAL_CONTEXT_FOUND"
    ]
    selection: list[Selection] = Field(max_length=3)
    bindings: list[ContextBinding] = Field(max_length=12)
    issues: list[OpenIssue] = Field(max_length=8)
    # Short observable explanation; not hidden chain-of-thought or a biological finding.
    decision_note: str = Field(max_length=500)
```

The host envelope additionally supplies a resolved model instance, immutable
asset/part registries, allowlisted lineage values, parser/meaning-review records,
tool/rule/prompt versions, durable usage ledger, and approved budgets. These
dependencies are injected through runtime context and never editable by the LLM.

The model sees the bounded question, gaps, relevant candidate labels, current
anchor content, compact asset inventory and remaining limits. Paginate inventory
through tools; do not inject a whole paper/workbook or an unbounded candidate list.
The permitted-assets list in the host record can be large without being serialized
in every prompt. References inside retrieved content are untrusted source data.

## 3. Source-part registry and common tool response

The host creates immutable `part_id` values from source identity, canonical
content and locators. Initial anchors and every tool-returned part are registered.
A selected part must have actually been returned in this investigation or supplied
as an initial anchor; guessing another valid corpus ID is not sufficient.

Each source-part record contains:

| Field | Type / contract |
|---|---|
| `part_id`, `publication_id`, `publication_version_id`, `asset_id`, `document_id` | Nonempty host-generated/resolved IDs. |
| `asset_sha256`, `document_sha256`, `part_sha256`, `parser_rule_version` | Host provenance; hashes validated on read and bundle publication. |
| `kind` | `paragraph`, `caption`, `table_region`, `table_rows`, `header`, `legend`, `methods`, `source_description`. |
| `locator` | Tagged structure: text `{start,end,xpath?}`; PDF `{page,item_id,bbox?,start?,end?}`; table `{table_id,sheet?,row_ids,column_ids,cell_refs}`. Offsets are half-open canonical Unicode character offsets, not invented PDF-byte offsets. |
| `text` | Exact canonical source text, not an agent summary. |
| `cells` | Zero or more `{cell_ref,row_id,column_id,header_path,raw_value,value_kind,normalized_value?,formula_text?,cached_value?,units_source_part_id?}`. Retain numeric literals as strings; null is distinct from zero/blank/censored text. |
| `context_links` | Source-backed linked part/table/experiment IDs, relation and supporting locator; unresolved links are explicit. |
| `quality_flags`, `meaning_review_record_id` | Parser/identity/semantics flags and existing review link; unavailable review is null. |

A bounded table region may combine a few rows with their repeated headers and
source-linked legend when already canonically represented. This is a versioned
deterministic representation, not permission to pack a whole workbook into one
part. The 3-part/6,000-character scientific-payload limit still applies.

Every tool returns this envelope:

```text
ToolResult {
  schema_version: "assembly-tool-1",
  status: "OK" | "NOT_FOUND" | "AMBIGUOUS" | "UNSUPPORTED" |
          "INVALID_ARGUMENT" | "DENIED" | "LIMIT_REACHED" | "SOURCE_CHANGED",
  data: tool-specific typed records,
  parts: SourcePart[],
  next_cursor: string | null,
  coverage: {returned: int, available: int|null, partial: bool},
  warnings: {code: string, message: string}[]
}
```

Error messages are sanitized, bounded and contain no filesystem/secrets dump.
Empty results are not source absence claims. Opaque cursors bind to the query,
asset hashes and ordering; tampered/wrong-query cursors are rejected. Coverage
counts describe the executed query, not exhaustive paper relevance.

## 4. Tools: exact argument and result contracts

All IDs/arguments are schema validated. Tool defaults and maxima are enforced by
Python. Bounds are reduced further if the remaining payload/token budget is smaller.
No tool executes an arbitrary expression, supplied SQL, regex, shell command or path.

| Tool | Arguments (all records reject unknown fields) | Data returned |
|---|---|---|
| `list_assets` | `{cursor: string|null = null, limit: int = 10 [1..20]}` | `{asset_id, role, format, version_id, acquisition_state, parse_state, document_ids, description_part_ids}[]`; only the host-permitted paper assets. |
| `search_content` | `{query: string [1..300], asset_ids: string[]|null = null, kinds: allowed_kind[]|null = null, cursor: string|null = null, limit: int = 5 [1..10]}` | Ranked `{part_id, kind, exact_match_terms, retrieval_score, excerpt}`; bounded source parts and search coverage. Reuse local lexical/retrieval indices. No external search/API. |
| `read_passages` | `{part_ids: string[] [1..3]}` | Exact source parts, including their own locators, flags and available context links. IDs may come from permitted search/reference results; scope is checked before access. |
| `inspect_table` | `{asset_id: string, table_id: string|null = null, cursor: string|null = null, limit: int = 5 [1..10]}` | Inventory or table profile: `{table_id,sheet,dimensions,columns,header_part_ids,legend_part_ids,meaning_review_state,unresolved_fields,quality_flags}`. Do not auto-read every row. |
| `read_table_rows` | `{table_id: string, column_ids: string[] [1..12], row_ids: string[]|null = null, filters: Filter[] = [], cursor: string|null = null, limit: int = 5 [1..20]}` | Original row IDs, cell records, repeated header semantics, linked descriptions, parser flags and filtered-view coverage. Stable source order; no silent aggregation. |
| `resolve_reference` | `{from_part_id: string, reference_label: string [1..120], limit: int = 5 [1..10]}` | `{target_part_id,target_asset_id,link_basis,link_source_part_id,ambiguity_reason?}[]`; use actual xrefs/reviewed linkage. Multiple matches remain ambiguous. |

`Filter = {column_id: string, op: "eq"|"in"|"contains_literal"|"lt"|"le"|"gt"|"ge",
values: string[] [1..20]}`. Maximum three filters; combine with AND. `in` may have
multiple values; all other operations require exactly one. Numeric comparisons
require a reviewed numeric column definition and declared units/scale. Match
identifiers with documented normalization; preserve original tokens. Use either
explicit row IDs (at most 20) or filters, not both. The tool returns selection
provenance. It does not calculate significance or choose a statistical method.

## 5. State machine and host output

```text
QUEUED → PREFLIGHT
  → BYPASSED_READY (existing complete bundle; no assembly LLM call)
  → BLOCKED_SOURCE (missing/failed/unverified input; no assembly LLM call)
  → INVESTIGATING → PROPOSAL_RECEIVED → VALIDATING
      → BUNDLE_VALIDATED → EXTRACT → VERIFY → FINDING_VALIDATION
      → NEEDS_HUMAN_REVIEW / NEEDS_ASSET / NEEDS_PARSE_REPAIR / ANALYSIS_REQUIRED
      → NO_ADDITIONAL_CONTEXT_FOUND / LIMIT_REACHED / FAILED
```

Host result fields: `schema_version`, `investigation_id`, `source_corpus_key`,
`input_hash`, `status` (one of the states above), `proposal` (validated schema or
null), `bundle_id` (only for a published validated bundle), `bundle_sha256`,
`validation_checks[]` (`name,passed,detail,source_part_ids`), `issues[]`,
`usage_record_id`, `event_log_id`, `model_identity`, `prompt_version`,
`tool_rule_version`, `code_fingerprint`, `started_at`, `ended_at`, `parent_run_id`.
The agent cannot output `BUNDLE_VALIDATED`, accepted evidence, or a graph edge.

Validation requirements:

1. All selected parts were seen; contain an anchor; IDs are unique; every binding
   cites selected parts, so the extractor/verifier sees the actual supporting text.
2. `SOURCE_STATED` bindings have a nonempty value and supporting refs. `UNKNOWN`
   has null value. Ambiguities/conflicts are retained, not silently arbitrated.
3. All parts belong to the allowed publication/version and compatible experiment.
   A content hash/PMID match does not prove experimental equivalence. Deterministic
   xref/metadata checks validate links; proposed semantic associations without
   sufficient source support remain unresolved. Existing meaning-review blockers
   cannot be cleared solely by the agent assigning `SOURCE_STATED`.
4. Verify each text/cell/locator/hash against its own source. A cross-asset bundle
   needs the tested multi-document contract. Until available it is `NEEDS_CONTEXT`.
5. Required headers, legends, methods and qualifiers are included. A bare column
   called “score” or source with unresolved scale/contrast cannot support a signed
   quantitative finding. Missing optional context stays unknown and limits claims.
6. Final scientific payload ≤3 parts and ≤6,000 characters including serialized
   cell values/header paths. Separately count the complete model prompt/tool schema
   and metadata for the token budget. No truncation or model-written substitute
   for indispensable source context. Larger cases go to review.
7. No unresolved essential issue, excluded/retracted primary source or parser/
   identity blocker. The host checks machine-verifiable conditions; semantic
   faithfulness is still checked against the source in extraction/verification.

A validated bundle is immutable: parent IDs, selected source parts, complete
source payload, context links, all checks and canonical payload hash. Context
bindings are proposed labels, not established biological observations. The
extractor/verifier receives the original sources and treats labels as untrusted;
it does not use the agent's decision note as evidence.

## 6. Middleware and execution policy

| Component | Implementation and responsibility |
|---|---|
| Scope guard | Custom tool wrapper resolves IDs from host context, enforces paper/version/asset boundary, schema validation and read-only access before executing. Denied attempts count toward limits. |
| Model-call cap | `ModelCallLimitMiddleware(run_limit=4, exit_behavior="error")` as a local backstop. Durable host ledger enforces the remaining lifetime investigation allowance across invocations. |
| Tool-call cap | `ToolCallLimitMiddleware(run_limit=8, exit_behavior="error")` as a local backstop. Validate every call in a parallel tool-call batch before execution; excess calls cannot slip through. |
| Shared budget | Custom model wrapper reserves an attempt and maximum permitted token/cost allowance atomically before dispatch. SDK retries disabled; every controlled retry, structured-output repair and preflight call is charged to its budget. |
| Context/output bounds | Before every model/tool call, enforce input/output limits. Paginate tools; omit already-used nonselected context deterministically when safe. Preserve message/tool-call pairing. If essential context cannot fit, stop. No LLM summarization middleware. |
| No-progress guard | Cache identical tool requests; count attempted repeats. Two consecutive nonproductive results (no new source parts or metadata) stop for review; another investigation ID cannot reset the same case's allowance. |
| Audit hooks | Host-only persistence of sanitized arguments, returned source IDs/hashes, observable outcomes, validation checks and token usage. Do not request hidden chain-of-thought. |

No middleware that gives shell/filesystem capabilities, automatic model fallbacks,
automatic retry loops, or self-editing prompts/rules. Do not enable remote tracing
by default. Local event logs suffice. Simple JSON review records handle human
handoff; LangChain HITL interrupts/checkpointers are not needed for read-only tools.
If later added, they require a separate implementation decision and durable state.

## 7. Model configuration and budgets

`ASSEMBLER_MODEL=provider:model_name` is optional; if unset it inherits the
resolved extractor model. Initialize a model instance through the shared project
factory and pass that to `create_agent`; do not rely on provider-string defaults
that bypass our routing/credential policy. Support the existing OpenRouter,
LiteLLM proxy and Groq adapters; only OpenRouter receives OpenRouter routing fields.
Do not set a model/API key or make calls as part of this design update.

Use Pydantic `AssemblyProposal` with an explicit structured-output strategy.
Choose `ToolStrategy(..., handle_errors=False)` as the initial compatibility path
only after verifying the selected model's tool calling; the final schema-response
tool is not a data-access tool. Any host repair attempt uses the same four-call
allowance. Provider-native structured output is an alternative only if tested
with ordinary tools simultaneously; never silently change models/strategies.
2026-09-23 repair decision: live tool calling succeeded, but a malformed final schema
response stopped the initial `handle_errors=False` path. Use an explicit host callback
that handles only `StructuredOutputValidationError` and permits at most one correction
within the same four-model-call/eight-tool-call allowance. Every raw response and known
usage is retained; a second malformed response stops. This is not a general tool/network
retry loop. Reopening an already stopped case requires a named repair invocation with
its parent ledger checksum and the unchanged cumulative budget; never erase its ledger.

Count all emitted tool calls, including the final structured response, against
the tool-call ceiling (or make the host total stricter than the framework count).

Starting configuration, to be validated by P4's selected-model dry run:

| Bound | Initial value |
|---|---:|
| Model attempts per investigation, including final response/repairs/retries | 4 |
| Tool attempts per investigation, including denied/repeated calls | 8 |
| Model input tokens per call, including tools/history | 8,000 |
| Billable output tokens per call, including reasoning where applicable | 1,000 |
| Tool response serialized characters | 6,000 |
| Model timeout | 60 seconds |
| Tool timeout | 10 seconds |
| Investigation active runtime | 300 seconds |
| Final source parts / scientific characters | 3 / 6,000 |
| Investigations scheduled per batch | At most 20, deduplicated by evidence question |

These are configurable ceilings, not a guarantee of sufficiency. A low cap yields
an explicit unresolved item, never fabricated completeness. Before live operation,
verify the provider actually enforces the mapped output/reasoning cap; otherwise
fail preflight or obtain an explicitly revised budget. Count full accumulated
history each turn; tool execution itself is local but tool results incur input
tokens when sent back to the model. Exact tokenizer support is required for an
exact token claim; otherwise use a conservative documented estimate and label it.

For the selected LiteLLM proxy, the user's unlimited-quota instruction permits the current bounded validation with finite attempt/input/output reservations and unknown dollar price; never report unknown price as zero. This is the current provider-specific exception to the original USD-cap prerequisite. The 24,000-byte conservative input bound in `configs/extraction.yaml` includes actual tool schemas/history; live GLM output/cap compatibility still needs validation.

For other priced-provider live runs, the host additionally requires a batch/corpus USD cap, model-attempt cap and selected provider rates. Reserve conservatively at configured maximum rates;
refund only known unused allowance. Unknown usage after a timeout remains
reserved/unknown, not zero. Serialize reservations or use atomic locking.

The old 40 scheduled calls apply to extractor/verifier ONLY (20 bundles ×2).
Agent calls are additional: at most 20 investigations ×4 =80 assembly attempts,
plus up to 40 scheduled extractor/verifier calls, plus explicitly budgeted
extractor/verifier retries and capability preflight. Thus 120 is an illustrative
combined ceiling BEFORE those extra allowances, not the new automatic permission
to spend. Deduplicated/successful cached work and direct-ready cases reduce calls.
P3's inference report must show assembly separately with low/typical/upper-bound
assumptions; P4 must reserve budget for extraction/verification instead of letting
assembly consume it all. Larger live budgets require the existing user decision.

## 8. Persistence, human review and failure handling

Keep one investigation identity from frozen source manifest hash, publication/
version, question/anchors, source tool rules, relevant review records, model and
prompt versions. Candidate/lineage associations can share a result only if the
actual question and source payload are identical. New sources or meaning-changing
rules create a new lineage; append rather than overwrite previous outcomes.

Persist sanitized input, messages with tool-call IDs, proposals and source parts
at completed turns in the existing artifact/work layout. Persist budget reservation
BEFORE every external attempt. Host JSON/JSONL records are authoritative for
cross-run accounting; an in-memory LangGraph checkpointer is not durable storage.
No server/checkpoint database is required. Rebuild an invocation from a consistent
completed turn and enforce remaining allowances; do not replay successful calls.
An interrupted in-flight request has unknown usage until reconciled; do not
automatically repeat it at no cost. Do not resume dangling tool messages blindly.

Human-review record: `{review_id, investigation_id, input_hash, issue_code,
question, supporting_part_ids, decision, note, reviewer, reviewed_at,
source_backed_resolution_part_ids}`. Decisions: `DEFER`, `EXCLUDE_WITH_REASON`,
`RETURN_TO_P3`, `RESOLVE_WITH_SOURCES`. Human interpretation is recorded separately
from source facts; `RESOLVE_WITH_SOURCES` does not rewrite source text or bypass
the finding verifier. Need for a new file/parser/analysis returns to P3 or a
separately scoped analysis. There is no invented “approved” evidence from a comment.

On budget/timeout/schema/tool failure, persist the exact stopping condition and
remaining work. `NO_ADDITIONAL_CONTEXT_FOUND` describes this bounded search, not
an exhaustive absence of evidence. No terminal failure is a negative experiment.

## 9. Implementation placement and acceptance

Add narrowly scoped modules under `src/regkg/extraction/`:
`assembly_schemas.py`, `assembly_tools.py`, `assembly.py`; extend the existing
planned model factory and extraction workflow. Reuse source registries, table
readers, retrieval and artifact utilities. Do not build a parallel corpus store.

`create_agent` uses LangGraph internally; that dependency is allowed. No custom
StateGraph, LangGraph service, multi-agent supervisor or Deep Agents package is
required. Pin/test the actual installed APIs when P4 begins; the reference mirror
is documentation, not a package to install. Tools/structured-output compatibility
must be demonstrated on the selected model within the approved preflight budget.

Acceptance checks (all pending; worker does not self-approve):

- [ ] Direct-ready bypass uses zero assembly calls; missing/failed sources fail preflight.
- [ ] Real/source-backed example follows a legend or methods reference and publishes
  a traceable bundle; ambiguous/mismatched experiments remain unresolved.
- [ ] Tool tests cover unknown/out-of-scope IDs, pagination, filter types, oversized
  outputs, hidden/missing table semantics and source changes after cache creation.
- [ ] Agent cannot forge source refs, clear reviewed semantic blockers, increase
  limits, execute code, download files or write graph records.
- [ ] Model/tool/total budget caps hold across retries, parallel tool calls,
  structured-output errors, timeouts and process restarts; replay does not repay.
- [ ] Valid negative/NO_RELATION outcomes do not trigger forced positive-search loops.
- [ ] Extraction/verifier operate on original source parts, with numerical and
  provenance checks; agent narratives never become independent evidence.
- [ ] Human review and changed-source reprocessing have explicit versioned outputs.
- [ ] Handoff reports all three roles' actual calls/costs and remaining questions;
  no claim of universal format interpretation or exhaustive paper understanding.

## 10. References checked

Local mirror inspected: `reference/langchain-sdk-main/_index.md`,
`langchain/agents.md`, `tools.md`, `structured-output.md`, `runtime.md`,
`middleware/built-in.md`, and `human-in-the-loop.md`.

Official references checked for the design:
[agents](https://docs.langchain.com/oss/python/langchain/agents),
[structured output](https://docs.langchain.com/oss/python/langchain/structured-output),
[call-limit middleware](https://docs.langchain.com/oss/python/langchain/middleware/built-in).
Framework schema validation, middleware and tool calling provide engineering
mechanisms; they do not establish biological validity or source fidelity.
