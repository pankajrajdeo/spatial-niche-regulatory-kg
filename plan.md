# Execution plan — Spatial NicheLinker Regulatory Evidence KG

**Prepared:** 2026-09-21. **Updated:** 2026-09-22. **Status:** P1, manuscript-wide P2, and the original P3 repair baseline accepted; expanded P3 corpus readiness required before P4.

This is the operational plan for building the biomedical KG described in the two synthesis documents. It is intentionally detailed so a worker can execute a bounded assignment without redesigning the science. The work is divided into **six review gates**, not dozens of separate agent turns. Detailed checkboxes are acceptance evidence within those gates.

## 0. Resume without this conversation

**Migration checkpoint (latest):** The user stopped local screening and authorized pushing code, plan and a private Git LFS data snapshot for continuation on their other laptop through LiteLLM GLM quota. Start at [docs/CONTINUE_HERE.md](docs/CONTINUE_HERE.md) and [docs/RESUME.md](docs/RESUME.md). plan.md is now tracked by explicit user instruction. Earlier no-push/ignored-plan/local-OpenRouter assumptions are superseded. The existing source repair handoff and LLM screening implementation must be reviewed proportionately; do not replay old P3 assignments. Preserve partial screening caches with their true provider provenance. No full KG extraction has run.

**Latest user scope update:** [LLM-assisted literature selection](docs/assignments/literature-llm-screening.md). The user authorizes LLM paper/context screening across the acquired corpus and discovered metadata, using BM25/embeddings for prioritization without a hard top-k exclusion. This supersedes earlier no-chat restrictions for this screening operation only. Complete the running source/cache repair first. A versioned source snapshot precedes screening; final extraction selection is frozen afterward. Do not treat 192 source-ready papers as the final scope or impose an arbitrary paper-count target.

**Latest lead review:** [P3 source-gap completion](docs/reviews/P3-source-gap-completion.md), 2026-09-22: `litcorpus-301a27a43b316dd7`; 201 tests, 92 checksums and preservation of prior covered papers verified. Source progress accepted. Reproduced selector/limit cache-identity defect and freeze-report inconsistency remain; the review authorizes those repairs plus the named Habermann supplement and PMID 42327275 full-text retry in one pass. No broad discovery, P4 implementation or live inference authorization.

Read [the new-computer transfer/setup checklist](docs/RESUME.md) before resuming elsewhere. This plan is now tracked; restore the private LFS snapshot for reference documents, generated artifacts and caches. Never transfer secrets.

The complete active [P3 correction assignment](docs/assignments/P3-corpus-corrections.md) records the per-paper screening decision, context corrections, serialized limits, supplemental dependencies, excluded-paper audit, budget, tests and stop boundary. It supersedes global top-10 exclusion and any conflicting older P3 selection wording. No chat history is required to reconstruct this assignment. Implementation reports exist but remain unaccepted until lead review; see the assignment snapshot and actual artifacts.

## 1. Finish line, time budget, and review ownership

### 1.1 Complete project finish line

**User clarification:** there is one complete manuscript-ready deliverable, not a V1, V2 or MVP. A small pilot validates the implementation before full approved-corpus processing. It does not replace full scope. Every required pending item must be completed or have an evidence-backed disposition approved by the lead/user; a worker's proposed deferral is not completion. Internal schema/rule versions remain necessary for reproducibility.

Produce a reproducible, locally runnable manuscript regulatory-evidence KG that:

1. Ingests all four available project-data sources without changing scientific meaning.
2. Preserves normalized data and provenance outside the graph.
3. Generates candidates for all four manuscript regulatory lineages from their named TFs, supplied ChromLinker observations, and signed expression/prior evidence.
4. Accounts for every advisor paper, screens available full texts, and extracts relevant atomic findings in bounded batches, retaining negative/null findings and explicit coverage gaps.
5. Exports and validates a reviewable graph-file bundle, then imports that exact bundle into local Neo4j in a separate command.
6. Exports lineage-specific nomination/evidence reports and an integrated manuscript claim-to-evidence matrix with uncertainty, counter-evidence, coverage, and exact sources.

The required lineage-specific TF seeds and comparisons are listed in [the manuscript scope](docs/manuscript_scope.md): 13 unique named regulators across 16 lineage–TF memberships and six primary lineage/condition niche comparisons. Do not force supporting literature to exist for any of them. A TF with no support remains visible with coverage/missingness, rather than receiving invented evidence.

**Scientific scope:** follow the user-supplied manuscript draft as summarized in [the manuscript requirements](docs/manuscript_scope.md). The KG must cover all four regulatory cases: AT1, alveolar macrophages, KRT5−/KRT17+ epithelial cells, and activated fibrotic fibroblasts. AT1 has no automatic priority. Use a reusable context-aware schema and manuscript-specific evidence coverage, rather than a universal regulatory atlas. Within-condition niche contrasts, disease-dependent patterns, attenuation, and redistribution all matter; do not select only positive Niche2 gains. The draft does not resolve missing score semantics or supply unprovided statistical results. Existing AT1-only outputs remain an accepted baseline, not completion of the expanded scope.

### 1.2 Keep the first build bounded

The original **3–5 hour** estimate described the small AT1 implementation slice, not the expanded manuscript scope, all-advisor acquisition, and PDF readiness. Reuse that implementation and work in bounded assignments; report actual remaining work and external-download dependencies. Do not sacrifice coverage or correctness to preserve the obsolete estimate.

- Parse the whole supplied numeric input set once; the files are manageable and this avoids repeated cell-type-specific parsers.
- Calculate candidate summaries for all four manuscript regulatory lineages with the same code and explicit per-lineage seeds/comparisons. Schedule batches by documented manuscript coverage gaps, without hard-coded AT1 priority.
- Account for all advisor papers (currently 110 unique PMIDs), preserving all list memberships. Use at most **10 unique real papers**, **20 extraction bundles**, and **40 scheduled extractor/verifier calls per live extraction batch**. These are batch limits, not a corpus cap. Audit/acquire the fixed advisor list in resumable batches; do not automatically run all paid extraction batches. See §9 corpus-readiness extension.
- Reuse cached source downloads and successful extraction results. Do not crawl PubMed or embed its full collection.
- No web application, REST/MCP, general-purpose agent platform, model comparison, NLP benchmark, fine-tuning, figure-vision analysis, or publication manuscript in this finish line. One bounded P4 evidence-assembly agent is specified in §6.4.3; extraction and verification remain tool-free.
- Implement the XML/BioC and local Docling PDF paths required by the advisor corpus before live extraction of their outputs. Abstract-only processing stays explicitly incomplete for full-text coverage. Complete corpus preparation and obtain a disposition for remaining download/parsing gaps before P4. The user will choose the LLM provider/model/key after reviewing the frozen corpus and inference budget.
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
| P1 | Runnable project, contracts, complete project-data ingestion | This plan | 45–60 min | ACCEPTED — [review](docs/reviews/P1.md) |
| P2 | Manuscript-lineage candidates, signed prior analysis, retrieval queues | P1 accepted | Baseline estimate 30–45 min; extension additional | ACCEPTED — [baseline review](docs/reviews/P2.md); [manuscript extension](docs/reviews/P2-manuscript.md) |
| P3 | Real literature acquisition, parsing, bounded passage retrieval | Reviewed candidate scope | Original slice 40–60 min; corpus extension additional | ORIGINAL REPAIR BASELINE ACCEPTED; manuscript corpus/readiness PENDING — [review](docs/reviews/P3.md) |
| P4 | Structured extraction, verification, accepted/uncertain/rejected findings | P3 accepted | 30–45 min | NOT_STARTED |
| P5 | Offline graph-file export, then separate Neo4j import and evidence queries | P4 accepted | 30–45 min | NOT_STARTED |
| P6 | Manuscript evidence/nomination reports, replay and final review | P5 accepted | 30–45 min | NOT_STARTED |

- [x] **P1 accepted** — environment/contracts/ingestion evidence reviewed.
- [x] **P2 AT1 baseline accepted** — historical candidate/prior/queue evidence reviewed.
- [x] **P2 manuscript extension accepted** — four lineages, named TF memberships, six primary comparisons, and manuscript-wide queues reviewed.
- [x] **P3 original repair baseline accepted** — R1–R4 and F1/F2 verified on the bounded original corpus; [review](docs/reviews/P3.md).
- [ ] **P3 accepted** — manuscript-wide acquisition, parsing, retrieval, coverage, and pre-P4 readiness/budget reviewed.
- [ ] **P4 accepted** — live evidence extraction and source grounding reviewed.
- [ ] **P5 accepted** — live local graph and repeat-import checks reviewed.
- [ ] **P6 accepted** — all four regulatory cases and manuscript claim/evidence coverage, provenance, and replay reviewed.

P1, the original AT1 P2 baseline, the manuscript P2 extension, and the original P3 repair baseline are accepted. Overall P3–P6 remain unchecked; expanded P3 implementation and reports exist but are not yet accepted. Inspect the correction assignment, current artifacts and lead reviews before continuing.

## 2. Sources of truth and inherited practices

Read in this order:

1. Latest user instructions and [AGENTS.md](AGENTS.md).
2. [Current manuscript requirements](docs/manuscript_scope.md), then the assigned package and shared contracts in this plan. These supersede older AT1-first statements in the syntheses.
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
| Lightweight biomedical embedding model/revision | Selected `ollama:pankajrajdeo/biomed-embeddings-16l-fp16:latest`; user reports local ID `b97df00ac434` | Use selected Ollama model; inspect digest, dimensions, token limits, and query/document encoding requirements in P3; no replacement download | Adapter/encoding-contract validation and real passage retrieval in P3; direct API smoke passed |
| Extraction provider/model/key | Selected `openrouter:z-ai/glm-5.3-flash`; API key supplied locally; never print it | Support all three adapters; default extractor/verifier to selected model; apply §6.4.2 routing; check key presence without printing | LangChain/schema integration and real-bundle P4 acceptance; direct API smoke passed |
| Neo4j/Docker availability | Not yet established | Inspect in P5; reuse this project's service if present; otherwise create its local service | Live graph acceptance if runtime unavailable |
| Gene/prior mapping snapshots | Not yet fetched | Fetch documented official snapshots in the assigned network-capable package; record provenance | Normalized external findings/ULM if mappings or prior unavailable |
| Donor counts/contributions | Not supplied | Store null with reason, never infer from cells | Donor-level inference only; not descriptive processing |

Workers should finish independent tasks while a decision is pending. Do not repeatedly ask for the same missing answer, silently select a different model, or declare blocked optional embeddings a blocker for ingestion.

### 3.3 External action bounds

