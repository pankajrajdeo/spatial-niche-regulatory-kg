> **Scope:** This remains biomedical KG work for a bioinformatics paper. LangChain and literature extraction are implementation support. No NLP benchmark, embedding study, model fine-tuning, or model-comparison campaign is part of the MVP.

Yes — **the uploaded LangChain SDK can be useful for this project**, but I would use only a small part of it. After comparing it against the KG architecture we just froze, I would **not change the project into an agentic system**.

The most useful insight from the package itself is that LangChain/LangGraph explicitly distinguishes a **workflow** from an **agent**:

> a workflow follows predetermined code paths; an agent dynamically decides its process and tool usage.

Our KG construction pipeline is overwhelmingly the first case.

## My recommended use of this SDK

I would change our software architecture slightly to this:

```text
Spatial NicheLinker / ChromLinker data
                │
                ▼
      deterministic Python ETL
                │
                ▼
     Dynamic retrieval queue
                │
                ▼
      PMC / Europe PMC / PDF
                │
                ▼
       document processing
                │
                ▼
         candidate passages
                │
                ▼
   ┌───────────────────────────────┐
   │       LANGCHAIN CORE          │
   │                               │
   │ model.with_structured_output  │
   │          ↓                    │
   │     LLM Extractor             │
   │          ↓                    │
   │     LLM Verifier              │
   └───────────────────────────────┘
                │
                ▼
     deterministic validation
                │
        ┌───────┴────────┐
        ▼                ▼
    accepted          uncertain
        │                │
        ▼                ▼
      Neo4j         JSONL/Parquet
        │
        ▼
     TF Nomination
        │
        ▼
     FastAPI / MCP
        │
   ┌────┴─────┐
   ▼          ▼
LungChat    LungMAP
```

Then optionally put **LangSmith** around the LLM portion for provenance/debugging.

That is where this SDK helps.

---

# 1. The highest-value feature: `with_structured_output()`

This is probably the single part of the uploaded SDK I would definitely use.

The package's `langchain/models.md` supports standalone model use **without creating an agent**, including:

```python
model.with_structured_output(MyPydanticModel)
```

and supports Pydantic validation.

That maps almost perfectly to our extraction requirement.

Instead of manually doing:

```text
prompt LLM
→ receive JSON-looking string
→ json.loads
→ repair malformed JSON
→ validate keys
→ retry
```

we can define:

```python
class RegulatoryClaimExtraction(BaseModel):
    regulator: str | None
    target_gene: str | None

    relation: RelationType
    direction: Direction
    directness: Directness
    evidence_type: EvidenceType

    assays: list[str]

    species: str | None
    tissue: str | None
    cell_type: str | None
    disease: str | None
    condition: str | None
    model_system: str | None

    measured_or_inferred: Literal[
        "measured",
        "inferred",
        "reported",
        "unclear",
    ]

    negated: bool
    statement_status: Literal["AFFIRMED", "NEGATED", "SPECULATIVE", "UNCLEAR"]
    experimental_outcome: Literal[
        "INCREASE", "DECREASE", "NO_DETECTED_EFFECT",
        "BINDING_DETECTED", "NO_BINDING_DETECTED", "UNCLEAR",
    ]
    evidence_spans: list[EvidenceSpan]  # source ID, exact quote, checked offsets
    relation_present: bool  # includes explicit negative/null findings
```

Define `EvidenceSpan` and the referenced enums in the canonical Pydantic contracts. Emit a list of atomic findings when a bundle contains several experiments. Preserve complex/family identity rather than silently mapping it to one gene; unresolved identity prevents gene-specific scoring.

Then:

```python
extractor = model.with_structured_output(
    RegulatoryClaimExtraction,
    include_raw=True,
)
```

This is **much better aligned with the project than `create_agent()`**.

The `include_raw=True` feature in the package is especially useful for us because it lets us retain both:

```text
validated parsed record
+
raw model response / metadata
```

