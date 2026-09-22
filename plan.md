# Execution plan — Spatial NicheLinker Regulatory Evidence KG

**Prepared:** 2026-09-21. **Status:** ready for the first worker assignment; implementation has not started.

This is the operational plan for building the biomedical KG described in the two synthesis documents. It is intentionally detailed so a worker can execute a bounded assignment without redesigning the science. The work is divided into **six review gates**, not dozens of separate agent turns. Detailed checkboxes are acceptance evidence within those gates.

## 1. Finish line, time budget, and review ownership

### 1.1 First finish line

Produce a reproducible, locally runnable AT1 demonstration that:

1. Ingests all four available project-data sources without changing scientific meaning.
2. Preserves normalized data and provenance outside the graph.
3. Generates AT1 candidates from fixed manuscript TFs, ChromLinker relationships, and signed expression/prior evidence.
4. Retrieves a bounded real literature corpus, extracts atomic findings, and retains negative/null findings.
5. Exports and validates a reviewable graph-file bundle, then imports that exact bundle into local Neo4j in a separate command.
6. Exports inspectable AT1 nomination tables and per-TF evidence reports with honest uncertainty and exact sources.

The initial named TFs are `TEAD1`, `KLF5`, `GATA6`, `FOXA2`, and `ETV1`. Do not force supporting literature to exist for any of them. A TF with no support remains visible with coverage/missingness, rather than receiving invented evidence.

### 1.2 Keep the first build bounded

Target one concentrated implementation session of roughly **3–5 hours plus review and external setup**, assuming a working Python environment, reachable literature APIs, a configured model, and a usable Docker runtime. This is an estimate, not a promise. Package estimates below describe a bounded first pass; do not sacrifice correctness when an external dependency takes longer.

- Parse the whole supplied numeric input set once; the files are manageable and this avoids repeated cell-type-specific parsers.
- Calculate candidate summaries for AT1 first. Other cell types reuse those parsers later.
- Start with at most **10 unique real papers**, at most **20 extraction bundles**, and at most **40 scheduled extractor/verifier calls** for the first live evidence pass. These are engineering bounds, not sufficient scientific coverage claims.
- Reuse cached source downloads and successful extraction results. Do not crawl PubMed or embed its full collection.
- No web application, REST/MCP, agent runtime, model comparison, NLP benchmark, fine-tuning, figure-vision analysis, or publication manuscript in this finish line.
- XML/abstract text is sufficient to prove the first live slice. Implement the PDF adapter as a bounded optional branch; enable it only when a selected accessible paper needs it.
- Embedding support is a simple model adapter; the user selects the lightweight biomedical model. Lexical retrieval works while that choice is pending.
- A missing provider/key, Docker runtime, or external resource can block a live acceptance item. It must not be disguised as a completed live pipeline by substituting fixture data.

### 1.3 Who checks the boxes

**Workers implement; the lead reviewer accepts.** The user brings each worker's handoff back before the next package begins.

- `[ ]` means not yet accepted, including work a worker reports as finished.
- `[x]` means the lead reviewer inspected the change, saw relevant checks, and recorded acceptance evidence.
- Workers must not edit acceptance checkboxes or review-status cells in this plan.
- Workers write `docs/handoffs/P1.md`, etc., with `READY_FOR_REVIEW`, `PARTIAL`, or `BLOCKED` and supporting evidence.
- The reviewer can accept independent subitems but leaves the package unchecked until every required item passes.
- Optional branches receive an explicit disposition, such as `deferred: model not selected`; this is not a claim the branch was tested.
- A user may change scope. Record that change explicitly; never silently redefine the finish line to obtain completion.

### 1.4 Package register

| Package | Outcome | Prerequisite | First-pass estimate | Reviewer status |
|---|---|---|---|---|
| P1 | Runnable project, contracts, complete project-data ingestion | This plan | 45–60 min | NOT_STARTED |
| P2 | AT1 candidates, signed prior analysis, deterministic retrieval queue | P1 accepted | 30–45 min | NOT_STARTED |
| P3 | Real literature acquisition, parsing, bounded passage retrieval | P2 accepted | 40–60 min | NOT_STARTED |
| P4 | Structured extraction, verification, accepted/uncertain/rejected findings | P3 accepted | 30–45 min | NOT_STARTED |
| P5 | Offline graph-file export, then separate Neo4j import and evidence queries | P4 accepted | 30–45 min | NOT_STARTED |
| P6 | Transparent nominations, AT1 reports, replay and final review | P5 accepted | 30–45 min | NOT_STARTED |

- [ ] **P1 accepted** — environment/contracts/ingestion evidence reviewed.
- [ ] **P2 accepted** — candidate/prior/queue evidence reviewed.
- [ ] **P3 accepted** — real source acquisition and retrieval reviewed.
- [ ] **P4 accepted** — live evidence extraction and source grounding reviewed.
- [ ] **P5 accepted** — live local graph and repeat-import checks reviewed.
- [ ] **P6 accepted** — real AT1 reports, provenance, and replay reviewed.

No application package is currently accepted. These checkboxes are deliberately unchecked.

## 2. Sources of truth and inherited practices

Read in this order:

1. Latest user instructions and [AGENTS.md](AGENTS.md).
2. Assigned package and shared contracts in this plan.
3. Relevant portions of [final synthesis](reference/chatgpt/chatgpt_final_synthesis.md).
4. Relevant portions of [LangChain synthesis](reference/chatgpt/chatgpt_langchain_synthesis.md).
5. Source data and its metadata. Older DPI documents provide context, not permission to expand scope.

The source synthesis diagrams contain illustrative alternatives; the contracts below choose a small consistent implementation. Do not introduce all example classes/modules simply because they appear in a reference.

Practices adopted from NeoXplorer: inspect before editing, preserve original data, keep logic shared and typed, avoid broad rewrites, use concise comments, test meaningful behavior, keep dependencies explicit, protect secrets, and record evidence before checking off tasks. Its `CLAUDE.md -> AGENTS.md` convention is reused here. The inspected web code also illustrates bounded requests and explicit failure behavior; no frontend code or JavaScript dependencies need copying.

**Do not touch NeoXplorer.** It is an inspiration source only. Its database, Docker volumes, credentials, UI, and agent architecture are unrelated to this project.

## 3. Decisions already made and unresolved inputs

### 3.1 Frozen scientific rules

- Niche identity is `dataset + definition run + focal cell type + niche label`, without Control/IPF.
- The clustering used condition-pooled `k = 25` neighborhood composition. Disease condition belongs to observations and nominations.
- Current expression signatures are descriptive mean-log-expression contrasts, not sample-aware DE or formal log2FC.
- Pseudobulk CPTT is supporting expression; do not assume it is the same normalization as the pooled signature means.
- ChromLinker scores are inferred connectivity. Preserve raw values/zeros. Do not assume monotonic biological meaning or reconstruct unprovided TF aggregate scores.
- A TF is a gene. Source family/complex mentions are not automatically individual TF findings.
- A claim, its experimental findings, project predictions, and a nomination remain distinct records.
- Source-supported negative/null findings can be accepted. Null effect, negation, repression, and failed extraction are not interchangeable.
- Binding alone does not imply functional regulation. Combined evidence requires compatible target/context and explicit source connections.
- Cells are not independent donors; donor coverage is unknown unless supplied.
- Search failure, not searched, no support found, and counter-evidence remain distinct.
- Shared source studies are not independent replication. Use conservative known-study counts plus unresolved-dependency counts.

### 3.2 Decision register

| Input | Current state | Worker action | What remains blocked |
|---|---|---|---|
| ChromLinker transform, zero meaning, aggregation, producing run | Unconfirmed | Preserve raw data; mark `score_semantics_status=unconfirmed`; keep connectivity rank null | Biological connectivity ranking and interpreted deltas |
| Lightweight biomedical embedding model/revision | User will select | Build one adapter boundary and lexical fallback; do not choose/download a model on the user's behalf | Dense retrieval live check only |
| Extraction provider/model/key | User requests LiteLLM, OpenRouter, and Groq; runtime model/key not yet selected | Support all three LangChain adapters with `provider:model_name` selectors; validate credentials only for selected roles; see §6.4.1 | Real model calls and P4 live acceptance |
| Neo4j/Docker availability | Not yet established | Inspect in P5; reuse this project's service if present; otherwise create its local service | Live graph acceptance if runtime unavailable |
| Gene/prior mapping snapshots | Not yet fetched | Fetch documented official snapshots in the assigned network-capable package; record provenance | Normalized external findings/ULM if mappings or prior unavailable |
| Donor counts/contributions | Not supplied | Store null with reason, never infer from cells | Donor-level inference only; not descriptive processing |

Workers should finish independent tasks while a decision is pending. Do not repeatedly ask for the same missing answer, silently select a different model, or declare blocked optional embeddings a blocker for ingestion.

### 3.3 External action bounds

Planning does not install software or provision services. A package assignment authorizes its stated local reversible implementation and named network capability. For live paid model calls, use only the user's configured provider and the bounded request/token budget in the assignment/configuration; never invent a dollar ceiling or silently select a paid service. Make a dry-run request/token estimate before the first batch. The call/bundle ceilings in this plan supply the default operational bounds; do not require an additional monetary approval when the user already authorized the configured live run. If no usable provider or enforceable request/token configuration exists, report exactly that; fixture tests remain possible but do not satisfy live acceptance.

Do not buy services, create cloud accounts, publish data, contact collaborators, or run unattended expansion searches as part of these packages.

## 4. Concrete source inventory and expected checks

Paths below are relative to the repository root and remain read-only.

| Source | Observed shape | Meaning/check |
|---|---:|---|
| `files/Yale_IPF_with_Niches_tf_to_gene_connection_scores_log10.csv` | 26,822 rows; `TF`, `Gene`, 45 context columns | 1,206,990 long observation rows if every supplied value is retained |
| `files/spatial_niche_pseudobulk_CPTT.txt` | 36,601 genes; 100 context columns | 3,660,100 long expression rows; tab separated despite `.txt` |
| `files/Yale_pooled_niche_expression_signatures.tsv` | 257,528 rows; 13 columns | 32,191 genes in each of 8 focal-cell-type/condition groups |
| `files/Neighbour_celltypes/*.tsv` | 4 files; 2 niche rows each | Three contain 47 neighbor categories; KRT5neg/KRT17pos contains 46; 374 long neighbor entries |
| `files/TF_target_disease_literature/lung_TF_target_disease_papers.csv` | 46 rows | Seed paper metadata, not accepted evidence |
| `files/TF_target_disease_literature/lung_experimental_edge_papers.csv` | 71 rows | Seed metadata; together the CSVs identify 110 unique PMIDs |
| `files/TF_target_disease_literature/logs/` | Search output/abstracts | Historical retrieval support; do not infer full-text review |
| `reference/langchain-sdk-main/` | Markdown mirror and mirror tools | Read selected docs; do not install/copy this tree as a Python library |

