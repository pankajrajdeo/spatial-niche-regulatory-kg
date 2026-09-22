I went back through the current conversation, the uploaded Spatial NicheLinker discussion, the older DPI-KG architecture/first-principles/schema documents, Shunya’s two matrices, and the advisor literature package. The main thing is that several earlier ideas were scientifically useful but are **now too broad for what you actually need to deliver**.

What follows is the version I would freeze and implement. I would stop redesigning the project after this unless Shunya/Nathan changes the scientific question.

# Final synthesis: Spatial NicheLinker Regulatory Evidence KG

> **Scope:** This is a biomedical evidence-KG contribution to a bioinformatics paper. Literature processing is supporting infrastructure. The MVP does not include an NLP benchmark, model-training project, embedding-model comparison, or retrieval-method contribution. Scientific evaluation centers on TF nominations, biological context, independent evidence, and reproducibility.

## 1. What the project actually is now

The primary scientific project is **Spatial NicheLinker**.

Its biological question is:

> Can cells of the same annotated cell type occupy different cellular neighborhoods and, as a consequence or correlate of that context, exhibit different transcriptional and regulatory states?

The project flows conceptually as:

```text
CELLULAR NEIGHBORHOOD
        ↓
SPATIAL NICHE
        ↓
CELL STATE
        ↓
NICHE-ASSOCIATED GENE PROGRAM
        ↓
MAP STATE INTO scRNA / MULTIOME
        ↓
RNA + CHROMATIN ACCESSIBILITY
        ↓
ChromLinker
        ↓
CANDIDATE TF → TARGET RELATIONSHIPS
        ↓
REGULATORY EVIDENCE KG
        ↓
TF NOMINATION
        ↓
EXPERIMENTAL FOLLOW-UP
```

Your component begins **after ChromLinker and the niche-associated transcriptional programs exist**.

Your deliverable is:

> **A literature-grounded, context-aware regulatory evidence KG that takes TF–target predictions and niche-associated gene programs from Spatial NicheLinker/ChromLinker and nominates a small, explainable set of transcription factors for follow-up, while preserving the exact evidence, assay, cell context, disease context, direction, directness, contradictions and provenance supporting each nomination.**

That is substantially narrower than the original standalone DPI-KG.

The original DPI architecture remains useful because it correctly insisted that TF regulation cannot be collapsed into a generic edge, that context must be explicit, that experimental evidence needs provenance, and that duplicate databases should not masquerade as independent evidence. :chatgpt-content-reference{index="1"}

---

# 2. What this project is NOT

Do **not** turn this into:

- a universal human regulatory KG;
- a PubMed-scale literature extraction project;
- BioAgentKG;
- a LangGraph/DeepAgents project;
- an autonomous scientific-agent project;
- a GLiNER benchmark;
- a PubMedBERT fine-tuning project;
- a new TF-ranking neural network;
- a GNN;
- a GWAS/QTL/drug-discovery platform;
- a database containing millions of single cells;
- a complete enhancer atlas;
- a system that parses every figure in every paper;
- a system that claims ChromLinker edges are causal regulation.

BioAgentKG remains a **separate agentic project**. Do not bring its Propose–Verify–Challenge–Revise architecture into this KG.

For Spatial NicheLinker, a deterministic scientific ETL/evidence pipeline is preferable.

---

# 3. The most important scientific distinction

A ChromLinker result such as:

```text
ETV1 → Gene X
score = ...
```

must **not** become:

```text
(:ETV1)-[:REGULATES]->(:GeneX)
```

in the KG.

ChromLinker gives an **inferred regulatory connection from the project's multiome analysis**.

The literature may independently provide things such as:

```text
ETV1 binds a regulatory region of Gene X
ETV1 knockdown changes Gene X
ETV1 activates Gene X in a reporter assay
ETV1 and Gene X are merely correlated
```

Those are fundamentally different forms of evidence.

The original DPI architecture already captured the right scientific decomposition:

- **B** = TF binding/occupancy;
- **L** = regulatory locus → gene support;
- **R** = regulatory effect after changing the TF.

Binding without functional effect does not prove regulation; perturbation without binding may be indirect. :chatgpt-content-reference{index="2"}

For the MVP, we preserve that philosophy but **do not require a full genomic-locus layer for every claim**.

---

# 4. What data we currently have

## A. Shunya's ChromLinker matrix

I inspected:

`Yale_IPF_with_Niches_tf_to_gene_connection_scores_log10.csv`

It contains:

| Property | Current data |
|---|---:|
| TF–gene rows | **26,822** |
| Unique TFs | **280** |
| Unique target genes | **5,541** |
| Context columns | **45** |
| Total columns | 47 |

Structure:

```text
TF
Gene
Control.AT1_niche_1
Control.AT1_niche_2
...
IPF.AT1_niche_1
IPF.AT1_niche_2
...
```

All the currently discussed manuscript TFs are present in this matrix:

```text
TEAD1
KLF5
GATA6
FOXA2
ETV1

SPI1
EGR2
BHLHE41
TFEC
IRF8
CEBPB

RFX2
FOSB
ATF3
```

### Important caution

The filename says `connection_scores_log10`.

Until Shunya confirms exactly:

```text
what the score mathematically represents
what the log10 transformation is
what 0 means
how TF-level aggregate scores were generated for the manuscript
```

we should **store and reshape the values exactly as supplied**, but not invent our own biological interpretation of score differences.

This does not block ingestion.

It only blocks the final interpretation of aggregate ChromLinker rank.

---

# 5. Shunya's pseudobulk RNA matrix

The uploaded pseudobulk file contains **36,601 genes across 100 biological populations**, including Control/IPF and the niche populations relevant to us. Its header explicitly includes AT1, alveolar macrophage, activated-fibrotic-fibroblast and KRT5−/KRT17+ niche columns. :chatgpt-content-reference{index="3"}

Every one of the **45 ChromLinker contexts is also present in the pseudobulk matrix**.

Most importantly, there are 12 niche-specific matched contexts:

```text
Control.AT1_niche_1
Control.AT1_niche_2

IPF.AT1_niche_1
IPF.AT1_niche_2

Control.Alveolar_Macrophages_niche_1
Control.Alveolar_Macrophages_niche_2

IPF.Alveolar_Macrophages_niche_1
IPF.Alveolar_Macrophages_niche_2

IPF.Activated_Fibrotic_FBs_niche_1
IPF.Activated_Fibrotic_FBs_niche_2

IPF.KRT5neg_KRT17pos_niche_1
IPF.KRT5neg_KRT17pos_niche_2
```

The expression matrix additionally has Control niche populations for activated fibrotic fibroblasts and KRT5−/KRT17+ cells, although those corresponding Control niche columns are not in this ChromLinker matrix.

### What the pseudobulk gives us now

It gives:

```text
gene expression support
TF expression support
target expression support
descriptive Niche1/Niche2 expression differences
```

It does **not** give inferential DE statistics.

Therefore do not generate a fake `log2FC/q-value` layer from this matrix.

Use the values as:

```text
ExpressionObservation
```

as supporting expression evidence alongside the Yale pooled niche-expression signature.

---

# 6. Optional future sample-aware differential-expression analysis

If a sample-aware DE analysis is produced in the future, its output could add an inferential evidence layer:

```text
cell_type
condition
niche/comparison
gene
log2FC
p_value
q_value
direction
pct_expression_case
pct_expression_reference
```

If some fields are unavailable, that is fine.

If that future sample-aware DE analysis becomes available, we can create:

```text
IPF_AT1_Niche2_vs_Niche1_UP
IPF_AT1_Niche2_vs_Niche1_DOWN

Control_AT1_Niche2_vs_Niche1_UP
...

IPF_AM_Niche2_vs_Niche1_UP
...
```

as explicit `GeneProgram` objects.

The **DE table does not require a redesign**.

It plugs into the architecture.

---

# 7. One small metadata clarification still needed from Shunya

Not another data export—just eventually get the answers to:

```text
What exactly is the ChromLinker connection score?

How was it log-transformed?

What does score == 0 mean?

How were the aggregate TF scores used in the manuscript calculated?

What exact ChromLinker software/code/run version produced this matrix?
```

Until then we preserve the raw score.

Do not block development on this.

---

# 8. The advisor literature package: what it actually is

I inspected the package directly.

It contains two curated paper sets:

```text
46 TF / target / lung-disease papers

71 experimental-edge papers
```

with seven overlapping PMIDs, giving:

> **110 unique PMIDs**

The first package was built from **1,962 screened PMIDs**.

The experimental-edge package was built from **2,429 screened PMIDs**.

It contains:

```text
selected-paper CSVs
PubMed metadata
abstracts
search logs
query parameters
reproducible Python scripts
```

But importantly:

> **No full paper was read when that package was created.**

And the experimental-edge README explicitly says that GEO/ENCODE accession extraction remains a next step.

So your advisor did **not** hand you a finished evidence KG.

He handed you an extremely useful:

> **seed corpus + search strategy + resource inventory.**

That is exactly how we should use it.

---

# 9. Why those papers are not sufficient

The selected metadata is heavily useful for NKX2-1 and contains some FOXA2/EGR2 coverage.

But if I search the selected CSV metadata—not the entire text of the papers—for the manuscript candidates, explicit hits are approximately:

```text
NKX2-1       10 papers
FOXA2         2
EGR2          2

TEAD1         0
KLF5          0
GATA6         0
ETV1          0
SPI1          0
BHLHE41       0
TFEC          0
IRF8          0
CEBPB         0
RFX2          0
FOSB          0
ATF3          0
```