which is good scientific provenance.

### I would therefore use LangChain for:

```text
model provider abstraction
structured output
Pydantic integration
retry/timeout handling
token/response metadata
```

Not autonomous reasoning.

---

# 2. Extractor → verifier is exactly a LangGraph "prompt chaining" workflow

The uploaded `langgraph/workflows-agents.md` describes **prompt chaining** as sequential LLM calls for well-defined tasks, including verification.

That is essentially our design:

```text
Passage
  ↓
Extractor
  ↓
Structured claim
  ↓
Verifier
  ↓
Accepted / uncertain / rejected
```

So we have two implementation choices.

### Simpler MVP

Just plain Python:

```python
extraction = extract_claim(passage)
verification = verify_claim(passage, extraction)
decision = deterministic_validate(extraction, verification)
```

### Slightly more engineered version

Use a fixed LangGraph:

```text
START
  ↓
extract_claim
  ↓
verify_claim
  ↓
validate_claim
  ↓
     ┌───────────────┐
     │               │
 accepted         uncertain
     │               │
     ▼               ▼
 write_graph       sidecar
     │               │
     └───────┬───────┘
             ▼
            END
```

Crucially, this is:

> **LangGraph as workflow orchestration, not LangGraph as an agent.**

That distinction matters.

---

# 3. Do we need LangGraph from day one?

**No.**

For the first AT1 demonstration I would use plain Python functions.

Our immediate pipeline is sufficiently simple:

```text
retrieve
→ parse
→ retrieve passages
→ extract
→ verify
→ validate
→ save
```

Adding a graph framework immediately creates another abstraction to debug.

However, LangGraph becomes attractive when we start processing hundreds or thousands of papers because the uploaded docs provide:

```text
persistence
checkpoints
fault tolerance
node-level retries/errors
resume after failure
parallel execution
streaming
```

Imagine we process 800 papers and the process dies after paper 593.

Plain ad-hoc Python often becomes:

```text
Which papers completed?
Which LLM calls completed?
Did verifier run?
Did Neo4j insertion happen?
Should this paper be rerun?
```

A persisted workflow makes that cleaner.

So my recommendation becomes:

> **Phase 1: plain Python + LangChain models.  
> Phase 2, if batch orchestration becomes painful: wrap the fixed pipeline in LangGraph.**

---

# 4. LangSmith could actually be very useful

This is the other component I would seriously consider.

The uploaded SDK contains substantial LangSmith support for:

```text
tracing
observability
datasets
evaluation
experiment comparison
regression testing
```

This could solve a real problem we identified:

> We have no dedicated human literature curator.

It does **not** solve the absence of human ground truth, but it does give us an excellent audit/debugging layer.

For each passage extraction we could trace:

```text
PMID
passage_id
TF candidate
target candidate

prompt version

model
model version

extractor output

verifier input
verifier output

validation rules

final disposition:
AUTO_ACCEPTED
UNCERTAIN
REJECTED

token use
latency
error
```

Then when something bizarre appears in Neo4j, instead of asking:

> Why does the KG say TEAD1 regulates X?

we can trace:

```text
Neo4j claim
   ↓
EvidenceAssertion
   ↓
Passage
   ↓
LLM extraction trace
   ↓
verification
   ↓
prompt/model version
```

That is excellent for an evidence-oriented KG.

---

# 5. Optional tracing and basic extraction checks

LangSmith can help inspect failed or surprising extractions, but local JSONL logs are sufficient initially. Record the passage, proposed finding, verifier result, and model/prompt/schema versions.

Keep a small regression set for practical failures: wrong gene/species, reversed regulator and target, missed negation, unsupported directness, and source-text mismatch. This is routine evidence quality control. Do not create a separate NLP benchmark, annotation campaign, or model-comparison deliverable.

With no dedicated curator, automated acceptance must remain labeled as such. Preserve exact evidence passages for scientist inspection.

---

# 6. Provider abstraction without a model-selection project

