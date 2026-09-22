# DPI Knowledge Graph Architecture
## Evidence-Weighted Gene Regulatory Network from Multi-Source Structured + Literature Evidence

> **Status:** Dual-resolution design (gene-level GRN + position-level `RegulatoryLocus` nodes), variant/GWAS overlay, DEG contextual annotation, and concrete IPF/AT2 use cases. Driven by advisor discussion (May 2026).

## Google Doc set-up by Dr. Nathan Salomonis: https://docs.google.com/document/d/1fAB6dKGWf_7ttOPLId5pacNGNUT7ED_yY31BvuE8368/edit?usp=sharing
---

## 1. Design Principles

### The One-Sentence Version

A **dual-resolution, evidence-weighted, context-conditioned knowledge graph** where every edge is a TF→Gene regulatory interaction supported by multiple independent evidence sources, conditioned on **cell system, disease, developmental stage, and species**, with weights learned from positive controls rather than hand-tuned. The graph operates at **gene-level for querying and visualization**, backed by **position-level regulatory locus evidence** for variant/GWAS/motif queries.

### Core Requirements

1. **One edge type:** TF binds regulatory region → regulates target gene. This is **DNA-protein interaction**, not STRING's hodgepodge of co-expression, pathway co-membership, and text mining.

2. **Multiple evidence sources per edge:** The ChromLinker/ChromBPNet pipeline gives you the edge. ChIP-seq databases confirm it. Literature adds regulatory direction. Each source is separate evidence.

3. **Cell-type-specific scores:** The same TF→Gene edge has **different weights in different cell types.** The correlation between TF accessibility and gene expression varies by cell context.

4. **Co-factor binding:** Sometimes TF1 + TF2 must both be present. Needs a cleaner representation than string concatenation.

5. **Regulatory direction from literature:** ChromLinker/ChromBPNet gives you the sign of the correlation (positive/negative), but knowing whether a TF is an **activator or repressor** with high confidence requires literature confirmation.

6. **Learned weights, not hand-assigned:** Use positive controls (known interactions from curated databases) to train a model that learns how much to trust each evidence source.

7. **Dual-resolution design:** The canonical graph query layer is `TF → Gene`. Underneath, `RegulatoryLocus` nodes retain position-level evidence (binding sites, peaks, seqlets) so the graph can answer GWAS variant overlap, motif disruption, and cross-context binding-site shift queries without losing the clean gene-level GRN view.

8. **Variant/GWAS overlay support:** GWAS variants, ClinVar mutations, and somatic variants can be overlapped with regulatory loci to identify disease-relevant TF binding disruptions. This is a first-class use case, not an afterthought.

### The Critical Distinction from STRING