Planning does not install software or provision services. A package assignment authorizes its stated local reversible implementation and named network capability. The latest user instruction adds a pre-P4 corpus/budget/provider-selection checkpoint; an existing key is not authorization to bypass it. After that checkpoint, for live paid model calls, use only the user's configured provider and the bounded request/token budget in the assignment/configuration; never invent a dollar ceiling or silently select a paid service. Make a dry-run request/token estimate before the first batch. The call/bundle ceilings in this plan supply the default operational bounds; do not require an additional monetary approval when the user already authorized the configured live run. If no usable provider or enforceable request/token configuration exists, report exactly that; fixture tests remain possible but do not satisfy live acceptance.

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
    project.yaml                   # inputs, scientific metadata, lineage scopes
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
        models.py                  # shared model factory for all three roles
        assembly_schemas.py        # proposal/source-reference contracts
        assembly_tools.py          # bounded read-only corpus tools
        assembly.py                # one evidence-assembly agent and host guards
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
    manuscript/<report_run_id>/    # per-lineage reports plus integrated claim/evidence table
```

**Implementation simplification:** verification lives behind `python -m regkg verify ...`; do not create parallel verification scripts. One implementation per check. No `api/`, UI, or `differential_expression.py` until separately assigned.

### 5.1 Dependencies

Use an available supported Python interpreter (prefer 3.11 or 3.12 if compatible with the selected packages); record the actual choice. No new global Python installation unless needed and assigned.

- Base: `pandas`, `pyarrow`, `pydantic`, `PyYAML`, `httpx`, `lxml`, `scipy`, `neo4j`, `rank-bm25`, `python-dotenv`.
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

### 6.2a Ontology decision — small reviewed context hierarchy

**Decision, 2026-09-22:** include a small versioned context-mapping and cell-type hierarchy layer in P5/P6. This helps group manuscript evidence by epithelial, immune and mesenchymal populations and distinguish broad mechanism evidence from exact experimental context. It is not an OWL-reasoning project and does not block P3 or initial P4 extraction. The current P3 worker assignment is unchanged.

- **Cell Ontology (CL):** review mappings for the four focal populations and their supported parent types; add other observed context labels only when needed for manuscript reports. Retain a small set of source-verified subclass edges needed for roll-up queries. A macrophage-level finding can be displayed as broader context for an alveolar-macrophage question, but cannot become direct alveolar-macrophage evidence by inheritance. A finding in a subtype must retain that subtype even when displayed under its parent.
- **UBERON:** use reviewed identifiers for observed anatomy needed to distinguish lung from non-lung contexts (including alveolar bone). Do not infer experimental tissue merely from an ontology's typical location or an ambiguous word. Full anatomical hierarchy traversal is not required.
- **MONDO:** map IPF and other diseases actually needed to distinguish experimental contexts, where a verified mapping exists. Control is a study condition, not an ontology disease or proof that the donor is universally healthy. A disease ancestor does not make evidence applicable to every subtype.
- **Species and genes:** keep the existing species-qualified records and HGNC/NCBI Gene/Ensembl mappings. HGNC is an identifier/nomenclature resource, not a substitute for context ontologies. Do not map nonhuman findings onto human genes or transfer claims across species automatically.
- **Project states:** retain dataset/run-qualified Niche 1/Niche 2, KRT5−/KRT17+ state qualifiers and fibroblast activation as project/source annotations. Map only a supported parent when no exact ontology class exists; explicitly record broader mapping rather than equivalence. No fabricated ontology class for an algorithm-defined niche, inferred lineage transition, or unknown cell state.

**Implementation/data contract (P5 offline export):** maintain a reviewed `configs/context_mappings.tsv` with local entity/raw label, entity kind, ontology ID/label, mapping relation (`exact` or `broader`), status (`reviewed`, `ambiguous`, `unmapped`), source URL, pinned release/version, and review rationale. Only reviewed mappings enter normalized context queries. Preserve unresolved raw labels and candidate mappings separately; never fill an ID from model memory or a label-only fuzzy match. External IDs supplement existing local IDs and must not invalidate historical observation identities.

Publish a versioned small term table and hierarchy edge table in Parquet with TSV inspection views, plus a JSON resource manifest containing source URLs, versions, retrieval dates, checksums and license/attribution. Cache the supporting release/subset under `data/external/ontologies/` and transfer it with other execution assets. Download a release file only if needed to reproducibly obtain the selected terms/edges; OWL, OBO or another documented release format is an acquisition detail. No mandatory full OWL download/import, automatic import closure, ontology server, reasoner, new NLP model or whole-ontology Neo4j load.

For the selected hierarchy use verified `subClassOf` edges between ontology terms and traverse those in ordinary Python/Cypher. Keep local-to-term mappings distinct from term hierarchy. Do not flatten `part_of`, `located_in`, or `develops_from` into `is_a`, or silently treat OWL restrictions as ordinary subclass edges. Preserve asserted versus publisher-inferred edge provenance if the selected release contains inferred relationships. Export only the selected mapped terms and required ancestor paths, with declared endpoint types and resource versions.

**Evidence boundary:** ontology membership groups labels; it never establishes TF regulation, target expression, disease causation, niche identity, experimental cell identity, or an independent supporting study. Maintain exact-context, broader-context, off-context and unknown-context evidence separately. Do not increase support scores or duplicate study counts merely because one finding appears in several ancestor views. Automatic ontology-based query expansion and semantic-similarity scoring are outside this assignment.

**Acceptance in P5/P6:** validate IDs/labels against the pinned source, obsolete/replacement status, mapping direction, selected-edge endpoint closure and subclass cycles. Test exact versus broader mapping, unknown preservation, the alveolar-bone/lung distinction, no downward propagation of findings, and no duplicated counts after roll-up. Add one report/query comparing direct-context evidence with explicitly labeled broader-context evidence for each manuscript lineage. A missing exact term remains an explicit mapping gap and does not block source-grounded extraction.

GO/Reactome enrichment stays deferred under §15. Preserve pathway terms reported by papers with their sources, but do not infer gene membership, new enrichment or significance from the context hierarchy.

Official references consulted for this decision: [CL](https://obofoundry.org/ontology/cl.html), [CL relation semantics](https://obophenotype.github.io/cell-ontology/relations_guide/), [UBERON](https://obofoundry.org/ontology/uberon.html), [MONDO](https://obofoundry.org/ontology/mondo.html). These are design sources; implementation must pin actual resource versions rather than rely on moving website content.

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

Use YAML for stage/run configuration and root `.env` for the user-selected models, routing, endpoints, and credentials specified in §6.4.2. Resolve these into one configuration and record nonsecret choices for reproducibility. No hidden current-directory dependence.

Required configuration fields:

- `project.yaml`: source paths/roles, dataset/definition-run identifiers, species/tissue, cell-type mappings, k and per-file resolution, lineage-specific manuscript TF seeds/comparisons, numeric tolerances.
- `literature.yaml`: metadata service, contact email if required, max papers/queries/results/passages, retry/timeouts, lexical policy, embeddings enabled/model/revision/encoding settings.
- `extraction.yaml`: `extractor.model` and optional `verifier.model` as qualified model strings, prompt/schema versions, generation settings, per-call timeout, total request/token limits, retry limits, selected source-bundle IDs. An omitted verifier model inherits the extractor model; record both resolved identities.
- `ranking.yaml`: target coverage threshold, component availability policy, weights, RRF k, ties, candidate universe, provisional literature ordering policy.
- `graph.yaml`: allowed endpoint mode, batch size, selected cell type/candidates, per-candidate materialization bounds, selected artifact keys.

Environment names: `NEO4J_URI`, `NEO4J_USERNAME`, `NEO4J_PASSWORD`, `NEO4J_DATABASE`, plus the model settings below. P1 must load root `.env` with `python-dotenv`, without overriding existing process environment; never log the content. The `.env.example` names supported settings, distinguishes required from optional, and contains no working secrets. No generic `API_KEY` or `BASE_URL` shared across providers.

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

**Ollama default:** `OLLAMA_BASE_URL` may be unset for a local server; the current `.env` explicitly sets the same localhost default at the user's request. Resolve an absent/blank value to `http://localhost:11434`; pass a nonblank override explicitly. Use this project's provider-specific env name, not `OLLAMA_HOST` (which configures the server). A connection failure must identify the configured endpoint without installing or starting Ollama automatically. A selected embedding model must already be available or be explicitly downloaded within the assigned setup; no automatic replacement model. If the Python process later runs inside a container, localhost refers to that container and the operator must supply a reachable override. Default server binding reference: [Ollama FAQ](https://docs.ollama.com/faq).

**Generic alternative configuration shapes:** the current user selections and env overrides are in §6.4.2. These examples do not override them.

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

The angle-bracket values are documentation placeholders: reject them as unconfigured before any live call. When no actual selector is supplied from YAML or env, treat extraction as unconfigured. The current selected model is supplied through `LLM_MODEL` in §6.4.2; an empty API key still blocks live calls. `enabled: true` requires a real embedding selector. When embeddings are disabled or pending, use lexical retrieval and report `dense_retrieval=not_configured`. When an enabled backend fails, record an error; a lexical-only continuation requires an explicit configured fallback policy and must record the degraded retrieval mode.

**Worker implementation and acceptance details:**

1. **P1:** parse and validate selectors/config without importing model SDKs, reading weights, opening connections, or requiring any provider key. Preserve the existing `.env.example` and user-owned `.env` from §6.4.2; keep credentials blank in the template and retain the selected nonsecret defaults. Never overwrite a populated user key. Test first-colon parsing with `ollama:ExampleModel:v1`, `openrouter:Org/Model:variant`, and `litellm:Org/Deployment:revision`; all suffixes must survive unchanged. Test alias canonicalization, empty values, unknown providers, and wrong-role rejection.
2. **P3:** create `build_embeddings(config)` behind one query/document encoding interface. Use `embed_query` and `embed_documents`; Sentence Transformers receives only the model suffix as `model_name`, plus selected revision/device and documented encoding kwargs. Keep query/document prefixes, normalization, batching, and token limits faithful to the selected model. Validate finite vectors, equal nonzero dimensions, and compatible query/document spaces. Both backend branches get offline wiring checks; only the user's selected backend needs a bounded live smoke run. Do not install/test both model stacks to satisfy one run.
3. **P4:** create `build_chat_model(model_spec, settings)` with three explicit lazy-import branches. Pass only the suffix as the provider's model name, except LiteLLM's internal proxy prefix above. Validate only selected roles' keys and LiteLLM URL immediately before constructing/calling their clients. Missing optional extras identify the exact installation extra. Config validation and `--help` remain usable with no keys. No silent provider failover, fallback paid model, router, or automatic model selection.
4. **Structured output:** use the integration's supported `with_structured_output` mode for the selected model and pinned package; capability is model-dependent. Record the configured mode and reject incompatible settings with a clear setup error. Do not silently replace validated structured output with permissive JSON parsing. Run one small schema smoke check on selected model configurations before a batch; count it and retries against the run's total request/token limits. Share the single budget across extractor, verifier, and SDK retries, preventing nested retries from bypassing it. No requirement to make live calls to all three providers.
5. **Reproducibility:** manifests/cache identity include canonical selectors for each role, available resolved model version/revision, nonsecret endpoint identity, generation/encoding settings, schema/prompt versions, and source/chunk hashes. For Ollama, record a model digest if exposed; for hosted aliases, record returned identity and leave unavailable revisions unknown. Changing embedding model, revision, dimension, prompts, or normalization rebuilds its index; do not mix cached spaces. Credentials never enter a manifest, cache key, exception dump, or transport fixture.
6. **Focused checks:** verify all three chat constructor mappings, LiteLLM proxy target/auth forwarding using dummy credentials, default/overridden Ollama URLs, Sentence Transformers model-name/revision forwarding, unselected-provider independence, and missing-extra errors. Test configured embedding failure vs deliberately disabled embeddings. Verify budgets/cache replay and preserve raw/parsed model results. Live handoff reports exactly the selected backends exercised; stub wiring checks do not imply live provider validation.