That does **not** prove those TFs are absent from the full papers.

It shows that the current 110-PMID package cannot be treated as a candidate-complete literature corpus.

Also, the advisor's search used a 2015–2026 date cutoff.

Mechanistic TF biology frequently predates 2015.

Therefore:

> Use the advisor package as the **seed**, then dynamically retrieve literature around the actual Spatial NicheLinker candidates.

This matches the original DPI plan, which recommended focused TF/gene-seeded retrieval, citation expansion and database-linked papers rather than whole-PubMed ingestion. :chatgpt-content-reference{index="4"}

---

# 10. Final KG architecture

I would freeze the **MVP node vocabulary** to this.

### Biological/project entities

```text
Gene
CellType
BiologicalContext
SpatialNicheState
NeighborhoodProfile
GeneProgram
Pathway
BiologicalProcess

Dataset
AnalysisRun
```

### Project evidence

```text
ChromLinkerObservation
ExpressionObservation
NicheExpressionSignature
```

### Literature evidence

```text
RegulatoryClaim
EvidenceAssertion
Passage
Publication
Experiment
Study
```

`Experiment` and `Study` are created when the underlying experiment can actually be resolved.

### Output

```text
TFNomination
```

### Optional, later

```text
RegulatoryLocus
BindingObservation
LocusGeneLink
PerturbationPrediction
```

---

# 11. Gene and TF representation

Do not create separate biological classes for genes and TFs.

Use:

```text
(:Gene {
    symbol: "ETV1",
    hgnc_id: "...",
    ensembl_id: "...",
    species: "human",
    is_tf: true,
    tf_family: "ETS"
})
```

A TF is still a gene.

This also allows:

```text
TF-A → TF-B → downstream targets
```

without schema hacks.