Counts are observed expectations for the current snapshot, not hard-coded parser logic. Recompute and attach source hashes. If they differ, investigate the file rather than dropping rows to match the table.

Context parsing:

```text
IPF.Activated_Fibrotic_FBs_niche_2
condition_raw = IPF
cell_type_raw = Activated_Fibrotic_FBs
niche_label = niche_2

Control.AT2
condition_raw = Control
cell_type_raw = AT2
niche_label = null
```

Split at the first period and match only a trailing `_niche_<integer>`. Do not split every underscore. Preserve raw labels and a curated display-name map. Store `Control` as the experimental condition without inventing a disease diagnosis.

Additional observations to recheck in P1:

- All 45 ChromLinker context labels exist in the 100-column expression input.
- Four AT1 contexts exist, with 107,288 total values and 36,253 nonzero values. Nonzero is an arithmetic observation, not an edge-validity rule.
- There are 12 niche-specific ChromLinker contexts; missing Control fibroblast/KRT contexts must not be manufactured.
- Neighborhood counts sum to 25 per supplied niche row; calculate fractions by dividing by 25.
- A missing neighbor category in one file is unreported, not automatically a measured zero.
- `pct_expressing_*` values are fractions in [0,1]. Preserve units.
- The signature effect is `mean_log_normalized_expression_niche_2 - mean_log_normalized_expression_niche_1`; verify within floating-point tolerance.
- Cell counts are constant within each signature cell-type/condition group. Example: Control AT1 6,591/143; IPF AT1 6,903/789; Control activated fibrotic fibroblasts 41/11.

## 5. Repository layout and dependency strategy

Create files when their package implements them. This is a target map, not an instruction to generate empty modules.

```text
AGENTS.md
CLAUDE.md -> AGENTS.md
plan.md
README.md
pyproject.toml
.env.example
.gitignore
compose.yaml                       # P5 only
configs/
    project.yaml                   # inputs, scientific metadata, AT1 scope
    literature.yaml                # source/retrieval bounds, optional embedding settings
    extraction.yaml                # provider/model, schema/prompt versions, run bounds
    ranking.yaml                   # component availability, weights, ties, sensitivity
    graph.yaml                     # materialization policy, batching
src/regkg/
    __init__.py
    __main__.py
    cli.py                         # argparse, dispatch only
    config.py
    models.py                      # shared enums/contracts; split only when useful
    provenance.py                  # hashes, semantic IDs, manifests, atomic artifacts
    identifiers.py                 # exact mapping/aliases/species, ambiguity handling
    project_data/
        contexts.py
        neighborhood.py
        chromlinker.py
        expression.py
        niche_expression_signatures.py
        ingest.py
    analysis/
        priors.py
        candidates.py
        concordance.py
        nomination.py
        report.py
    literature/
        search.py
        fetch.py
        parse.py                   # XML/abstract contract
        parse_pdf.py               # optional Docling adapter
        passages.py
        retrieval.py
        embeddings.py              # optional selected-model adapter
    extraction/
        schemas.py
        models.py                  # configured LangChain model, no agent loop
        extractor.py
        verifier.py
        validate.py
        prompts/extractor.txt
        prompts/verifier.txt
    workflows/
        literature.py              # ordinary bounded loops and manifests
    graph/
        schema.cypher
        neo4j.py
        materialize.py             # offline selection and graph CSV export
        upsert.py
        queries.py
        checks.py
tests/
    fixtures/
    test_project_data.py
    test_candidates.py
    test_literature.py
    test_extraction.py
    test_graph.py
    test_nomination.py
    test_replay.py
    test_contracts.py
    test_provenance.py
docs/
    decisions.md
    handoffs/P1.md ... P6.md
    reviews/                       # lead reviewer only
data/                              # generated/large content ignored by Git
    external/                      # versioned identifier/prior snapshots
    processed/<ingest_key>/
    papers/<publication_id>/<source_hash>/
    runs/<run_id>/
    graph_exports/<export_key>/     # immutable CSV import bundle + schema/manifest
reports/
    at1/<report_run_id>/
```

**Implementation simplification:** verification lives behind `python -m regkg verify ...`; do not create parallel verification scripts. One implementation per check. No `api/`, UI, or `differential_expression.py` until separately assigned.

### 5.1 Dependencies

Use an available supported Python interpreter (prefer 3.11 or 3.12 if compatible with the selected packages); record the actual choice. No new global Python installation unless needed and assigned.

- Base: `pandas`, `pyarrow`, `pydantic`, `PyYAML`, `httpx`, `lxml`, `scipy`, `neo4j`, `rank-bm25`.
- `analysis` extra: `decoupler` and its directly imported resource client if needed.
- Provider extras: `llm-litellm` → `langchain-litellm`; `llm-openrouter` → `langchain-openrouter`; `llm-groq` → `langchain-groq`. Declare `langchain-core` directly if shared interfaces import it; add `langchain` only if actually imported. Implement all three adapter branches in P4, but install only the extras selected for the assigned run. No router or plugin framework.
- `pdf` extra: `docling`, only when selected PDF processing is exercised.
- Embedding extras: `embeddings-ollama` → `langchain-ollama`; `embeddings-sentence-transformers` → `langchain-huggingface` and `sentence-transformers`. Implement both branches in P3, loading only the selected backend. Do not download weights or install the local transformer stack before the user selects that model/backend.
- `test` extra: `pytest`, `ruff`. Add no unused testing framework.

P1 resolves compatible versions, writes exact direct-dependency pins, and records a reproducible installation from the project manifest. If `uv` is already installed, a checked-in `uv.lock` is appropriate; otherwise use `.venv`/pip plus a project-generated pinned requirements lock. Do not install an extra package manager just for this task. Declare direct dependencies in `pyproject.toml` either way. Later packages update manifest and lock together and run `pip check`.

Install from the repository, e.g. `.venv/bin/python -m pip install -e '.[test]'`. Add extras as packages need them. `python -m regkg --help` must work without a database, LLM key, or heavy optional model import. Import optional dependencies only in their feature paths, with a concise missing-extra error.

## 6. Shared contracts — implement once

### 6.1 IDs, runs, and artifacts

Use deterministic application IDs derived from a namespace and canonical identity JSON (sorted keys, fixed representation). A stable hash is acceptable. Never use an LLM-generated identifier, Python's process-dependent `hash()`, an absolute machine path, or a Neo4j internal ID.

Separate three identities:

1. `dataset_id` identifies the Yale input collection; `source_id` identifies file content plus source role.
2. `artifact_key` identifies source hashes plus result-affecting configuration/code/schema versions. Identical inputs reproduce identical output identities.
3. `execution_id` identifies an attempt and its timestamps/status. A repeat execution is allowed, but must not duplicate semantic observations or evidence.

A manifest contains: stage, input artifact/source IDs, output paths/checksums/counts, configuration fingerprint, code revision or code-file hash if Git is absent, schema version, software versions, start/end/status, sanitized error, and actual live/fixture mode. Success is recorded only after outputs are atomically committed. A failed attempt must not overwrite a prior successful artifact.

Plain JSON manifests and local files are enough. No job scheduler or metadata database.

### 6.2 Minimum records/tables

All applicable records retain `source_id`, `analysis_run_id`/artifact provenance, original labels, and units. Use nullable fields explicitly; reject non-finite numeric values where measurements require finite values.

| Record/table | Required identity and fields |
|---|---|
| `SourceFile` | source role, original relative path, SHA-256, bytes, delimiter/format, row/column counts |
| `GeneRecord` | local gene ID, species, source symbol, normalized symbol, HGNC/Ensembl/NCBI IDs when resolved, mapping status/source/version, `is_tf` evidence/source |
| `CellType` | stable project label, raw label, display label; ontology ID nullable |
| `BiologicalContext` | species, tissue, cell type, condition, disease nullable, model system; distinguish unknown from explicit absence |
| `SpatialNicheState` | dataset, definition-run ID, focal cell type, niche label, condition-pooled flag, k, clustering resolution |
| `NeighborhoodProfile` | profile ID and niche ID, source/run; long entries contain neighbor type, mean count, fraction, k |
| `ChromLinkerObservation` | ID, TF ID/raw, target ID/raw, context ID, niche ID nullable, original context label, raw score, score label, semantics status |
| `ExpressionObservation` | ID, gene ID/raw, context ID, niche ID nullable, CPTT value/unit |
| `NicheExpressionSignature` | comparison ID, gene ID/raw, cell type, condition, case/reference niche IDs, both means, effect, both expressing fractions, both cell counts, effect definition |
| `GeneProgram` | comparison ID, target niche/direction, all ranked signature genes or documented derived set, method/version; no invented significant flag |
| `PriorInteraction` | regulator identity/type, target ID, sign including unknown, resource/version, source references/PMIDs/accessions, license/retrieval metadata |
| `Candidate` | TF ID, comparison/target niche, reasons as a set, seed flag, raw connectivity observations, signature/prior scores and coverage, missing-component reasons |
| `Publication` | canonical publication ID, PMID/PMCID/DOI where present, title, year, retrieval/access status, references, correction/retraction status if known |
| `Passage` | document hash/version, passage ID, exact canonical text, section, character offsets, XML element or PDF page/item location |
| `EvidenceBundle` | ordered passage/table IDs from one publication, query/candidate IDs, retrieval reasons, token/size bounds |
| `RegulatoryClaim` | normalized proposition at stated entity level, relation/claimed direction, biological context; independent of a single supporting paper |
| `EvidenceAssertion` | atomic finding ID, claim link when valid, regulator/target mapping, assay, outcome, statement status, directness, context, spans, publication, experiment/study identity nullable, extraction status |
| `TFNomination` | TF + comparison + target niche + ranking version, component scores/ranks, availability, evidence counts/context/contradictions, category, explanations/references |