Use nonsecret HTTP(S) URLs without embedded user/password/token parameters; credentials travel through their dedicated SDK fields. Keep optional embedding dependencies unloaded during ingestion, graph operations, and lexical-only retrieval. Provider factories must remain small ordinary functions, with no new framework or service.

### 6.4.2 Current `.env` selections and OpenRouter routing

The user selected these values after the generic adapter design. Root `.env.example` is the tracked template; root `.env` is ignored and the user has supplied its API key; the template key remains blank. The application/configuration reader is not yet implemented. Separate direct-API smoke checks are recorded below; they do not complete P3/P4 acceptance.

```dotenv
LLM_MODEL=openrouter:z-ai/glm-5.3-flash
OPENROUTER_API_KEY=
OPENROUTER_REASONING=low
OPENROUTER_PROVIDER_SORT=latency
OPENROUTER_PROVIDER_ORDER=morph,deepinfra,together,baseten,coreweave
OPENROUTER_MAX_PRICE_INPUT=0.15
OPENROUTER_MAX_PRICE_OUTPUT=0.50
EMBEDDINGS_ENABLED=true
EMBEDDING_MODEL=ollama:pankajrajdeo/biomed-embeddings-16l-fp16:latest
OLLAMA_BASE_URL=http://localhost:11434
```

**GLM reasoning compatibility:** a live request with the inherited `none` setting returned HTTP 400: reasoning is mandatory. Set `OPENROUTER_REASONING=low` explicitly; retain bounded completion tokens (including reasoning). Do not let an omitted setting select the model's potentially larger default reasoning budget.