Use one suitable structured-output model configuration initially. LangChain makes it possible to change providers if a practical issue warrants it; multiple-model benchmarking is not a project requirement.

Record provider, model/version, prompt version, schema version, generation settings, and run date. The goal is reproducible extraction, not a new NLP method.

---

# 7. Automatic retries are useful, but don't build an agent just for them

The SDK supports retries for model/API failures.

This matters because our pipeline may make many calls.

A paper processing job should not fail because one request gets:

```text
429
timeout
500
network disconnect
```

But we don't need agent middleware for the basic case.

The standalone LangChain model interface already has configurable:

```text
max_retries
timeout
```

with exponential retry behavior.

So:

```python
model = init_chat_model(
    ...,
    max_retries=6,
    timeout=120,
)
```

is sufficient initially.

---

# 8. LangChain retrieval utilities: useful, but optional

The package provides standard abstractions for:

```text
Documents
text splitters
embeddings
vector stores
retrievers
```

We could therefore represent each paper passage as:

```python
Document(
    page_content=passage_text,
    metadata={
        "pmid": ...,
        "section": "Results",
        "start_offset": ...,
        "end_offset": ...,
        "tf_mentions": [...],
    }
)
```

and use its retrieval interfaces.

That's reasonable.

But I would **not make LangChain RAG infrastructure a core architectural dependency**.

Our retrieval requirement is specialized:

```text
PubTator entities
+
exact TF/target matches
+
biomedical regulatory terms
+
BM25
+
optional embeddings
```

A small custom retriever may be clearer scientifically.

So LangChain retrieval is:

> convenience, not fundamental infrastructure.