Keep table schemas in one place. Large tables can be Arrow/Pandas with typed schema checks; small external records can be Pydantic models. No need to build a generalized ontology framework.

### 6.3 Evidence states

```text
extraction_status: AUTO_ACCEPTED | UNCERTAIN | REJECTED
statement_status: AFFIRMED | NEGATED | SPECULATIVE | UNCLEAR
experimental_outcome:
  INCREASE | DECREASE | NO_DETECTED_EFFECT |
  BINDING_DETECTED | NO_BINDING_DETECTED | UNCLEAR
directness: DIRECT | FUNCTIONAL | ASSOCIATIVE | PREDICTED | UNCLEAR
polarity relative to a specified claim: SUPPORTS | CONTRADICTS | INCONCLUSIVE
context_match relative to a nomination: EXACT | CLOSE | PARTIAL | MISMATCHED | UNKNOWN
```

Do not infer that `NO_DETECTED_EFFECT` automatically contradicts every regulatory claim. Null findings qualify a specific assay/condition/claim; preserve them as inconclusive unless the proposition and comparison justify a counter-evidence link. Opposite regulatory signs across mismatched contexts are context differences unless a comparison establishes a conflict.

A finding can be valid without complete assay/context details; retain unknowns and limit its directness/nomination eligibility. A statement can contain an explicit negated finding and still have `relation_present=true`. `NO_RELATION` is for absence of a relevant expressed relation/finding, not absence of an experimental effect.

### 6.4 Runtime/configuration

Use YAML for reproducible nonsecret choices, environment variables for secrets, and explicit CLI paths. No hidden current-directory dependence.

Required configuration fields:

- `project.yaml`: source paths/roles, dataset/definition-run identifiers, species/tissue, cell-type mappings, k and per-file resolution, AT1 TF seeds, numeric tolerances.
- `literature.yaml`: metadata service, contact email if required, max papers/queries/results/passages, retry/timeouts, lexical policy, embeddings enabled/model/revision/encoding settings.
- `extraction.yaml`: `extractor.model` and optional `verifier.model` as qualified model strings, prompt/schema versions, generation settings, per-call timeout, total request/token limits, retry limits, selected source-bundle IDs. An omitted verifier model inherits the extractor model; record both resolved identities.
- `ranking.yaml`: target coverage threshold, component availability policy, weights, RRF k, ties, candidate universe, provisional literature ordering policy.
- `graph.yaml`: allowed endpoint mode, batch size, selected cell type/candidates, per-candidate materialization bounds, selected artifact keys.

Environment names: `NEO4J_URI`, `NEO4J_USERNAME`, `NEO4J_PASSWORD`, `NEO4J_DATABASE`, plus the model settings below. An optional dotenv loader may read root `.env` without overriding existing process environment; never log the content. The `.env.example` names supported settings, distinguishes required from optional, and contains no working secrets. No generic `API_KEY` or `BASE_URL` shared across providers.

### 6.4.1 Model selection and provider wiring — explicit user requirement

**Scope:** three chat backends for extraction/verification and two embedding backends for passage retrieval. This adds interchangeable infrastructure, not model comparison, fine-tuning, or an NLP research workstream. No new work package is needed.

**One selector contract:** `{provider}:{model_name}`. Implement one small parser in `config.py`, reused by `extraction/models.py` and `literature/embeddings.py`. Split at the **first colon only** (`partition(":")`); normalize the provider token to lowercase, preserve the model suffix's case, slashes, and additional colons. Reject missing provider/model, leading/trailing whitespace in the model suffix, unknown providers, and providers used in the wrong role. Do not hard-code a catalog of available model names or query remote catalogs during configuration parsing. Canonical provider tokens are `litellm`, `openrouter`, `groq`, `ollama`, and `sentence_transformers`; accept `sentence-transformers` as an alias for the last token and canonicalize it before computing cache keys. Do not keep a second independent `provider` YAML field that can disagree with the string.

| Role / selector | LangChain integration and constructor | Required environment | Optional configuration / default |
| --- | --- | --- | --- |
| Chat: `litellm:<proxy-model-alias>` | `langchain-litellm`: `langchain_litellm.ChatLiteLLM` | `LITELLM_BASE_URL`, `LITELLM_API_KEY` | No default gateway; explicitly map these application env names to `api_base` and `api_key` |
| Chat: `openrouter:<organization>/<model>` | `langchain-openrouter`: `langchain_openrouter.ChatOpenRouter` | `OPENROUTER_API_KEY` | Built-in OpenRouter endpoint; optional `OPENROUTER_APP_URL` / `OPENROUTER_APP_TITLE` mapped to `app_url` / `app_title` |
| Chat: `groq:<model-name>` | `langchain-groq`: `langchain_groq.ChatGroq` | `GROQ_API_KEY` | Built-in Groq endpoint; no base URL required |
| Embeddings: `ollama:<model>:<tag>` | `langchain-ollama`: `langchain_ollama.OllamaEmbeddings` | None for the default local server | Optional `OLLAMA_BASE_URL`; default `http://localhost:11434` |
| Embeddings: `sentence_transformers:<organization>/<model>` | `langchain-huggingface`: `langchain_huggingface.HuggingFaceEmbeddings` | None for public/cached models | Optional `HF_TOKEN` only for gated/private access; model revision, device, cache directory, and encoding settings in YAML |