Normalize genes with species-specific stable identifiers and versioned alias mappings. Preserve the source mention and mapping status. A complex or family mention must not silently become a claim about an individual gene: represent resolved `RegulatoryComplex` / `TFFamily` entities when needed, or retain the unresolved mention outside gene-specific scoring. Membership alone does not transfer a complex-level finding to each member. [CollecTRI complex handling](https://decoupler.readthedocs.io/en/stable/api/generated/decoupler.op.collectri.html)

---

# 12. SpatialNicheState must remain separate from BiologicalContext

This was one of the best improvements we made during the discussion.

`Human / lung / AT1 / IPF` is biological context.

`AT1 Niche 2` is **algorithm-derived**.

It depends on:

```text
dataset
neighborhood definition
cell annotations
Spatial NicheLinker version
clustering procedure
parameters
```

Therefore:

```text
(:CellType {name:"AT1"})
       |
       | HAS_NICHE_STATE
       v
(:SpatialNicheState {name:"AT1_Niche2"})
```

and project observations additionally link to:

```text
(:BiologicalContext {
   species:"human",
   tissue:"lung",
   cell_type:"AT1",
   disease:"IPF"
})
```

Do not encode `Niche2` as if it were a universal biological ontology term.

---

# 13. ChromLinker representation

One matrix value becomes something conceptually like:

```text
(:ChromLinkerObservation {
    score_log10: ...,
    origin: "predicted",
    matrix_column: "IPF.AT1_niche_2"
})
```

connected as:

```text
ChromLinkerObservation
      ├──PREDICTS_TF──────▶ ETV1
      ├──PREDICTS_TARGET──▶ GeneX
      ├──FOR_STATE────────▶ AT1_Niche2
      ├──IN_CONTEXT───────▶ Human_Lung_IPF_AT1
      └──GENERATED_BY─────▶ ChromLinker_Run_X
```

It does **not** create a truth edge.

---

# 14. Expression representation

Similarly:

```text
ExpressionObservation
      ├──OF_GENE──────────▶ ETV1
      ├──FOR_STATE────────▶ AT1_Niche2
      ├──IN_CONTEXT───────▶ Human_Lung_IPF_AT1
      └──GENERATED_BY─────▶ RNA_Pseudobulk_Run
```

Property:

```text
value_cptt
```

Do not interpret absence of TF differential expression as absence of TF activity.

TF activity can change through:

```text
phosphorylation
nuclear localization
cofactor availability
chromatin accessibility
ligand signaling
```

So TF RNA is a **supporting feature**, not a mandatory gate.

---

# 15. Optional future sample-aware differential-expression representation

If a future sample-aware DE analysis becomes available (not the current Yale pooled niche-expression signature):

```text
DEAnalysis
   ├──CASE_STATE──────▶ AT1_Niche2
   ├──REFERENCE_STATE─▶ AT1_Niche1
   ├──IN_CONTEXT──────▶ Human_Lung_IPF_AT1
   └──GENERATED_BY────▶ AnalysisRun
```

Then:

```text
Gene
 └──DE_IN {
       log2FC,
       p_value,
       q_value,
       pct_case,
       pct_reference,
       direction
   }
      ────────────────▶ DEAnalysis
```

The old DPI design explicitly warns that DE tells you **what changed**, not which TF caused the change. :chatgpt-content-reference{index="5"}

Keep that rule.

---

# 16. GeneProgram

Using the Yale pooled niche-expression signature, create ranked niche-expression programs such as:

```text
AT1_IPF_Niche2_Higher_Expression_Program
AT1_IPF_Niche1_Higher_Expression_Program
```

rather than one vague:

```text
AT1 Niche2 genes
```

This captures the descriptive contrast without implying statistical significance.

Then:

```text
SpatialNicheState
   └──HAS_PROGRAM──▶ GeneProgram

GeneProgram
   └──CONTAINS_GENE {direction, effect_niche2_minus_niche1, rank}
                    ──▶ Gene
```

And pathway analysis:

```text
GeneProgram
    └──ENRICHED_FOR {p_value, q_value}
                    ──▶ Pathway
```

Use Reactome/GO structured annotations rather than asking the LLM to invent pathway membership.

---

# 17. The central literature object: RegulatoryClaim

Do not write:

```text
FOXA2 -[:ACTIVATES]-> SFTPC
```

as universal truth.

Write:

```text
FOXA2
  │
  └──REGULATOR_OF_CLAIM──▶ RegulatoryClaim
                                 │
                                 ├──TARGET_GENE──▶ SFTPC
                                 ├──IN_CONTEXT───▶ Context
                                 └──HAS_EVIDENCE─▶ EvidenceAssertion
```

Example claim properties:

```yaml
relation: regulates
direction: positive
directness: direct
measured_or_inferred: measured
status: auto_accepted
```

The actual evidence remains separate.

---

# 18. EvidenceAssertion

This is where the science lives.

Use evidence types such as:

```text
TF_BINDING
TF_PERTURBATION
TF_BINDING_PLUS_PERTURBATION
REPORTER_ASSAY
CRE_PERTURBATION
EXPRESSION_ASSOCIATION
COMPUTATIONAL_NETWORK
CURATED_LITERATURE
PROTEIN_INTERACTION
```

And separate:

```text
directness:
    DIRECT
    FUNCTIONAL
    ASSOCIATIVE
    PREDICTED
    UNCLEAR
```

Also store:

```text
polarity:
    supports
    contradicts
    inconclusive

assay:
    ChIP-seq
    CUT&RUN
    CUT&Tag
    knockdown
    knockout
    CRISPRi
    overexpression
    luciferase
    RNA-seq
    etc.

extraction_status:
    AUTO_ACCEPTED
    UNCERTAIN
    REJECTED

experimental_outcome:
    INCREASE
    DECREASE
    NO_DETECTED_EFFECT
    BINDING_DETECTED
    NO_BINDING_DETECTED
    UNCLEAR

statement_status:
    AFFIRMED
    NEGATED
    SPECULATIVE
    UNCLEAR
```

---

Extraction validity, experimental outcome, directness, and evidence polarity are separate dimensions. A correctly extracted negative result can be accepted evidence. `NO_RELATION` means no relevant relation or experimental finding is stated; it does not mean that an experiment detected no effect.

Keep findings atomic by assay, target, and experimental context. Combine binding and functional-effect findings only through explicit compatible evidence links; co-occurrence in a paper does not establish a shared experiment or direct regulation. A null result is qualified by its assay, sensitivity, controls, and conditions; it is not universal proof of no regulation.

Store original experimental context on the finding. Compute `context_match = exact | close | partial | mismatched | unknown` relative to a particular nomination, with species, cell type, disease, and model-system components plus a versioned matching rule. Support/contradiction is also relative to a specified proposition and context. [SEPIO evidence model](https://github.com/monarch-initiative/SEPIO-ontology)

# 19. Literature provenance

Every accepted claim should lead all the way back to:

```text
RegulatoryClaim
      ↓
EvidenceAssertion
      ↓
Passage
      ↓
Publication
```

Where resolvable:

```text
EvidenceAssertion
      ↓
Experiment
      ↓
Study
      ↓
Publication
```

This matters because three databases may simply reprocess the same GEO experiment.

The old architecture explicitly requires deduplication at the experiment/study level instead of treating multiple databases as independent replication. :chatgpt-content-reference{index="6"}

Useful independence keys include:

```text
PMID
DOI
GEO
SRA
ENCODE experiment
BioProject
other study accession
```

A PMID identifies a publication, not a unique experiment. An accession may identify a study containing several experiments. Preserve accession type, experiment details, and dependency groups; unknown experiment identity stays unknown. Do not count unresolved records as independent replication by default.

Use stable application IDs and retain source checksums, retrieval times, parser/model/prompt/schema versions, and analysis-run IDs. Reprocessing must be reproducible and must not duplicate evidence.

---

# 20. Regulatory loci and B/L/R: keep, but don't make them block the MVP

Long-term, this remains scientifically ideal:

```text
TF
 ↓ B
RegulatoryLocus
 ↓ L
Gene

TF perturbation
 ↓ R
Gene response
```

But do **not** first ingest every enhancer and ChIP peak in existence.

For v1:

```text
RegulatoryLocus = optional
```

Create one when a high-value paper/resource gives a credible regulatory element or coordinate.

Meanwhile `EvidenceAssertion` can record:

```text
binding evidence present
locus→gene evidence present
regulatory-effect evidence present
```

The richer dual-resolution locus graph can grow later.

---

# 21. Final database architecture

## Deployment: local Community for development; Aura Free for a bounded demo

Use self-managed **Neo4j Community Edition** for the main development graph, preferably via a version-pinned official Docker image with persistent storage. It avoids Aura Free's small graph quota; actual capacity still depends on the host's memory, disk, and workload. A native installation is an alternative. [Official Docker setup](https://neo4j.com/docs/operations-manual/current/docker/introduction/)

**AuraDB Free is a valid cloud option for a deliberately selected AT1 demo.** It requires no local database server. As checked on 2026-09-21, the official limit is **50,000 nodes and 175,000 relationships**, with no included database backups. [Aura Free limits](https://neo4j.com/free-graph-database/)

Aura Free pauses after **72 hours of inactivity** and is deleted if it remains paused for **more than 30 days**. Keep reproducible source/processed artifacts and exports outside the database. [Instance lifecycle](https://neo4j.com/docs/aura/managing-instances/instance-actions/)

Measured from the supplied ChromLinker CSV:

| Scope | Matrix values | Nonzero values |
|---|---:|---:|
| All 45 contexts | 1,206,990 | 387,835 |
| Four AT1 niche contexts | 107,288 | 36,253 |

These are data counts, not a rule to discard zeros. Under the five-relationship observation model in section 13, even materializing only the 36,253 nonzero AT1 observations would require **181,265 relationships**, before genes, expression, claims, or provenance are added. A complete AT1 observation graph therefore cannot be assumed to fit Aura Free.

Keep full observations in Parquet. Define and version an explicit graph materialization policy for selected candidates, targets, summaries, and evidence. Estimate node/relationship counts before each import; do not silently truncate to satisfy hosting limits. A cloud demo uses a documented subset of the same scientific model. See section 64 for integration details.

---

### Do not use SQL only

Graph questions are central:

```text
Niche2
 → GeneProgram
 → Genes
 ← RegulatoryClaims
 ← TF
 → other targets
 → Pathways
```

and:

```text
TF
 → Claim
 → Evidence
 → Passage
 → Paper
 → Experiment
```

Neo4j makes that natural.

### Do not switch to FalkorDB now

Not because FalkorDB is inherently unsuitable.

Because there is **no project requirement that FalkorDB solves better enough to justify changing the stack**.

Your bottleneck is evidence quality, not graph traversal throughput.

### Do not create Postgres either

Use:

```text
Neo4j
    canonical graph

Parquet / JSONL
    large tabular intermediates

Filesystem/object storage
    XML/PDF/supplements/model artifacts

DuckDB
    optional local analysis over Parquet
```

That is enough.

---

# 22. Graph versus warehouse

Do not put the original matrices into Neo4j.

The old architecture explicitly says:

> graph ≠ raw warehouse. :chatgpt-content-reference{index="8"}

So:

```text
NEO4J
────────────────────────
Genes
TFs
Niche states
Gene programs
summarized observations
claims
evidence
publications
experiments
pathways
nominations


PARQUET / FILE STORE
────────────────────────
full ChromLinker matrix
full pseudobulk matrix
niche expression signatures (and optional future sample-aware DE tables)
full supplementary tables
paper XML
PDFs
candidate passages
LLM extraction responses
uncertain claims
embeddings
```

---

# 23. Exact transformation of Shunya's ChromLinker matrix

First transform:

```text
WIDE

TF | Gene | Control.AT1_niche_1 | Control.AT1_niche_2 | ...


                         ↓ melt


LONG

TF
target_gene
condition
cell_type
niche
score_log10
raw_context_label
```

Output:

```text
data/processed/chromlinker_observations.parquet
```

Do not discard the source label.

Example:

```text
raw_context_label =
IPF.Activated_Fibrotic_FBs_niche_2

condition = IPF

cell_type_raw =
Activated_Fibrotic_FBs

cell_type_normalized =
activated fibrotic fibroblast

niche =
2
```

Keep both normalized and raw labels.

---

# 24. Zero values

Do not assume:

```text
0 = biological absence
```

yet.

Preserve them in the raw/processed Parquet.

Once the ChromLinker score definition is confirmed, decide whether zero means:

```text
no predicted edge
below threshold
missing score
transformed zero
```

Only then decide what is materialized into Neo4j.

---

# 25. Transforming the pseudobulk matrix

Similarly:

```text
gene | context | CPTT
```

Output:

```text
expression_observations.parquet
```

Do **not** put all 3.6M gene-context values into Neo4j.

Materialize graph observations primarily for:

```text
TFs
ChromLinker target genes
genes in the ranked niche-expression program
nomination-relevant genes
```

Keep the rest in Parquet.

---

# 26. Initial biological priority

Do **AT1 first**.

It is the clearest use case and has both Control and IPF paired niches.

Initial TF set:

```text
TEAD1
KLF5
GATA6
FOXA2
ETV1
```

Then:

### Alveolar macrophage

```text
SPI1
EGR2
BHLHE41
TFEC
IRF8
CEBPB
```

### KRT5−/KRT17+

```text
TEAD1
KLF5
RFX2
```

### Activated fibrotic fibroblast

```text
FOSB
TEAD1
+ whatever additional TFs emerge from the actual ranking
```

Once AT1 works end-to-end, every subsequent cell type uses the same pipeline.

---

# 27. Candidate generation must have TWO routes

This is essential.

## Route A: ChromLinker-first

```text
ChromLinker
   ↓
candidate TF
   ↓
candidate target genes
   ↓
overlap with niche program
   ↓
literature evidence
   ↓
TF nomination
```

## Route B: Gene-program-first

```text
Niche expression signature
   ↓
known TF-target networks
   ↓
TF enrichment
   ↓
candidate TF
   ↓
literature evidence
   ↓
TF nomination
```

This enables the KG to find:

> a literature-supported TF regulating many Niche2 genes that ChromLinker did not rank highly.

That is much more interesting than merely confirming ChromLinker.

---

# 28. Structured prior resources

Use existing TF-target resources as **candidate/evidence priors**, not as truth.

Useful immediate sources:

### CollecTRI

It provides curated TF-target interactions, signed mode-of-regulation weights and, when available, supporting PMIDs. :chatgpt-content-reference{index="9"}

### TRRUST

TRRUST v2 contains literature-curated human and mouse TF-target regulatory interactions, including mode-of-regulation information for many interactions. :chatgpt-content-reference{index="10"}

### hTFtarget

Useful for ChIP-derived human TF-target predictions across experimental contexts; the published resource integrated 7,190 ChIP-seq samples representing hundreds of TFs. :chatgpt-content-reference{index="11"}

### KnockTF

Useful for the functional-regulation side: KnockTF 2.0 collects TF/cofactor knockdown/knockout expression datasets across tissues/cell types and species. :chatgpt-content-reference{index="12"}

These resources serve different evidence purposes.

Do not combine them into:

```text
4 databases support this edge
```

unless they correspond to four independent studies.

---

# 29. TF enrichment against niche programs

Using the Yale pooled niche-expression signature:

For every TF:

```text
known targets of TF
        ∩
niche gene program
```

Prefer enrichment using the complete signed/ranked niche-expression signature. If a binary gene set is derived using an explicitly documented analysis threshold, Fisher's exact test can assess target overlap; that threshold does not imply differential-expression significance.

For a binary-set analysis, document the eligible gene background; genes expressed in either relevant pseudobulk niche can serve as a provisional background. If a future sample-aware DE analysis is used, prefer the genes actually tested in that analysis.

For Fisher's exact test, report:

```text
overlap_count
target_set_size
program_size
odds_ratio
p_value
FDR
```

This becomes an important nomination feature.

For the first signed-regulon baseline, evaluate **CollecTRI + decoupler ULM** against the descriptive Niche2-minus-Niche1 vector. Record network version, signed edges, mapped/eligible target counts, target coverage, and filtering rules. Call the output **regulon–signature concordance** or an **exploratory inferred activity contrast**; it is not measured TF activity. ULM is a concrete baseline to evaluate on these inputs, not an already validated choice for this dataset. Its model-based p-values do not establish donor-level differential activity. [CollecTRI study](https://pubmed.ncbi.nlm.nih.gov/37843125/), [ULM method](https://decoupler.readthedocs.io/en/stable/api/generated/decoupler.mt.ulm.html)

Check sensitivity to expression-detection filters, influential targets, and regulon coverage. Preserve complex-level regulators. Fisher enrichment remains an optional, explicitly thresholded companion analysis, with its own background and null hypothesis.

---

# 30. Dynamic literature retrieval

“Dynamic retrieval” does **not** mean an autonomous agent.

It means the current project data automatically determines which queries are generated.

For example, when AT1 IPF produces:

```text
ETV1
```

and high-scoring targets overlapping the ranked niche-expression program:

```text
GeneA
GeneB
GeneC
```

the software generates searches such as:

```text
ETV1 AND GeneA AND regulation

ETV1 AND GeneA AND
(ChIP OR CUT&RUN OR knockdown OR knockout OR CRISPR)

ETV1 AND
(lung OR alveolar OR pulmonary)

ETV1 AND
(IPF OR fibrosis)

ETV1 AND
(epithelial OR AT1 OR alveolar epithelial)

ETV1 AND
(transcriptional regulation OR target genes)
```

The retrieval set changes whenever:

```text
ChromLinker changes
niche expression signatures change
candidate ranking changes
```

That is dynamic retrieval.

No agent planner is needed.

Version and cache queries, pagination, date windows, retrieved identifiers, source versions, and retrieval reasons. Deduplicate PMID/PMCID/DOI records and preserve correction/retraction metadata when available. Record `NOT_SEARCHED`, `SEARCHED_NO_SUPPORT_FOUND`, `ABSTRACT_ONLY`, `FULL_TEXT_PROCESSED`, and `FETCH_FAILED` coverage separately. Search both supportive and negative findings; retrieval failure and lack of accessible text are not evidence against a TF. Use bounded retries, provider rate limits, and `Retry-After` handling.

---

# 31. Retrieval priority

Do not issue 26,822 PubMed pair searches.

Create a priority queue.

Initially:

```text
top ~15 TFs per niche comparison

+

top target edges for those TFs

+

targets overlapping the niche expression signature

+

literature-derived TF candidates from enrichment
```

Then retrieve deeply around those.

---

# 32. Literature source hierarchy

Use:

```text
1. advisor seed corpus
2. PubTator relation/entity search
3. PubMed / Europe PMC targeted search
4. structured TF-target resources
5. citation expansion from valuable papers
```

PubTator 3.0 already provides biomedical entity normalization and searchable entity/relation annotations over PubMed and the PMC-OA full-text subset, so it is an excellent retrieval and normalization layer. :chatgpt-content-reference{index="13"}

But:

> PubTator relations are not automatically your final regulatory evidence.

Your ontology needs finer distinctions such as binding versus perturbation versus activation versus association.

---

# 33. Full-text acquisition

The order should be:

```text
PMID
 │
 ▼
Europe PMC / PMC structured OA text available?
 │
 ├── YES → XML/BioC
 │
 └── NO
       │
       ▼
authorized/accessibly supplied PDF?
       │
       ├── YES → Docling
       └── NO  → abstract/metadata only
```

Europe PMC provides:

```text
fullTextXML
references
supplementaryFiles
```

for eligible full-text/open-access content. :chatgpt-content-reference{index="14"}

That means:

> **XML first. PDF parsing second.**

Do not start by downloading every PDF.

Resolve and record access/reuse status per article and asset. PMC availability does not imply that every article is available for text mining; use the documented retrieval services and eligible subsets. Store source URL, identifier, retrieval time, license/access status, and checksum. Keep acquisition failures separate from evidence absence. [PMC developer guidance](https://pmc.ncbi.nlm.nih.gov/tools/developers/)

Normalize XML/BioC and PDF fallback into the same versioned document contract. Preserve sections, paragraph IDs, table cells/headers/footnotes, caption links, and source locators. For XML keep element IDs or paths; for PDFs keep page/item references and bounding boxes where available. Canonical-text offsets must identify the exact parser version and text artifact. PubTator offsets refer to its own text representation and require checked alignment before reuse. [PubTator paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC11223843/), [Docling document model](https://docling-project.github.io/docling/reference/docling_document/)

---

# 34. Docling versus LiteParse

Freeze this decision:

> **Use Docling only as PDF fallback. Do not add LiteParse right now.**

Docling's full PDF pipeline already handles:

- document layout;
- OCR;
- table structure extraction;
- figures/picture regions;
- structured document output. :chatgpt-content-reference{index="15"}

Maintaining two PDF extraction engines buys you very little for this deadline.

---

# 35. Paper folder structure

Use:

```text
papers/
└── PMID_12345678/
    │
    ├── metadata.json
    │
    ├── source/
    │   ├── article.xml
    │   └── article.pdf
    │
    ├── parsed/
    │   ├── document.json
    │   ├── content.md
    │   ├── sections.jsonl
    │   ├── figure_captions.jsonl
    │   └── tables/
    │       ├── table_01.csv
    │       └── ...
    │
    ├── supplementary/
    │   ├── raw/
    │   └── parsed/
    │
    ├── retrieval/
    │   └── candidate_passages.jsonl
    │
    ├── extraction/
    │   ├── claims.jsonl
    │   ├── verifier.jsonl
    │   ├── uncertain.jsonl
    │   └── rejected.jsonl
    │
    └── provenance/
        └── run.json
```

`document.json` is canonical.

`content.md` exists mainly for debugging/readability.

---

# 36. Figures

Do **not** extract every figure image.

Always extract:

```text
figure caption
```

because captions often describe experiments.

Do not routinely create:

```text
figures/Figure1.png
figures/Figure2.png
...
```

The earlier DPI design independently reached the same conclusion: vision extraction should be deferred and not drive scoring unless a measured panel contains otherwise unavailable evidence. :chatgpt-content-reference{index="16"}

Given that you have **no human reviewer**, I would be even stricter:

> **No figure-VLM claim should contribute to TF nomination in v1.**

At most use figure images for discovery.

---

# 37. Tables and supplements

These matter much more than figure pixels.

Priority:

```text
CSV
TSV
XLSX
XLS
```

then:

```text
XML
HTML
DOCX
```

then supplementary PDF only when necessary.

Structured supplemental tables can contain:

```text
complete TF target sets
ChIP peaks
perturbation results
GEO accession numbers
gene lists
regulatory coordinates
```

The old DPI design explicitly recommends parsing structured supplements directly. :chatgpt-content-reference{index="17"}

---

# 38. Candidate passage retrieval

Don't send whole papers to an LLM.

Candidate selection should combine:

```text
PubTator entity hits

+

exact TF/target lexical matches

+

regulatory keywords

+

BM25

+

optional embedding similarity
```

For example prioritize paragraphs containing:

```text
bind
binding
ChIP
CUT&RUN
CUT&Tag

knockdown
knockout
CRISPR
overexpression

activate
repress
regulate
target

promoter
enhancer
reporter
luciferase
```

Send only the best passages.

For a few hundred papers you **do not need a dedicated vector database**.

FAISS or a small local embedding index is enough.

Start with normalized identifiers, aliases, regulatory terms, and BM25. A lightweight biomedical embedding model can add semantic matches alongside lexical retrieval; section 63 leaves model selection open.

Preserve section and paragraph boundaries. A retrieved result can form a bounded **evidence bundle**: the result paragraph plus necessary neighboring text, a linked caption/table row, or methods context from the same paper. Give each component its own ID and exact locator. Do not force an entire experiment into an isolated sentence, or merge findings from unrelated experiments.

Retain lexical and dense retrieval scores separately. Similarity and reranker scores select text to inspect; they never become biological evidence strength. Deterministic parsing handles structured supplement rows where possible, preserving sheet/row/column provenance and association with the relevant assay. LLMs interpret only the bounded ambiguous content that needs them.

---

# 39. LLM role

The LLM is a:

> **structured scientific information extractor**

not the arbiter of biological truth.

Input:

```text
bounded source evidence bundle
section and source locators for each component
paper metadata
normalized entities
```

Output strict schema:

```json
{
  "regulator": "FOXA2",
  "target": "SFTPC",
  "relation": "regulates",
  "direction": "positive",
  "directness": "direct",
  "evidence_type": "TF_BINDING_PLUS_PERTURBATION",
  "assays": ["ChIP-seq", "knockdown"],
  "species": "human",
  "tissue": "lung",
  "cell_type": "alveolar epithelial",
  "disease": null,
  "model_system": "primary cell",
  "measured_or_inferred": "measured",
  "negated": false,
  "pmid": "...",
  "section": "Results",
  "start_offset": 1234,
  "end_offset": 1432
}
```

And critically:

```text
NO_RELATION
```

must be a valid output.

Abstention is a feature.

The schema must additionally retain statement status, experimental outcome, mapping status, and exact evidence spans. Return a list of atomic findings, allowing several distinct experiments in one bundle. Offsets are assigned or verified against stored text by code; an LLM-supplied offset or identifier is not trusted without validation. `NO_RELATION` is distinct from an explicit negative or null experimental finding.

The verifier receives exactly the same bounded source bundle and the proposed extraction, with no autonomous search or claim repair. If additional context is required, emit `INSUFFICIENT_CONTEXT`; a deterministic, logged rule may expand the bundle for a new extraction run. Do not let the verifier silently add evidence.

---

# 40. No GLiNER fine-tuning right now

Final model decision:

| Tool/model | Role now |
|---|---|
| PubTator 3.0 | **Yes** — entity normalization/retrieval |
| Strong LLM | **Yes** — regulatory claim extraction |
| Second LLM verification pass | **Yes** |
| GLiNER2.5 | Optional later for cheaper prefiltering |
| GLiNER / GLiNER2 | No |
| GLiFormer | No |
| PubMedBERT/BiomedBERT fine-tuning | Later |
| Synthetic-data training project | No |
| Agent framework | No |

We need a working scientific resource before optimizing model cost.

---

# 41. No human reviewer changes the extraction policy

The old DPI plan recommended manual double-annotated QC. That is scientifically ideal. :chatgpt-content-reference{index="18"}

You have explicitly said that there will be no human reviewer in this pipeline.

So for this project we replace that operationally with:

```text
LLM EXTRACTOR
     ↓
LLM VERIFIER
     ↓
DETERMINISTIC CHECKS
     ↓
ACCEPT / UNCERTAIN / REJECT
```

This is **not equivalent to a human gold-standard evaluation**.

Therefore never call accepted edges:

```text
human validated
ground truth
confirmed true
```

Call them:

```text
AUTO_ACCEPTED
AUTO_VERIFIED
UNCERTAIN
REJECTED
```

---

# 42. Exact automatic acceptance rule

Accept an extracted finding only when all applicable checks pass:

```text
regulator and target identifiers are resolved at the stated biological level
explicit relation or experimental finding is present in the source bundle
extractor and verifier agree on the finding as expressed
statement status, outcome, and direction are faithfully preserved
assay supports the assigned directness and evidence type
experimental context is retained, with unknown fields explicit
exact quotations and locators match the versioned source artifacts
publication identity and primary-source attribution are retained
```

An unambiguous negated or null finding can be `AUTO_ACCEPTED`. It contributes as qualified counter-evidence or an inconclusive outcome relative to a specified claim; it never becomes positive support merely because extraction passed. A null result does not automatically disprove regulation.

Use `UNCERTAIN` for ambiguous entities, insufficient context, or unresolved factual support. Use `REJECTED` for a demonstrably incorrect extraction, invalid source span, or `NO_RELATION`. Preserve all dispositions in versioned artifacts. Speculative/review statements may be retained for discovery with their status, but cannot supply independent primary experimental support.

Acceptance determines extraction validity. Eligibility and polarity for a particular nomination are separate deterministic decisions. Section 65 defines basic evidence checks and the biological evaluation; no separate NLP benchmark is required.

---

# 43. Section weighting

Evidence preference:

```text
Results
   >
Figure captions
   >
Abstract
   >
Discussion
   >
Introduction
```

Methods are valuable mainly for:

```text
assay
species
cell system
experimental design
```

Reviews are:

```text
discovery sources
```

not independent primary experiments.

This matches the older DPI literature plan. :chatgpt-content-reference{index="19"}

---

# 44. The key no-human strategy: precision over recall

With no curator:

> Missing some valid edges is preferable to inserting many wrong edges.

Therefore accept:

```text
very clear claims
```

and keep ambiguous ones outside the scoring graph.

This is particularly important for phrases like:

```text
associated with
correlated with
enriched for
predicted target
motif present
possibly regulates
```

Those are not equivalent to direct regulation.

---

# 45. Evidence tiers

For scientist-facing summaries, use something like:

| Tier | Meaning |
|---|---|
| **A** | Binding + functional effect, with relevant/near-relevant biological context |
| **B** | Strong binding OR perturbational evidence in relevant context |
| **C** | Experimental/curated directional evidence but context limited |
| **D** | Computational/association evidence only |
| **U** | Evidence strength or extraction remains unresolved |

Contradiction is a separate flag/count, not a low-quality tier: two strong experiments can conflict. Keep assay/directness, context match, extraction validity, and polarity as separate fields; any displayed tier is a versioned summary for the requested nomination.

This is much more meaningful than:

```text
confidence = 0.92
```

---

# 46. Context match

A paper can be scientifically useful without being perfect context.

For an AT1/IPF nomination:

### Exact

```text
human
lung
AT1/alveolar epithelial
IPF
```

### Close

```text
human
lung
alveolar epithelial
fibrotic context
```

### Partial

```text
mouse AT1
normal lung
```

### Mismatched

```text
human colon cancer cell line
```

Do not throw context-limited evidence away.

Label it appropriately.

Compute the match against each requested nomination, rather than storing one universal match label on the evidence. AT1 and broadly described alveolar epithelium are not automatically equivalent; preserve annotation granularity and uncertainty. Missing context is `unknown`, not implicitly exact.

---

# 47. TF nomination is the central output

Create an explicit:

```text
TFNomination
```

for:

```text
TF × cell type × niche × disease/condition × gene program
```

Example:

```yaml
tf: ETV1
cell_type: AT1
niche: Niche2
condition: IPF
program: AT1_IPF_Niche2_Higher_Expression_Program

chromlinker_rank: ...
chromlinker_delta: ...

tf_expression: ...

program_overlap_count: ...
program_enrichment_fdr: ...

binding_evidence_count: ...
perturbation_evidence_count: ...
reporter_evidence_count: ...

lung_study_count: ...
cell_type_matched_count: ...
ipf_matched_count: ...

independent_study_count: ...
contradiction_count: ...

context_match_rank: ...
literature_rank: ...

nomination_status: ...
ranking_version: v1
```

---

# 48. Nomination evidence vector

Do not collapse everything too early.

Keep three major groups.

### Project evidence

```text
ChromLinker TF rank
ChromLinker connectivity difference
number of ChromLinker targets
TF expression support
target expression
target-program overlap
descriptive expression support
directional compatibility
```

### Literature evidence

```text
direct-binding studies
perturbation studies
reporter studies
CRE perturbations

lung studies
cell-type-matched studies
fibrosis/IPF studies

independent experiments
independent publications

contradictory evidence
```

### Program evidence

```text
target enrichment
pathway coverage
biological-process coverage
```

Later:

```text
Geneformer evidence
Perturb-seq evidence
```

---

# 49. Ranking

Use transparent prioritization, with component scores and evidence visible. Do not report a probability that a TF causes a niche.

First aggregate within three evidence groups:

1. **Project connectivity:** ChromLinker evidence, once its score semantics are confirmed.
2. **Expression-program concordance:** signed-regulon concordance, target overlap, and descriptive expression support.
3. **External experimental evidence:** assay strength, independent study support, and qualified counter-evidence, with context assessed against the nomination.

TF RNA is supporting information, not an obligatory activity gate. Context qualifies the experimental evidence; it is not automatically a second independent vote for the same studies. Preserve lineage when a curated prior and retrieved publication share a source. The groups are useful organizational boundaries, not a claim of statistical independence.

A proposed baseline is weighted reciprocal rank fusion over the group ranks:

```text
score(TF) = sum(weight[g] / (k + rank[g, TF]))
```

Use fixed, versioned weights, ranking universes, tie handling, and missingness rules per comparison. An unavailable component contributes no term, with availability shown separately; do not renormalize each TF's weights in a way that rewards missing data. Missing experimental coverage is not a negative finding. Retain separate route-specific lists for literature-only and ChromLinker-only candidates, and inspect how missing coverage affects the combined list.

RRF is an information-retrieval baseline, not a validated biological ranker. [Original RRF paper](https://research.google/pubs/reciprocal-rank-fusion-outperforms-condorcet-and-individual-rank-learning-methods/)

Compare ChromLinker-only, signature/prior-only, and combined rankings. Report top-candidate changes under leave-one-evidence-group-out and leave-one-study-out checks, reasonable weighting choices, and target-coverage filters. These are robustness checks, not biological confidence intervals. Store algorithm, parameters, component ranks, coverage, source versions, and ranking version. Formal predictive improvement requires held-out experimental outcomes.

---

# 50. Direction consistency

Using the direction of the Yale pooled niche-expression signature:

Suppose literature says:

```text
TF-X ACTIVATES Gene-A
```

and:

```text
Gene-A has higher pooled mean expression in Niche2
```

while project evidence suggests stronger TF-X connectivity in Niche2.

That is:

```text
directionally compatible
```

not causal proof.

Conversely:

```text
TF-X REPRESSES Gene-A

Gene-A has higher pooled mean expression in Niche2
```

may be discordant.

Keep the language cautious because ChromLinker connectivity itself is not necessarily TF activation.

---

# 51. Literature-only nominations

This is one of the highest-value analyses.

Imagine ChromLinker does not prioritize TF-X.

But TF-X has experimentally supported targets:

```text
GDF15
KRT17
CD44
AREG
...
```

and those targets are significantly enriched in the Niche2 gene program.

Then create:

```text
nomination_source =
LITERATURE_PROGRAM_ENRICHMENT
```

This candidate may be biologically interesting specifically because it was missed by ChromLinker.

---

# 52. Candidate classes

I would surface candidates as:

```text
SUPPORTED
    project evidence + good literature evidence

QUALIFIED
    strong project signal, but literature context/directness limited

CHROMLINKER_ONLY
    strong project prediction with little prior evidence

LITERATURE_ONLY
    gene-program regulator supported externally but not strongly by ChromLinker

CONTRADICTORY
    meaningful support and counter-evidence

INSUFFICIENT
    evidence too weak/uncertain
```

These categories are much more useful for experimental planning than a single score.

---

# 53. Why contradictions should remain

Do not resolve:

```text
Study A → activates
Study B → represses
```

into:

```text
activates
```

because one happens to be newer.

Store both.

Differences may come from:

```text
species
cell type
disease
dose
time
cofactor state
experimental system
```

Contradictory evidence is useful information.

---

# 54. Experiment independence

If:

```text
hTFtarget
ChIP-Atlas
CistromeDB
Paper A
```

all ultimately use:

```text
GEO GSE12345
```

then:

```text
independent_experiments = 1
```

not four.

That is one of the strongest scientific features inherited from DPI-KG.

---

# 55. Software stack I would freeze

```text
Python

pandas / pyarrow
DuckDB optional

Pydantic
    extraction/data contracts

httpx / requests
    APIs

lxml
    PMC/Europe PMC XML

PubTator 3.0
    entities + retrieval assistance

Docling
    PDF fallback

LangChain standalone model API + Pydantic
    structured extraction + verification
LangSmith optional
    tracing and evaluation

FAISS optional
    passage retrieval

Neo4j Community
    canonical KG

neo4j Python driver

FastAPI
    eventual shared API

pytest
    deterministic tests
```

Not:

```text
LangGraph required
DeepAgents required
Airflow required
FalkorDB required
Postgres required
Pinecone required
```

---

# 56. Repository layout

I would create:

```text
spatial-niche-regulatory-kg/
│
├── README.md
├── pyproject.toml
│
├── configs/
│   ├── project.yaml
│   ├── literature.yaml
│   ├── graph.yaml
│   ├── extraction.yaml
│   └── ranking.yaml
│
├── data/
│   ├── raw/
│   │   ├── chromlinker/
│   │   ├── expression/
│   │   ├── neighborhood/
│   │   ├── niche_expression_signatures/
│   │   └── advisor_literature/
│   │
│   ├── processed/
│   │   ├── genes.parquet
│   │   ├── contexts.parquet
│   │   ├── chromlinker_observations.parquet
│   │   ├── expression_observations.parquet
│   │   ├── neighborhood_profiles.parquet
│   │   ├── niche_expression_signatures.parquet
│   │   ├── gene_programs.parquet
│   │   └── retrieval_queue.parquet
│   │
│   └── papers/
│
├── src/regkg/
│   ├── models.py
│   │
│   ├── identifiers/
│   │   ├── genes.py
│   │   └── cell_types.py
│   │
│   ├── project_data/
│   │   ├── neighborhood.py
│   │   ├── chromlinker.py
│   │   ├── expression.py
│   │   ├── niche_expression_signatures.py
│   │   └── differential_expression.py  # optional future sample-aware DE
│   │
│   ├── literature/
│   │   ├── search.py
│   │   ├── fetch.py
│   │   ├── parse_xml.py
│   │   ├── parse_pdf.py
│   │   ├── supplements.py
│   │   ├── pubtator.py
│   │   ├── passages.py
│   │   ├── retrieval.py
│   │   ├── embeddings.py      # optional
│   │   ├── extract.py
│   │   └── verify.py
│   │
│   ├── evidence/
│   │   ├── validate.py
│   │   ├── context.py
│   │   └── independence.py
│   │
│   ├── graph/
│   │   ├── schema.cypher
│   │   ├── neo4j.py
│   │   ├── upsert.py
│   │   └── materialize.py
│   │
│   ├── analysis/
│   │   ├── tf_enrichment.py
│   │   ├── pathways.py
│   │   ├── ranking.py
│   │   └── nomination.py
│   │
│   └── api/
│       └── app.py
│
└── tests/
```

---

# 57. Pydantic first

Before writing literature prompts, define canonical contracts for:

```text
GeneRecord
BiologicalContext
SpatialNicheState
ChromLinkerObservation
ExpressionObservation
NeighborhoodProfile
NicheExpressionSignature
Publication
Passage
RegulatoryClaim
EvidenceAssertion
TFNomination
```

Everything entering Neo4j has to pass these schemas.

That eliminates many downstream inconsistencies.

---

# 58. Exact execution plan

## Phase 0 — freeze scope

Write this at the top of the README:

> **This project builds a literature-grounded regulatory evidence graph for Spatial NicheLinker that prioritizes transcription factors associated with niche-specific regulatory programs.**

Anything not supporting that goes to backlog.

---

## Phase 1 — ingest what we already have

Do now:

```text
neighbor-composition tables → neighborhood profiles

Yale pooled niche-expression signatures → normalized signatures

ChromLinker wide → long

pseudobulk wide → long

parse contexts

normalize cell-type names

normalize genes

build Dataset + AnalysisRun metadata

identify matched niche comparisons
```

Outputs:

```text
neighborhood_profiles.parquet
niche_expression_signatures.parquet
chromlinker_observations.parquet
expression_observations.parquet
contexts.parquet
genes.parquet
```

No literature needed yet.

---

## Phase 2 — derive preliminary TF summaries

Using the available project data, including the Yale pooled niche-expression signature, generate descriptive summaries:

```text
TF
cell_type
condition
niche
number_of_targets
score distribution
TF CPTT
```

If ChromLinker aggregation semantics are known, also reproduce:

```text
aggregate TF connectivity
Niche2-vs-Niche1 change
TF rank
```

If not, preserve raw data and wait for that one definition.

---

## Phase 3 — Neo4j foundation

Create:

```text
Gene
CellType
SpatialNicheState
BiologicalContext
Dataset
AnalysisRun
NeighborhoodProfile
NicheExpressionSignature
ChromLinkerObservation
ExpressionObservation
```

and constraints/indexes.

Then load **AT1 only** first.

Acceptance criterion:

> From Neo4j you can ask for all ETV1 predicted targets in IPF AT1 Niche2 and retrieve the corresponding project observations.

---

## Phase 4 — build AT1 retrieval queue

Use:

```text
TEAD1
KLF5
GATA6
FOXA2
ETV1
```

plus their strongest/most relevant ChromLinker targets.

Add:

```text
advisor seed PMIDs
CollecTRI records
TRRUST records
hTFtarget records
KnockTF records
```

Produce:

```text
retrieval_queue.parquet
```

Each row:

```text
query_id
tf
target_gene
cell_type
condition
query_type
query
priority
reason
source_candidate
```

---

## Phase 5 — literature acquisition

For every candidate paper:

```text
metadata
abstract
PMCID
DOI
OA status
```

Then:

```text
OA XML → retrieve
supplements → retrieve selectively
PDF → fallback only
```

Record every retrieval as a versioned run.

---

## Phase 6 — parse

Produce:

```text
document.json
sections.jsonl
figure_captions.jsonl
tables/
supplementary parsed tables
```

No mass figure vision.

---

## Phase 7 — candidate passage ranking

Identify passages containing likely regulatory evidence.

Produce:

```text
candidate_passages.jsonl
```

Each passage contains:

```text
PMID
section
text
TF mentions
target mentions
retrieval score
offsets
```

---

## Phase 8 — LLM extraction

Pass only bounded candidate evidence bundles.

Produce:

```text
raw_claims.jsonl
```

Require abstention.

---

## Phase 9 — LLM verification + deterministic validation

With basic source-grounding checks in place (section 65), the second pass determines:

```text
SUPPORTED_BY_PASSAGE
NOT_SUPPORTED
AMBIGUOUS
```

Then deterministic checks.

Outputs:

```text
accepted_claims.parquet
uncertain_claims.parquet
rejected_claims.parquet
```

Only accepted findings are eligible for nomination evidence; support, contradiction, and inconclusive outcomes remain distinct.

---

## Phase 10 — literature graph

Create:

```text
Publication
Passage
RegulatoryClaim
EvidenceAssertion
Experiment/Study when resolvable
```

Now AT1 has:

```text
project predictions
+
expression
+
literature evidence
```

in one graph.

---

## Phase 11 — analyze the Yale pooled niche-expression signature

Using the signature ingested in Phase 1:

```text
ingest
normalize
use NicheExpressionSignature
create ranked niche-expression programs
calculate pathway enrichment
calculate TF-target program overlap
calculate literature TF enrichment
```

No restructuring.

---

## Phase 12 — TF nomination

For each:

```text
cell type × condition × niche × TF
```

calculate evidence vector.

Then:

```text
group/component ranks and coverage
RRF baseline and sensitivity checks
nomination category
evidence tier plus separate contradiction status
```

Create `TFNomination`.

---

## Phase 13 — AT1 scientist-facing output

The first output for Shunya should resemble:

| TF | ChromLinker | Program overlap | TF RNA | Literature | Direct evidence | Lung context | Contradiction | Status |
|---|---|---|---|---|---|---|---|---|
| TEAD1 | ... | ... | ... | ... | ... | ... | ... | ... |
| KLF5 | ... | ... | ... | ... | ... | ... | ... | ... |
| GATA6 | ... | ... | ... | ... | ... | ... | ... | ... |
| FOXA2 | ... | ... | ... | ... | ... | ... | ... | ... |
| ETV1 | ... | ... | ... | ... | ... | ... | ... | ... |

Clicking a TF should eventually show:

```text
Why nominated
ChromLinker targets
niche-program overlap
pathways
binding evidence
perturbation evidence
context-matched papers
contradictions
exact evidence passages
PMIDs
```

Compare this output with ChromLinker-only and expression-signature/prior-only nominations. Show which candidates change, what independent evidence was added, and whether conclusions depend on a single study. These comparisons demonstrate the contribution of the KG; a predictive-accuracy claim needs held-out outcomes.

---

## Phase 14 — replicate across other populations

After AT1:

```text
alveolar macrophages
activated fibrotic fibroblasts
KRT5−/KRT17+
```

Same code.

No separate pipelines.

---

## Phase 15 — API

Then expose things like:

```text
GET /niches

GET /tf-nominations
    ?cell_type=AT1
    &condition=IPF
    &niche=2

GET /tf/ETV1/evidence

GET /tf/ETV1/targets
    ?cell_type=AT1
    &condition=IPF

GET /claims/{claim_id}

GET /publications/{pmid}
```

Later LungMAP and LungChat can consume the same API/database.

---

# 59. What is deferred

Explicitly backlog:

```text
full regulatory-locus atlas
all ENCODE/Cistrome peaks
GWAS
QTL
drugs
variants
GNNs
learned TF ranker
GLiNER fine-tuning
PubMedBERT fine-tuning
synthetic training corpus
universal TFome crawling
figure VLM extraction
agent swarm
LangGraph
BioAgentKG reasoning
Geneformer
Perturb-seq
```

Geneformer and Perturb-seq are scientifically interesting later, but they become additional independent evidence streams—not blockers.

---

# 60. Future Geneformer integration

Later:

```text
PerturbationPrediction
      ├──PERTURBED_GENE──▶ TF
      ├──START_STATE─────▶ Niche-associated state
      ├──TOWARD_STATE────▶ alternate state
      └──GENERATED_BY────▶ GeneformerRun
```

Then candidates can be categorized:

```text
ChromLinker + literature
ChromLinker only
literature only
Geneformer + literature
ChromLinker + Geneformer
all three
```

Future Perturb-seq can test whether those evidence combinations predict real perturbational outcomes.

That could become a particularly strong later analysis.

---

# 61. The final scientific story

The manuscript can eventually say:

```text
Spatial neighborhood
      ↓
niche-defined cell population
      ↓
distinct gene-expression program
      ↓
corresponding state recovered in multiome
      ↓
different inferred TF-gene regulatory programs
      ↓
evidence KG evaluates prior experimental support
      ↓
context-aware TF nomination
```

And importantly:

> **Spatial NicheLinker discovers the niche-associated regulatory difference. The KG does not manufacture that result; it tells you how much independent evidence exists for the mechanisms implied by that result.**

That distinction protects the paper from overclaiming.

---

# 62. The final scope in one sentence

If Nathan, Shunya, Anshunya, or anyone else asks what you are building:

> **I am building the evidence and knowledge-graph layer that connects the transcription factors and target programs inferred by Spatial NicheLinker's multiome analysis to experimentally supported regulatory mechanisms from the literature, and uses that combined evidence to prioritize context-specific TFs for follow-up.**

And the mental model to keep in your head is:

```text
WHO SURROUNDS THE CELL
        ↓
WHAT STATE THE CELL ENTERS
        ↓
WHAT GENES CHARACTERIZE THAT STATE
        ↓
WHAT TFs MAY REGULATE THOSE GENES
        ↓
WHAT PREVIOUS EXPERIMENTS SUPPORT THOSE TF→TARGET LINKS
        ↓
WHICH TFs ARE MOST DEFENSIBLE TO TEST NEXT
```

That is the project I would now build.


# Authoritative project-data update: neighborhood definition and Yale niche-expression signatures

> **This section supersedes earlier references in this document to an expected Shunya differential-expression table containing formal log2FC, p-values and FDR. That table does not currently exist. The Yale pooled niche-expression file is intentionally descriptive and must not be represented as sample-aware differential expression.**

## 1. Niche definition is condition-pooled and condition-agnostic at the clustering stage

Shunya confirmed that Niche 1 and Niche 2 were defined by clustering target cells jointly across Control and IPF tissue.

For each focal cell, the 25 nearest spatially adjacent cells were identified and classified by cell type. The neighborhood feature vector therefore represents the cellular composition of a fixed `k = 25` spatial neighborhood. Target cells were clustered from these neighborhood-composition vectors without using Control/IPF condition to define the clusters.

Condition was used only afterward to summarize niche prevalence and downstream molecular differences.

Therefore, Niche 1 and Niche 2 are **condition-agnostic in how they are defined**, although their abundance and molecular state can differ between Control and IPF.

The correct hierarchy is:

```text
Focal Cell Type
      ↓
25 nearest spatial neighbors
      ↓
neighbor cell-type composition
      ↓
joint clustering across Control + IPF
      ↓
SpatialNicheState
   Niche 1 / Niche 2
      ↓
condition-specific downstream observations
      ├── Control expression signature
      ├── IPF expression signature
      ├── Control ChromLinker
      └── IPF ChromLinker
```

Condition therefore **must not be encoded as part of the identity of `SpatialNicheState`**.

A niche state should instead retain methodological provenance such as:

```yaml
cell_type: AT1
niche: 1
definition_scope: condition_pooled
conditions_used_for_clustering:
  - Control
  - IPF
k_neighbors: 25
clustering_resolution: 0.08
```

The clustering resolution is analysis-specific and should be retained as provenance rather than treated as a biological property.

Condition belongs on downstream observations such as:

```text
NicheExpressionSignature
ChromLinkerObservation
ExpressionObservation
TFNomination
```

This distinction is important scientifically: disease condition did not define the niche clusters and is therefore not circularly encoded into the neighborhood state subsequently compared between Control and IPF.

## 2. `NeighborhoodProfile` is now a required project object

The neighbor-composition files provide direct quantitative definitions for the niche states and make `NeighborhoodProfile` part of the MVP rather than an optional future node.

Use:

```text
CellType
   │
   └──HAS_NICHE_STATE──▶ SpatialNicheState
                              │
                              └──DEFINED_BY──▶ NeighborhoodProfile
                                                   │
                                                   ├──HAS_NEIGHBOR──▶ CellType
                                                   ├──HAS_NEIGHBOR──▶ CellType
                                                   └──...
```

Each neighborhood relationship retains:

```text
mean_neighbor_count
neighbor_fraction
```

with:

```text
neighbor_fraction = mean_neighbor_count / 25
```

The normalized project table should contain:

```text
focal_cell_type
niche
neighbor_cell_type
mean_neighbor_count
neighbor_fraction
k_neighbors
clustering_resolution
source_file
analysis_run
```

The neighborhood layer answers:

> **What spatial cellular environment defines this niche?**

It should remain distinct from the later transcriptional and regulatory observations.

## 3. Yale pooled niche-expression signatures are descriptive, not formal differential expression

`Yale_pooled_niche_expression_signatures.tsv` is the intended current niche-expression comparison file.

It contains, for each focal cell type, condition and gene:

```text
dataset
cell_type
condition
comparison = niche_2_vs_niche_1
gene

mean_log_normalized_expression_niche_1
mean_log_normalized_expression_niche_2

niche_2_minus_niche_1_mean_log_normalized_expression

pct_expressing_niche_1
pct_expressing_niche_2

n_cells_niche_1
n_cells_niche_2
```

Retain sampling metadata beside every signature and nomination. The supplied file contains, for example:

| Population | Niche 1 cells | Niche 2 cells |
|---|---:|---:|
| Control AT1 | 6,591 | 143 |
| IPF AT1 | 6,903 | 789 |
| Control activated fibrotic fibroblasts | 41 | 11 |

These counts describe coverage, not independent biological replication. Donor counts and contributions are unknown in this file and should remain null until available. Show small/imbalanced groups explicitly; do not invent a validated minimum-cell threshold. Future donor-resolved inputs can support donor-level robustness analysis, but do not block descriptive ingestion now. [Biological-replication evidence](https://www.nature.com/articles/s41467-021-25960-2)

The `pct_expressing_*` columns in the supplied file use fractions in [0, 1]; preserve their unit explicitly. Neighborhood mean counts sum to 25 in each supplied row, consistent with the documented denominator.

Its effect is explicitly:

```text
mean log-normalized expression in Niche 2
minus
mean log-normalized expression in Niche 1
```

It does **not** contain donor/sample-aware inferential statistics.

Therefore it must not generate or imply:

```text
formal log2FC
p_value
q_value / FDR
significant = true/false
DEG
sample-aware differential expression
```

The recommended graph object is:

```text
NicheExpressionSignature
```

or equivalently `ExpressionContrastObservation`, with the original descriptive quantities retained exactly.

The broad pseudobulk CPTT matrix remains useful as a supporting absolute-expression reference across the wider Yale cell populations, but the pooled niche-expression-signature table becomes the primary source for direct Niche 1-versus-Niche 2 expression comparisons in the four focal populations.

## 4. Replace DE-derived gene programs with ranked niche-expression programs

Do not currently define the Yale niche programs as statistically significant DEG sets.

The primary representation should instead be a **signed, ranked expression signature** for each:

```text
cell type × condition × Niche2-vs-Niche1 comparison
```

For example:

```text
AT1_IPF_Niche2_vs_Niche1_ExpressionSignature
```

Genes are ranked by:

```text
niche_2_minus_niche_1_mean_log_normalized_expression
```

with positive values representing higher pooled mean expression in Niche 2 and negative values representing higher pooled mean expression in Niche 1.

Scientist-facing derived labels may use:

```text
AT1_IPF_Niche2_Higher_Expression_Program
AT1_IPF_Niche1_Higher_Expression_Program
```

but these must not be described as statistically significantly upregulated/downregulated programs.

Preferred manuscript/interface terminology is:

> “genes with higher pooled mean log-normalized expression in Niche 2”

rather than:

> “genes significantly upregulated in Niche 2.”

If binary gene sets are later created for a specific enrichment analysis, the threshold must be explicitly documented as an analysis threshold and must not be interpreted as statistical significance.

Where possible, TF-target enrichment should exploit the complete signed/ranked expression signature rather than depend exclusively on an arbitrary DEG cutoff.

## 5. Updated project evidence hierarchy

The project-derived side of the KG is now:

```text
1. Neighborhood composition
   condition-pooled Control + IPF
   kNN = 25
        ↓
2. SpatialNicheState
   Niche 1 / Niche 2
        ↓
3. Condition-specific descriptive expression signature
   Control: Niche2 vs Niche1
   IPF:     Niche2 vs Niche1
        ↓
4. Condition-specific ChromLinker observations
   Control Niche1 / Niche2
   IPF Niche1 / Niche2
        ↓
5. TF/target candidate generation
        ↓
6. External experimental and literature evidence
        ↓
7. Context-aware TF nomination
```

The complete conceptual model is therefore:

```text
WHO SURROUNDS THE CELL
        ↓
NeighborhoodProfile
        ↓
SpatialNicheState
        ↓
HOW THE CELL'S EXPRESSION DIFFERS
        ↓
NicheExpressionSignature
        ↓
WHAT REGULATORY CONNECTIONS ARE INFERRED
        ↓
ChromLinkerObservation
        ↓
WHICH TFs/TARGETS ARE CANDIDATES
        ↓
WHAT PRIOR EXPERIMENTS SUPPORT THEM
        ↓
RegulatoryClaim + EvidenceAssertion
        ↓
WHICH TFs ARE MOST DEFENSIBLE TO TEST
        ↓
TFNomination
```

## 6. Updated MVP project-data schema

The current project-data nodes should therefore include:

```text
Gene
CellType
BiologicalContext

SpatialNicheState
NeighborhoodProfile

NicheExpressionSignature
ExpressionObservation
ChromLinkerObservation

GeneProgram / ranked expression program
Pathway
BiologicalProcess

Dataset
AnalysisRun
```

`DifferentialExpressionAnalysis` should **not be instantiated for the current Yale pooled signature file**.

The schema may reserve a `DifferentialExpressionAnalysis` object for a future donor/sample-aware statistical analysis, but it is optional future evidence rather than a present input.

## 7. Updated normalized project tables

Create:

```text
neighborhood_profiles.parquet
niche_expression_signatures.parquet
chromlinker_observations.parquet
expression_observations.parquet
contexts.parquet
genes.parquet
```

`neighborhood_profiles.parquet`:

```text
focal_cell_type
niche
neighbor_cell_type
mean_neighbor_count
neighbor_fraction
k_neighbors
clustering_resolution
source_file
analysis_run
```

`niche_expression_signatures.parquet`:

```text
dataset
cell_type
condition
comparison
gene

mean_expr_niche1
mean_expr_niche2
effect_niche2_minus_niche1

pct_expr_niche1
pct_expr_niche2

n_cells_niche1
n_cells_niche2

effect_definition
```

Derived direction may be stored as:

```text
NICHE2_HIGHER
NICHE1_HIGHER
EQUAL
```

while retaining the original continuous effect.

## 8. Updated implementation order

The project no longer needs to wait for another Shunya file before constructing the core project-data layer.

Phase 1 should now ingest in parallel:

```text
neighbor-composition tables
        ↓
NeighborhoodProfile

pooled niche-expression signatures
        ↓
NicheExpressionSignature

pseudobulk CPTT
        ↓
supporting ExpressionObservation

ChromLinker matrix
        ↓
ChromLinkerObservation
```

Then build the first AT1 graph:

```text
AT1
 ↓
Niche1 / Niche2
 ↓
NeighborhoodProfile
 ↓
Control/IPF expression signatures
 ↓
Control/IPF ChromLinker observations
 ↓
candidate TFs and targets
```

The literature/evidence pipeline can proceed concurrently.

No additional project-data export is currently required from Shunya for the MVP.

## 9. Hard terminology constraints

The implementation, manuscript and UI must preserve the following rules:

```text
Niche1/Niche2
    = condition-pooled neighborhood states defined jointly across Control + IPF

Control/IPF
    = downstream condition attached to observations, not niche identity

Yale pooled expression difference
    = descriptive pooled mean-log-expression contrast

Yale pooled expression difference
    ≠ formal log2FC
    ≠ statistical DE
    ≠ FDR-significant change

ChromLinker
    = inferred regulatory connectivity

ChromLinker
    ≠ direct binding
    ≠ demonstrated causal regulation
```

These distinctions are now frozen project semantics.

# 63. Biomedical embeddings for passage retrieval

**Biomedical embeddings are useful for retrieving relevant passages when their wording differs from the query.** Use a lightweight biomedical retrieval model alongside exact gene/TF aliases and BM25. The user will select the model; the architecture does not lock in a specific encoder.

```text
TF/target/context query
    ├── exact aliases + BM25
    └── biomedical semantic retrieval
                 ↓
        combined candidate passages
                 ↓
        structured extraction and verification
```

Keep lexical matches so semantic retrieval does not suppress exact gene evidence. Use a small local index and bounded passages with source IDs. Follow the chosen model's query/document encoding, token limits, pooling, and similarity recipe. Record the model revision and source/chunk hashes. Check on a few representative papers that the added passages are relevant; no model-comparison study is required.

MedCPT is one established biomedical retrieval example, not a mandated or necessarily smallest model. [NCBI implementation](https://github.com/ncbi/MedCPT)

Embeddings retrieve text; similarity does not establish a regulatory relationship, directness, context match, or evidence strength. The same extractor/verifier and source checks apply afterward. Quantitative ingestion, TF scoring, and Neo4j writes do not require text embeddings. BM25 remains a working fallback before the selected model is connected. No separate reranker, fine-tuning, or synthetic training-data generation is needed.

# 64. Neo4j integration contract

Neo4j is the canonical served evidence graph; versioned source and processed artifacts remain sufficient to rebuild it. The same application model supports local Community and a bounded Aura demo.

```text
source files and paper assets
    ↓ deterministic parsing / extraction / validation
versioned Parquet + JSONL + manifests
    ↓ explicit materialization policy
official neo4j Python driver
    ↓ parameterized Cypher
Neo4j evidence graph
    ↓ predefined application queries
TF reports / later FastAPI and MCP
```

Use environment configuration for `NEO4J_URI`, `NEO4J_USERNAME`, `NEO4J_PASSWORD`, and `NEO4J_DATABASE`; never commit credentials. Typical URIs are `neo4j://localhost:7687` locally and the supplied `neo4j+s://...databases.neo4j.io` URI for Aura. [Driver connection documentation](https://neo4j.com/docs/python-manual/current/)

Before ingestion, create Community-compatible uniqueness constraints on application IDs. Validate required properties in Pydantic. Merge nodes by immutable IDs and load relationships only after referenced nodes are present. Use bounded, parameterized `UNWIND` batches and idempotent managed write transactions; callbacks can be retried, so perform no LLM calls, file mutation, or other external side effects inside them. Record batch completion only after commit. [Batching guidance](https://neo4j.com/docs/python-manual/current/performance/), [Transaction retry contract](https://neo4j.com/docs/python-manual/current/transactions/)

Keep source observations and extraction runs immutable by version; derived nominations carry ranking versions. Do not key records by Neo4j internal IDs. Distinguish source-level deduplication from claim grouping so agreeing studies retain separate provenance.

The graph writer accepts only validated records through fixed Cypher templates. LangChain handles model calls, not autonomous schema design or database mutation. APOC, Graph Data Science, GraphRAG builders, generated Cypher, and vector indexes are not prerequisites. The first API uses predefined queries over the schema.

Before importing, estimate unique nodes and relationships under the selected materialization policy. After importing, check counts, duplicate IDs, dangling/missing reference attempts, and complete source paths for nominations. A repeated identical import must not increase counts. Demonstrate an AT1 query returning ETV1 candidates, supporting and opposing findings, exact source passages, and the relevant project observations.

Deploy local Community with a pinned version and persistent volumes; retain offline backups/exports and a tested rebuild process. Aura Free remains an optional selected demo under the limits in section 21. Recheck hosted-plan limits and lifecycle rules when provisioning. This document specifies the setup; it does not install software or create a cloud account.

# 65. Practical evidence checks and biological evaluation

The literature pipeline is supporting infrastructure for the biomedical KG:

```text
candidate TFs/targets → targeted literature search
→ eligible XML/BioC or PDF fallback → passages/tables with source locators
→ exact/BM25 + lightweight biomedical semantic retrieval
→ structured extraction → structured verification + basic checks
→ accepted evidence with context/provenance → Neo4j → TF nominations
```

Keep a simple run manifest with source hashes, processing status, and parser/model/prompt versions. Cache successful outputs so interrupted runs resume without duplicating work. Distinguish unavailable full text, failed processing, no relevant finding, and an explicit negative experiment. Store uncertain/rejected outputs outside the scoring graph.

Before accepting evidence, check exact source quotations, gene identity/species, direction or null outcome, assay/directness, and source attribution. Maintain a small regression set covering obvious errors such as reversed TF/target, negation, unsupported directness, and mixed contexts. These are normal data-quality checks, not an NLP benchmark or an annotated-corpus deliverable. No model comparison, fine-tuning, or dedicated NLP evaluation study is required.

Keep the extractor/verifier design simple. Their agreement is an automated filter, not human validation. With no dedicated curator, state that limitation and preserve the source passages so every nomination remains inspectable. Avoid claiming a measured target-domain extraction accuracy that has not been established.

The bioinformatics paper should evaluate:

- **Biological relevance:** which TFs and target programs are nominated in each niche/condition, and which assays and contexts support them.
- **Added value:** how combined evidence changes nominations relative to ChromLinker-only and expression-signature/curated-prior baselines.
- **Evidence independence and contradictions:** whether support comes from distinct studies, and what qualified counter-evidence remains.
- **Robustness:** whether top nominations depend heavily on one study, evidence group, or filtering choice; show cell counts and missing donor coverage.
- **Reproducibility:** whether the same inputs/configuration reproduce the processed artifacts and graph without duplicate records.

If future perturbation outcomes are used for predictive validation, exclude those studies and their derivative database records from the evidence used to build the predictions. Until such outcomes exist, describe the output as evidence-backed prioritization for follow-up.