| | STRING | This DPI-KG |
|---|---|---|
| **Edge meaning** | Vague "association" (co-expression, pathway co-membership, text mining all mixed) | **Explicit DPI:** TF binds DNA regulatory region, regulates target gene |
| **Evidence** | Similar gene expression ≈ "interaction" (it's not) | Physical TF-DNA binding + expression correlation + locus-level provenance |
| **Cell context** | None | Cell-type-specific weights |

---

## 2. Graph Schema

### 2.1 The Actual Schema

Three-layer design: canonical gene-level edges + context-specific observations + position-level regulatory loci.

```
              GENE-LEVEL GRN (query layer)
              ════════════════════════════
Gene(:TF) ──REGULATES_VIA──▶ RegulatoryInteraction ──TARGETS──▶ Gene
                                      │                          ▲
                                 HAS_CONTEXT              IS_DEG_IN──DEGSet
                                      │                   TARGETS──Drug
                              ┌───────┴───────┐
                              ▼               ▼
                     InteractionContext   InteractionContext
                     (A549, NSCLC,        (Jurkat, T-ALL,
                      activator, +0.72)    unknown, -0.15)
                              │               │
                          SUPPORTS         SUPPORTS
                              │               │
                    ┌─────────┼─────┐         │
                    ▼         ▼     ▼         ▼
                Evidence  Evidence Evidence Evidence
                (ChromBPNet)(ChIP) (Lit)    (ChromBPNet)

              POSITION-LEVEL EVIDENCE (locus layer)
              ═══════════════════════════════════════
              Gene(:TF) ──BINDS_AT──▶ RegulatoryLocus ──LINKED_TO_GENE──▶ Gene
                                            ▲
                                      OVERLAPS
                                            │
                                        Variant ──HAS_GWAS──▶ GWASAssociation
```

**Context handling:**
- **RegulatoryInteraction** = canonical "this TF can regulate this gene" (gene-level)
- **InteractionContext** = "in THIS specific cell/disease/species, it behaves like THIS"
- **Evidence** → supports a specific InteractionContext, not the global edge
- **RegulatoryLocus** = position-level binding site backing the gene-level edge (optional layer, required for variant/GWAS queries)
- **Variant** + **GWASAssociation** = noncoding variants overlapping regulatory loci, with trait/study provenance

### 2.2 Node Definitions

#### Core Entities

| Node Type | Properties | Notes |
|---|---|---|
| **Gene** | `gene_id` (HGNC), `symbol`, `entrez_id`, `chromosome`, `tss_position` | Every node is a Gene. TFs get an additional `:TF` label. A target gene can also be a TF (cascading regulation). |
| **RegulatoryInteraction** | `interaction_id`, `base_confidence` | Canonical TF→Gene link. One per unique pair. Context-specific direction/confidence live on InteractionContext. |
| **InteractionContext** | `direction`, `context_confidence`, `correlation`, `cell_system`, `disease`, `species`, `dev_stage`, `evidence_count` | One per unique context combination. This is where direction, scores, and context tags live. |
| **RegulatoryComplex** | `complex_id`, `condition` (AND/OR), `complex_type` (cobinding/cooperative/competitive) | Only created when co-factor binding is present. Supports N-member TF sets (2-4 TFs per binding site). All TFs are `:MEMBER_OF` the complex. |
| **Evidence** | `evidence_id`, `source` (enum), `cell_type`, `supported` (bool), `score` (optional float), `direction` (optional), `directness` (direct_binding/regulatory_effect/unclear), `metadata` (JSON) | One evidence node per source per context. |
| **RegulatoryLocus** | `locus_id`, `chr`, `start`, `end`, `assembly` (hg38/mm10/etc.), `locus_type` (promoter/enhancer/unknown) | Position-level binding site. Links TF binding evidence to specific genomic coordinates. Required for variant/GWAS overlap queries. |
| **Variant** | `variant_id` (rsID or chr:pos:ref:alt), `chr`, `pos`, `ref`, `alt`, `assembly`, `variant_type` (SNP/indel/structural), `source` (GWAS Catalog/ClinVar/somatic) | Noncoding or coding variant with genomic coordinates. Overlaps with `RegulatoryLocus` to identify binding disruptions. |
| **GWASAssociation** | `study_id`, `trait`, `p_value`, `odds_ratio`, `credible_set_id` (optional), `source` (GWAS Catalog/Open Targets), `population` | Trait-variant association with study provenance. Linked from `Variant` via `:HAS_GWAS`. Optionally links to `CredibleSet` for fine-mapping. |
| **DEGSet** | `degset_id`, `disease` (MONDO ID), `cell_system` (CL/Cellosaurus ID), `species` (NCBITaxon), `source`, `n_genes` | Contextual overlay for disease differential expression. **NOT edge evidence** — annotates genes, does not create or weight TF→Gene edges. |
| **Drug** | `drug_id`, `name`, `source` (DGIdb/ChEMBL/Open Targets) | Lightweight drug-target mapping. Linked to Gene via `:TARGETS`. |

#### Context Properties on InteractionContext

| Property | Type | Grounded To |
|---|---|---|
| `cell_system` | String (ontology ID) | Cell Ontology (CL) or Cellosaurus. Use **BOND** (lab-developed ontology harmonization system, in review) to automatically map researcher cell-type annotations to standardized CL/EFO IDs using biological context (species, tissue, disease, assay, dev stage). |
| `disease` | String (ontology ID) | MONDO |
| `species` | String (ontology ID) | NCBITaxon |
| `dev_stage` | String | Free-text for now |
| `direction` | Enum | activator / repressor / dual / unknown |
| `context_confidence` | Float 0-1 | Model-learned |
| `correlation` | Float -1 to +1 | ChromLinker/ChromBPNet correlation score |

> [!TIP]
> **Use ontology IDs from day one.** `MONDO:0005233` instead of `"NSCLC"`, `NCBITaxon:9606` instead of `"human"`, `CL:0000066` instead of `"epithelial cell"`. Cheap to do now, expensive to fix later. BOND handles the cell-line-to-lineage abstraction automatically.

> [!IMPORTANT]
> **Genome assembly is mandatory** on every `RegulatoryLocus` and `Variant` node. Without `assembly` (e.g., `hg38`, `hg19`, `mm10`), GWAS/ClinVar/ChIP coordinate overlaps become unsafe. All position-level data must carry its assembly tag.

### 2.3 Evidence Source Details

The ChromLinker/ChromBPNet pipeline gives continuous scores, **everything else is mostly binary** ("does database X support this edge, yes or no?").

| Evidence Source | Value Type | Key Properties | Role |
|---|---|---|---|
| **ChromLinker / ChromBPNet** | **Continuous** (signed correlation) | `correlation_score` (+/-), `accessibility_score`, `cell_type`, `model_version`. Position-level intermediates (seqlets, peaks) feed `RegulatoryLocus` nodes. | **Primary structured source.** ChromLinker is the framework (combines RNA, surface protein, chromatin); ChromBPNet is the underlying base-resolution binding model. The sign of the correlation is the initial activator/repressor signal. |
| **CistromeDB** | **Binary** + quality metadata | `supported` (bool), `peak_score`, `q_value`, `experiment_id`, `cell_type` | Standardized re-analysis of public ChIP-seq/ATAC-seq/DNase-seq. Supports **both** peak/binding-site-level evidence and derived TF-target gene views. Community-standard ChIP-seq resource. |
| **ChIP-Atlas** | **Binary** + quality metadata | `supported` (bool), `peak_score`, `q_value`, `experiment_id`, `antibody`, `cell_type` | 224K+ uniformly processed ChIP-seq experiments. Includes annotation tracks for GWAS Catalog SNPs, ClinVar variants, GTEx eQTLs, JASPAR motifs, FANTOM5 enhancers, and conserved regions. |
| **UniBind** | **Binary** (highest stringency) | `supported` (bool), `peak_score`, `q_value`, `experiment_id`, `cell_type` | Motif-validated ChIP-seq peaks — direct DPI only. |
| **Curated TF-target DBs** | **Binary** + direction | `supported` (bool), `direction` (activator/repressor), `database` (TRRUST/CollecTRI/DoRothEA), `confidence_level` (for DoRothEA: A-E) | **Validation gold standard** initially, then evidence source. Note: TRRUST is human-only; cross-species extrapolation is acceptable for validation/training. |
| **Literature** | **Semi-structured** | `pmid`, `source_sentence`, `direction`, `directness` (direct_binding/regulatory_effect/unclear), `cell_type_mentioned`, `species`, `confidence`, `extraction_method` | Provides **direction confirmation** and **biological context**. |
| **Motif** | **Binary** + p-value | `supported` (bool), `jaspar_id`, `motif_name`, `p_value`, `position`, `strand` | Motif presence supports binding plausibility. Motif disruption by a variant is stored as metadata on the Variant evidence (`motif_disrupted: true`, `jaspar_id`, `disruption_score`). |
| **BioGRID PPI** | **Binary** | `supported` (bool), `biogrid_id`, `detection_method`, `pmid` | **Co-factor evidence only.** Confirms TF-TF physical interaction for RegulatoryComplex nodes. |
| **Perturb-seq** | **Continuous** (fold change) | `perturbation_type`, `fold_change`, `p_value`, `cell_type` | **Gold-standard validation.** Causal evidence from direct perturbation. |
| **GWAS / Variant databases** | **Binary** + statistics | `rsid`, `trait`, `p_value`, `odds_ratio`, `source` (GWAS Catalog/Open Targets/RegulomeDB/ENCODE SCREEN) | Variant-to-regulatory-locus overlap. Open Targets provides credible sets, L2G scores, and colocalisation. ENCODE SCREEN provides cCRE annotations for human and mouse. |

> [!IMPORTANT]
> **Dual-resolution position handling.** The gene-level GRN is the primary query layer. Underneath, `RegulatoryLocus` nodes carry genomic coordinates (`chr`, `start`, `end`, `assembly`) for binding sites derived from ChromLinker/ChromBPNet peaks, ChIP-seq peaks, and motif positions. These locus nodes enable variant/GWAS overlap queries, motif disruption analysis, and cross-context binding-site comparisons. Evidence nodes link to both `InteractionContext` (for context scoring) and optionally to `RegulatoryLocus` (for position-level provenance).

### 2.4 Edge Types (Complete)

| Edge | From → To | Purpose |
|---|---|---|
| `:REGULATES_VIA` | Gene:TF → RegulatoryInteraction | TF regulates target gene (canonical) |
| `:TARGETS` (RI) | RegulatoryInteraction → Gene | Target of regulation |
| `:HAS_CONTEXT` | RegulatoryInteraction → InteractionContext | Context-specific observation |
| `:SUPPORTS` | Evidence → InteractionContext | Evidence supports a context |
| `:MEMBER_OF` | Gene:TF → RegulatoryComplex | TF is part of co-binding complex |
| `:MEDIATES` | RegulatoryComplex → RegulatoryInteraction | Complex mediates regulation |
| `:BINDS_AT` | Gene:TF → RegulatoryLocus | TF binds at this genomic position |
| `:LINKED_TO_GENE` | RegulatoryLocus → Gene | `link_method` (proximity/HiC/eQTL), `distance_bp`, `score`, `source` |
| `:OVERLAPS` | Variant → RegulatoryLocus | Variant falls within a regulatory locus |
| `:HAS_GWAS` | Variant → GWASAssociation | Variant is associated with a trait |
| `:IS_DEG_IN` | Gene → DEGSet | `logFC`, `q_value`, `direction` (up/down), `comparison` |
| `:TARGETS` (Drug) | Drug → Gene | Drug targets this gene |

---

## 3. The Co-Factor Problem

### Current approach (Sid): String concatenation
`"MYC_MAX" → BCL2` — this breaks the moment MYC participates in MYC+MAX, MYC+MIZ1, and MYC solo interactions.

### Recommended approach: Intermediate RegulatoryComplex node

```
┌──────┐     ┌──────────────────────┐     ┌────────────────────┐
│ MYC  │──▶  │ RegulatoryComplex    │──▶  │ RegulatoryInteract │──▶ BCL2
│ (:TF)│     │ condition: AND       │     │ base_confidence:   │
└──────┘     │ type: cobinding      │     │   0.87             │
             │                      │     └────────────────────┘
┌──────┐     │                      │
│ MAX  │──▶  │                      │
│ (:TF)│     └──────────────────────┘
└──────┘
```

**Why this works:**
- MYC keeps its own solo interactions (MYC → other targets without MAX)
- MAX keeps its own interactions too
- The complex node is queryable: "What complexes does MYC participate in?"
- condition: `AND` means both must be present; `OR` means either is sufficient
- Supports **N-member TF sets** (2-4 TFs per binding site, per advisor). Up to 2 JASPAR ICE elements can co-occur at a single site.
- Complexes should be tied to **locus-level** motif/co-binding evidence where available (via the `RegulatoryLocus` layer).

**When NOT to create a complex:** If two TFs independently regulate the same gene without co-binding, they get **separate** `RegulatoryInteraction` nodes, not a complex. The complex is only for joint binding.

---

## 4. Data Source Inventory

### 4.1 Structured Sources (Computation-First)

| Source | URL / Access | What It Gives You | Scale |
|---|---|---|---|
| **ChromLinker / ChromBPNet** (lab pipeline) | Internal | ATAC-seq → TF binding predictions with correlation scores per cell type. Base-resolution seqlet/peak intermediates feed `RegulatoryLocus` nodes; final output is TF→Gene edges. | Per-experiment |
| **CistromeDB** | cistrome.org | Standardized re-analysis of public ChIP-seq/ATAC-seq/DNase-seq. Supports both peak/binding-site-level evidence and derived TF-target gene abstractions. | ~45K datasets (human + mouse) |
| **ChIP-Atlas** | chip-atlas.org | 224K+ uniformly processed ChIP-seq experiments; peak data + enrichment + GWAS/ClinVar/GTEx/JASPAR/FANTOM5 annotation tracks | ~1,100 TFs |
| **UniBind** | unibind.uio.no | Motif-validated ChIP-seq peaks (highest stringency — direct DPI only) | ~400 TFs, ~56M binding sites |
| **JASPAR** | jaspar.elixir.no | TF binding motif PWMs (position weight matrices) | ~2,000 profiles |
| **BioGRID** | thebiogrid.org | Physical protein-protein interactions (Y2H, co-IP, etc.) | ~1.2M interactions |
| **Mouse GRNs** (lab pipeline) | Internal | ChromLinker/ChromBPNet runs on mouse ATAC-seq data (when available). Enables cross-species conservation queries for TF→Gene edges in disease-relevant models. | Data-dependent |

### 4.2 Curated Gold Standards (Validation → Then Evidence)

| Source | What It Provides | Scale | Key Feature |
|---|---|---|---|
| **TRRUST v2** | Literature-curated TF→target with direction | ~8,400 interactions (human) | Has activator/repressor annotation |
| **CollecTRI** | Literature-curated TF→target via decoupler | ~47K signed interactions | Largest curated set with direction |
| **DoRothEA** | Confidence-tiered TF regulons | ~1.5M interactions (A-E levels) | A/B levels are gold; C-E are noisy |
| **GTRD** | ChIP-seq-derived TF binding from 8K+ experiments | ~800 TFs | Large but needs quality filtering |

### 4.3 Unstructured Source (Literature)

| Source | Pipeline | What You Extract |
|---|---|---|
| **PubMed Central** | Section-aware extraction pipeline (see §6) | TF→Gene direction (activator/repressor), directness (direct_binding/regulatory_effect/unclear), cell type, species |

> [!NOTE]
> **The full corpus selection and extraction pipeline is defined in §6.** Gene-seeded PubMed/PMC retrieval, article triage/tiering, section-aware extraction, table/supplement parsing, and figure/vision processing are all covered there.

### 4.4 Variant & GWAS Sources

| Source | URL / Access | What It Gives You | Key Feature |
|---|---|---|---|
| **GWAS Catalog** | ebi.ac.uk/gwas | Curated GWAS associations with rsIDs, traits, p-values | Standard reference for trait-variant associations |
| **Open Targets** | platform.opentargets.org | Credible sets, posterior probabilities, locus-to-gene (L2G) predictions, enhancer-to-gene predictions, colocalisation | Fine-mapping and causal gene assignment |
| **ENCODE SCREEN** | screen.wenglab.org | cCRE annotations (promoter-like, enhancer-like, CTCF-bound) for human and mouse. Searchable by gene, cCRE, variant, GWAS, or locus. | Regulatory element classification |
| **RegulomeDB** | regulomedb.org | Regulatory potential scoring for variants. Accepts dbSNP IDs, BED, VCF, GFF3. | Variant-to-regulatory-site functional scoring |
| **ClinVar** | ncbi.nlm.nih.gov/clinvar | Clinically interpreted variants with pathogenicity classifications | Disease-relevant coding and noncoding variants |

### 4.5 Drug-Target Databases

| Source | URL / Access | What It Gives You | Notes |
|---|---|---|---|
| **DGIdb** | dgidb.org | Drug-gene interactions aggregated from 40+ sources | Open, aggregated, preferred for initial build |
| **Open Targets** | platform.opentargets.org | Drug-target associations with clinical evidence | Also provides tractability assessments |
| **ChEMBL** | ebi.ac.uk/chembl | Bioactivity data for drug-like molecules | Large-scale pharmacology data |

> [!WARNING]
> **DrugBank is licensed.** Do not use DrugBank as a default source. Prefer DGIdb, Open Targets, or ChEMBL for drug-target mapping. If Drug nodes add too much scope initially, drug-target lookup can remain external to the core graph.

### 4.6 Cell-System Harmonization

| Tool | Access | What It Does |
|---|---|---|
| **BOND** (lab-developed, in review) | Internal | Automated ontology harmonization system. Maps messy, inconsistent cell-type/disease labels to standardized CL/EFO/MONDO ontology IDs using biological context (species, tissue, disease, assay type, developmental stage). Enables cell-line-to-cell-lineage abstraction across datasets. |

## 5. Evidence Integration & Weight Learning

### 5.1 Two-Stage Weight Learning

TRRUST and CollecTRI are good priors for edge existence, but they are not strong labels for cell-type-specific activity. ChromLinker/ChromBPNet and Perturb-seq are better for context-specific scoring. Therefore: **two models, not one.**

| Model | Question | Training Labels | Key Features |
|---|---|---|---|
| **Base edge model** | "Is this a real direct TF→target edge at all?" | TRRUST + CollecTRI (A/B) for positives; random pairs for negatives | ChIP-seq support, motif match, curated DB overlap, literature mentions, n_independent_sources |
| **Context model** | "Is this edge active/signed in this cell system?" | Perturb-seq + matched ChromLinker/ChromBPNet data | ChromLinker/ChromBPNet correlation, cell-matched ChIP-seq, context-specific literature direction |

Final query score = combination of both.

### 5.2 Feature Vector Per Edge

For every TF→Gene pair, build a feature vector from all available evidence:

```python
class EdgeFeatureVector:
    """Features for the base edge model."""
    
    # ChromBPNet features
    chrombpnet_score: float            # Correlation score (signed)
    chrombpnet_abs_score: float        # Absolute correlation (strength)
    chrombpnet_n_binding_sites: int    # Number of genomic positions
    
    # ChIP-seq features
    chipseq_supported: bool            # Any ChIP-seq database confirms?
    chipseq_n_experiments: int         # How many independent experiments?
    chipseq_best_qvalue: float         # Best peak q-value across experiments
    chipseq_n_databases: int           # How many databases (ChIP-Atlas, UniBind, etc.)?
    
    # Motif features
    motif_match: bool                  # JASPAR motif present at binding site?
    motif_best_pvalue: float           # Best motif p-value
    
    # Curated database features
    trrust_supported: bool
    collectri_supported: bool
    dorothea_level: str                # A, B, C, D, E, or None
    
    # Literature features
    literature_mentions: int           # Number of papers mentioning this interaction
    literature_direction_consensus: str  # Consistent activator/repressor across papers?
    literature_directness: str         # direct_binding / regulatory_effect / unclear
    
    # BioGRID (co-factor evidence)
    cofactor_ppi_supported: bool       # Co-TFs physically interact in BioGRID?
    
    # Derived features
    n_independent_sources: int         # Total distinct evidence sources
    direction_agreement: float         # Agreement across sources on activator/repressor
```

### 5.3 Base Edge Model Pipeline

```
┌─────────────────────────────────────────────────────┐
│  Positive Controls                                  │
│  • TRRUST + CollecTRI (level A/B)                   │
│  • Perturb-seq validated edges                      │
│  • Known TF→target from focused seed papers         │
├─────────────────────────────────────────────────────┤
│  Negative Controls                                  │
│  • Random TF-Gene pairs with zero evidence          │
│  • Hard negatives: partial evidence, no validation  │
└───────────────────────┬─────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────┐
│  Supervised Classifier                              │
│                                                     │
│  Input: EdgeFeatureVector                           │
│  Output: P(real interaction | all evidence)          │
│                                                     │
│  Start with logistic regression (interpretable)     │
│  Upgrade to XGBoost if needed                       │
│                                                     │
│  Validation: 5-fold CV + held-out cell type test    │
└───────────────────────┬─────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────┐
│  Output: base_confidence per RegulatoryInteraction  │
│  + context_confidence per InteractionContext        │
│  + learned modality weights (interpretable)         │
└─────────────────────────────────────────────────────┘
```

### 5.4 Validation Strategy

| Validation Set | Source | Size | Purpose |
|---|---|---|---|
| **Gold positives** | TRRUST + CollecTRI (A/B) + Perturb-seq | ~5K-10K edges | Known true TF→Gene interactions |
| **Gold negatives** | Random TF-Gene pairs with zero evidence across all sources | Same size as positives | True negatives |
| **Hard negatives** | TF-Gene pairs with weak/partial evidence but not validated | ~2K-5K | Prevents overfitting to easy negatives |
| **Held-out cell type** | All edges in a specific cell system (e.g., A549 or AT2) | ~1K-3K | Tests generalization to unseen cell context |

---

## 6. Corpus and Evidence Processing Pipeline

The graph schema defines **what** the graph stores. This section defines **how** evidence gets there.

```
retrieve broadly → triage aggressively → route assets → extract by modality
→ ground/contextualize → validate → score → materialize
```

### 6.1 Pipeline Overview

```
╔══════════════════════════════════════════════════════════════════════════════╗
║                    DPI-KG EVIDENCE PROCESSING PIPELINE                      ║
╠══════════════════════════════════════════════════════════════════════════════╣
║                                                                              ║
║  ┌──────────────────────────────────────────────────────────┐                ║
║  │  LAYER 1: STRUCTURED DATA (build first)                  │                ║
║  │                                                          │                ║
║  │  ChromLinker/ChromBPNet ──▶ edges + RegulatoryLocus      │                ║
║  │  ChIP-Atlas / CistromeDB / UniBind ──▶ binding evidence  │                ║
║  │  JASPAR ──▶ motif evidence                               │                ║
║  │  TRRUST / CollecTRI / DoRothEA ──▶ curated + validation  │                ║
║  │  BioGRID ──▶ co-factor PPI                               │                ║
║  │  Perturb-seq ──▶ causal validation                       │                ║
║  │  GWAS Catalog / Open Targets / ClinVar ──▶ variants      │                ║
║  │  GTEx eQTLs ──▶ variant-gene expression links            │                ║
║  │  DGIdb / ChEMBL ──▶ drug-target                          │                ║
║  │  ENCODE SCREEN ──▶ cCRE annotations                      │                ║
║  └──────────────────────────────────────────────────────────┘                ║
║                              │                                               ║
║                              ▼                                               ║
║  ┌──────────────────────────────────────────────────────────┐                ║
║  │  LAYER 2: CORPUS SELECTION (gene-seeded, not all PubMed) │                ║
║  │                                                          │                ║
║  │  GRN gene list ──▶ PubMed/PMC query ──▶ ~2K-5K papers    │                ║
║  │  Citation expansion ──▶ forward/backward refs            │                ║
║  │  DB-linked papers ──▶ papers cited by TRRUST/CistromeDB  │                ║
║  │  Article triage ──▶ Tier 0/1/2/3/Reject                  │                ║
║  └──────────────────────────────────────────────────────────┘                ║
║                              │                                               ║
║                              ▼                                               ║
║  ┌──────────────────────────────────────────────────────────┐                ║
║  │  LAYER 3: DOCUMENT PROCESSING                            │                ║
║  │                                                          │                ║
║  │  PMC JATS/XML ──▶ structured sections, tables, fig refs  │                ║
║  │  PDF fallback ──▶ Docling (layout, tables, images, OCR)  │                ║
║  │  Supplements ──▶ CSV/XLSX/TSV direct, PDF via Docling     │                ║
║  │                                                          │                ║
║  │  Section routing:                                        │                ║
║  │    Results ──▶ primary claims (highest confidence)        │                ║
║  │    Methods ──▶ context only (assay, cell, species)        │                ║
║  │    Figure captions ──▶ evidence claims (high value)       │                ║
║  │    Abstract ──▶ summary claims (medium confidence)        │                ║
║  │    Discussion ──▶ interpretive (low confidence)           │                ║
║  │    Introduction ──▶ background only (lowest)              │                ║
║  └──────────────────────────────────────────────────────────┘                ║
║                              │                                               ║
║                 ┌────────────┼────────────┐                                  ║
║                 ▼            ▼            ▼                                  ║
║           ┌──────────┐ ┌──────────┐ ┌──────────┐                            ║
║           │   TEXT   │ │  TABLES  │ │ FIGURES  │                            ║
║           │ extract  │ │  parse   │ │  vision  │                            ║
║           │ TF→Gene  │ │ TF→Gene  │ │  LLM     │                            ║
║           │ claims   │ │ lists    │ │ extract  │                            ║
║           └────┬─────┘ └────┬─────┘ └────┬─────┘                            ║
║                │            │            │                                   ║
║                └────────────┼────────────┘                                   ║
║                             ▼                                                ║
║  ┌──────────────────────────────────────────────────────────┐                ║
║  │  LAYER 4: GROUNDING + CONTEXT (BOND)                     │                ║
║  │                                                          │                ║
║  │  Gene mentions ──▶ HGNC IDs (reference.db alias table)   │                ║
║  │  Cell mentions ──▶ CL/Cellosaurus IDs (via BOND)         │                ║
║  │  Disease mentions ──▶ MONDO IDs                           │                ║
║  │  Species ──▶ NCBITaxon IDs                                │                ║
║  │  Coordinates ──▶ hg38 (LiftOver from hg19 if needed)     │                ║
║  └──────────────────────────────────────────────────────────┘                ║
║                             ▼                                                ║
║  ┌──────────────────────────────────────────────────────────┐                ║
║  │  LAYER 5: VALIDATION + SCORING                           │                ║
║  │                                                          │                ║
║  │  Precision gate: >80% vs TRRUST/CollecTRI? ──▶ proceed   │                ║
║  │  Contradiction detection ──▶ store both, flag conflict    │                ║
║  │  Two-stage weight learning:                               │                ║
║  │    Stage 1: base existence (structured DB labels)         │                ║
║  │    Stage 2: revised weights (after literature features)   │                ║
║  └──────────────────────────────────────────────────────────┘                ║
║                             ▼                                                ║
║  ┌──────────────────────────────────────────────────────────┐                ║
║  │  LAYER 6: GRAPH MATERIALIZATION                          │                ║
║  │                                                          │                ║
║  │  Evidence above threshold ──▶ Evidence nodes in graph     │                ║
║  │  Weak evidence ──▶ sidecar store, does not drive scores   │                ║
║  │  Context assembly ──▶ InteractionContext + DEG/Drug/GWAS  │                ║
║  └──────────────────────────────────────────────────────────┘                ║
╚══════════════════════════════════════════════════════════════════════════════╝
```

### 6.2 Corpus Selection

Do **not** process all of PubMed uniformly. Use gene-seeded retrieval:

```
Phase 1: SEED (~500-2000 papers)
════════════════════════════════
Input: GRN gene list from ChromLinker (200 TFs + 2000 targets)

Query PubMed/PMC for each TF-Gene pair:
  "{TF}[Title/Abstract] AND {Gene}[Title/Abstract]
   AND (regulates OR activates OR represses OR ChIP OR knockdown)"

Filter: primary research, human/mouse, not retracted
Expected: ~500-2000 papers, mostly relevant

Phase 2: EXPAND (~1000 more)
═════════════════════════════
Forward/backward citations from Phase 1 hits
Filter: same TFs/genes mentioned

Phase 3: DB-LINKED
═══════════════════
Papers cited by TRRUST/CollecTRI for TF-Gene pairs in the GRN
Papers linked to ChIP-Atlas/CistromeDB experiments being used
```

**Article triage** — score before expensive processing:

| Score | Measures |
|-------|----------|
| `domain_score` | IPF/lung/AT2 relevance |
| `regulatory_score` | TF, enhancer, ChIP, ATAC, perturbation keywords |
| `evidence_score` | experimental > computational > review > editorial |
| `asset_score` | has full text, figures, tables, supplements |
| `trust_score` | journal quality, retraction status, species clarity |

**Tiers:**
- **Tier 0:** Curated gold papers for validation
- **Tier 1:** Full multimodal processing (text + tables + figures)
- **Tier 2:** Text/caption/table only
- **Tier 3:** Abstract-only / metadata-only
- **Reject:** Irrelevant, editorials, vague association papers

### 6.3 NLP Shortcuts

Do not rebuild basic NER from scratch:

- **PubTator Central** — NCBI already pre-annotated gene/disease/species/mutation mentions for all of PubMed. Use these annotations directly.
- **BioRED** — NCBI's pre-annotated biomedical relation dataset. Useful as training/validation supervision for relation extraction, though not a perfect TF-target benchmark specifically.

### 6.4 Section-Specific Text Extraction

```
  PAPER SECTIONS
  ══════════════
                                                    Confidence
  Results ──────▶ primary TF→Gene claims ────────── HIGHEST
  Methods ──────▶ context: assay, cell, species ──── (context only)
  Figure captions ▶ evidence claims ─────────────── HIGH
  Abstract ─────▶ summary claims ────────────────── MEDIUM
  Discussion ───▶ interpretive claims ───────────── LOW
  Introduction ─▶ background / second-hand cites ── LOWEST
  Reviews ──────▶ seed discovery only, not edges ── DO NOT USE AS EDGE EVIDENCE
```

**Extraction output per claim:**

```python
class TFTargetClaim:
    tf_symbol: str              # "MYC", "FOXA2"
    target_gene_symbol: str     # "BCL2", "MUC5B"
    direction: str              # "activator" | "repressor" | "unknown"
    directness: str             # "direct_binding" | "regulatory_effect" | "unclear"
    cell_type: str | None       # "AT2 cells", "A549"
    species: str | None         # "human", "mouse"
    disease: str | None         # "IPF", "NSCLC"
    assay: str | None           # "ChIP-seq", "knockdown", "luciferase"
    pmid: str
    source_sentence: str        # Exact sentence from paper
    section: str                # "Results", "Abstract", etc.
    confidence: float           # Section-weighted
    measured_or_inferred: str   # "measured" | "inferred" | "reported"
```

**Citation context mining:** The sentence around "(Smith et al., 2015)" often contains a compact regulatory claim. Mine these as secondary evidence.

### 6.5 Table and Supplement Processing

Tables and supplementary files often contain the densest regulatory data — full ChIP-seq target lists, complete DEG tables, perturbation results that the main text only summarizes.

```
  SUPPLEMENT ROUTING
  ══════════════════

  CSV / XLSX / TSV ──▶ direct parse
                       ⚠ check for Excel gene name corruption
                         (MARCH1→date, SEPT1→date — a common problem in published gene lists;
                          see [PMID 32346221](https://pubmed.ncbi.nlm.nih.gov/32346221/))

  PDF tables ─────────▶ Docling table extraction

  Non-standard ────────▶ skip gracefully (PPT, ZIP, Word)
```

**Table classification:**
- "TF target genes from ChIP-seq" → direct edges, `directness: ChIP_binding`
- "DEGs upon TF knockdown" → causal evidence, `directness: perturbation`
- "Gene expression across cell types" → SKIP (expression, not regulation)

### 6.6 Figure / Vision Layer

**Build last.** The figure layer is a targeted evidence extraction layer, not the backbone. It adds provenance, context, and direction from evidence that is often only in figures.

```
  FIGURE ROUTING
  ══════════════

  Extract figure + caption + nearby text
         │
         ▼
  Classify panel type:
         │
    ┌────┼────────────────────┬──────────────┬──────────────────┐
    ▼    ▼                    ▼              ▼                  ▼
  GRN/    ChIP/ATAC          Perturbation   Motif logo/        Microscopy/
  pathway  genome browser     plots (bar/    heatmap            histology
  diagram  tracks             volcano)
    │      │                  │              │                  │
    ▼      ▼                  ▼              ▼                  ▼
  EXTRACT  EXTRACT            EXTRACT        EXTRACT            SKIP
  (medium) (medium)           (medium)       (low)              (not relevant)
```

**Vision LLM output → `Evidence {source: "figure_vision"}`**

Must emit `measured_or_schematic`:
- A ChIP track in a figure is **measured** data → can support edge
- A cartoon pathway diagram is **schematic** → reported/inferred, lower weight

> [!WARNING]
> **Vision LLM guardrails:**
> - Do NOT use as unverified truth for exact quantitative values from plots
> - Do NOT infer causality from cartoon/schematic diagrams
> - Do NOT create high-confidence edges from figure-only claims without text/caption support
> - Always cross-validate figure claims against text claims from the same paper

### 6.7 Grounding and Context Harmonization

Use BOND early. Normalize everything before graph insertion:

| Raw Mention | Grounded To | System |
|-------------|------------|--------|
| "AT2", "alveolar type II", "AEC2" | CL:0002063 | BOND |
| "p53", "TP53", "Trp53" | HGNC:11998 | reference.db alias table |
| "lung fibrosis", "IPF" | MONDO:0005570 | MONDO |
| "A549", "HCC827" | CVCL_0023, CVCL_2060 | Cellosaurus via BOND |
| chr11:1219991 (hg19) | hg38 coordinates | LiftOver |

### 6.8 Validation and Precision Gate

```
  Extracted claims from text/tables/figures
         │
         ▼
  Compare TF→Gene pairs against TRRUST + CollecTRI
         │
    ┌────┴────┐
    ▼         ▼
  >80%      <80%
  precision  precision
    │         │
    ▼         ▼
  Proceed:   STOP:
  attach as  fix extraction
  Evidence   pipeline first
  nodes
```

Every extracted claim is also checked for:
- Gene normalization success (unmapped = reject)
- Context compatibility (cell type + disease + species makes biological sense)
- `measured` vs `inferred` vs `reported` vs `schematic`
- Contradiction with other sources → store both, flag conflict

### 6.9 Edge Cases Checklist

| # | Edge Case | Mitigation |
|---|-----------|------------|
| 1 | Gene name collisions with English words (REST, IMPACT, NOT) | Context-aware NER + PubTator |
| 2 | Indirect vs direct regulation | Extract `directness` metadata |
| 3 | Negative results ("no evidence X regulates Y") | Store as negative evidence |
| 4 | Reviews restating old claims | `source_type: review`, weight lowest |
| 5 | Species confusion (human MYC vs mouse Myc) | Track species per claim |
| 6 | Cell line drift (HEK293 ≠ normal kidney) | BOND + weight primary cells > lines |
| 7 | Excel gene name corruption in supplements | Detect + correct (MARCH→MARCHF) |
| 8 | Preprint→published duplicates | Dedup by DOI/title, keep published |
| 9 | Retracted papers | Check PubMed retraction status |
| 10 | Multi-panel figure / caption misalignment | Panel segmentation |
| 11 | Same TF-Gene, opposite direction across contexts | InteractionContext handles this |
| 12 | GWAS variant → nearest gene (often wrong) | Require eQTL/Hi-C for LINKED_TO_GENE |
| 13 | Dosage/threshold effects | Separate evidence with dose metadata |
| 14 | Gene families (AP-1 = FOS/JUN) | Map to members via RegulatoryComplex |
| 15 | Non-standard supplement formats | Skip gracefully |

### 6.10 Build Order

| Phase | What | Why |
|-------|------|-----|
| 1 | Structured databases (ChromLinker, ChIP-Atlas, TRRUST, etc.) | 80% of graph value, deterministic |
| 2 | GWAS/Variant overlay + GTEx eQTLs | Variant interpretation needs eQTL support early |
| 3 | Initial weight learning (Stage 1: structured DB labels) | Makes graph queryable |
| 4 | Corpus selection + text extraction | Adds direction, novel claims |
| 5 | Table/supplement extraction | High-value structured data from papers |
| 6 | Revised weight learning (Stage 2: with literature features) | Incorporates literature signal |
| 7 | Context assembly (BOND, InteractionContext, DEG/Drug overlays) | Makes it disease-specific |
| 8 | Figure/vision extraction | Enhancement layer, additional claims |

### 6.11 Key References

- [NCBI E-utilities API](https://www.ncbi.nlm.nih.gov/home/develop/api/)
- [PMC FTP / OA packages](https://pmc.ncbi.nlm.nih.gov/tools/ftp/)
- [PMC OAI-PMH](https://pmc.ncbi.nlm.nih.gov/tools/oai/)
- [PubTator Central](https://www.ncbi.nlm.nih.gov/CBBresearch/Lu/Demo/PubTatorCentral/)
- [Docling](https://docling-project.github.io/docling/reference/document_converter/) / [Docling paper](https://arxiv.org/abs/2408.09869)
- [BioRED relation dataset](https://ftp.ncbi.nlm.nih.gov/pub/lu/BioRED/)
- [Biomedical figure extraction (PMID 30949681)](https://pubmed.ncbi.nlm.nih.gov/30949681/)

---

## 7. Cypher Schema (Core Example)

```cypher
// ═══════════════════════════════════════
// CORE NODES
// ═══════════════════════════════════════

CREATE (g:Gene:TF {
    gene_id: 'HGNC:7553',
    symbol: 'MYC',
    entrez_id: 4609,
    tf_family: 'bHLH'
})

CREATE (target:Gene {
    gene_id: 'HGNC:990',
    symbol: 'BCL2',
    entrez_id: 596
})

// ═══════════════════════════════════════
// REGULATORY INTERACTION (canonical edge)
// ═══════════════════════════════════════

CREATE (ri:RegulatoryInteraction {
    interaction_id: 'RI-MYC-BCL2',
    base_confidence: 0.92
})

CREATE (g)-[:REGULATES_VIA]->(ri)
CREATE (ri)-[:TARGETS]->(target)

// ═══════════════════════════════════════
// INTERACTION CONTEXT (per cell/disease/species)
// ═══════════════════════════════════════

CREATE (ctx1:InteractionContext {
    context_id: 'CTX-MYC-BCL2-A549-NSCLC',
    cell_system: 'CVCL_0023',
    disease: 'MONDO:0005233',
    species: 'NCBITaxon:9606',
    dev_stage: 'adult',
    direction: 'activator',
    context_confidence: 0.87,
    correlation: 0.72,
    evidence_count: 4
})
CREATE (ri)-[:HAS_CONTEXT]->(ctx1)

// Second context: different cell system
CREATE (ctx2:InteractionContext {
    context_id: 'CTX-MYC-BCL2-Jurkat-TALL',
    cell_system: 'CVCL_0065',
    disease: 'MONDO:0004967',
    species: 'NCBITaxon:9606',
    dev_stage: 'adult',
    direction: 'unknown',
    context_confidence: 0.45,
    correlation: -0.15,
    evidence_count: 1
})
CREATE (ri)-[:HAS_CONTEXT]->(ctx2)

// ═══════════════════════════════════════
// EVIDENCE NODES (support a specific context)
// ═══════════════════════════════════════

// ChromLinker/ChromBPNet — supports the A549 context
CREATE (e1:Evidence {
    evidence_id: 'EV-CBPN-001',
    source: 'chrombpnet',
    cell_type: 'CVCL_0023',
    score: 0.72,
    binding_positions: ['chr18:63100100-63100450'],
    model_version: 'chrombpnet_v2.1'
})
CREATE (e1)-[:SUPPORTS]->(ctx1)

// ChIP-seq — supports the A549 context
CREATE (e2:Evidence {
    evidence_id: 'EV-CHIP-002',
    source: 'chipseq',
    database: 'ChIP-Atlas',
    supported: true,
    peak_score: 245.3,
    q_value: 1e-12,
    experiment_id: 'SRX3456789',
    cell_type: 'CVCL_0023',
    antibody: 'anti-MYC'
})
CREATE (e2)-[:SUPPORTS]->(ctx1)

// Literature — supports the A549/NSCLC context
CREATE (e3:Evidence {
    evidence_id: 'EV-LIT-003',
    source: 'literature',
    pmid: '35000001',
    source_sentence: 'MYC directly activates BCL2 transcription in epithelial cells',
    direction: 'activator',
    directness: 'direct_binding',
    cell_type_mentioned: 'epithelial cells',
    species: 'NCBITaxon:9606',
    confidence: 0.9
})
CREATE (e3)-[:SUPPORTS]->(ctx1)

// Curated database — supports the A549 context
CREATE (e4:Evidence {
    evidence_id: 'EV-TRRUST-004',
    source: 'curated_db',
    database: 'TRRUST',
    supported: true,
    direction: 'activator'
})
CREATE (e4)-[:SUPPORTS]->(ctx1)

// ChromLinker/ChromBPNet — supports the Jurkat context (different cell system)
CREATE (e5:Evidence {
    evidence_id: 'EV-CBPN-005',
    source: 'chrombpnet',
    cell_type: 'CVCL_0065',
    score: -0.15,
    binding_positions: ['chr18:63100200-63100500'],
    model_version: 'chrombpnet_v2.1'
})
CREATE (e5)-[:SUPPORTS]->(ctx2)

// ═══════════════════════════════════════
// CO-FACTOR (when applicable)
// ═══════════════════════════════════════

CREATE (cofactor:Gene:TF {
    gene_id: 'HGNC:6913',
    symbol: 'MAX',
    entrez_id: 4149
})

CREATE (rc:RegulatoryComplex {
    complex_id: 'RC-MYC-MAX',
    condition: 'AND',
    complex_type: 'cobinding'
})

CREATE (g)-[:MEMBER_OF]->(rc)
CREATE (cofactor)-[:MEMBER_OF]->(rc)
CREATE (rc)-[:MEDIATES]->(ri)

// ═══════════════════════════════════════
// CONSTRAINTS & INDEXES
// ═══════════════════════════════════════

CREATE CONSTRAINT gene_id_unique FOR (g:Gene) REQUIRE g.gene_id IS UNIQUE;
CREATE CONSTRAINT interaction_id_unique FOR (ri:RegulatoryInteraction) REQUIRE ri.interaction_id IS UNIQUE;
CREATE CONSTRAINT context_id_unique FOR (ctx:InteractionContext) REQUIRE ctx.context_id IS UNIQUE;
CREATE CONSTRAINT evidence_id_unique FOR (e:Evidence) REQUIRE e.evidence_id IS UNIQUE;
CREATE INDEX gene_symbol FOR (g:Gene) ON (g.symbol);
CREATE INDEX evidence_source FOR (e:Evidence) ON (e.source);
CREATE INDEX context_cell FOR (ctx:InteractionContext) ON (ctx.cell_system);
CREATE INDEX context_disease FOR (ctx:InteractionContext) ON (ctx.disease);
CREATE INDEX context_species FOR (ctx:InteractionContext) ON (ctx.species);
CREATE INDEX context_confidence FOR (ctx:InteractionContext) ON (ctx.context_confidence);
```

---

## 8. How This Differs from MechGate

| Dimension | MechGate | DPI-KG |
|---|---|---|
| **Scope** | All mechanistic biology (12 event types, 40+ fields per claim) | **One relationship type:** TF regulates Gene |
| **Primary data** | Literature (PubMed Central) is the primary source | **Computation is primary** (ChromLinker/ChromBPNet + ChIP-seq); literature is supplementary |
| **Literature role** | THE evidence | Confirms **direction** (activator/repressor) and adds **context** |
| **Hallucination risk** | HIGH (LLM extraction of complex mechanistic frames) | **LOW** (structured data dominant; literature extraction is simple) |
| **Context engine** | 9-dimensional compatibility check | **4 context dimensions** on InteractionContext nodes |
| **Scale** | ~60-120M claims target | **~50K-200K edges** per focused cell system |
| **Ontologies needed** | ~20 ontologies | **Core 4:** HGNC, CL/Cellosaurus, MONDO, NCBITaxon + GWAS Catalog/Open Targets for variants |
| **Schema complexity** | Four-layer graph (Entities → Events → Claims → Bridging Concepts) | **Dual-resolution:** Gene-level GRN (Gene → RI → InteractionContext ← Evidence) + position-level locus layer (TF → RegulatoryLocus → Gene, Variant → GWASAssociation) |

---

## 9. Implementation Roadmap

The detailed build order is defined in §6.10 above. Summary:

| Phase | What |
|-------|------|
| 1 | Structured databases (ChromLinker, ChIP-Atlas, TRRUST, etc.) → core graph |
| 2 | GWAS/Variant overlay + GTEx eQTLs |
| 3 | Initial weight learning (Stage 1: structured DB labels) |
| 4 | Corpus selection + text extraction (precision gate >80%) |
| 5 | Table/supplement extraction |
| 6 | Revised weight learning (Stage 2: with literature features) |
| 7 | Context assembly (BOND, InteractionContext, DEG/Drug overlays) |
| 8 | Figure/vision extraction (enhancement layer) |

---

## 10. Concrete Use Cases (IPF AT2 Workflow)

> From advisor discussion (May 2026). These are the target user queries the graph must support.

**Use Case 1: Core GRN from Epigenomics + ChIP-seq**
> Show me the core GRN of IPF considering AT2 cells, based on epigenomics data (ChromLinker) and ChIP-seq evidence.

Graph path: `Gene:TF -[:REGULATES_VIA]-> RI -[:HAS_CONTEXT]-> InteractionContext {cell_system: AT2, disease: IPF}` filtered by evidence source = ChromLinker/ChIP-seq.

**Use Case 2: DEG Enrichment**
> Are genes differentially expressed in AT2 cells in IPF enriched in this network?

Graph path: `Gene -[:IS_DEG_IN]-> DEGSet {disease: IPF, cell_system: AT2}` intersected with genes in the GRN subnetwork.

**Use Case 3: Druggable DEG Targets**
> Find drugs that specifically target the DEGs in AT2 cells in IPF that are in this network.

Graph path: `Drug -[:TARGETS]-> Gene -[:IS_DEG_IN]-> DEGSet {disease: IPF, cell_system: AT2}` where Gene is also a target in the GRN.

**Use Case 4: Literature Support Quantification**
> How many of these edges are literature-supported?

Graph path: Count `Evidence {source: 'literature'} -[:SUPPORTS]-> InteractionContext` for edges in the subnetwork.

**Use Case 5: Underdocumented Central Regulators**
> Find me central transcriptional regulators in AT2 cells that are not well documented in the literature.

Graph query: TFs with high degree/betweenness centrality in the AT2 GRN but low `literature_mentions` count across their evidence nodes.

**Use Case 6: GWAS Variant Overlap**
> Are there GWAS variants that are known to affect genes in this network?

Graph path: `Variant -[:OVERLAPS]-> RegulatoryLocus -[:LINKED_TO_GENE]-> Gene` where Gene is in the GRN and `Variant -[:HAS_GWAS]-> GWASAssociation {trait: IPF-related}`.

**Use Case 7: TFs Regulating Multiple GWAS-Affected Genes**
> Return TFs that appear to regulate multiple genes which have GWAS variants that would affect DNA binding of that TF.

Graph query: TFs where `TF -[:BINDS_AT]-> RegulatoryLocus <-[:OVERLAPS]- Variant` across multiple target genes, with motif disruption metadata (`motif_disrupted: true`) on the variant evidence.

**Use Case 8: Mouse Conservation Evidence**
> Which of these networks has conservation evidence in murine models of IPF?

Graph path: TF→Gene edges with `InteractionContext {species: NCBITaxon:10090}` matching orthologous edges in the human AT2 IPF GRN.

---

## 11. Open Design Decisions

> [!WARNING]
> These need answers before implementation starts.

### Decided

- **Position-level resolution:** DECIDED — dual-resolution design. Gene-level GRN for querying, `RegulatoryLocus` nodes for position-level evidence.
- **Mouse GRNs:** DECIDED — include when available from lab ChromLinker runs. Species is a property on InteractionContext; ortholog mapping connects human and mouse edges.
- **DEG treatment:** DECIDED — contextual overlay via `DEGSet`, NOT edge evidence.
- **BOND for cell harmonization:** DECIDED — use lab-developed BOND system for cell-line-to-lineage abstraction.

### Still Open

1. **Graph database:** Neo4j (mature, rich tooling, disk-based, free community edition) vs. FalkorDB (in-memory, faster for small graphs)? At ~50K-200K edges, either works. Neo4j is safer for a multi-person project.

2. **Starting cell system:** Which cell type(s) does Shunya already have ChromLinker/ChromBPNet predictions for? Start there.

3. **Scope of initial literature extraction:** Start with seed papers, validate, then expand.

4. **Who builds what:** Pankaj builds the evidence integration pipeline and literature extraction. Shunya builds the ChromLinker/ChromBPNet regulatory network predictions and contributes to validation. Sid's co-factor concatenation gets replaced with the RegulatoryComplex node.

5. **Preprints:** Skip for now.

6. **CistromeDB abstraction level:** In Kyle's paper, was CistromeDB used at peak/bed binding-site level or already abstracted to TF-target gene level? This affects how CistromeDB evidence feeds the dual-resolution schema.

7. **ChromLinker/CESeek output format:** Does the lab pipeline emit TF-site-gene, TF-gene, or both? Determines whether `RegulatoryLocus` nodes are populated directly from the primary pipeline or require post-processing.

8. **Open Targets integration depth:** Initially, use GWAS Catalog + basic variant overlap. Later, consider Open Targets credible sets, L2G scores, and colocalisation for higher-resolution causal gene assignment.

9. **Drug nodes initially:** Lightweight DGIdb/Open Targets mapping, or keep drug-target lookup external until later?

## 12. Engineering Notes

- **Raw data warehouse**: Keep raw source tables in Postgres or Parquet. Don't use the graph database as your raw warehouse. Feature engineering and model training are much easier in tabular format.
- **Graph as materialized view**: Neo4j is the clean, query-optimized view. ETL pipeline reads from Postgres/Parquet, writes to Neo4j.
- **Ontology IDs from day one**: MONDO for disease, NCBITaxon for species, CL/Cellosaurus for cell systems. BOND automates the cell-line-to-lineage mapping.
- **Genome assembly from day one**: Every `RegulatoryLocus` and `Variant` must carry `assembly` (hg38, mm10, etc.). Without this, coordinate overlaps are unsafe.
- **hTFtarget**: Treat as a benchmark/sanity-check source, not a primary evidence source, because it already aggregates inputs similar to what you are ingesting.
- **ENCODE SCREEN**: Now a planned source for cCRE annotations and variant-to-regulatory-site queries (promoted from "add later").
- **DrugBank is licensed**: Use DGIdb, Open Targets, or ChEMBL instead.