Constructor references: [LiteLLM](https://docs.langchain.com/oss/python/integrations/chat/litellm), [OpenRouter](https://docs.langchain.com/oss/python/integrations/chat/openrouter), [Groq](https://docs.langchain.com/oss/python/integrations/chat/groq), [Ollama embeddings](https://docs.langchain.com/oss/python/integrations/embeddings/ollama), and [Sentence Transformers](https://docs.langchain.com/oss/python/integrations/embeddings/sentence_transformers). Check these interfaces against the pinned versions during implementation.

**LiteLLM means the configured proxy in this project.** Turn `litellm:my-deployment` into the internal LiteLLM route `litellm_proxy/my-deployment`, passing `api_base=LITELLM_BASE_URL` and `api_key=LITELLM_API_KEY` explicitly. Preserve the deployment alias, including any nested slashes/colons. The SDK's documented environment names differ from the application's requested names; do not assume automatic loading. Verify the pinned ChatLiteLLM adapter forwards the route and credentials correctly. Never infer an upstream provider from the alias or require upstream provider credentials on this client. Preserve an explicitly supplied gateway path without blindly appending `/v1`; test the outgoing target using a stub transport. Do not deploy a proxy as part of this adapter task. Routing reference: [LiteLLM proxy provider](https://docs.litellm.ai/docs/providers/litellm_proxy).

**Ollama default:** leave `OLLAMA_BASE_URL` unset for a local server. Resolve an absent/blank value to `http://localhost:11434`; pass a nonblank override explicitly. Use this project's provider-specific env name, not `OLLAMA_HOST` (which configures the server). A connection failure must identify the configured endpoint without installing or starting Ollama automatically. A selected embedding model must already be available or be explicitly downloaded within the assigned setup; no automatic replacement model. If the Python process later runs inside a container, localhost refers to that container and the operator must supply a reachable override. Default server binding reference: [Ollama FAQ](https://docs.ollama.com/faq).

**Example shapes, not chosen runtime models:**

```yaml
# configs/extraction.yaml — excerpt; retain the other required run bounds
extractor:
  model: "litellm:<proxy-model-alias>"
# Optional override; omit to use the extractor model for verification.
# verifier:
#   model: "openrouter:<organization>/<model>"
# Either role may instead use "groq:<model-name>".
```

```yaml
# configs/literature.yaml — excerpt; retain the source/retrieval settings
embeddings:
  enabled: false
  model: null
  # Once selected: "ollama:<model>:<tag>"
  # Or: "sentence_transformers:<organization>/<model>"
  revision: null
```

The angle-bracket values are documentation placeholders: reject them as unconfigured before any live call. Ship extraction disabled/unconfigured until an actual model is supplied. `enabled: true` requires a real embedding selector. When embeddings are disabled or pending, use lexical retrieval and report `dense_retrieval=not_configured`. When an enabled backend fails, record an error; a lexical-only continuation requires an explicit configured fallback policy and must record the degraded retrieval mode.

**Worker implementation and acceptance details:**

1. **P1:** parse and validate selectors/config without importing model SDKs, reading weights, opening connections, or requiring any provider key. Add the names above to `.env.example` as commented/empty placeholders; document Ollama's default with a commented override. Test first-colon parsing with `ollama:ExampleModel:v1`, `openrouter:Org/Model:variant`, and `litellm:Org/Deployment:revision`; all suffixes must survive unchanged. Test alias canonicalization, empty values, unknown providers, and wrong-role rejection.
2. **P3:** create `build_embeddings(config)` behind one query/document encoding interface. Use `embed_query` and `embed_documents`; Sentence Transformers receives only the model suffix as `model_name`, plus selected revision/device and documented encoding kwargs. Keep query/document prefixes, normalization, batching, and token limits faithful to the selected model. Validate finite vectors, equal nonzero dimensions, and compatible query/document spaces. Both backend branches get offline wiring checks; only the user's selected backend needs a bounded live smoke run. Do not install/test both model stacks to satisfy one run.
3. **P4:** create `build_chat_model(model_spec, settings)` with three explicit lazy-import branches. Pass only the suffix as the provider's model name, except LiteLLM's internal proxy prefix above. Validate only selected roles' keys and LiteLLM URL immediately before constructing/calling their clients. Missing optional extras identify the exact installation extra. Config validation and `--help` remain usable with no keys. No silent provider failover, fallback paid model, router, or automatic model selection.
4. **Structured output:** use the integration's supported `with_structured_output` mode for the selected model and pinned package; capability is model-dependent. Record the configured mode and reject incompatible settings with a clear setup error. Do not silently replace validated structured output with permissive JSON parsing. Run one small schema smoke check on selected model configurations before a batch; count it and retries against the run's total request/token limits. Share the single budget across extractor, verifier, and SDK retries, preventing nested retries from bypassing it. No requirement to make live calls to all three providers.
5. **Reproducibility:** manifests/cache identity include canonical selectors for each role, available resolved model version/revision, nonsecret endpoint identity, generation/encoding settings, schema/prompt versions, and source/chunk hashes. For Ollama, record a model digest if exposed; for hosted aliases, record returned identity and leave unavailable revisions unknown. Changing embedding model, revision, dimension, prompts, or normalization rebuilds its index; do not mix cached spaces. Credentials never enter a manifest, cache key, exception dump, or transport fixture.
6. **Focused checks:** verify all three chat constructor mappings, LiteLLM proxy target/auth forwarding using dummy credentials, default/overridden Ollama URLs, Sentence Transformers model-name/revision forwarding, unselected-provider independence, and missing-extra errors. Test configured embedding failure vs deliberately disabled embeddings. Verify budgets/cache replay and preserve raw/parsed model results. Live handoff reports exactly the selected backends exercised; stub wiring checks do not imply live provider validation.

Use nonsecret HTTP(S) URLs without embedded user/password/token parameters; credentials travel through their dedicated SDK fields. Keep optional embedding dependencies unloaded during ingestion, graph operations, and lexical-only retrieval. Provider factories must remain small ordinary functions, with no new framework or service.

### 6.5 CLI contract

Use `argparse` with one entry point: `.venv/bin/python -m regkg`. Implement each command in its owning package; pending commands must not silently claim success.

```text
regkg ingest --config configs/project.yaml
regkg verify project-data --run <ingest_key>
regkg candidates --run <ingest_key> --cell-type AT1
regkg verify candidates --run <candidate_key>
regkg literature search --run <candidate_key> --max-papers 10
regkg literature fetch --run <search_key>
regkg literature retrieve --run <parsed_key>
regkg verify literature --run <retrieval_key>
regkg extract --run <retrieval_key> --dry-run
regkg extract --run <retrieval_key> --live
regkg verify evidence --run <extraction_key>
regkg graph export --run <extraction_key> --project-run <ingest_key>
regkg verify graph-export --bundle data/graph_exports/<export_key>
regkg graph load --bundle data/graph_exports/<export_key> --dry-run
# Separate import stage, after file inspection:
regkg graph init
regkg graph load --bundle data/graph_exports/<export_key>
regkg verify graph --run <graph_key>
regkg nominate --project-run <ingest_key> --candidate-run <candidate_key> --evidence-run <extraction_key> --cell-type AT1
regkg report --run <nomination_key>
regkg verify report --run <report_key>
regkg run-at1 --config configs/project.yaml --resume
```

Commands print concise artifact IDs, relative output locations, counts, and status. They return nonzero for invalid input or failed required stages. A command with honest partial coverage must say `PARTIAL` and list reasons; never silently report full success. `<...>` above are placeholders copied from actual command output, not literal arguments.

### 6.6 Initial evidence/ranking rules a worker must not invent

These are transparent **provisional implementation rules**, retained in configuration and reports. They are not calibrated biological confidence estimates.

**Eligible positive experimental support:** an AUTO_ACCEPTED primary finding with resolved individual-gene TF/target, checked source spans, an explicit assay, and SUPPORTS polarity relative to the target claim. Binding, perturbation, reporter, or CRE-perturbation findings retain their actual directness. Computational/association/prior-database records alone are not primary experimental support. A prior with a PMID still requires a retrieved source-grounded finding for that role.

**Context ordering for a human AT1 nomination:**

| Match | Default rule |
|---|---|
| EXACT | Explicit human lung AT1, matching Control/IPF experimental condition, primary/native context |
| CLOSE | Explicit human lung AT1 or alveolar epithelium, compatible primary/native context, with broader cell annotation or unspecified disease condition; retain each missing/broader component |
| PARTIAL | Explicit relevant mouse lung/AT1, or human lung cell model with known differences; an explicitly different condition/model system cannot be called exact |
| MISMATCHED | Explicit incompatible tissue/cell context, e.g. a non-lung cancer line |
| UNKNOWN | Too little source context to apply the above; unknown is never promoted to exact |

A conflicting explicit field overrides a favorable broader match. Do not infer tissue/species from author affiliations or a paper title when the experiment used another system. Matching the project disease label does not establish matching a niche. The exact match implementation must be covered by small fixtures.

**Provisional assay ordering for positive support:** compatible binding plus functional effect; then TF perturbation or TF binding individually; then reporter/CRE effect that supports the precise scoped claim; then association/computational evidence for display only. Report the assay class itself so this convenient ordering cannot hide an assay's limitations. An endogenous CRE perturbation can support locus function without identifying a particular TF; exclude it from TF-specific support when that link is absent. Do not upgrade a reporter-only effect to endogenous regulation.

**Candidate categories, evaluated in this order:**

1. `CONTRADICTORY`: accepted positive support and qualified opposing findings for a comparable proposition/context. Explicit null findings are not automatically opposing.
2. `SUPPORTED`: observed project connection and at least one eligible positive experiment in EXACT/CLOSE context. This means evidence supports a candidate link, not that an unconfirmed ChromLinker score is strong.
3. `QUALIFIED`: observed project connection with eligible positive support limited to PARTIAL/MISMATCHED/UNKNOWN context, or support whose directness limits the claim.
4. `LITERATURE_ONLY`: eligible positive support for signature/prior-linked targets, with no supplied project connection for that TF/target context. Zero-valued supplied observations are not called absent merely because their meaning is unresolved.
5. `PROJECT_PREDICTION_ONLY`: supplied project connection exists but no eligible positive experimental support was found in the executed search. Attach search coverage; this is not a negative biological conclusion.
6. `INSUFFICIENT`: remaining candidates, including seed-only and prior-only candidates lacking the evidence above.

`project connection exists` means a source record exists; its presence is descriptive while score semantics remain unconfirmed. If the criterion would depend on interpreting zero as a connection/no-connection, use `INSUFFICIENT` with `unconfirmed_zero_semantics` instead of guessing. Never equate a curated prior with an independently verified experiment.

Where source context or dependencies prevent a reliable category, preserve the uncertainty and choose the conservative category/reason. Do not add learned weights, arbitrary numerical penalties, or a confidence percentage to solve an ambiguity.

## 7. P1 — Foundation, contracts, and project-data ingestion

**Goal:** the whole supplied quantitative data set becomes validated, reproducible Parquet tables with correct niche/context identities. No external models or database required.

**Allowed writes:** root README/manifest/env example/gitignore, `configs/project.yaml`, shared modules, `src/regkg/project_data/`, focused P1 tests, generated `data/processed/`, P1 handoff. Do not edit source files or synthesis documents.

### P1 execution order

- [ ] **P1.1 Environment audit and bootstrap.** Inspect directory/Git/environment and available Python. Create `.venv` if absent. Create package metadata and minimal CLI. Declare/pin verified base/test dependencies. Record actual versions and lock strategy. Add ignores for `.env`, `.venv`, generated data, caches, large model assets, and `.DS_Store`; keep `.env.example` visible.
- [ ] **P1.2 Configuration and small contracts.** Implement the records/enums required by ingestion, config validation, canonical IDs, source hashes, and manifests. Reject unknown config fields that would otherwise be ignored. Implement source-path resolution against project config/repository location. Implement the shared `provider:model_name` parser, role allowlists, unconfigured model states, and `.env.example` contract in §6.4.1; test them without SDK imports, network, weights, or credentials.
- [ ] **P1.3 Source audit.** Read headers/delimiters, count rows, check duplicate keys, finite numeric values, and source hashes. Write `source_inventory.json` and a human-readable audit. If duplicate semantic source keys exist, report them; do not silently drop/average them.
- [ ] **P1.4 Context/niche normalization.** Implement anchored suffix parsing and raw/display mapping. Produce `contexts.parquet`, `cell_types.parquet`, and `niche_states.parquet`. Observations with no niche remain null. Eight niche-state identities are expected for the four focal types; Control/IPF must not double their identity count.
- [ ] **P1.5 Gene mapping boundary.** Produce the exact source-symbol inventory and species-qualified stable local IDs. Populate external canonical IDs only from a documented supplied/cached mapping; otherwise mark `unresolved_external_id`, without inventing HGNC IDs. P2 can enrich these IDs without changing existing observation identities. Do not force all pseudobulk features to be protein-coding genes or discard unrecognized symbols.
- [ ] **P1.6 ChromLinker parser.** Melt wide to long in bounded chunks; preserve every source value, all raw labels, and null niche/context membership. Output `chromlinker_observations.parquet` (partitioned dataset acceptable). Add `score_semantics_status=unconfirmed`. No exponentiation, zero filtering, biological rank, aggregate score, or inferred truth edges.
- [ ] **P1.7 Pseudobulk parser.** Stream/chunk melt to `expression_observations.parquet`, preserving CPTT values and labels. Prevent oversized all-in-memory lists and per-row Pydantic processing. No normalization or DE calculation.
- [ ] **P1.8 Neighborhood parser.** Parse each file's focal type/resolution through explicit config. Emit `neighborhood_profiles.parquet` long rows with original counts and count/25 fractions. Check each row sum within `1e-6`; preserve source column sets; do not fill unreported neighbor categories with measured zeros.
- [ ] **P1.9 Signature parser.** Rename fields only via an explicit map, retain effect-definition text, and output `niche_expression_signatures.parquet`. Verify effect equals mean2-minus-mean1 (`abs_tol=1e-8`, `rel_tol=1e-6`), fractions [0,1], nonnegative integer cell counts, uniqueness by dataset/cell-type/condition/comparison/gene, and per-group cell-count consistency. No significance labels.
- [ ] **P1.10 Joins and sampling metadata.** Verify the 45-context overlap, expected missing niche contexts, 8 signature groups, and available gene overlap. Unmatched genes are counted and preserved, never inner-joined away. Export sampling coverage with donor fields null.
- [ ] **P1.11 Reproducible artifact commit.** Write tables and manifest atomically. A second identical execution reuses or verifies the existing artifact; it must not append duplicate rows. Execution timestamps may differ; semantic IDs/counts/measurement content must match.
- [ ] **P1.12 Tests, README, and handoff.** Cover parsing underscores/non-niche labels, cross-condition shared niche identity, zero vs missing, signature units/effect, absent neighbor category, duplicate-key failure, and replay. Record real input counts and output sizes; stop for review.

### P1 commands and evidence

```bash
.venv/bin/python -m pip check
.venv/bin/python -m ruff check src tests
.venv/bin/python -m pytest tests/test_project_data.py tests/test_contracts.py tests/test_provenance.py -q
.venv/bin/python -m regkg ingest --config configs/project.yaml
.venv/bin/python -m regkg verify project-data --run <actual_ingest_key>
.venv/bin/python -m regkg ingest --config configs/project.yaml
```

Required handoff evidence: actual counts from section 4, hashes/manifest, table schema listing, sampling table, gene/context unmatched counts, replay outcome, exact successful commands and any failures. Do not dump millions of rows into the handoff.

**Review gate:** counts and semantics agree with source data; source files unchanged; no fake mappings/statistics; output is usable by P2. Acceptance is not just that pytest is green.

## 8. P2 — AT1 candidates, one curated prior, and retrieval queue

**Goal:** a deterministic AT1 candidate set and bounded literature queue with two candidate routes. Start with one prior source, CollecTRI; adapters for TRRUST/hTFtarget/KnockTF are later extensions, not prerequisites.

**Allowed writes:** identifier enrichment, `analysis/priors.py`, `candidates.py`, `concordance.py`, candidate CLI, `configs/literature.yaml`, `ranking.yaml`, needed dependency extra/lock changes, P2 tests/artifacts/handoff. Shared contract additions must be small and backwards compatible; report changes explicitly.

### P2 execution order

- [ ] **P2.1 Resolve gene identities.** Acquire/cache a documented official human gene mapping snapshot using appropriate source access. Normalize exact stable IDs/approved symbols first; resolve aliases only if unambiguous and species-consistent. Preserve mappings/rejected candidates and original symbols. Never merge two source features solely because a fuzzy string match is close.
- [ ] **P2.2 Import advisor metadata.** Read the two selected-paper CSVs; deduplicate PMID identity to 110 expected unique papers while retaining both resource memberships and annotations. Write `seed_publications.parquet`. The existing prose about evidence does not become accepted scientific findings.
- [ ] **P2.3 Acquire CollecTRI.** Use the pinned official decoupler/OmniPath integration or a documented resource export; verify the installed API. Cache raw response, retrieval timestamp, version/license metadata, PMIDs/signs/complexes. Produce `prior_interactions.parquet`. Do not silently split a complex into individually supported TFs. Unknown sign stays unknown; contradictory signs remain traceable, not randomly deduplicated.
- [ ] **P2.4 Define AT1 comparison objects.** Build Control and IPF Niche2-vs-Niche1 comparisons. For each, retain the complete signed vector; Niche2 is the case/target and Niche1 is the reference. An optional opposite-niche view negates the contrast and must be labelled as a view of the same comparison, not an independent analysis. Do not label either vector as DE. Do not merge Control/IPF contrasts.
- [ ] **P2.5 Signed-regulon baseline.** Call decoupler ULM through the pinned public API on resolved, finite gene-level contrast values and signed prior weights. Default minimum mapped targets is 5, explicitly an engineering/coverage setting. Unresolved duplicated mappings are excluded from this calculation with counts; do not average them silently. Preserve prior-universe size, observed targets, eligibility/filter rules, raw ULM score, sign, and method version. Omit donor-level significance claims; method p-values, if retained at all, are labeled method-specific and not used as DE FDR.
- [ ] **P2.6 Candidate union.** Include the five named TF seeds regardless of score. Add at most 5 additional individual-gene TFs per condition from the largest absolute concordance scores meeting coverage rules; stable TF-ID order breaks ties. Preserve concordance sign separately so an inverse pattern is not called increased activity. A TF from several routes gets one candidate identity plus multiple reasons. The first report uses one Niche2-versus-Niche1 comparison per condition, showing both niches and concordance sign. Do not duplicate independent-evidence counts for an optional reversed view, or pretend a score sign measures causal activity.
- [ ] **P2.7 Project evidence for candidates.** Attach supplied ChromLinker target observations and TF/target expression support. Keep numeric distributions/target row counts descriptive. Connectivity rank and interpreted delta remain null while semantics are unconfirmed. The manuscript seed order must not masquerade as a scientific ranking.
- [ ] **P2.8 Select bounded target searches.** For each TF, choose up to 3 resolved target genes that overlap its prior/project target lists and have the largest absolute descriptive AT1 signature effects (gene ID breaks ties). Selection is for retrieval coverage only, not a biological ranking. Preserve source route and effect. If none are eligible, retain TF-only queries; do not invent targets.
- [ ] **P2.9 Build reproducible query rows.** Emit `retrieval_queue.parquet` with query ID, candidate/comparison/target, query text/type, priority, reason, source route, and version. Generate TF + target + regulatory-assay terms and TF + lung/alveolar/fibrosis queries, using exact approved names and safe aliases. Include negative/null phrasing where helpful; do not require positive regulation terms for every query. Do not restrict all searches to 2015 onward. Bound live execution to a small deterministic queue slice (initially at most 20 queries); all unexecuted rows remain `NOT_SEARCHED`.
- [ ] **P2.10 Verify and hand off.** Test ambiguous alias exclusion, complex preservation, deterministic seed inclusion/top-k/ties, target coverage, unknown connectivity semantics, repeated source provenance, and repeatable queues. Report which real prior/mapping services worked, dataset versions, candidate counts, and unmapped genes.

### P2 commands and evidence

```bash
.venv/bin/python -m pip check
.venv/bin/python -m pytest tests/test_candidates.py -q
.venv/bin/python -m regkg candidates --run <ingest_key> --cell-type AT1
.venv/bin/python -m regkg verify candidates --run <candidate_key>
```

`verify candidates` must show the five seeds for each AT1 comparison, no interpreted ChromLinker rank under unconfirmed semantics, target/identifier coverage, reproducible query ordering, and source-linked prior records.

**Review gate:** two candidate routes exist on actual inputs. If the prior API is unavailable, submit partial work; five hard-coded seeds plus fixtures alone do not satisfy the prior-analysis item. A missing embedding model does not block this package.

## 9. P3 — Bounded real literature processing and passage retrieval

**Goal:** process up to 10 relevant real papers and produce inspectable evidence bundles. This is a practical literature service, not an NLP research project.

**Allowed writes:** `literature/`, `workflows/literature.py`, literature CLI/config, optional dependency declarations, P3 tests, ignored paper/run caches, P3 handoff. No extraction/graph truth writes yet.

### P3 execution order

- [ ] **P3.1 Search adapter.** Use documented PubMed/Europe PMC APIs. Execute at most 20 queued queries with up to 10 metadata results per query, caching the query response and timestamp. Bound network retries (e.g. 2 retries with backoff and `Retry-After`) and timeouts. Store per-query executed/error/unexecuted status. Avoid unbounded citation expansion.
- [ ] **P3.2 Publication resolution/deduplication.** Merge PMID/PMCID/DOI aliases only when verified, preserve query/resource memberships, normalize DOI case/prefix, and prevent duplicate fetches. Capture available correction/retraction metadata. Never combine preprint/published versions merely on a similar title without explicit identity evidence.
- [ ] **P3.3 Select the live corpus.** Prioritize relevant seed hits and returned results by exact candidate identity and lung/assay metadata, with documented deterministic ordering and PMID tie breaks. Select at most 10 unique papers, aiming for coverage of all five seeded TFs where results exist. Lack of coverage remains visible. Do not assume every advisor paper is pertinent to AT1.
- [ ] **P3.4 Fetch eligible assets.** XML/BioC first; store metadata, abstract, access/reuse status, URL, timestamp, checksum, and raw asset. If eligible full text is unavailable, retain abstract-only status. Download only supplied/authorized PDFs. Respect API terms/limits; no access bypass. Preserve failures without labelling them absence of biology.
- [ ] **P3.5 Parse the canonical document.** Produce `document.json`, `sections.jsonl`, `figure_captions.jsonl`, and table rows with section/item IDs. Maintain exact canonical text plus stable offsets and original XML location. XML parsing disables external entity/network resolution. Captions are included; no figure pixel inference. Preserve table headers/footnotes and supplementary asset identity.
- [ ] **P3.6 Optional PDF adapter.** If a selected paper requires an accessible PDF, use Docling behind the same document contract and retain page/item provenance. Limit OCR/pages/resources by config. Do not install/run PDF processing for XML-only work. Record this branch as exercised or deferred; do not fabricate a PDF test result.
- [ ] **P3.7 Normalize passage entities.** Reuse gene mappings and PubTator annotations when available, with species and original mention retained. Check alignment of PubTator spans to the canonical text; if text versions differ, preserve the external offsets separately and rematch/verify exact text. No blind offset copying or fuzzy automatic identity acceptance.
- [ ] **P3.8 Lexical retrieval.** Build exact alias/identifier hits and BM25 over section-aware paragraphs/captions/table descriptions. Rank per candidate query with stable ties, preserving raw retrieval scores/reasons. Do not treat an assay term or entity co-occurrence as an accepted edge.
- [ ] **P3.9 Lightweight embedding adapters.** Implement both Ollama and Sentence Transformers branches behind the interface in §6.4.1, selected through `embeddings.model`. Default Ollama to localhost port 11434 without an env setting; honor `OLLAMA_BASE_URL` overrides. Add focused offline wiring checks for both branches. If the user has supplied a model, exercise that backend, follow its actual pooling/token limits and query/document encoding, and make a bounded local index; record revision/chunk hashes and vector dimensions. Merge lexical and semantic candidate lists while retaining exact hits. If model is pending, emit `dense_retrieval=not_configured` and proceed with lexical retrieval; a configured failure is a different status. No automatic model shopping, training, cross-encoder, or separate vector service.
- [ ] **P3.10 Assemble bounded bundles.** Select at most 20 bundles across the run, with per-paper/per-candidate limits recorded. Start with the result passage, adding at most necessary adjacent context or a linked caption/table/methods passage from the same publication. Suggested default is 3 passages and 6,000 characters per bundle, subordinate to the provider's token limit. Do not split away negation, comparison groups, or a required table header. Prefer marking insufficient context over silent truncation.
- [ ] **P3.11 Coverage and caches.** Distinguish NOT_SEARCHED, SEARCHED_NO_SUPPORT_FOUND, ABSTRACT_ONLY, FULL_TEXT_PROCESSED, FETCH_FAILED, PARSE_FAILED, and NO_CANDIDATE_PASSAGES. The search-level label means no support found in the performed retrieval, not a biological negative. Cache successful stages using source/config hashes; retry failures without duplicating successes.
- [ ] **P3.12 Verify/handoff.** Inspect a small real sample of returned bundles, checking gene identity, section, source text, and locators. Include at least one actual source-backed evidence candidate if available; report honestly if none are found. Tests cover deduplication, external text offset mismatch, valid zero-result search, timeout status, XML safety, and bounded bundle construction.

### P3 commands and evidence

```bash
.venv/bin/python -m pytest tests/test_literature.py -q
.venv/bin/python -m regkg literature search --run <candidate_key> --max-papers 10
.venv/bin/python -m regkg literature fetch --run <search_key>
.venv/bin/python -m regkg literature retrieve --run <parsed_key>
.venv/bin/python -m regkg verify literature --run <retrieval_key>
```

Handoff: chosen paper list with identifiers/access/source status, query execution counts, actual downloaded/parsed counts, source hashes, retrieval mode, bundle IDs with several short exact examples, and optional branch dispositions. Do not copy entire papers into a handoff.

**Review gate:** real sources and reusable locators exist; no guessed metadata or substituted fixture corpus; all operational limits and source failures are visible. NLP retrieval benchmarking is explicitly not required.

## 10. P4 — Structured evidence extraction and verification

**Goal:** convert real retrieved text into atomic source-grounded evidence artifacts, retaining support, negative/null results, and uncertainty. No autonomous model tools.

**Allowed writes:** `extraction/`, extraction workflow/CLI, minimal shared schema additions, extraction config/provider extra/lock, P4 tests/artifacts/handoff. No graph integration changes before P5.

### P4 execution order

- [ ] **P4.1 Implement chat providers and configure selected roles.** Implement LiteLLM proxy, OpenRouter, and Groq via their LangChain integrations following §6.4.1. Resolve qualified extractor/verifier selectors; an omitted verifier selector inherits the extractor. Check constructor/proxy routing offline for all three, install/load only selected extras, and validate only selected credentials. Confirm the selected model's structured-output mode within the total run budget. Keep raw responses/metadata locally, whether or not optional tracing is enabled. Provider absence is a clear setup error; never silently use a different model or provider.
- [ ] **P4.2 Define extraction/verification schemas.** The extractor returns zero or more atomic findings with source span IDs/quotes, entities and mapping hints, relation/direction, assay/outcome, statement status, directness, context, and explicit unknowns. The verifier checks each field against the exact same bundle. It may say insufficient context; it cannot retrieve, repair the finding, or invent missing assays.
- [ ] **P4.3 Write concise prompts.** State that source text is data, not instructions. Require explicit source grounding, allow NO_RELATION, keep primary findings separate from cited/review summaries, forbid binding-to-causality promotion, preserve complexes/species/negation, and use no external knowledge to fill missing facts. One prompt version each; no prompt tournament.
- [ ] **P4.4 Extract and verify.** Call extractor once per selected bundle. Verify returned findings using the same bundle in a bounded second call; batch findings from one bundle if schema allows. Store raw/parsed responses and usage. Do not call a verifier for an empty NO_RELATION output unless a specific regression requires it. Keep the scheduled-call ceiling at 40 for 20 bundles, and include bounded retries in the configured total-attempt/token budget.
- [ ] **P4.5 Deterministic source checks.** Validate quotes/offsets against stored canonical text and document hash; map entities through approved resolver; validate schema/enums and source IDs; flag missing or conflicting fields. The model cannot assign unchecked passage offsets, stable IDs, or a made-up PMID.
- [ ] **P4.6 Disposition and eligibility.** AUTO_ACCEPTED requires a faithfully stated finding, resolved scoring entities, matching source spans, and verifier support. Ambiguous entity/context/meaning becomes UNCERTAIN. Unsupported extraction/invalid quotes/NO_RELATION becomes REJECTED or explicit empty-result record. Accepted review/speculative statements, if retained, are discovery-only and not independent experimental support. Null or negated findings can be AUTO_ACCEPTED; their polarity is decided relative to a claim, not inferred from acceptance.
- [ ] **P4.7 Claims, evidence, and deduplication.** Keep claim IDs independent of one paper and preserve separate evidence assertions. Deduplicate exact repeated spans/findings within a source, but do not discard distinct experiments. Retain unresolved experiment identity and known shared-study dependencies. Compatible binding/perturbation findings can be linked; do not collapse them into DIRECT merely because both appear in the same paper.
- [ ] **P4.8 Persist artifacts.** Write `accepted_findings.parquet`, `claims.parquet`, `evidence_assertions.parquet`, `uncertain.jsonl`, `rejected.jsonl`, and extraction manifest; a single normalized table plus views is acceptable if it preserves these logical contracts. Store raw outputs separately. Do not overwrite earlier model/prompt-version results.
- [ ] **P4.9 Minimal quality checks.** Use a small fixture set for reversal, explicit no effect, repression vs negation, speculation, mismatched species, fabricated quote, mixed experiment contexts, and unresolved complex. Test deterministic disposition. Include §6.4.1's provider mapping, credential isolation, schema-mode failure, shared-budget, and cache-identity checks. Fixtures are clearly labelled engineering-only; no NLP performance claims.
- [ ] **P4.10 Live dry-run and bounded run.** Show the selected bundle IDs, proposed calls/token estimates, provider/model, and configured caps without secrets. Run only with actual configured credentials/budget. Attach actual usage. Zero accepted findings is a valid outcome if faithfully reported; no acceptance rule may be loosened to populate the graph.
- [ ] **P4.11 Replay and handoff.** Replaying identical source/model/prompt configuration uses cached successful outputs and does not re-spend calls. Failures can be retried explicitly; changed prompts create a new artifact lineage. Submit actual findings with exact spans and all dispositions for review.

### P4 commands and evidence

```bash
.venv/bin/python -m pip check
.venv/bin/python -m pytest tests/test_extraction.py -q
.venv/bin/python -m regkg extract --run <retrieval_key> --dry-run
.venv/bin/python -m regkg extract --run <retrieval_key> --live
.venv/bin/python -m regkg verify evidence --run <extraction_key>
.venv/bin/python -m regkg extract --run <retrieval_key> --live
```

Handoff: resolved extractor/verifier qualified model identities, selected extras/versions and structured-output modes, which adapters were checked offline versus exercised live, source/model/prompt run IDs, sanitized usage, scheduled/attempted calls (including preflight/retries), accepted/uncertain/rejected/empty counts, real examples and their exact evidence spans, and cache replay result. Raw credential values must never appear.

**Review gate:** real extraction ran within bounds and source integrity holds. Automated agreement is not human validation. If keys are unavailable, code/fixtures may be reviewed independently but live P4 acceptance remains open.

## 11. P5 — Local Neo4j and graph integration

**Goal:** first produce reviewable graph files without Neo4j, then separately import those files into a locally running graph with traceable project observations and real accepted evidence. Aura is not the primary target of this package.

**Allowed writes:** `compose.yaml`, `configs/graph.yaml`, graph modules/Cypher/CLI, minimal contract additions, graph tests/artifacts, README setup, P5 handoff. Never alter another project's services.

### P5 file-first contract — export before import

```text
Raw project data + literature
    → normalized Parquet tables / JSON evidence artifacts
    → inspect, validate, and correct the processing rules
    → versioned Neo4j CSV bundle + manifest + import mapping
    → inspect and validate the exact bundle
    → separate Neo4j import command
    → graph count, identity, and provenance checks
```

**Working files are the source of truth.** Ingestion, extraction, candidate analysis, and nomination calculations read/write files without a Neo4j connection. Use Parquet for typed analytical tables and JSON/JSONL for nested extraction/source records; optional TSV/CSV views aid inspection. Neo4j is a rebuildable query representation of a selected subset. Never write to Neo4j inside ingestion, extraction, or nomination functions. Corrections create new versioned artifacts and exports; do not silently edit a checksum-recorded bundle or make the database the only location of a scientific correction.

**Export bundle:** `graph export` reads completed artifacts, applies the materialization policy, and writes `data/graph_exports/<export_key>/` atomically. It must work with no server, driver connection, Docker runtime, or database credentials. Include:

- `nodes/<Label>.csv`: one typed logical table per allowed node label, with a stable `id` and explicit properties.
- `relationships/<Type>.csv`: one table per relationship type/endpoint-label combination, with stable relationship `id`, `source_id`, `target_id`, and explicit properties. Declare endpoint labels in the schema; never infer them from free text.
- `schema.json`: column types, nullable fields, endpoint labels, graph-property mappings, and CSV serialization rules. Use UTF-8, headers, standard CSV quoting, and lossless numeric precision. For nullable columns, declare an explicit null flag when empty string is meaningful; preserve zero vs missing. Flatten supported graph properties; keep arbitrary nested metadata in its source artifact. Do not add admin-import-specific header syntax to ordinary `LOAD CSV` tables.
- `manifest.json`: source artifact/run keys and hashes, export/schema/policy versions, file checksums, row counts, expected distinct IDs by label/type, selection/omission counts, and any parent bundle dependency.
- `validation.json` and `preview.md`: validation results and a small readable sample of nodes, relationships, source chains, and counts. No secret values or invented evidence.
- `import.cypher`: deterministic schema-specific `LOAD CSV WITH HEADERS` statements, explicit type/null conversions, fixed labels/types, and parameterized file URLs. Generate from maintained mappings, never from LLM text. Include import order and use stable IDs in `MERGE`.

**Pre-import validation:** verify checksums, schema/header agreement, value types, finite numerics, required properties, unique semantic IDs, relationship endpoint closure, and exact source provenance. Reject duplicate/conflicting IDs and dangling endpoints. Validate CSV round-trip for quotes, commas, newlines, Unicode, empty vs null, and zero-valued measurements. Report legitimate self-links without automatically rejecting scientific autoregulation. The first bundle is self-contained; later nomination additions may reference a declared parent bundle, whose endpoint inventory must be checked. Export verification and load `--dry-run` are offline and must not initialize a database. A modified bundle fails checksum validation; regenerate it after correcting its upstream artifact or mapping.

**Import choice:** use local Neo4j's native `LOAD CSV` for this first implementation. CSV is directly supported; tab-separated input is possible with `FIELDTERMINATOR`, but supporting a second import format is unnecessary. Parquet stays the analytical master format. Current `neo4j-admin database import full` also supports Parquet for initial bulk creation; that is a separate, version/edition-sensitive administrative path and is deferred. Do not treat `LOAD CSV` as a Parquet reader or run a full database replacement for routine reloads. References: [LOAD CSV](https://neo4j.com/docs/cypher-manual/current/clauses/load-csv/) and [full administrative import](https://neo4j.com/docs/operations-manual/current/import/full-import/).

**Separation of commands:** `graph load --bundle <path>` reads only a validated, already-created bundle. It cannot regenerate evidence, select targets, call models, or rerun export. Mount this project's `data/graph_exports/` read-only into the container's import directory; derive confined `file:///` URLs from manifest-relative paths and reject path traversal. Driver code executes the maintained import statements and verification queries. Load nodes first, verify endpoint presence, then relationships; never allow `MATCH` to silently discard a relationship. Revalidate checksums before import and verify actual IDs/counts against the bundle afterward. No implicit database writes from export, report, or `run-at1 --resume`.

**Two executions within P5:** first assign the offline part of P5.4 (schema definition) and P5.5 (export/validation) and inspect its files. Then assign P5's service/import steps using the same export key. This does not add a new top-level package; an export-only handoff is `PARTIAL` for P5 and the live import checkbox stays open. The files can be processed/reviewed while Neo4j setup is unavailable.

### P5 execution order

Prepare the offline bundle as above first. The numbered service/import items below apply only when the separate import work is assigned.

- [ ] **P5.1 Inspect local runtime.** Check Docker availability and existing containers/ports without printing secrets. Use Compose service key `neo4j`, project-specific container name `regkg-neo4j`, and volume `regkg-neo4j-data` unless this project's existing service dictates otherwise. Prefer loopback host ports 7474/7687 if free; use documented alternatives if occupied. Do not stop another project's container to obtain a port.
- [ ] **P5.2 Define local deployment.** Pin a verified supported Neo4j Community image version, use persistent `/data`, a read-only project graph-export mount at `/import`, loopback port bindings, environment-provided authentication, and a simple health/readiness check. Keep credentials out of compose/config source. Do not install Enterprise/APOC/GDS/GraphRAG plugins for this task.
- [ ] **P5.3 Driver configuration.** Create one driver per command/process, verify connectivity, set database explicitly, and close resources. Fail closed on a nonlocal endpoint unless the user explicitly selected a cloud mode. Use bounded query timeouts, parameterized values, and a chosen batch size (default 500 rows; tune only if needed).
- [ ] **P5.4 Schema.** Create uniqueness constraints on stable IDs for Gene, CellType, BiologicalContext, SpatialNicheState, NeighborhoodProfile, Dataset, AnalysisRun, ExpressionObservation, ChromLinkerObservation, GeneProgram, Publication, Passage, RegulatoryClaim, EvidenceAssertion, NicheExpressionSignature, and TFNomination when loaded. Use one NicheExpressionSignature node per comparison with selected per-gene values on HAS_GENE links. Do not materialize both redundant row-nodes and equivalent links without a query need.
- [ ] **P5.5 Materialization policy.** Start with AT1 states/contexts, selected candidates, and at most 25 target genes per candidate/comparison chosen by documented descriptive signature relevance among its project/prior targets, plus genes needed by accepted findings. Include selected TF/target expression and original ChromLinker values in their AT1 contexts, including selected zero-valued observations. Keep full matrices in Parquet. Materialize each accepted finding and every source span needed to inspect it. Implement the offline `graph export` and `verify graph-export` commands and bundle contract above. Produce expected unique node/relationship counts before touching the graph. Return the bundle for inspection before the separate import work.
- [ ] **P5.6 Import identity nodes then observations from CSV.** Consume only the specified validated bundle through schema-specific `LOAD CSV` statements. Use `MERGE` on immutable IDs, not mutable text. Add context/niche/source/run links from exported records. Missing referenced IDs fail the batch/report, not silently drop relationships. Do not turn raw ChromLinker observations into REGULATES edges.
- [ ] **P5.7 Import evidence from the same bundle.** Use Claim→EvidenceAssertion→Passage→Publication with experiment/study links when resolved. Keep original finding context and relative support/counter-evidence links. Multiple evidence assertions can share one claim. Uncertain/rejected findings stay in artifacts outside scored evidence.
- [ ] **P5.8 Transaction and rerun behavior.** Batch `LOAD CSV` with `CALL { ... } IN TRANSACTIONS` using syntax supported by the pinned Neo4j version. Execute such statements in an implicit transaction via `session.run` and consume the result, not inside `execute_write`/a managed transaction. Other bounded queries may use managed transactions. Record progress after results complete; earlier batches may remain committed on failure, so rerunning an incomplete file must be idempotent. No model calls or source transformations during import. Repeat semantic imports cannot duplicate nodes/links. New versions preserve prior evidence rather than clobber it; do not silently delete records absent from a later bundle. Driver execution reference: [implicit transactions and CSV imports](https://neo4j.com/docs/python-manual/current/query-advanced/).
- [ ] **P5.9 Required queries.** Implement fixed parameterized functions: AT1 niche neighborhood; a TF's raw predicted targets in a specified condition/niche; signature effect and expression for a gene; claims and supporting/negative/inconclusive findings for a TF; exact cited passages/publications. Return honest empty results and coverage fields.
- [ ] **P5.10 Live validation.** Prove offline export/validation works without database credentials first. Import the inspected bundle, then run actual local queries, counts by label/type, unique-ID checks, expected-vs-loaded counts, source-chain checks, and a second identical import. Failure-injection can use a small fixture transaction; never corrupt live imported data to test recovery.
- [ ] **P5.11 Retention/setup documentation.** Document start/stop/connect, chosen ports, one persistent volume, export/rebuild from accepted artifacts, and safe shutdown. No destructive volume removal command in a routine reset recipe. Log that no Aura account is provisioned.

### Minimum graph paths

```text
CellType --HAS_NICHE_STATE--> SpatialNicheState --DEFINED_BY--> NeighborhoodProfile
NeighborhoodProfile --HAS_NEIGHBOR {mean_count, fraction}--> CellType
ChromLinkerObservation --PREDICTS_TF/PREDICTS_TARGET--> Gene
ChromLinkerObservation --FOR_STATE/IN_CONTEXT/GENERATED_BY--> State/Context/Run
NicheExpressionSignature --CASE_STATE/REFERENCE_STATE/IN_CONTEXT--> State/Context
NicheExpressionSignature --HAS_GENE {mean1, mean2, effect, fractions}--> Gene
Gene --REGULATOR_OF_CLAIM--> RegulatoryClaim --TARGET_GENE--> Gene
RegulatoryClaim --HAS_EVIDENCE {polarity, comparison_basis}--> EvidenceAssertion
EvidenceAssertion --GROUNDED_IN--> Passage --FROM_PUBLICATION--> Publication
TFNomination --NOMINATES--> Gene
TFNomination --FOR_STATE/IN_CONTEXT/USES_PROGRAM/GENERATED_BY--> State/Context/Program/Run
TFNomination --USES_EVIDENCE {context_match, rule_version}--> EvidenceAssertion
```

Relationship naming can be adjusted once for a coherent schema, but document the mapping and keep query/report clients consistent. Do not add arbitrary generated relationship types from LLM strings.

### P5 commands and evidence

```bash
.venv/bin/python -m pytest tests/test_graph.py -q
# Offline file stage: no Neo4j required.
.venv/bin/python -m regkg graph export --run <extraction_key> --project-run <ingest_key>
.venv/bin/python -m regkg verify graph-export --bundle data/graph_exports/<export_key>
.venv/bin/python -m regkg graph load --bundle data/graph_exports/<export_key> --dry-run
# Inspect the bundle; run the following only in the separate import assignment.
docker compose up -d neo4j
.venv/bin/python -m regkg graph init
.venv/bin/python -m regkg graph load --bundle data/graph_exports/<export_key>
.venv/bin/python -m regkg verify graph --run <graph_key>
.venv/bin/python -m regkg graph load --bundle data/graph_exports/<export_key>
```

Compose service key is `neo4j`; container name may be `regkg-neo4j`. If runtime is unavailable, do not pretend a driver mock proves a live graph.

**Review gate:** offline export and its validation/preview are inspectable; the live graph was imported from that exact checksummed bundle; imports are idempotent; evidence paths and units are correct; source graph matches the manifest; data remain persistent after normal service stop/start.

### Hosting note

As checked in the synthesis, Aura Free allows 50,000 nodes/175,000 relationships and has inactivity rules. Even the 36,253 nonzero AT1 observations would need 181,265 relationships under five links per observation. Local Community is therefore the development default; any later Aura demo uses an explicit subset and a preflight size estimate. Recheck official limits if actually provisioning. This hosting decision does not justify dropping provenance or conflating scientific records.

## 12. P6 — Nominations, reports, and integrated acceptance

**Goal:** a scientist can inspect each AT1 nomination and trace its evidence. This package evaluates the biomedical contribution, not NLP model performance.

**Allowed writes:** nomination/report modules, complete CLI orchestration, ranking/materialization updates for nomination nodes, targeted tests, README/runbook, report artifacts, P6 handoff. No new UI/server, broad corpus, or framework migration.

### P6 execution order

- [ ] **P6.1 Assemble evidence components.** Join P1 observations, P2 candidates/concordance, and P4 accepted findings by explicit IDs/context. Preserve missing components and retrieval coverage. Context match is computed for each nomination; use a documented conservative rule, not a single global evidence property.
- [ ] **P6.2 Context rules.** EXACT requires explicit matching species, focal cell type, condition/disease, and compatible model system for the requested claim. Broad alveolar epithelium alone is not exact AT1. CLOSE/PARTIAL/MISMATCHED/UNKNOWN retain component-level reasons; unknown fields do not imply matches. Rule changes create a ranking version.
- [ ] **P6.3 Experimental grouping.** Count known independent studies conservatively with accession/PMID lineage; show publication count separately, plus unresolved-dependency count. An unresolved experiment must not receive an invented ID implying known independence. Accepted reviews/association-only findings cannot be counted as primary experimental studies.
- [ ] **P6.4 Transparent provisional literature ordering.** Order evidence profiles using a documented tuple: best eligible assay class (compatible binding+functional > functional or binding > reporter/context-limited > association-only), then context-match class, then known distinct study count. This is a provisional prioritization rule, not a validated confidence scale. Report the tuple and counts. Qualified opposing/null findings remain visible separately; do not invent numeric penalties from their count or downgrade high-quality conflicts to uncertain extraction.
- [ ] **P6.5 Group ranks and missingness.** Rank connectivity only if confirmed semantics have been supplied. Rank expression/prior evidence by absolute eligible signed-concordance score, preserving sign/direction and coverage. Rank external evidence by P6.4. Use deterministic average ranks for exact ties; stable TF-ID order affects display only. No finite rank for missing components.
- [ ] **P6.6 RRF baseline.** Use fixed group weights (initial default 1 each for available defined groups) and `k=60` as a conventional configurable baseline, not a scientific constant. Score is the sum of `weight/(k+rank)` for observed components; do not renormalize per TF. Keep the candidate universe fixed within each comparison. Show connectivity as unavailable when unresolved and label the score as an evidence-based prioritization using the available groups. Preserve route-specific lists so missing literature coverage is not mistaken for a negative study.
- [ ] **P6.7 Categories and explanations.** Emit supported/qualified/project-prediction-only/literature-only/contradictory/insufficient with explicit rule reasons. Do not label a candidate CHROMLINKER_ONLY based on a supposedly strong score while score semantics remain unknown; use `PROJECT_PREDICTION_ONLY` or `INSUFFICIENT` with reason until a strength criterion exists. Seed membership alone gives no support category. Negative findings alone never count as positive nomination evidence.
- [ ] **P6.8 Baselines and sensitivity.** Compare expression/prior-only and combined rankings. Provide ChromLinker-only rankings only if semantics are confirmed; otherwise export descriptive connectivity profiles and mark that comparison unavailable. Repeat ranking after removing one evidence group and each resolved study; report top-list/rank changes with the same universe. These are robustness checks, not donor confidence intervals or predictive-accuracy estimates.
- [ ] **P6.9 Reports.** Export `nominations.csv`, `nominations.parquet`, `evidence.csv`, `coverage.csv`, `ranking_sensitivity.csv`, `summary.md`, and one evidence Markdown report per TF. Optional static HTML may reuse these results but is not a separate frontend requirement. Include condition/target niche, concordance sign/coverage, raw connectivity summary/semantic caveat, TF expression, independent evidence/context/contradictions, cell counts/donor unknowns, source passages/PMIDs, and ranking version. Clearly label full-text vs abstract-only sources.
- [ ] **P6.10 Graph nominations.** Export nomination records to a new CSV bundle using `graph export --nomination-run <nomination_key> --parent-bundle <base_bundle_path>`, with stable versioned IDs and links to the exact evidence/project artifacts used. Validate/inspect it, then import separately with `graph load --bundle <nomination_bundle_path>`. Nomination/report generation must succeed without Neo4j. Do not recompute a separate ranking inside Cypher. Ensure reports and graph return the same candidate identities/counts/component values.
- [ ] **P6.11 Integrated command and replay.** Implement `run-at1 --resume` as a thin sequence of existing stage functions using manifests, not another pipeline framework. It must stop explicitly when required live configuration is missing. Its default endpoint is validated files/reports and graph export, with no graph connection or import. Preserve worker review boundaries; a resume command does not authorize advancing an unreviewed package. Graph loading remains the explicit separate `graph load --bundle ...` command. A completed replay uses cached literature/model outputs and reproduces scientific results (ignoring execution timestamps); replay the import separately to check graph idempotency.
- [ ] **P6.12 Final handoff.** Run focused integration checks, save a complete actual command transcript without secrets, report optional branches exercised/deferred, and list all limitations. No claim of human-validated extraction, causal TF discovery, all-cell-type completion, or publication readiness without the relevant evidence.

### P6 commands and evidence

```bash
.venv/bin/python -m pytest tests/test_nomination.py tests/test_replay.py -q
.venv/bin/python -m regkg nominate --project-run <ingest_key> --candidate-run <candidate_key> --evidence-run <extraction_key> --cell-type AT1
.venv/bin/python -m regkg report --run <nomination_key>
.venv/bin/python -m regkg verify report --run <report_key>
.venv/bin/python -m regkg run-at1 --config configs/project.yaml --resume
.venv/bin/python -m ruff check src tests
.venv/bin/python -m pytest -q
.venv/bin/python -m pip check
```

Report checks: every evidence ID resolves, quotes match stored text, no unsupported statistical/causal claims, all required seeds are visible, missing connectivity rank remains null, cell counts/units are preserved, and repeated output is stable. Final full tests are appropriate once for this integrated boundary; avoid repeated full runs absent a change/failure.

**Review gate:** the AT1 report uses actual input data and actual retrieved/processed literature, matches the live graph, and exposes its limitations. If no supporting findings were accepted, the report must show that and the reviewer assesses whether the initial demonstration is informative enough; workers must not fabricate a minimum number of positive edges.

## 13. Worker assignment and handoff templates

### 13.1 Copy/paste assignment

```text
Repository: /Users/rajlq7/Desktop/Projects/spatial-niche-regulatory-kg
Read AGENTS.md and plan.md. Execute package P<n> only.
Prerequisite review: <link or statement that prior package was accepted>.
Outcome: <copy the package goal>.
Allowed write scope: <copy the package scope>.
Inputs/configuration supplied: <actual artifact IDs; model/budget or selected model if relevant>.
Perform the listed execution steps and acceptance commands using actual inputs.
Do not edit plan checkboxes or reviewer status. Do not start P<n+1>.
Do not change scientific semantics or expand NLP/product scope.
Write docs/handoffs/P<n>.md with exact files, commands, artifact IDs, results,
optional-branch dispositions, and any blockers. Stop for lead review.
```

A new worker does not rerun the entire source audit if it was accepted; read the prior handoff/manifests and verify relevant inputs. A worker may fix a directly blocking regression from its own work within scope; unrelated refactors require a separate assignment.

### 13.2 Required handoff content

```markdown
# P<n> handoff
Status: READY_FOR_REVIEW | PARTIAL | BLOCKED
Assigned outcome:
Prerequisite artifacts/review:

## Changes
- File and resulting behavior; explain only consequential decisions.

## Actual verification
| Command | Exit/result | Evidence/artifact path |
| ... | ... | ... |

## Run/artifact identity
- Input hashes and upstream artifact IDs.
- Output artifact IDs, counts, versions, and live/fixture mode.
- Optional branch exercised/deferred and reason.

## Scientific checks
- Units/context/ID/coverage/source-grounding checks relevant to this package.

## Limitations and blockers
- Exact missing setting/source/decision; independent work completed.
- Do not include secrets or full credential-bearing URLs.

## Proposed review disposition
- Which acceptance item IDs have evidence (leave plan boxes unchanged).
```

Screenshots alone are not sufficient for data/code acceptance. Use reproducible commands and saved artifacts. A worker's narrative is not proof of a live network/model/database call.

## 14. Lead-review procedure and completion log

For each returned package, the lead reviewer:

1. Reads its handoff and actual changed files. Uses Git diff if available; otherwise inspects files and source hashes. Never assumes a worker's status is accurate.
2. Checks implementation against package boundaries, contracts, scientific invariants, and the user's latest decisions.
3. Reads the relevant actual output artifacts and reruns focused checks sufficient to verify the claim. Avoid needless repeat paid calls; validate cached outputs/source grounding first.
4. Separates passed implementation tests from live acceptance and optional branches.
5. Records findings in `docs/reviews/P<n>.md`, with corrections if needed. Returns a bounded repair assignment when there is a failure.
6. Only after acceptance, changes the corresponding item boxes to `[x]`, marks the package `ACCEPTED`, and fills the ledger below with review date/evidence.
7. Gives the next package assignment. Does not rewrite the architecture between routine packages.

| Package | Reviewed on | Reviewer evidence | Corrections / unresolved limitations |
|---|---|---|---|
| P1 | — | — | — |
| P2 | — | — | — |
| P3 | — | — | — |
| P4 | — | — | — |
| P5 | — | — | — |
| P6 | — | — | — |

### Final acceptance checklist

- [ ] All six required packages accepted with real evidence and linked reviews.
- [ ] Source data/reference files preserved; no unrelated project modifications.
- [ ] No fabricated IDs, assay facts, donor counts, connectivity semantics, DE statistics, or positive findings.
- [ ] Real AT1 evidence report exists with citations, counter-evidence, coverage, and provenance.
- [ ] Local Neo4j contains the selected evidence graph; repeated loads preserve counts/identities.
- [ ] Replay works from accepted artifacts without unnecessary network/model calls.
- [ ] Missing score semantics and optional model/PDF branches are explicitly described.
- [ ] Instructions remain centralized in AGENTS.md and CLAUDE.md remains its relative symlink.

## 15. Deferred expansion after the first accepted AT1 result

This list is deliberately not part of the six-package finish line. The reviewer/user chooses later assignments based on the first real report:

- Increase literature coverage and resolve missing TF/target/context evidence.
- Add further curated resources with preserved provenance and dependency grouping.
- Apply the same code to alveolar macrophages, activated fibrotic fibroblasts, and KRT5neg/KRT17pos cells.
- Add pathway interpretation from versioned Reactome/GO annotations with a documented tested/eligible background; do not infer pathway membership with an LLM. This is deferred to keep the first result bounded, not removed from the broader scientific design.
- Incorporate confirmed ChromLinker aggregation rules without reinterpreting earlier stored values.
- Improve the optional embedding/PDF branch only if actual retrieval needs justify it.
- Add donor-aware analysis if donor-resolved inputs arrive.
- Add REST/MCP over fixed scientific queries for LungMAP/LungChat.
- Consider LangGraph only if ordinary resumable loops become operationally inadequate.
- Add held-out perturbation validation, richer regulatory-locus modeling, or an expanded paper analysis when there is data and explicit scope.

Do not convert this list into mandatory scaffolding during P1–P6.

## 16. Current next assignment

**Assign P1 only.** No provider key, embedding download, Neo4j server, or live literature search is required for P1. Ask the worker to return `docs/handoffs/P1.md`; bring that work to the lead reviewer before P2.