Use identifiers/aliases and BM25 alongside a lightweight biomedical embedding model for semantic passage retrieval. The user will choose the model; keep the adapter model-independent. BM25 works as a fallback before that selection is connected. Preserve exact matches and source locators; similarity never becomes regulatory evidence. MedCPT is one biomedical retrieval example, not a required choice. [NCBI MedCPT](https://github.com/ncbi/MedCPT)

Do not add SapBERT, a separate reranker, model-comparison experiments, or synthetic training data to the MVP. The quantitative pipeline and Neo4j writer need no text embeddings. See section 63 of [the final synthesis](chatgpt_final_synthesis.md).

---

# 9. DeepAgents: mostly NO for KG construction

This is where I would **not** use the uploaded package.

Deep Agents provides a large harness with:

```text
task planning
filesystem
sandboxes
code execution
subagents
skills
memory
context offloading
delegation
human-in-the-loop
```

That is useful when the task is:

> "Here is an open-ended research problem. Figure out what tools/files/searches you need and complete it."

Our pipeline instead says:

```text
Given TF X
→ generate these queries
→ retrieve these records
→ parse these assets
→ extract these exact fields
→ verify
→ validate
→ write graph
```

There is almost no reason to let an LLM autonomously decide that workflow.

And allowing it to do so would make the scientific method **less reproducible**.

### Therefore:

```text
DeepAgents for core KG construction:        NO
DeepAgents for TF ranking:                  NO
DeepAgents for paper parsing:               NO
DeepAgents for Neo4j writes:                NO
DeepAgents for automated evidence scoring:  NO
```

---

# 10. There is one place DeepAgents might be interesting later

After the KG is complete.

Imagine LungChat eventually receives:

> "Why is FOXA2 nominated for IPF AT1 Niche2, and is there evidence against it?"

A future scientist assistant could have tools:

```text
query_tf_nomination()
query_chromlinker()
query_gene_program()
query_regulatory_claims()
get_publication_passage()
query_pathways()
find_contradictory_evidence()
```

Then a Deep Agent could investigate those resources and produce an evidence-backed explanation.

That would be:

```text
FINISHED KG
    ↓
SCIENTIST ASSISTANT
```

not:

```text
AGENT
   ↓
creates scientific KG however it feels like
```

That difference is crucial.

And because LungChat already exists as the product/runtime direction, **that is the natural future home for DeepAgents**, if you want it at all.

---

# 11. MCP becomes very interesting later

The uploaded SDK has first-class MCP support.

This connects nicely with your lab's goal:

> **LungMAP and LungChat should eventually consume the same evidence service rather than maintain separate biology.**

Our backend could ultimately expose a small set of capabilities:

```text
search_tf_nominations

get_tf_evidence

get_tf_targets

get_niche_gene_program

get_regulatory_claim

get_supporting_passages

get_publication

compare_niches
```

through:

```text
FastAPI
+
FastMCP
```

Conceptually:

```text
               Regulatory Evidence Service
                       │
            ┌──────────┴───────────┐
            │                      │
         REST API                MCP
            │                      │
            ▼                      ▼
      LungMAP website          LungChat
                              / agents
```

This is one of the most compelling longer-term uses of the LangChain ecosystem for this project.

But again:

> **MCP is an interface over our evidence system, not how we construct biological evidence.**

---

# 12. LangGraph parallelization could eventually save time

The uploaded docs also show parallelization as a workflow pattern.

For us:

```text
              Paper
                │
       ┌────────┼────────┐
       ▼        ▼        ▼
   Results   captions   tables
       │        │        │
       └────────┼────────┘
                ▼
          candidate passages
```

or across papers:

```text
PMID1 ──┐
PMID2 ──┤
PMID3 ──┤── parallel processing
PMID4 ──┤
PMID5 ──┘
```

Similarly, the two LLM analyses could be independent in some designs:

```text
extractor A
    │
    ├──────────────┐
    ▼              ▼
relation check   context check
    │              │
    └──────┬───────┘
           ▼
       validator
```

But don't optimize this before the AT1 pipeline works.

---

# 13. Don't use LangGraph memory as the KG

This deserves saying explicitly.

The uploaded SDK includes:

```text
checkpointers
stores
long-term memory
```

Those are for **application/runtime state**.

They should **not replace Neo4j**.

Use:

```text
Neo4j
    = scientific canonical knowledge/evidence

LangGraph checkpoint
    = workflow execution state

LangSmith
    = LLM trace/evaluation state

Parquet/files
    = raw/intermediate scientific artifacts
```

These are different things.

---

# 14. Don't use an agent to dynamically search literature

Our previous phrase **dynamic retrieval** might sound agentic.

It doesn't need to be.

Use deterministic Python:

```python
for candidate in tf_candidates:
    searches = build_queries(
        tf=candidate.tf,
        targets=candidate.targets,
        cell_type=candidate.cell_type,
        disease=candidate.disease,
    )
```

Then:

```text
PubMed / Europe PMC / PubTator
```

No LLM planning required.

An LLM may perhaps rewrite a difficult search query later, but it should not control the corpus construction process.

---

# 15. What from the SDK maps to each project module

| Our component | LangChain ecosystem | Use? |
|---|---|---|
| ChromLinker parsing | pandas/Python | **No LangChain** |
| Pseudobulk parsing | pandas/Python | **No LangChain** |
| Neighborhood and niche-expression signatures | pandas/Python | **No LangChain** |
| Future sample-aware DE ingestion | pandas/Python | Optional future |
| TF enrichment | scipy/Python | **No LangChain** |
| PubMed query generation | deterministic Python | **No agent** |
| Paper fetching | requests/httpx | **No LangChain required** |
| PDF parsing | Docling | **No LangChain required** |
| Passage retrieval | custom / LangChain retriever | Optional |
| PubTator normalization | PubTator API | **Yes, external** |
| Regulatory extraction | `with_structured_output()` | **Strong yes** |
| Extraction schema | Pydantic | **Strong yes** |
| LLM verification | structured model call | **Strong yes** |
| Extractor→verifier orchestration | Python initially / LangGraph later | Optional |
| Batch fault tolerance | LangGraph | Later |
| LLM tracing | LangSmith | **Useful** |
| Basic extraction debugging | Local logs / optional LangSmith | **Useful; no benchmark project** |
| Scientific graph | Neo4j | **Not LangGraph Store** |
| Graph API | FastAPI | **Yes** |
| AI-facing graph API | MCP | **Later yes** |
| Scientist conversational assistant | LungChat + potentially DeepAgents | Later |
| Core KG builder | DeepAgents | **No** |

---

# 16. I would revise the repository structure slightly

Earlier I proposed:

```text
src/regkg/
```

I would now make the LLM layer explicit:

```text
src/regkg/
│
├── project_data/
│   ├── neighborhood.py
│   ├── chromlinker.py
│   ├── expression.py
│   ├── niche_expression_signatures.py
│   │
│   │   # optional future:
│   └── differential_expression.py  # sample-aware DE only
│
├── literature/
│   ├── search.py
│   ├── fetch.py
│   ├── parse_xml.py
│   ├── parse_pdf.py
│   ├── pubtator.py
│   ├── passages.py
│   ├── retrieval.py
│   └── embeddings.py      # selected lightweight biomedical model
│
├── extraction/
│   ├── schemas.py
│   ├── models.py
│   ├── prompts/
│   │   ├── extractor_v1.txt
│   │   └── verifier_v1.txt
│   ├── extractor.py       ← LangChain model
│   ├── verifier.py        ← LangChain model
│   └── validate.py
│
├── workflows/
│   ├── process_paper.py   ← plain Python first
│   └── process_corpus.py
│
├── graph/
│   ├── neo4j.py
│   ├── upsert.py
│   └── materialize.py
│
├── analysis/
│   ├── enrichment.py
│   ├── pathways.py
│   └── nomination.py
│
└── api/
    ├── rest.py
    └── mcp.py             ← later
```

Then, **only if needed**, add:

```text
workflows/langgraph_pipeline.py
```

later.

---

# 17. The concrete extractor architecture I now recommend

This is probably where the uploaded SDK improves our plan the most.

```text
       bounded source evidence bundle
                    │
                    ▼
      LangChain standalone model
                    │
        with_structured_output()
                    │
                    ▼
        RegulatoryExtraction
             Pydantic object
                    │
       ┌────────────┴────────────┐
       │                         │
 NO_RELATION                 relation
       │                         │
       ▼                         ▼
    reject                Verifier model
                              │
                    with_structured_output()
                              │
                              ▼
                    VerificationResult
                              │
                              ▼
                  deterministic validator
                     /         |        \
                    /          |         \
                   ▼           ▼          ▼
                ACCEPT      UNCERTAIN    REJECT
                   │           │
                   ▼           ▼
                 Neo4j       sidecar
```

That is clean, reproducible, and testable.

---

# 18. The verifier should not be a free-form agent

Give it exactly:

```text
original bounded evidence bundle with source locators
+
extractor result
```

and ask for:

```python
class VerificationResult(BaseModel):
    relation_supported: bool
    regulator_supported: bool
    target_supported: bool

    direction_supported: bool | None
    directness_supported: bool
    evidence_type_supported: bool

    context_supported: bool

    statement_status_supported: bool
    experimental_outcome_supported: bool
    evidence_spans_supported: bool
    insufficient_context: bool

    verdict: Literal[
        "VALID",
        "INVALID",
        "UNCERTAIN",
    ]

    reasons: list[str]
```

No tools.

No web.

No additional literature retrieval.

No revising the claim.

Its job is:

> Does this exact source bundle support the extraction, including its negation, outcome, and experimental context?

A valid negative or null result can pass verification. `NO_RELATION` means no relevant finding is expressed; it does not mean an experiment found no effect. Contradictory evidence can be high quality. Keep extraction status, outcome, evidence strength, and support/counter-evidence polarity separate.

If context is missing, return `insufficient_context = true`. A deterministic logged expansion rule may assemble a new bundle and run extraction again; the verifier cannot search or repair the claim. Exact quotation/offset checks remain deterministic code. Keep basic regression/source checks and do not treat model agreement as ground truth. See sections 42, 45, and 65 of [the final synthesis](chatgpt_final_synthesis.md).

---

# 19. LangSmith tracing could become part of scientific provenance—but don't confuse them

There are two provenance systems:

### Scientific provenance

Stored in our KG:

```text
PMID
experiment
study
dataset
assay
passage
analysis run
```

### Computational LLM provenance

Potentially LangSmith:

```text
model
prompt
schema
tokens
latency
raw response
verifier response
trace
```

Then our `AnalysisRun` can retain something like:

```text
langsmith_trace_id
```

if we use LangSmith.

That gives a very strong audit chain:

```text
TFNomination
    ↓
RegulatoryClaim
    ↓
EvidenceAssertion
    ↓
Passage
    ↓
PMID

AND

EvidenceAssertion
    ↓
ExtractionRun
    ↓
LangSmith trace
    ↓
prompt + model + raw output
```

That would be excellent engineering.

---

# 20. One thing I would *not* do: LangSmith as scientific storage

Don't put your canonical papers/claims only in LangSmith.

Still store:

```text
accepted_claims.parquet
raw extraction JSON
verifier output
prompt version
```

yourself.

LangSmith is observability/evaluation infrastructure, not your research dataset of record.

---

# 21. Could LangGraph replace Airflow/Prefect for this?

Potentially—but only for the LLM-heavy paper-processing workflow.

For example:

```text
retrieve paper
     ↓
parse
     ↓
passage selection
     ↓
extract
     ↓
verify
     ↓
validate
     ↓
graph write
```

is a natural LangGraph workflow because some nodes can:

```text
retry
fail
resume
branch
```

But things like:

```text
read CSV
melt dataframe
run Fisher's exact test
calculate RRF
```

remain plain Python.

So even if we adopt LangGraph later:

> it orchestrates a narrow **literature-processing workflow**, not the entire scientific project.

---

# 22. What I would implement from this SDK NOW

I would take exactly **three things** from the uploaded package initially:

### A. LangChain standalone model API

```text
init_chat_model
```

### B. Pydantic structured output

```text
with_structured_output()
```

for:

```text
RegulatoryClaimExtraction
VerificationResult
```

### C. Optional LangSmith tracing

for:

```text
extractor
verifier
prompt/model versions
failures
cost
latency
```

And stop there.

No LangGraph yet.

No DeepAgents.

---

# 23. What I would implement SECOND

Once the AT1 pipeline works and we begin processing the full corpus:

Add a small fixed LangGraph if batch reliability becomes necessary:

```text
PaperProcessingState
```

with nodes:

```text
retrieve
parse
candidate_passages
extract
verify
validate
persist
```

Then use its persistence/fault tolerance.

---

# 24. What I would implement LAST

Once the KG is scientifically useful:

```text
FastMCP/MCP layer
      ↓
LungChat
```

and perhaps:

```text
DeepAgent scientist assistant
```

that can ask questions across:

```text
Neo4j
literature
project observations
pathways
```

but only as a **consumer of the curated KG**.

---

# 25. This actually improves the project architecture

Previously we were treating the choice as:

> "Agentic LangChain system or no LangChain?"

That's the wrong choice.

The better architecture is:

```text
                     ┌────────────────────────┐
                     │ SCIENTIFIC PIPELINE    │
                     │ deterministic Python   │
                     └───────────┬────────────┘
                                 │
                                 ▼
                     candidate evidence passage
                                 │
                     ┌───────────▼────────────┐
                     │ LANGCHAIN MODEL LAYER  │
                     │                        │
                     │ structured extractor   │
                     │ structured verifier    │
                     └───────────┬────────────┘
                                 │
                     deterministic validation
                                 │
                                 ▼
                            NEO4J KG
                                 │
                 ┌───────────────┼───────────────┐
                 ▼               ▼               ▼
            TF ranking        FastAPI           MCP
                                 │               │
                                 ▼               ▼
                              LungMAP         LungChat
                                                 │
                                                 ▼
                                     optional DeepAgent later
```

That is the architecture I would use.

## Bottom line

**Yes, use the LangChain SDK—but narrowly.**

The uploaded package is valuable for this project mainly because of:

1. **model-provider abstraction;**
2. **Pydantic/schema-constrained structured output;**
3. **extractor → verifier prompt chaining;**
4. **retry/reliability support;**
5. **optional LangSmith tracing/debugging;**
6. later, **LangGraph durable workflow orchestration;**
7. later, **MCP/LungChat integration**.

I would **not use DeepAgents for KG construction**, and I would **not describe this as an agentic KG pipeline**.

The strongest implementation is still:

> **deterministic scientific ETL + LangChain structured LLM extraction + deterministic validation + Neo4j evidence graph + transparent TF nomination.**

The LangChain package makes the LLM portion substantially cleaner and more auditable without changing the scientific design.


# Project-data update after final Shunya clarification

The LangChain/LangGraph recommendation is unchanged: the project remains a **deterministic scientific workflow**, with LangChain used narrowly for schema-constrained literature extraction and verification rather than for autonomous KG construction.

However, the deterministic project-data layer now has two additional/clarified inputs that should be reflected in the implementation.

## Neighborhood-definition ingestion

Spatial Niche 1/Niche 2 states were defined by clustering focal cells jointly across Control and IPF using their local neighborhood composition.

For every focal cell:

```text
k nearest spatial neighbors = 25
```

were classified by cell type, and the resulting 25-neighbor composition vector was used for clustering.

Control/IPF condition was **not used to define the niche clusters**. Condition was applied only to downstream summaries and molecular analyses.

Therefore:

```text
SpatialNicheState
```

is condition-pooled at definition time, while:

```text
NicheExpressionSignature
ChromLinkerObservation
TFNomination
```

may carry `condition = Control | IPF`.

Add a deterministic parser such as:

```text
project_data/
    neighborhood.py
```

producing:

```text
neighborhood_profiles.parquet
```

No LangChain/LLM component is needed for this transformation.

## Yale niche-expression-signature ingestion

The Yale pooled expression-signature file is the intended current Niche2-versus-Niche1 comparison output.

It provides:

```text
mean log-normalized expression in each niche
Niche2 − Niche1 mean-expression difference
fraction of cells expressing each gene
cell counts
```

but it does **not** provide donor/sample-aware:

```text
p-values
FDR
formal log2FC
```

Therefore the deterministic project-data module should be:

```text
project_data/
    niche_expression_signatures.py
```

rather than treating the current file as formal differential expression.

Its canonical object should be:

```text
NicheExpressionSignature
```

or `ExpressionContrastObservation`, not `DEAnalysis`.

A future:

```text
differential_expression.py
```

module may be retained only as an optional extension if a true sample-aware DE analysis is produced later.

The project-data portion of the pipeline is now:

```text
Neighborhood tables
      ↓
deterministic Python
      ↓
NeighborhoodProfile

Yale pooled signatures
      ↓
deterministic Python
      ↓
NicheExpressionSignature

Pseudobulk CPTT
      ↓
deterministic Python
      ↓
ExpressionObservation

ChromLinker matrix
      ↓
deterministic Python
      ↓
ChromLinkerObservation

                     ┌────────────────────────┐
                     │ no LLM required above │
                     └────────────────────────┘

Literature candidate passages
      ↓
LangChain `with_structured_output()`
      ↓
RegulatoryClaimExtraction
      ↓
structured verifier
      ↓
deterministic validation
      ↓
Neo4j
```

This reinforces rather than changes the original LangChain decision:

> **LangChain belongs in the literature interpretation layer, not in the quantitative Spatial NicheLinker data-ingestion layer.**

The updated implementation mapping is:

```text
Neighbor-composition parsing       → pandas/Python
Niche-expression-signature parsing → pandas/Python
Pseudobulk parsing                 → pandas/Python
ChromLinker parsing                → pandas/Python
Program/signature analysis         → scipy/Python
Literature retrieval               → deterministic Python
Regulatory claim extraction        → LangChain structured model
Claim verification                 → LangChain structured model
Final acceptance                   → deterministic validation
Scientific evidence graph          → Neo4j
```

No DeepAgents or autonomous LangGraph workflow is introduced by these new data sources.

# Implementation update: literature processing, evidence validity, and Neo4j

Research/design review dated 2026-09-21. The project remains a deterministic workflow with narrow structured model calls. Sections 18–21, 29, 38–49, and 63–65 of [the final synthesis](chatgpt_final_synthesis.md) define the detailed policies.

## Literature workflow and contracts

```text
versioned candidate queries and retrieval coverage
    ↓
identifier-deduplicated publications and eligible source assets
    ↓
XML/BioC first; Docling PDF fallback
    ↓
canonical document + source locators + structured supplements
    ↓
normalized entities + BM25 + selected biomedical embeddings
    ↓
bounded evidence bundles with exact spans
    ↓
LangChain structured extractor → structured verifier
    ↓
deterministic validity and evidence-eligibility checks
    ↓
accepted / uncertain / rejected artifacts
    ↓
fixed, idempotent Neo4j writer
```

Version stage inputs, source hashes, schemas, prompts, models, and parser outputs. Cache successful stage results and resume from a local run manifest. Workflow retries cannot create duplicate observations. LangSmith is optional; raw extraction and verification outputs remain in project storage.

Preserve negative and null experimental findings. Support and contradiction refer to a particular proposition; context match is computed relative to a nomination. An extraction's acceptance is independent of whether it supports the nominated TF. Unknown experimental identity remains unknown, and multiple databases reusing one study do not establish replication.

Check source locators, entity identity, assay/directness, and negative/null outcomes with a small regression set. No dedicated NLP benchmark or model comparison is required. Preserve the no-curator constraint without claiming automated agreement is ground truth; evaluate the paper contribution through biological nominations, independent evidence, and robustness.

## Analysis stays outside the LLM layer

Evaluate signed CollecTRI/decoupler ULM concordance as an exploratory baseline for the pooled expression contrasts. Keep cell counts, regulon coverage, and unknown donor coverage visible; do not interpret method p-values as donor-level significance. Group connectivity, expression-program concordance, and external experimental evidence before rank fusion. Retain coverage and dependency information, compare route-specific baselines, and assess sensitivity to studies and evidence groups.

## Neo4j deployment and integration

Use the official `neo4j` Python driver with Pydantic-validated records, parameterized Cypher, stable IDs, uniqueness constraints, bounded `UNWIND` batches, and idempotent managed transactions. Transaction callbacks may be retried, so keep model/API calls and filesystem side effects outside them. The graph writer is independent of LangChain and uses fixed queries; no generated Cypher or generic LLM graph builder is required. [Neo4j transaction documentation](https://neo4j.com/docs/python-manual/current/transactions/)

**Default: local Neo4j Community for the development graph.** A version-pinned Docker deployment with persistent storage is suitable. **AuraDB Free: optional selected AT1 demo**, with no local server installation needed. Its current quota is 50,000 nodes / 175,000 relationships; estimate materialized size before loading and retain rebuild artifacts separately. The capacity calculation, lifecycle constraints, configuration variables, and import checks are documented in sections 21 and 64 of the final synthesis. [Aura Free](https://neo4j.com/free-graph-database/)

Cloud/local selection changes connection configuration and the explicit materialization scope, not scientific semantics. Full matrices, document assets, uncertain findings, and optional embeddings remain outside the graph. A later FastAPI/MCP service exposes the same evidence model to LungMAP and LungChat.