**GLM routing selection (2026-09-22 UTC):** `morph → deepinfra → together → baseten → coreweave`, using verified endpoint base slugs. Morph leads for its discounted $0.08/$0.28 input/output per million tokens and the supplied 1.51 s / 20 tokens/s snapshot. DeepInfra offers $0.075/$0.25 but lower throughput in that snapshot. Together, Baseten, and CoreWeave provide faster fallbacks at $0.15/$0.50. This is a practical preference order, not a benchmark optimum. Discounts may expire; never apply their percentage twice to already-discounted API prices. Account-wide effective/cache-hit averages do not predict our new workload's cost. GMICloud and Relace do not advertise `structured_outputs` in the inspected endpoint metadata and each returned HTTP 404 (no eligible endpoints) in a pinned strict-schema check, so they are not initial strict-schema preferences; Open Inference's supplied uptime was weaker. Current prices/capabilities were checked through the [model endpoints API](https://openrouter.ai/api/v1/models/z-ai/glm-5.3-flash/endpoints); timing comparisons above are from the user's snapshot, since the API returned null latency/throughput metrics. Recheck on material pricing/availability changes, not per passage.

**Price guard for P4:** parse `OPENROUTER_MAX_PRICE_INPUT` and `OPENROUTER_MAX_PRICE_OUTPUT` as finite nonnegative decimal USD per million tokens. Map supplied values directly to `openrouter_provider.max_price.prompt` and `.completion`; do not divide these ceilings by one million. Current values are 0.15 and 0.50. Apply them to ordered and fallback routing, retaining `require_parameters=true`. These are per-token-rate ceilings, not a total-spend budget; existing request/output/retry limits still apply. If no eligible endpoint fits, report failure without relaxing the ceiling. Keep returned host, actual usage/cost, and requested routing in sanitized run records. Add offline payload tests for units, invalid values, and routing/ceiling coexistence.

**Direct-API smoke results (2026-09-22 UTC):** Ollama returned three finite, nonzero 384-dimensional unit-normalized vectors; duplicate inputs matched exactly, digest `b97df00ac434eaf8aba134f66fe50cd132ea88fcc2d75cdd1a75c7e74b6b5779`. With GLM reasoning `low`, synthetic extraction passed via Together (0.60 s) and verification passed via Morph (3.58 s), preserving a null finding and rejecting an unsupported direct-activation claim. A separate pinned DeepInfra schema check passed (2.97 s). These are single-request timings, not a latency benchmark or biological validation. The three successful GLM requests reported $0.000101675 combined cost; compatibility failures are recorded separately, without assuming their billing. Reports are local ignored artifacts under `data/model_checks/`; the original combined embedding/DeepSeek report remains under `data/runs/model-smoke-20260922T011823Z/`. Current LangChain adapters remain unimplemented and must be checked in their assigned packages. No implementation checkbox is accepted by these setup checks.

**Resolution rules for P1:** load `.env` relative to the repository/config root using `python-dotenv` with interpolation disabled; never execute it as shell code. Actual process env takes precedence over the file, including explicitly empty values. Nonblank `LLM_MODEL` overrides `extraction.yaml`'s `extractor.model`; `verifier.model`, when explicitly configured in YAML, retains its override, otherwise inherits the resolved extractor. Nonblank `EMBEDDING_MODEL` overrides `literature.yaml`'s `embeddings.model`. Explicit `EMBEDDINGS_ENABLED` overrides YAML and must parse strictly as `true` or `false`; absent means use YAML's setting, default false. Parse every resolved selector through §6.4.1. `LLM_MODEL` is one model selector in this project, not NeoXplorer's comma-separated model fallback list. Empty optional model overrides use YAML; an empty required key remains missing. Persist the resolved nonsecret configuration in each relevant manifest/cache key; no secret values or hashes of credentials.

**Both roles, OpenRouter only:** construct extractor and verifier through the same `build_chat_model` factory. For each role independently, apply the shared order `morph → deepinfra → together → baseten → coreweave`, reasoning setting, schema requirements, and price ceilings only when its resolved provider token is `openrouter`. There is no verifier-specific order or role-specific latency preference. Both direct-API smoke calls used the same routing object; their different serving hosts reflect fallback/availability, not different settings. Check OpenRouter-specific env fields only when at least one role uses OpenRouter. A LiteLLM or Groq role must neither require nor validate those fields nor receive `openrouter_provider`, OpenRouter `reasoning`, host order/sort, or OpenRouter price ceilings. This applies even if a LiteLLM proxy internally routes to OpenRouter: proxy-side routing belongs to that gateway, not this application's OpenRouter adapter. Shared request/token budgets, timeouts, and schema validation still apply to all providers. If the verifier uses another provider, only the extractor gets these OpenRouter controls, and vice versa. Add captured-request checks for both OpenRouter roles and mixed-provider pairs, proving no OpenRouter fields leak into other SDK requests.

**OpenRouter behavior for P4:** adapt the configuration mapping inspected in NeoXplorer's `services/neoxplorer/src/neoxplorer/models.py`, `tests/test_models.py`, and `docs/operations/copilot.md`. Do not import that application's code or access its `.env`.

- Map `OPENROUTER_REASONING=low` to `ChatOpenRouter(reasoning={"effort": "low"})`. Confirm acceptance by the chosen model/host in the bounded P4 schema check; do not silently change reasoning effort when unsupported.
- Split `OPENROUTER_PROVIDER_ORDER` on commas, trim each entry, and retain the user's order and names. When nonempty, pass `openrouter_provider={"order": [...], "allow_fallbacks": true}` and **omit `sort`**. When empty and a sort is configured, pass `openrouter_provider={"sort": "latency"}` for the current selection. Validate sort against `price`, `throughput`, and `latency`; blank leaves routing unspecified. Validate names against the selected model's available provider identifiers during P4 preflight; report unmatched preferences without substituting guessed identifiers.
- Here provider fallback means OpenRouter host fallback for the **same selected model**, including eligible hosts outside the preference list that meet the configured price ceilings and parameter requirements. It is not permission to switch the model or switch the application's provider to Groq/LiteLLM. Record returned serving-host identity where available.
- For both structured extraction and verification, add `require_parameters=true` to the provider object so a host cannot silently ignore the requested structured-output parameters. Prove the emitted request retains routing, reasoning, schema mode, and the exact model ID using a captured offline request. If no eligible endpoint supports them, report the incompatibility rather than accepting unvalidated output.
- Reuse the principle of explicit SDK timeout/retry controls from NeoXplorer, checking units and retry behavior against this project's pinned `langchain-openrouter`/OpenRouter SDK versions. Do not copy its copilot token limits, model fallbacks, or TLS configuration wholesale. Count SDK attempts within our existing bounded call budget.

Routing and parameter support: [OpenRouter provider selection](https://openrouter.ai/docs/guides/routing/provider-selection). Reasoning controls: [OpenRouter reasoning tokens](https://openrouter.ai/docs/guides/best-practices/reasoning-tokens). The explicit-order-over-sort choice is the inherited application policy.

**Ollama behavior for P3:** use the server root `http://localhost:11434` with `OllamaEmbeddings`; do not append `/api` or `/v1` to `base_url`. The adapter selects its API path. Send the complete suffix `pankajrajdeo/biomed-embeddings-16l-fp16:latest` as its model. The user reports this model already installed (84 MB, short ID `b97df00ac434`); verify the actual available digest and metadata during P3 instead of treating that report as a live check. Determine vector dimension/token limits and any required query/document prefixes from this model's metadata/documentation, not its name or an assumed generic biomedical model. No download or inference call is required to create the env files. [Ollama API introduction](https://docs.ollama.com/api/introduction)

**Focused acceptance additions:** P1 checks `.env`/process/YAML precedence, quoted provider names with spaces, strict booleans, exact Ollama tag preservation, and missing-key handling without printing secrets. P4 checks order-vs-sort payloads, same-model host fallback, reasoning `low`, and schema parameter enforcement. P3 exercises only the selected local embeddings and preserves the existing configured-failure/lexical-fallback distinction. These extend existing tasks, not new work packages.

### 6.4.3 Bounded evidence-assembly agent — design amendment, 2026-09-22

Use [the complete agent contract](docs/assignments/P4-evidence-assembly-agent.md): one local LangChain `create_agent` with six read-only corpus tools, strict structured proposals, host source validation, durable budgets and human-review records. This supersedes the old blanket no-agent rule only for context assembly. LangGraph is used internally by `create_agent`; no custom graph/service, Deep Agents, subagents, arbitrary code execution or agent graph writes are required.

`ASSEMBLER_MODEL` is an optional qualified selector and otherwise inherits the resolved extractor. Pass the shared factory's initialized model to the agent. Apply OpenRouter-only routing/credential fields to any OpenRouter role, including assembly; never leak them to LiteLLM/Groq. Earlier two-role smoke checks do not validate the agent's tool/structured-output compatibility. Validate it in P4 within the selected provider budget. Do not change current credentials or call a model as part of planning.

P3 remains free of chat calls. Freeze acquired/parsed source artifacts and reviewed dispositions, ready bundles, plus an explicit investigation queue for context questions answerable within those sources. Investigation items are not ready evidence. Missing files, parse/identity failures and new-analysis requests still need P3 repair/disposition. P4 assembly emits new immutable bundles over the frozen source set, validated before extraction; it cannot mutate the P3 readiness manifest or approve its own source interpretation.

Initial assembly ceilings: four model attempts and eight tool attempts per investigation, retained across retries/resumes; at most 20 investigations per batch. Budget token/cost/runtime limits as specified in the contract, separately from the existing 40 scheduled extractor/verifier calls. The illustrative worst case is 80 assembly attempts plus 40 scheduled extraction/verification calls, before separately budgeted extraction retries/preflight. No automatic increase to a user's approved spend/call cap. P3's report must include this additional role and P4 must dry-run the selected model's actual payloads.

### 6.5 CLI contract

Use `argparse` with one entry point: `.venv/bin/python -m regkg`. Implement each command in its owning package; pending commands must not silently claim success.

```text
regkg ingest --config configs/project.yaml
regkg verify project-data --run <ingest_key>
regkg candidates --run <ingest_key> --cell-type "<cell_type>"
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
regkg nominate --project-run <ingest_key> --candidate-run <candidate_key> --evidence-run <extraction_key> --cell-type "<cell_type>"
regkg report --run <nomination_key>
regkg verify report --run <report_key>
regkg run-manuscript --config configs/project.yaml --resume
```

Commands print concise artifact IDs, relative output locations, counts, and status. They return nonzero for invalid input or failed required stages. A command with honest partial coverage must say `PARTIAL` and list reasons; never silently report full success. `<...>` above are placeholders copied from actual command output, not literal arguments.

### 6.6 Initial evidence/ranking rules a worker must not invent

These are transparent **provisional implementation rules**, retained in configuration and reports. They are not calibrated biological confidence estimates.

**Eligible positive experimental support:** an AUTO_ACCEPTED primary finding with resolved individual-gene TF/target, checked source spans, an explicit assay, and SUPPORTS polarity relative to the target claim. Binding, perturbation, reporter, or CRE-perturbation findings retain their actual directness. Computational/association/prior-database records alone are not primary experimental support. A prior with a PMID still requires a retrieved source-grounded finding for that role.

**Context ordering for a nomination in its requested manuscript lineage:**

| Match | Default rule |
|---|---|
| EXACT | Explicit matching species, lung focal cell type, requested experimental condition, and compatible primary/native context |
| CLOSE | Compatible human lung lineage with broader cell annotation or unspecified condition; e.g. alveolar epithelium for AT1 or broader macrophages for alveolar macrophages; retain differences and unknowns |
| PARTIAL | Explicit relevant mouse counterpart or human lung cell model with known differences; an explicitly different condition/model system cannot be called exact |
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

- [x] **P1.1 Environment audit and bootstrap.** Inspect directory/Git/environment and available Python. Create `.venv` if absent. Create package metadata and minimal CLI. Declare/pin verified base/test dependencies. Record actual versions and lock strategy. Add ignores for `.env`, `.venv`, generated data, caches, large model assets, and `.DS_Store`; keep `.env.example` visible.
- [x] **P1.2 Configuration and small contracts.** Implement the records/enums required by ingestion, config validation, canonical IDs, source hashes, and manifests. Reject unknown config fields that would otherwise be ignored. Implement source-path resolution against project config/repository location. Implement the shared `provider:model_name` parser, role allowlists, unconfigured model states, and `.env.example` contract in §6.4.1; test them without SDK imports, network, weights, or credentials.
- [x] **P1.3 Source audit.** Read headers/delimiters, count rows, check duplicate keys, finite numeric values, and source hashes. Write `source_inventory.json` and a human-readable audit. If duplicate semantic source keys exist, report them; do not silently drop/average them.
- [x] **P1.4 Context/niche normalization.** Implement anchored suffix parsing and raw/display mapping. Produce `contexts.parquet`, `cell_types.parquet`, and `niche_states.parquet`. Observations with no niche remain null. Eight niche-state identities are expected for the four focal types; Control/IPF must not double their identity count.
- [x] **P1.5 Gene mapping boundary.** Produce the exact source-symbol inventory and species-qualified stable local IDs. Populate external canonical IDs only from a documented supplied/cached mapping; otherwise mark `unresolved_external_id`, without inventing HGNC IDs. P2 can enrich these IDs without changing existing observation identities. Do not force all pseudobulk features to be protein-coding genes or discard unrecognized symbols.
- [x] **P1.6 ChromLinker parser.** Melt wide to long in bounded chunks; preserve every source value, all raw labels, and null niche/context membership. Output `chromlinker_observations.parquet` (partitioned dataset acceptable). Add `score_semantics_status=unconfirmed`. No exponentiation, zero filtering, biological rank, aggregate score, or inferred truth edges.
- [x] **P1.7 Pseudobulk parser.** Stream/chunk melt to `expression_observations.parquet`, preserving CPTT values and labels. Prevent oversized all-in-memory lists and per-row Pydantic processing. No normalization or DE calculation.
- [x] **P1.8 Neighborhood parser.** Parse each file's focal type/resolution through explicit config. Emit `neighborhood_profiles.parquet` long rows with original counts and count/25 fractions. Check each row sum within `1e-6`; preserve source column sets; do not fill unreported neighbor categories with measured zeros.
- [x] **P1.9 Signature parser.** Rename fields only via an explicit map, retain effect-definition text, and output `niche_expression_signatures.parquet`. Verify effect equals mean2-minus-mean1 (`abs_tol=1e-8`, `rel_tol=1e-6`), fractions [0,1], nonnegative integer cell counts, uniqueness by dataset/cell-type/condition/comparison/gene, and per-group cell-count consistency. No significance labels.
- [x] **P1.10 Joins and sampling metadata.** Verify the 45-context overlap, expected missing niche contexts, 8 signature groups, and available gene overlap. Unmatched genes are counted and preserved, never inner-joined away. Export sampling coverage with donor fields null.
- [x] **P1.11 Reproducible artifact commit.** Write tables and manifest atomically. A second identical execution reuses or verifies the existing artifact; it must not append duplicate rows. Execution timestamps may differ; semantic IDs/counts/measurement content must match.
- [x] **P1.12 Tests, README, and handoff.** Cover parsing underscores/non-niche labels, cross-condition shared niche identity, zero vs missing, signature units/effect, absent neighbor category, duplicate-key failure, and replay. Record real input counts and output sizes; stop for review.

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

## 8. P2 — Manuscript candidates, one curated prior, and retrieval queues

**Goal:** deterministic candidate sets and bounded literature queues for all four manuscript regulatory cases, with two candidate routes. The checked P2.1–P2.10 items below document the accepted AT1 baseline only; the P2.11–P2.13 extension is separately accepted in [its review](docs/reviews/P2-manuscript.md). Start with one prior source, CollecTRI; adapters for TRRUST/hTFtarget/KnockTF are later extensions, not prerequisites.

**Allowed writes:** identifier enrichment, `analysis/priors.py`, `candidates.py`, `concordance.py`, candidate CLI, `configs/literature.yaml`, `ranking.yaml`, needed dependency extra/lock changes, P2 tests/artifacts/handoff. Shared contract additions must be small and backwards compatible; report changes explicitly.

### P2 execution order

- [x] **P2.1 Resolve gene identities.** Acquire/cache a documented official human gene mapping snapshot using appropriate source access. Normalize exact stable IDs/approved symbols first; resolve aliases only if unambiguous and species-consistent. Preserve mappings/rejected candidates and original symbols. Never merge two source features solely because a fuzzy string match is close.
- [x] **P2.2 Import advisor metadata.** Read the two selected-paper CSVs; deduplicate PMID identity to 110 expected unique papers while retaining both resource memberships and annotations. Write `seed_publications.parquet`. The existing prose about evidence does not become accepted scientific findings.
- [x] **P2.3 Acquire CollecTRI.** Use the pinned official decoupler/OmniPath integration or a documented resource export; verify the installed API. Cache raw response, retrieval timestamp, version/license metadata, PMIDs/signs/complexes. Produce `prior_interactions.parquet`. Do not silently split a complex into individually supported TFs. Unknown sign stays unknown; contradictory signs remain traceable, not randomly deduplicated.
- [x] **P2.4 Define AT1 comparison objects.** Build Control and IPF Niche2-vs-Niche1 comparisons. For each, retain the complete signed vector; Niche2 is the case/target and Niche1 is the reference. An optional opposite-niche view negates the contrast and must be labelled as a view of the same comparison, not an independent analysis. Do not label either vector as DE. Do not merge Control/IPF contrasts.
- [x] **P2.5 Signed-regulon baseline.** Call decoupler ULM through the pinned public API on resolved, finite gene-level contrast values and signed prior weights. Default minimum mapped targets is 5, explicitly an engineering/coverage setting. Unresolved duplicated mappings are excluded from this calculation with counts; do not average them silently. Preserve prior-universe size, observed targets, eligibility/filter rules, raw ULM score, sign, and method version. Omit donor-level significance claims; method p-values, if retained at all, are labeled method-specific and not used as DE FDR.
- [x] **P2.6 Candidate union.** Include the five named TF seeds regardless of score. Add at most 5 additional individual-gene TFs per condition from the largest absolute concordance scores meeting coverage rules; stable TF-ID order breaks ties. Preserve concordance sign separately so an inverse pattern is not called increased activity. A TF from several routes gets one candidate identity plus multiple reasons. The first report uses one Niche2-versus-Niche1 comparison per condition, showing both niches and concordance sign. Do not duplicate independent-evidence counts for an optional reversed view, or pretend a score sign measures causal activity.
- [x] **P2.7 Project evidence for candidates.** Attach supplied ChromLinker target observations and TF/target expression support. Keep numeric distributions/target row counts descriptive. Connectivity rank and interpreted delta remain null while semantics are unconfirmed. The manuscript seed order must not masquerade as a scientific ranking.
- [x] **P2.8 Select bounded target searches.** For each TF, choose up to 3 resolved target genes that overlap its prior/project target lists and have the largest absolute descriptive AT1 signature effects (gene ID breaks ties). Selection is for retrieval coverage only, not a biological ranking. Preserve source route and effect. If none are eligible, retain TF-only queries; do not invent targets.
- [x] **P2.9 Build reproducible query rows.** Emit `retrieval_queue.parquet` with query ID, candidate/comparison/target, query text/type, priority, reason, source route, and version. Generate TF + target + regulatory-assay terms and TF + lung/alveolar/fibrosis queries, using exact approved names and safe aliases. Include negative/null phrasing where helpful; do not require positive regulation terms for every query. Do not restrict all searches to 2015 onward. Bound live execution to a small deterministic queue slice (initially at most 20 queries); all unexecuted rows remain `NOT_SEARCHED`.
- [x] **P2.10 Verify and hand off.** Test ambiguous alias exclusion, complex preservation, deterministic seed inclusion/top-k/ties, target coverage, unknown connectivity semantics, repeated source provenance, and repeatable queues. Report which real prior/mapping services worked, dataset versions, candidate counts, and unmapped genes.

### P2 accepted AT1 baseline commands and evidence

```bash
.venv/bin/python -m pip check
.venv/bin/python -m pytest tests/test_candidates.py -q
.venv/bin/python -m regkg candidates --run <ingest_key> --cell-type AT1
.venv/bin/python -m regkg verify candidates --run <candidate_key>
```

`verify candidates` must show the five seeds for each AT1 comparison, no interpreted ChromLinker rank under unconfirmed semantics, target/identifier coverage, reproducible query ordering, and source-linked prior records.

**Review gate:** two candidate routes exist on actual inputs. If the prior API is unavailable, submit partial work; five hard-coded seeds plus fixtures alone do not satisfy the prior-analysis item. A missing embedding model does not block this package.

### P2 manuscript-scope extension — required before expanded retrieval

Follow [docs/manuscript_scope.md](docs/manuscript_scope.md). Preserve accepted baseline artifacts and checkmarks as historical evidence. The extension is now separately accepted: `mcandidates-c278c6625ff7c537`; see [review](docs/reviews/P2-manuscript.md).

- [x] **P2.11 Scope/config migration.** Replace AT1-only operational assumptions with explicit lineage-specific seeds and six primary comparisons. Preserve all P1 input observations, absent Control niche regulatory contexts, stable gene identities, and reproducibility of the original baseline. Version scope changes; do not require global re-ingestion solely to change candidate scope.
- [x] **P2.12 Candidates and queues for every manuscript case.** Reuse the current prior/resolver/concordance logic with each lineage’s actual signature and project contexts. Emit per-lineage/comparison candidates, targets, and queries with a reconciled manuscript manifest. Keep shared TF identity distinct from nomination context; preserve seed-only and no-target cases. Use bounded additional candidates and fair resumable batch scheduling across all lineages.
- [x] **P2.13 Review the extension.** Test six primary comparisons, all named TF memberships, cross-lineage isolation, shared TEAD1/KLF5 identities, missing Control regulatory contexts, sparse results, and replay. Submit a separate extension handoff; only the lead accepts it. Whole-advisor metadata audit can proceed independently; new manuscript-specific P3 retrieval requires this reviewed manifest.

## 9. P3 — Bounded real literature processing and passage retrieval

**Goal:** account for all advisor papers, acquire/parse available content, produce a complete actionable download list, and prepare inspectable evidence bundles in batches of at most 10 papers. Coverage does not require every paper to supply a regulatory finding. This is a practical literature service, not an NLP research project.

**Allowed writes:** `literature/`, `workflows/literature.py`, literature CLI/config, optional dependency declarations, P3 tests, ignored paper/run caches, P3 handoff. No extraction/graph truth writes yet.

### P3 implementation starting point — adapt the supplied search tool

**Decision:** reuse and simplify `reference/literature_search_tool.py` as the starting point for `src/regkg/literature/search.py`. Preserve the reference file unchanged. Do this during P3, not during the ongoing P1 assignment. Prefer targeted adaptation of suitable code over an unrelated replacement, but do not preserve broken dependencies merely to minimize the diff.

**Dependency boundary:** the supplied file is a 269-line wrapper. It imports `StandardSearch`, `sources`, `agent_payload`, `tls`, and tracing from `lungchat.infrastructure`; those backend implementations are not included with this reference. Copying/renaming the wrapper alone will not produce a working search service. Inventory those dependencies first. If their source is subsequently supplied, inspect and reuse suitable pieces; otherwise implement only the missing bounded HTTP source adapters against the public APIs. Do not install an unrelated `lungchat` package, create a compatibility package with that name, or claim the original retrieval/ranking engine has been reused when it is unavailable.

Adaptation checklist within the existing P3 tasks:

1. Copy the reference into the planned `search.py` destination, then remove the Research Agent framing, `@tool` decorators, tool alias, and `langchain_core.tools` dependency. Merge the redundant search wrapper/core layers into an ordinary typed `search_papers` entry point used by the existing CLI/workflow. Return structured records; serialize at artifact/CLI boundaries.
2. Retain useful source labels, bounded-result validation, explicit error classifications, publication metadata, and identifier parsing. Move/adapt the `get_paper_details` responsibility into the already-planned `fetch.py`; share the publication resolver from P3.2. No duplicate search/fetch implementations or separate agent payload service.
3. Remove `_reranker_name`, `_build_reranker`, MedCPT imports, `LITERATURE_RERANKER`, and reranker-specific warnings. Do not replace them with another cross-encoder or LLM reranking step. Exact-match/metadata paper selection remains P3.3; exact identifiers, BM25, and the selected biomedical embeddings rank passages in P3.8/P3.9. Combining those retrieval lists is still ranking; it does not require a second neural model.
4. Replace `lungchat` trace/session/TLS dependencies with this project's manifests, explicit source statuses, and shared HTTP handling. Use the existing `httpx` dependency rather than adding `aiohttp` just to retain the wrapper's client type. Preserve certificate verification and use bounded per-service requests, timeouts, backoff, and `Retry-After`. No source requests, model loading, or network preflight at import time.
5. Preserve warnings and per-source coverage on success, partial success, empty results, and failures. Correct the original non-success branch, which drops its warnings. Distinguish definitive identifier-not-found from a failed details request; neither partial source failure nor timeout is evidence that relevant literature does not exist. Pass trace/status data explicitly rather than relying on unavailable global tracing state.
6. Replace chat-oriented defaults and comments (such as always returning five papers, fixed hidden retrieval depth, and returning only abstract snippets) with this plan's explicit search, source-page, corpus, and bundle bounds. Validate limits in the core function, not only a tool wrapper. Keep full metadata/abstracts and raw responses in cached artifacts; compact snippets/bundles are downstream views with source locators.
7. Keep date, publication-type, species, and preprint controls only where their semantics are implemented and tested for each source. Do not blindly send the wrapper's literal tokens to every API. Defaults must not impose a new date window or MeSH-only species restriction. Use the P2 query variants rather than requiring every concept to appear in every search result. Preserve indexed/unknown species separately from explicitly incompatible species.
8. Reuse one publication identity across PubMed and Europe PMC memberships, retaining source provenance. Use PubTator primarily for existing annotations in P3.7; its predicted relations remain discovery/normalization aids, not accepted regulatory evidence. Adding PubTator relation search is optional and must stay within the same retrieval budget.
9. In P3, support optional `NCBI_API_KEY`, user-supplied `NCBI_EMAIL`, and `NCBI_TOOL=spatial-niche-regulatory-kg` for E-utilities. Keep credentials out of URLs recorded in logs/manifests and send the key only to its intended API. Do not require Europe PMC or PubTator API keys for their public endpoints, and do not apply E-utilities key-based rate allowances to those separate services. Validate current service policies when implementing their adapters. Preserve the existing `.env` when adding optional placeholders to the example/configuration.
10. Update module/function comments to describe the resulting KG pipeline, removing references to unavailable ADRs, agent tools, evaluation harnesses, and fixed neural ranking. Record the reference checksum and which pieces were retained, removed, or implemented to replace missing dependencies in `docs/handoffs/P3.md`.

**Focused acceptance:** importing and running search must not require `lungchat`, a chat-model SDK/key, or MedCPT weights. Verify core limit validation, identifier resolution, source deduplication, genuine empty results, one-source failure with surviving results/warnings, all-source failure, details-fetch failure vs not-found, caching, and preservation of source locators. Complete the original P3 real-source checks as well; reference adaptation alone is not P3 completion. No additional package/review gate is introduced.

### P3 execution order

- [ ] **P3.1 Adapt the reference search entry point and complete source adapters.** Follow the adaptation checklist above, starting from `reference/literature_search_tool.py` and producing `src/regkg/literature/search.py`. Use documented PubMed/Europe PMC APIs and implement only missing backend behavior. Execute at most 20 queued queries per assigned batch with up to 10 metadata results per query, caching the query response and timestamp. Bound network retries (e.g. 2 retries with backoff and `Retry-After`) and timeouts. Store per-query executed/error/unexecuted status. Avoid unbounded citation expansion.
- [ ] **P3.2 Publication resolution/deduplication.** Merge PMID/PMCID/DOI aliases only when verified, preserve query/resource memberships, normalize DOI case/prefix, and prevent duplicate fetches. Capture available correction/retraction metadata. Never combine preprint/published versions merely on a similar title without explicit identity evidence.
- [ ] **P3.3 Account for the whole advisor corpus and select batches.** Every advisor PMID enters the coverage ledger and acquisition/screening route, independent of candidate-name matches in title/abstract. Preserve all memberships and resolve source overlap by publication identity. Separate primary evidence, biological context, resource/method background, and other-context material with documented reasons and uncertain cases. Select at most 10 papers per ready batch; additional search results cannot displace mandatory advisor coverage. All manuscript TF/lineage memberships remain visible across batches; regulator, lineage/comparison, and advisor-paper coverage are separate metrics.
- [ ] **P3.4 Fetch eligible assets.** XML/BioC first; store metadata, abstract, access/reuse status, URL, timestamp, checksum, and raw asset. If eligible full text is unavailable, retain abstract-only status. Download only supplied/authorized PDFs. Respect API terms/limits; no access bypass. Preserve failures without labelling them absence of biology.
- [ ] **P3.5 Parse the canonical document.** Produce `document.json`, `sections.jsonl`, `figure_captions.jsonl`, and table rows with section/item IDs. Maintain exact canonical text plus stable offsets and original XML location. XML parsing disables external entity/network resolution. Captions are included; no figure pixel inference. Preserve table headers/footnotes and supplementary asset identity.
- [ ] **P3.6 Local PDFs and required supplements.** Implement manual intake and Docling behind the same document contract, retaining source hashes and page/item provenance. Bound OCR/pages/resources; inspect real PDF output when available. Inventory supplements, parse accessible PDFs and relevant supplied CSV/TSV/XLSX tables with source coordinates, and record unsupported or missing assets. Essential missing context blocks its bundle. PDF fixtures alone do not establish live PDF readiness; see the linked extension for exact requirements.
- [ ] **P3.7 Normalize passage entities.** Reuse gene mappings and PubTator annotations when available, with species and original mention retained. Check alignment of PubTator spans to the canonical text; if text versions differ, preserve the external offsets separately and rematch/verify exact text. No blind offset copying or fuzzy automatic identity acceptance.
- [ ] **P3.8 Lexical retrieval.** Build exact alias/identifier hits and BM25 over section-aware paragraphs/captions/table descriptions. Rank per candidate query with stable ties, preserving raw retrieval scores/reasons. Do not treat an assay term or entity co-occurrence as an accepted edge.
- [ ] **P3.9 Lightweight embedding adapters.** Implement both Ollama and Sentence Transformers branches behind the interface in §6.4.1, selected through `embeddings.model`. Default Ollama to localhost port 11434 without an env setting; honor `OLLAMA_BASE_URL` overrides. Add focused offline wiring checks for both branches. If the user has supplied a model, exercise that backend, follow its actual pooling/token limits and query/document encoding, and make a bounded local index; record revision/chunk hashes and vector dimensions. Merge lexical and semantic candidate lists while retaining exact hits. If model is pending, emit `dense_retrieval=not_configured` and proceed with lexical retrieval; a configured failure is a different status. No automatic model shopping, training, cross-encoder, or separate vector service.
- [ ] **P3.10 Assemble bounded bundles.** Select at most 20 bundles per batch, with per-paper/per-candidate limits recorded and a resumable remaining-work queue across the corpus. Start with the result passage, adding at most necessary adjacent context or a linked caption/table/methods passage from the same publication. Suggested default is 3 passages and 6,000 characters per bundle, subordinate to the provider's token limit. Do not split away negation, comparison groups, or a required table header. Prefer marking insufficient context over silent truncation.
- [ ] **P3.11 Coverage and caches.** Distinguish NOT_SEARCHED, SEARCHED_NO_SUPPORT_FOUND, ABSTRACT_ONLY, FULL_TEXT_PROCESSED, FETCH_FAILED, PARSE_FAILED, and NO_CANDIDATE_PASSAGES. The search-level label means no support found in the performed retrieval, not a biological negative. Cache successful stages using source/config hashes; retry failures without duplicating successes.
- [ ] **P3.12 Verify/handoff.** Inspect a small real sample of returned bundles, checking gene identity, section, source text, and locators. Include at least one actual source-backed evidence candidate if available; report honestly if none are found. Tests cover deduplication, external text offset mismatch, valid zero-result search, timeout status, XML safety, and bounded bundle construction, plus the adaptation acceptance checks above. Document reused reference code, removed agent/reranker dependencies, and the missing source-adapter behavior implemented locally.

### P3 commands and evidence

```bash
.venv/bin/python -m pytest tests/test_literature.py -q
.venv/bin/python -m regkg literature search --run <candidate_key> --max-papers 10
.venv/bin/python -m regkg literature fetch --run <search_key>
.venv/bin/python -m regkg literature retrieve --run <parsed_key>
.venv/bin/python -m regkg verify literature --run <retrieval_key>
```

Handoff: chosen paper list with identifiers/access/source status, query execution counts, actual downloaded/parsed counts, source hashes, retrieval mode, bundle IDs with several short exact examples, and optional branch dispositions. Do not copy entire papers into a handoff.

**Review gate:** R1–R4 repairs and the corpus-readiness checklist below are reviewed. All advisor IDs/memberships are reconciled; acquisition failures, manual downloads, parser limitations, and ready/pending batches are visible. Each proposed live P4 batch has verified source locators and sufficient context. Implementation/batch readiness is distinct from complete corpus processing. NLP retrieval benchmarking is not required.

### P3 corpus-readiness extension — user instruction of 2026-09-22

The [worker specification](docs/assignments/P3-corpus-readiness.md) is part of this plan and supersedes the old whole-corpus 10-paper cap and PDF deferral. Keep the original repair evidence separate from this expanded coverage work. The [file-readiness specification](docs/assignments/P3-file-readiness.md) adds format-specific edge cases, supported library choices, scientific interpretation and numerical validation requirements. Implement required formats against actual sources; record unsupported assets rather than building a universal parser. Parsing success does not imply extraction readiness.

- [ ] **P3.13 Advisor coverage and relevance routing.** Reconcile all advisor IDs/memberships; screen every paper and keep primary evidence, contextual studies, resource/method papers, and other-context findings distinguishable. No automatic exclusion from title/abstract TF absence and no automatic promotion of advisor annotations into facts. Lead-review background/no-eligible-bundle dispositions.
- [ ] **P3.14 Full-text audit and download list.** Audit the fixed advisor corpus; publish `advisor_coverage.parquet/.csv` and `manual_downloads.csv/.md` with titles, identifiers, verified landing/asset links, missing article/supplement items, expected filenames, priority/reason, and current status. Separate system failures from user-download needs. Publish this before waiting for PDFs. Prioritize evidence required by the manuscript’s four regulatory cases over optional background assets; no lineage gets automatic priority.
- [ ] **P3.15 Intake and parser readiness.** Implement checksummed local PDF/supplement intake, identity validation, Docling and actual required table formats, source-located canonical output, and complete/incomplete context checks. Verify representative real outputs when available. No figure-pixel inference or universal-format parser project. Apply [file-readiness](docs/assignments/P3-file-readiness.md): validate identity, parse completeness, table/experiment/contrast/unit meaning, formulas/missing values, and source provenance. New raw-data analysis remains separately scoped; unresolved semantics block dependent findings.
- [ ] **P3.16 Batch readiness and corpus reconciliation.** Publish `extraction_readiness.json`, a readable coverage report, immutable ready-batch manifests, and a resumable remaining-work queue. Record separately papers accounted for, full texts processed, and findings extracted. Missing files remain pending; reviewed background-only dispositions do not need LLM calls. Ready batches are preparation artifacts only until the corpus-wide P3.17 checkpoint and user model decision; a partial batch cannot establish complete corpus coverage. Required context across files must use verified publication/version/experiment links and per-part hashes/document IDs/locators; unsupported joins stay NEEDS_CONTEXT. Count serialized cells, headers, legends and methods in size/token accounting; preserve row/page/sheet screening frontiers.

- [ ] **P3.17 Freeze corpus and present inference budget before P4.** Complete preparation for the approved manuscript corpus, reconcile manual files and outstanding items, and publish `inference_budget.json/.md` with actual paper/bundle counts, separate extractor/verifier inputs, prompt/schema/output/reasoning allowances, retries, per-batch/cumulative totals, and rate-parameterized cost scenarios. No chat calls or remote VLM/OCR. Missing inputs require explicit disposition, not invented completion. Present the frozen corpus and budget; wait for the user’s LLM provider/model/key decision before starting P4. Refine exact token counts in P4’s no-inference dry run once prompts/tokenizer are fixed. See the assignment for the report contract. Include the separate evidence-assembly investigation queue and allowance from §6.4.3; do not label its pending cases extraction-ready.

### Provisional corpus/cost planning worksheet — not an execution budget

Observed on 2026-09-22: 110 advisor PMIDs plus nine distinct non-advisor papers in the current processed selection gives 119 unique papers across those two sets. The search artifact contains 343 unique metadata records; these are discovery results, not 343 approved full-text/extraction inputs. For scheduling only, allow approximately 150–200 unique papers for screening/preparation after manuscript-targeted discovery. This is a provisional capacity estimate, not a target, hard cap, or assertion that every paper needs LLM extraction. The actual final corpus depends on coverage/access review.

Before P4, planned additional chat API token usage/cost is zero. The following historical estimate covers extractor/verifier only; assembly costs must now be added separately under §6.4.3. For an illustrative eventual P4 estimate, 400–800 bundles at 8,000 combined extractor/verifier input tokens and 2,000 combined billable output tokens per bundle imply 3.2–6.4 million input and 0.8–1.6 million output tokens. These allowances include prompt/schema and reasoning overhead only to the extent assumed; actual payloads and runtime caps must replace them in the P3.17 report/P4 dry run.

At illustrative rates of $0.15 input/$0.50 output per million tokens (the previously configured OpenRouter ceilings, not a newly verified quote), this is $1.10–$2.20 with a 25% planning reserve. At illustrative $1/$5 rates it is $9–$18 with the same reserve. Formula: `(input_tokens * input_rate + output_tokens * output_rate) / 1,000,000`. No cache discounts or universal retry cap are assumed; the reserve is not a hard spend guarantee. Provider/model selection remains pending the user's decision.

## 10. P4 — Evidence assembly, structured extraction and verification

**Goal:** convert verified ready batches into atomic source-grounded evidence artifacts, retaining support, negative/null results, and uncertainty. P3 parses documents; P4 extracts biological findings. Start P4 only after completed corpus preparation, reviewed readiness/budget reports, and the user’s provider/model/credential decision. The current key does not authorize this expanded run. No autonomous model tools.

**Allowed writes:** `extraction/`, extraction workflow/CLI, minimal shared schema additions, extraction config/provider extra/lock, P4 tests/artifacts/handoff. No graph integration changes before P5.

The [evidence-assembly contract](docs/assignments/P4-evidence-assembly-agent.md) specifies inputs/outputs, six tools, middleware, states, persistence, validation and limits. It is required design work within P4, not permission to begin before P3 review and user model/budget selection. Complete bundles bypass assembly.

### P4 execution order

- [ ] **P4.1 Implement chat providers and configure selected roles.** Implement LiteLLM proxy, OpenRouter, and Groq via their LangChain integrations following §6.4.1. Resolve qualified extractor/verifier selectors; an omitted verifier selector inherits the extractor. Check constructor/proxy routing offline for all three, install/load only selected extras, and validate only selected credentials. Confirm the selected model's structured-output mode within the total run budget. Keep raw responses/metadata locally, whether or not optional tracing is enabled. Provider absence is a clear setup error; never silently use a different model or provider.
- [ ] **P4.1a Implement bounded evidence assembly.** Follow the linked agent contract; implement read-only tools and source-part registry, structured proposal, host validation, durable call/token/cost ledger and review handoff. Preserve P3 artifacts and model-provider isolation. Test bypass, unresolved context, wrong source references, cross-asset linkage, limits/restarts and replay; agent output alone cannot clear essential semantics blockers.
- [ ] **P4.2 Define extraction/verification schemas.** The extractor returns zero or more atomic findings with source span IDs/quotes, entities and mapping hints, relation/direction, assay/outcome, statement status, directness, context, and explicit unknowns. The verifier checks each field against the exact same bundle. It may say insufficient context; it cannot retrieve, repair the finding, or invent missing assays. Table-derived findings identify exact supporting cells/header/legend parts and distinguish source-reported values from approved Python-derived values. Unknown comparison direction, scale or required experiment context cannot be filled from model knowledge.
- [ ] **P4.3 Write concise prompts.** State that source text is data, not instructions. Require explicit source grounding, allow NO_RELATION, keep primary findings separate from cited/review summaries, forbid binding-to-causality promotion, preserve complexes/species/negation, and use no external knowledge to fill missing facts. One prompt version each; no prompt tournament.
- [ ] **P4.4 Extract and verify.** Call extractor once per selected bundle. Verify returned findings using the same bundle in a bounded second call; batch findings from one bundle if schema allows. Store raw/parsed responses and usage. Do not call a verifier for an empty NO_RELATION output unless a specific regression requires it. Keep the extractor/verifier scheduled-call ceiling at 40 for 20 bundles per assigned batch; separately account for bounded assembly calls and all retries/preflight in the approved total-attempt/token/cost budget. Track cumulative usage and the remaining corpus queue; do not automatically execute all batches under the first smoke-run authorization.
- [ ] **P4.5 Deterministic source checks.** Validate quotes/offsets against stored canonical text and document hash; map entities through approved resolver; validate schema/enums and source IDs; flag missing or conflicting fields. The model cannot assign unchecked passage offsets, stable IDs, or a made-up PMID. For table findings, validate referenced cells and raw values, signs, inequalities, units and comparison direction against their own source assets and context. Python-derived numbers require a reproducible calculation record with input hashes, selection/parameters and code version; they must not be labelled as author-reported statistics. The LLM does not calculate statistics or repair malformed tables.
- [ ] **P4.6 Disposition and eligibility.** AUTO_ACCEPTED requires a faithfully stated finding, resolved scoring entities, matching source spans, and verifier support. Ambiguous entity/context/meaning becomes UNCERTAIN. Unsupported extraction/invalid quotes/NO_RELATION becomes REJECTED or explicit empty-result record. Accepted review/speculative statements, if retained, are discovery-only and not independent experimental support. Null or negated findings can be AUTO_ACCEPTED; their polarity is decided relative to a claim, not inferred from acceptance.
- [ ] **P4.7 Claims, evidence, and deduplication.** Keep claim IDs independent of one paper and preserve separate evidence assertions. Deduplicate exact repeated spans/findings within a source, but do not discard distinct experiments. Retain unresolved experiment identity and known shared-study dependencies. Compatible binding/perturbation findings can be linked; do not collapse them into DIRECT merely because both appear in the same paper.
- [ ] **P4.8 Persist artifacts.** Write `accepted_findings.parquet`, `claims.parquet`, `evidence_assertions.parquet`, `uncertain.jsonl`, `rejected.jsonl`, and extraction manifest; a single normalized table plus views is acceptable if it preserves these logical contracts. Store raw outputs separately. Do not overwrite earlier model/prompt-version results.
- [ ] **P4.9 Minimal quality checks.** Use a small fixture set for reversal, explicit no effect, repression vs negation, speculation, mismatched species, fabricated quote, mixed experiment contexts, and unresolved complex. Test deterministic disposition. Include §6.4.1's provider mapping, credential isolation, schema-mode failure, shared-budget, and cache-identity checks. Fixtures are clearly labelled engineering-only; no NLP performance claims. Include table-specific failures: invented cells, reversed contrasts/signs, wrong units, missing legends, mixed asset versions/experiments, untraceable derived numbers, and omitted structured content in token/size accounting.
- [ ] **P4.10 Live dry-run and bounded run.** Validate the immutable P3 source/readiness manifests and any derived assembly-bundle manifest; extraction rejects failed, unverified, or context-incomplete bundles. Context-investigation items may enter assembly only under its separate preflight and budget. Show selected papers/bundle IDs, coverage gaps, proposed calls/token estimates, provider/model, and configured caps without secrets. Run only with actual configured credentials/budget. Attach actual usage. Zero accepted findings is a valid outcome if faithfully reported; no acceptance rule may be loosened to populate the graph.
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

- [ ] **P5 context mapping and hierarchy extension.** Implement the small versioned mapping/term/edge artifacts and validations in §6.2a as part of offline graph export. Keep local IDs stable and include only reviewed mappings and source-verified selected hierarchy paths. No full ontology import or reasoner.

**Export bundle:** `graph export` reads completed artifacts, applies the materialization policy, and writes `data/graph_exports/<export_key>/` atomically. It must work with no server, driver connection, Docker runtime, or database credentials. Include:

- `nodes/<Label>.csv`: one typed logical table per allowed node label, with a stable `id` and explicit properties.
- `relationships/<Type>.csv`: one table per relationship type/endpoint-label combination, with stable relationship `id`, `source_id`, `target_id`, and explicit properties. Declare endpoint labels in the schema; never infer them from free text.
- `schema.json`: column types, nullable fields, endpoint labels, graph-property mappings, and CSV serialization rules. Use UTF-8, headers, standard CSV quoting, and lossless numeric precision. For nullable columns, declare an explicit null flag when empty string is meaningful; preserve zero vs missing. Flatten supported graph properties; keep arbitrary nested metadata in its source artifact. Do not add admin-import-specific header syntax to ordinary `LOAD CSV` tables.
- `manifest.json`: source artifact/run keys and hashes, export/schema/policy versions, file checksums, row counts, expected distinct IDs by label/type, selection/omission counts, and any parent bundle dependency.
- `validation.json` and `preview.md`: validation results and a small readable sample of nodes, relationships, source chains, and counts. No secret values or invented evidence.
- `import.cypher`: deterministic schema-specific `LOAD CSV WITH HEADERS` statements, explicit type/null conversions, fixed labels/types, and parameterized file URLs. Generate from maintained mappings, never from LLM text. Include import order and use stable IDs in `MERGE`.

**Pre-import validation:** verify checksums, schema/header agreement, value types, finite numerics, required properties, unique semantic IDs, relationship endpoint closure, and exact source provenance. Reject duplicate/conflicting IDs and dangling endpoints. Validate CSV round-trip for quotes, commas, newlines, Unicode, empty vs null, and zero-valued measurements. Report legitimate self-links without automatically rejecting scientific autoregulation. The first bundle is self-contained; later nomination additions may reference a declared parent bundle, whose endpoint inventory must be checked. Export verification and load `--dry-run` are offline and must not initialize a database. A modified bundle fails checksum validation; regenerate it after correcting its upstream artifact or mapping.

**Import choice:** use local Neo4j's native `LOAD CSV` for this first implementation. CSV is directly supported; tab-separated input is possible with `FIELDTERMINATOR`, but supporting a second import format is unnecessary. Parquet stays the analytical master format. Current `neo4j-admin database import full` also supports Parquet for initial bulk creation; that is a separate, version/edition-sensitive administrative path and is deferred. Do not treat `LOAD CSV` as a Parquet reader or run a full database replacement for routine reloads. References: [LOAD CSV](https://neo4j.com/docs/cypher-manual/current/clauses/load-csv/) and [full administrative import](https://neo4j.com/docs/operations-manual/current/import/full-import/).

**Separation of commands:** `graph load --bundle <path>` reads only a validated, already-created bundle. It cannot regenerate evidence, select targets, call models, or rerun export. Mount this project's `data/graph_exports/` read-only into the container's import directory; derive confined `file:///` URLs from manifest-relative paths and reject path traversal. Driver code executes the maintained import statements and verification queries. Load nodes first, verify endpoint presence, then relationships; never allow `MATCH` to silently discard a relationship. Revalidate checksums before import and verify actual IDs/counts against the bundle afterward. No implicit database writes from export, report, or `run-manuscript --resume`.

**Two executions within P5:** first assign the offline part of P5.4 (schema definition) and P5.5 (export/validation) and inspect its files. Then assign P5's service/import steps using the same export key. This does not add a new top-level package; an export-only handoff is `PARTIAL` for P5 and the live import checkbox stays open. The files can be processed/reviewed while Neo4j setup is unavailable.

### P5 execution order

Prepare the offline bundle as above first. The numbered service/import items below apply only when the separate import work is assigned.

- [ ] **P5.1 Inspect local runtime.** Check Docker availability and existing containers/ports without printing secrets. Use Compose service key `neo4j`, project-specific container name `regkg-neo4j`, and volume `regkg-neo4j-data` unless this project's existing service dictates otherwise. Prefer loopback host ports 7474/7687 if free; use documented alternatives if occupied. Do not stop another project's container to obtain a port.
- [ ] **P5.2 Define local deployment.** Pin a verified supported Neo4j Community image version, use persistent `/data`, a read-only project graph-export mount at `/import`, loopback port bindings, environment-provided authentication, and a simple health/readiness check. Keep credentials out of compose/config source. Do not install Enterprise/APOC/GDS/GraphRAG plugins for this task.
- [ ] **P5.3 Driver configuration.** Create one driver per command/process, verify connectivity, set database explicitly, and close resources. Fail closed on a nonlocal endpoint unless the user explicitly selected a cloud mode. Use bounded query timeouts, parameterized values, and a chosen batch size (default 500 rows; tune only if needed).
- [ ] **P5.4 Schema.** Create uniqueness constraints on stable IDs for Gene, CellType, BiologicalContext, SpatialNicheState, NeighborhoodProfile, Dataset, AnalysisRun, ExpressionObservation, ChromLinkerObservation, GeneProgram, Publication, Passage, RegulatoryClaim, EvidenceAssertion, NicheExpressionSignature, and TFNomination when loaded. Use one NicheExpressionSignature node per comparison with selected per-gene values on HAS_GENE links. Do not materialize both redundant row-nodes and equivalent links without a query need.
- [ ] **P5.5 Materialization policy.** Include all four manuscript regulatory lineages, their supported states/contexts, selected candidates, and at most 25 target genes per candidate/comparison chosen by documented descriptive signature relevance among its project/prior targets, plus genes needed by accepted findings. Include selected TF/target expression and original ChromLinker values in the corresponding lineage/condition contexts, including selected zero-valued observations. Do not manufacture Control regulatory observations for KRT/fibroblasts. Keep full matrices in Parquet. Materialize each accepted finding and every source span needed to inspect it. Implement the offline `graph export` and `verify graph-export` commands and bundle contract above. Produce expected unique node/relationship counts before touching the graph. Return the bundle for inspection before the separate import work.
- [ ] **P5.6 Import identity nodes then observations from CSV.** Consume only the specified validated bundle through schema-specific `LOAD CSV` statements. Use `MERGE` on immutable IDs, not mutable text. Add context/niche/source/run links from exported records. Missing referenced IDs fail the batch/report, not silently drop relationships. Do not turn raw ChromLinker observations into REGULATES edges.
- [ ] **P5.7 Import evidence from the same bundle.** Use Claim→EvidenceAssertion→Passage→Publication with experiment/study links when resolved. Keep original finding context and relative support/counter-evidence links. Multiple evidence assertions can share one claim. Uncertain/rejected findings stay in artifacts outside scored evidence.
- [ ] **P5.8 Transaction and rerun behavior.** Batch `LOAD CSV` with `CALL { ... } IN TRANSACTIONS` using syntax supported by the pinned Neo4j version. Execute such statements in an implicit transaction via `session.run` and consume the result, not inside `execute_write`/a managed transaction. Other bounded queries may use managed transactions. Record progress after results complete; earlier batches may remain committed on failure, so rerunning an incomplete file must be idempotent. No model calls or source transformations during import. Repeat semantic imports cannot duplicate nodes/links. New versions preserve prior evidence rather than clobber it; do not silently delete records absent from a later bundle. Driver execution reference: [implicit transactions and CSV imports](https://neo4j.com/docs/python-manual/current/query-advanced/).
- [ ] **P5.9 Required queries.** Implement fixed parameterized functions: a requested lineage’s niche neighborhood; a TF's raw predicted targets in a specified condition/niche; signature effect and expression for a gene; claims and supporting/negative/inconclusive findings for a TF; exact cited passages/publications. Return honest empty results and coverage fields.
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

**Goal:** a scientist can inspect the regulatory evidence and nominations for every manuscript lineage and trace their relationship to manuscript claims. This package evaluates the biomedical contribution, not NLP model performance.

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
- [ ] **P6.9 Reports.** Export `nominations.csv`, `nominations.parquet`, `evidence.csv`, `coverage.csv`, `ranking_sensitivity.csv`, `summary.md`, and one evidence Markdown report per TF and lineage/comparison, plus `manuscript_claim_evidence.csv` and `.md` covering the four regulatory narratives. Preserve project-prediction, literature-mechanism, context-only, contradiction, and unverified manuscript-claim status separately. Optional static HTML may reuse these results but is not a separate frontend requirement. Include condition/target niche, concordance sign/coverage, raw connectivity summary/semantic caveat, TF expression, independent evidence/context/contradictions, cell counts/donor unknowns, source passages/PMIDs, and ranking version. Clearly label full-text vs abstract-only sources.
- [ ] **P6.10 Graph nominations.** Export nomination records to a new CSV bundle using `graph export --nomination-run <nomination_key> --parent-bundle <base_bundle_path>`, with stable versioned IDs and links to the exact evidence/project artifacts used. Validate/inspect it, then import separately with `graph load --bundle <nomination_bundle_path>`. Nomination/report generation must succeed without Neo4j. Do not recompute a separate ranking inside Cypher. Ensure reports and graph return the same candidate identities/counts/component values.
- [ ] **P6.11 Integrated command and replay.** Implement `run-manuscript --resume` with explicit lineage/comparison selection as a thin sequence of existing stage functions using manifests, not another pipeline framework. It must stop explicitly when required live configuration is missing. Its default endpoint is validated files/reports and graph export, with no graph connection or import. Preserve worker review boundaries; a resume command does not authorize advancing an unreviewed package. Graph loading remains the explicit separate `graph load --bundle ...` command. A completed replay uses cached literature/model outputs and reproduces scientific results (ignoring execution timestamps); replay the import separately to check graph idempotency.
- [ ] **P6.12 Final handoff.** Run focused integration checks, save a complete actual command transcript without secrets, report optional branches exercised/deferred, and list all limitations. No claim of human-validated extraction, causal TF discovery, all-cell-type completion, or publication readiness without the relevant evidence.

- [ ] **P6.13 Context hierarchy reporting.** Apply §6.2a reviewed mappings and selected hierarchy to report broad versus exact evidence context across the four lineages. Preserve original experiment context and count each finding/study once; unresolved mapping is visible. No automatic transfer of regulatory claims through the hierarchy.

### P6 commands and evidence

```bash
.venv/bin/python -m pytest tests/test_nomination.py tests/test_replay.py -q
.venv/bin/python -m regkg nominate --project-run <ingest_key> --candidate-run <candidate_key> --evidence-run <extraction_key> --cell-type "<cell_type>"
.venv/bin/python -m regkg report --run <nomination_key>
.venv/bin/python -m regkg verify report --run <report_key>
.venv/bin/python -m regkg run-manuscript --config configs/project.yaml --resume
.venv/bin/python -m ruff check src tests
.venv/bin/python -m pytest -q
.venv/bin/python -m pip check
```

Report checks: every evidence ID resolves, quotes match stored text, no unsupported statistical/causal claims, all required seeds are visible, missing connectivity rank remains null, cell counts/units are preserved, and repeated output is stable. Final full tests are appropriate once for this integrated boundary; avoid repeated full runs absent a change/failure.

**Review gate:** all four lineage reports and the integrated manuscript claim/evidence matrix use actual input data and retrieved/processed literature, match the live graph, and expose missing inputs, contradictions, and uncertainty. If no supporting findings were accepted, the report must show that and the reviewer assesses whether the initial demonstration is informative enough; workers must not fabricate a minimum number of positive edges.

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
| P1 | 2026-09-21 | [Accepted repair review](docs/reviews/P1.md): 79 tests, 56/56 real checks, replay REUSED; `ingest-6f3b10c688adf3b6` | R1/R2 resolved; old artifact preserved; external gene resolution deferred to P2 as planned |
| P2 | 2026-09-21 | [Accepted repair review](docs/reviews/P2.md): 96 tests, 29/29 artifact checks, zero-network replay; `candidates-ad74f8d35867b7f3` | R1/R2 resolved; six ambiguous mappings excluded; inferred-sign/regulator-scope caveats retained |
| P2 manuscript extension | 2026-09-22 UTC | [Accepted](docs/reviews/P2-manuscript.md): 155 tests, 33/33 real checks, zero-network replay; `mcandidates-c278c6625ff7c537` | Six primary comparisons; 16 lineage–TF memberships; 57 candidates; 248 queued queries. P3 consumer adaptation and query translation checks next |
| P3 | 2026-09-22 UTC | [Residual repair accepted](docs/reviews/P3.md): 147 tests, 18/18 real checks; independent F1/F2 probes; search/retrieval replay and prior output checksums verified | Original repair baseline accepted. Fix generic BioC footnote classification during expanded P3; manuscript coverage/PDF/readiness/budget remain pending |
| P4 | — | — | — |
| P5 | — | — | — |
| P6 | — | — | — |

### Final acceptance checklist

- [ ] All six required packages accepted with real evidence and linked reviews.
- [ ] Source data/reference files preserved; no unrelated project modifications.
- [ ] No fabricated IDs, assay facts, donor counts, connectivity semantics, DE statistics, or positive findings.
- [ ] Evidence reports exist for all four manuscript regulatory cases, plus the integrated claim-to-evidence matrix, with citations, counter-evidence, coverage, and provenance.
- [ ] Local Neo4j contains the selected evidence graph; repeated loads preserve counts/identities.
- [ ] Replay works from accepted artifacts without unnecessary network/model calls.
- [ ] All advisor papers have reviewed coverage dispositions; missing full texts/supplements, parse failures, unprocessed bundles, and extraction failures remain visible. Do not claim complete extraction from metadata coverage or top-k retrieval.
- [ ] Missing score semantics and format/model limitations are explicitly described.
- [ ] Instructions remain centralized in AGENTS.md and CLAUDE.md remains its relative symlink.

## 15. Deferred expansion beyond the required manuscript KG

This list is deliberately not part of the six-package finish line. The reviewer/user chooses later assignments based on the first real report:

- Expand discovery beyond the mandatory advisor corpus and resolve remaining TF/target/context evidence gaps. Whole-advisor accounting and required parsing are already part of P3, not deferred.
- Add further curated resources with preserved provenance and dependency grouping.
- Extend regulatory analyses to additional cell types beyond the four manuscript cases only when corresponding inputs and a manuscript need are established. The four current lineages are mandatory, not deferred.
- Add pathway interpretation from versioned Reactome/GO annotations with a documented tested/eligible background; do not infer pathway membership with an LLM. This is deferred to keep the first result bounded, not removed from the broader scientific design.
- Incorporate confirmed ChromLinker aggregation rules without reinterpreting earlier stored values.
- Extend parsing to additional formats or improve retrieval only when actual scientific inputs justify it; required advisor-PDF readiness is already part of P3.
- Add donor-aware analysis if donor-resolved inputs arrive.
- Add REST/MCP over fixed scientific queries for LungMAP/LungChat.
- Consider custom LangGraph orchestration only if ordinary resumable loops become inadequate; the bounded P4 agent already uses create_agent and its internal LangGraph runtime.
- Add held-out perturbation validation, richer regulatory-locus modeling, or an expanded paper analysis when there is data and explicit scope.

Do not convert this list into mandatory scaffolding during P1–P6.

## 16. Current next assignment

**Assign P3 corpus readiness** using [the detailed assignment](docs/assignments/P3-corpus-readiness.md). P2.11–P2.13 are accepted in [the manuscript extension review](docs/reviews/P2-manuscript.md). Consume `mcandidates-c278c6625ff7c537` for expanded candidates and queues; retain `candidates-ad74f8d35867b7f3` and `litretrieval-6a092b32d5f87020` as regression baselines.

Adapt P3 to the reviewed manuscript schema and fair resumable schedule. Audit all 110 advisor papers/117 memberships; execute the fixed 248-query discovery queue in resumable batches of at most 20, with acquisition batches of at most 10 papers. Reuse identical source requests and cached assets. Preserve all pending queries/papers/passages; per-batch limits are not total-corpus limits. Validate source handling of KRT5/KRT17 query punctuation before bulk execution, recording any versioned query normalization. Do not add further discovery expansion without a demonstrated manuscript evidence gap and a bounded follow-up assignment.

Publish the manual-download report early, then implement/review required local Docling and supplement parsing, including the recorded BioC generic-footnote classification correction. Complete available source preparation, ready-batch manifests, and cumulative token/cost estimates without chat calls. Missing user files or review dispositions remain explicit pending items; hand off useful reports without pretending the corpus is frozen. P4 stays paused until corpus preparation/dispositions are reviewed and the user chooses the provider/model/key. No Neo4j, commit, or push. Pending P3–P6 acceptance items remain unchecked.
