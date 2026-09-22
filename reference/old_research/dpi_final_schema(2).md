# DPI Knowledge Graph — Final Schema (Dual-Resolution)

## Concrete Example: MYC activates BCL2 in A549

Read left to right. This is one complete interaction in the graph:

```
┌─────────┐              ┌──────────────────────┐              ┌─────────┐
│  MYC    │─REGULATES_VIA─▶│ RegulatoryInteraction│─── TARGETS ──▶│  BCL2   │
│  (:TF)  │              │  (canonical edge)    │              │  (:Gene)│
└─────────┘              └──────────┬───────────┘              └─────────┘
                                    │
                              HAS_CONTEXT
                                    │
                                    ▼
                         ┌─────────────────────────┐
                         │   InteractionContext     │
                         │   cell_system: A549      │
                         │   disease: MONDO:0005233 │ (NSCLC)
                         │   species: NCBITaxon:9606│ (human)
                         │   dev_stage: adult       │
                         │   direction: activator   │
                         │   context_confidence:0.87│
                         │   correlation: +0.72     │
                         └──────────┬──────────────┘
                                    │
                                SUPPORTS
                                    │
                    ┌───────────────┼───────────────┐
                    ▼               ▼               ▼
              ┌──────────┐   ┌──────────┐    ┌──────────┐
              │ChromBPNet│   │ChIP-Atlas│    │ TRRUST   │
              │score:0.72│   │q: 1e-12  │    │dir: act  │
              └──────────┘   └──────────┘    └──────────┘
              ┌──────────┐
              │Literature│
              │PMID:350..│
              │dir: act  │
              └──────────┘
```

If the same TF→Gene pair is observed in a different context (e.g., Jurkat / T-ALL):

```
RegulatoryInteraction (MYC→BCL2)
     │
     ├── HAS_CONTEXT ──▶ InteractionContext (A549, NSCLC, activator, +0.72)
     │                       ◀── Evidence_1, Evidence_2, ...
     │
     └── HAS_CONTEXT ──▶ InteractionContext (Jurkat, T-ALL, unknown, -0.15)
                             ◀── Evidence_5, Evidence_6, ...
```

## Abstract Schema

```
  GENE-LEVEL GRN (query layer)
  ════════════════════════════
  Gene:TF ── REGULATES_VIA ──▶ RegulatoryInteraction ── TARGETS ──▶ Gene
                                         │                (canonical: "can regulate")
                                         │                      ▲
                                    HAS_CONTEXT           IS_DEG_IN──DEGSet
                                         │                TARGETS──Drug
                                         ▼
                                 InteractionContext
                                 │  direction
                                 │  context_confidence
                                 │  correlation
                                 │  cell_system (CL/Cellosaurus ID)
                                 │  disease (MONDO ID)
                                 │  species (NCBITaxon ID)
                                 │  dev_stage (string)
                                 │
                              SUPPORTS
                                 │
                                 ▼
                              Evidence
                             (one per source)

  POSITION-LEVEL EVIDENCE (locus layer)
  ═════════════════════════════════════
  Gene:TF ── BINDS_AT ──▶ RegulatoryLocus ── LINKED_TO_GENE ──▶ Gene
                                 ▲
                           OVERLAPS
                                 │
                             Variant ── HAS_GWAS ──▶ GWASAssociation

  Co-factor case:

  Gene:TF ── MEMBER_OF ──▶ RegulatoryComplex ── MEDIATES ──▶ RegulatoryInteraction
  Gene:TF ── MEMBER_OF ──┘
```

---

## 1. Node Types (10)

| Node | Key Properties | Grounded To |
|---|---|---|
| **Gene** | `gene_id`, `symbol`, `entrez_id`, `tf_family` (if TF) | HGNC |
| **RegulatoryInteraction** | `interaction_id`, `base_confidence` | — |
| **InteractionContext** | `direction`, `context_confidence`, `correlation`, `cell_system`, `disease`, `species`, `dev_stage`, `evidence_count` | CL, MONDO, NCBITaxon |
| **RegulatoryComplex** | `condition` (AND/OR), `type`, supports N-member TF sets (2-4) | — |
| **Evidence** | `source`, `score`, `supported`, `direction`, `directness`, `metadata` | — |
| **RegulatoryLocus** | `locus_id`, `chr`, `start`, `end`, `assembly` (hg38/mm10), `locus_type` (promoter/enhancer/unknown) | — |
| **Variant** | `variant_id` (rsID or chr:pos:ref:alt), `chr`, `pos`, `ref`, `alt`, `assembly`, `variant_type`, `source` | GWAS Catalog, ClinVar |
| **GWASAssociation** | `study_id`, `trait`, `p_value`, `odds_ratio`, `credible_set_id`, `source`, `population` | GWAS Catalog, Open Targets |
| **DEGSet** | `degset_id`, `disease`, `cell_system`, `species`, `source`, `n_genes` | MONDO, CL, NCBITaxon |
| **Drug** | `drug_id`, `name`, `source` (DGIdb/ChEMBL/Open Targets) | — |

TFs get an additional `:TF` label on Gene. `cell_system` is a unified field that accepts both cell line IDs (e.g., `CVCL_0004` for K562 from Cellosaurus) and cell type IDs (e.g., `CL:0000066` for epithelial cell from Cell Ontology) — the ID prefix distinguishes which. BOND (lab-developed, in review) automates cell-line-to-lineage abstraction.

> [!IMPORTANT]
> **Genome assembly is mandatory** on `RegulatoryLocus` and `Variant` nodes. Without `assembly`, coordinate overlaps are unsafe.

> [!CAUTION]
> **DEGSet is NOT edge evidence.** DEGs annotate genes via `:IS_DEG_IN` but do not create or weight TF→Gene edges. A DEG tells you a gene changes in disease; it does not prove which TF caused it.

## 2. Edge Types (12)

| Edge | From → To | Carries |
|---|---|---|
| `:REGULATES_VIA` | Gene:TF → RegulatoryInteraction | — |
| `:TARGETS` (RI) | RegulatoryInteraction → Gene | — |
| `:HAS_CONTEXT` | RegulatoryInteraction → InteractionContext | — |
| `:SUPPORTS` | Evidence → InteractionContext | — |
| `:MEMBER_OF` | Gene:TF → RegulatoryComplex | — |
| `:MEDIATES` | RegulatoryComplex → RegulatoryInteraction | — |
| `:BINDS_AT` | Gene:TF → RegulatoryLocus | TF binds at this genomic position |
| `:LINKED_TO_GENE` | RegulatoryLocus → Gene | `link_method` (proximity/HiC/eQTL), `distance_bp`, `score`, `source` |
| `:OVERLAPS` | Variant → RegulatoryLocus | Variant falls within a regulatory locus |
| `:HAS_GWAS` | Variant → GWASAssociation | Variant is associated with a trait |
| `:IS_DEG_IN` | Gene → DEGSet | `logFC`, `q_value`, `direction` (up/down), `comparison` |
| `:TARGETS` (Drug) | Drug → Gene | Drug targets this gene |

## 3. Property Split

| Layer | What Lives Here | Why |
|---|---|---|
| **RegulatoryInteraction** | Canonical TF→Gene link, `base_confidence` | "This TF can regulate this gene (across any context)" |
| **InteractionContext** | `direction`, `context_confidence`, `correlation`, `cell_system`, `disease`, `species`, `dev_stage` | "In THIS specific context, the regulation looks like THIS" |
| **Evidence** | Source-specific scores, experiment IDs, PMIDs | "This source says so, with these quality metrics" |
| **RegulatoryLocus** | `chr`, `start`, `end`, `assembly`, `locus_type` | "At THIS genomic position, evidence for binding exists" |
| **Variant / GWASAssociation** | rsID, trait, p-value, credible set | "This variant overlaps a regulatory locus with this trait association" |
| **DEGSet** | Disease/cell-type-specific DEG set ID | "These genes change in this disease context" (annotation, not edge evidence) |
| **Drug** | Drug ID and name | "This drug targets this gene" |

## 4. Evidence Sources (12)

| Source | Type | What It Provides |
|---|---|---|
| **ChromLinker / ChromBPNet** | Continuous (signed) | ATAC-seq → TF binding prediction. **Primary edge source.** Base-resolution intermediates feed `RegulatoryLocus` nodes. |
| **CistromeDB** | Binary + q-value | Community-standard ChIP-seq. Supports both peak/binding-site and derived TF-target views. |
| **ChIP-Atlas** | Binary + q-value | 224K+ ChIP-seq experiments + GWAS/ClinVar/JASPAR/FANTOM5 annotation tracks. |
| **UniBind** | Binary (highest stringency) | Motif-validated ChIP-seq peaks — direct DPI only. |
| **JASPAR motifs** | Binary + p-value | TF's known binding motif exists at the site |
| **TRRUST / CollecTRI** | Binary + direction | Curated gold-standard TF→target with activator/repressor. TRRUST is human-only. |
| **Literature** (PubMed Central) | Semi-structured | Direction + context + `directness`. Section-aware extraction (Results > Abstract > Discussion). |
| **BioGRID** | Binary | Co-factor PPI evidence (TF-TF interaction only) |
| **Perturb-seq** | Continuous (fold change) | Causal: knock out TF, measure what changes |
| **GWAS / Variant DBs** | Binary + statistics | GWAS Catalog, Open Targets (credible sets, L2G), ENCODE SCREEN (cCREs), RegulomeDB, ClinVar |
| **GTEx eQTLs** | Continuous (effect size) | Variant→gene expression in specific tissues. Strengthens `LINKED_TO_GENE {link_method: eQTL}`. |
| **DGIdb / ChEMBL** | Binary + clinical evidence | Drug→Gene target interactions from 40+ aggregated sources. Open-source only. |

## 5. Two-Stage Weight Learning

| Model | Question | Training Labels | Key Features |
|---|---|---|---|
| **Base edge model** | "Is this a real direct TF→target edge at all?" | TRRUST + CollecTRI (A/B) for positives; random pairs for negatives | ChIP-seq support, motif match, curated DB overlap, literature mentions |
| **Context model** | "Is this edge active/signed in this cell system?" | Perturb-seq + matched ChromLinker/ChromBPNet data | ChromLinker/ChromBPNet correlation, cell-matched ChIP-seq, context-specific literature |

Final query score = combination of both models.

**Why two models, not one:** TRRUST/CollecTRI labels say "MYC → BCL2 is real" but don't know about cell types — they're context-free. Perturb-seq/ChromLinker data says "this edge is active in A549 specifically" but is too narrow to judge edge existence across all contexts. One model can't learn from both label types simultaneously without compromising on what it's predicting. Two models keeps the questions clean: Model 1 uses context-free gold standards for existence, Model 2 uses context-specific data for activity.

## 6. Co-Factor Representation

```
TF1 (MYC) ──MEMBER_OF──▶ RegulatoryComplex (AND) ──MEDIATES──▶ RegulatoryInteraction ──▶ Gene
TF2 (MAX) ──MEMBER_OF──┘
```

Only when co-binding is required. Independent TFs get separate interactions. Supports N-member TF sets (2-4 TFs per binding site). Complexes should be tied to locus-level motif/co-binding evidence where available.

---

## 7. GWAS Variant Overlap Example

A complete path from GWAS variant to regulatory network impact:

```
  Variant (rs35705950)                    GWASAssociation
  chr11:1219991:G:T                       trait: IPF
  assembly: hg38                          p_value: 5e-60
       │                                  source: GWAS Catalog
       │ OVERLAPS                              ▲
       ▼                                       │ HAS_GWAS
  RegulatoryLocus                              │
  chr11:1219800-1220200                   ─────┘
  assembly: hg38
  locus_type: promoter
       │
       │ LINKED_TO_GENE              BINDS_AT
       ▼                                 │
  MUC5B (:Gene)                     FOXA2 (:TF)
  HGNC:7515                         HGNC:5022
       │
       │ IS_DEG_IN
       ▼
  DEGSet
  disease: MONDO:0005570 (IPF)
  cell_system: CL:0002063 (AT2)
```

**Reading this:** The IPF GWAS variant rs35705950 overlaps a regulatory locus (MUC5B promoter) where FOXA2 binds. MUC5B is differentially expressed in AT2 cells in IPF. This connects a GWAS hit to a specific TF-gene regulatory mechanism in a disease-relevant cell type. (Source: [PMID 28272906](https://pubmed.ncbi.nlm.nih.gov/28272906/))

> [!TIP]
> Motif disruption is stored as metadata on the Variant evidence node: `motif_disrupted: true`, `jaspar_id`, `disruption_score`. If motif-centric queries become important, promote to `MotifInstance` node.

---

## 8. Evidence Processing Pipeline (Summary)

The full pipeline is defined in `dpi_knowledge_graph_architecture.md` §6. Brief summary:

```
  STRUCTURED DATA ──▶ edges + loci + variants + drugs
       │
       ▼
  CORPUS SELECTION ──▶ gene-seeded PubMed/PMC (~2K-5K papers)
       │
       ▼
  DOCUMENT PROCESSING ──▶ JATS/XML or Docling, section-routed
       │
       ├──▶ TEXT claims (Results > Abstract > Discussion)
       ├──▶ TABLE parsing (ChIP-seq target lists, DEG tables)
       └──▶ FIGURE vision (pathway diagrams, tracks — build last)
       │
       ▼
  GROUNDING (BOND) ──▶ HGNC, CL, MONDO, NCBITaxon, hg38
       │
       ▼
  VALIDATION ──▶ precision gate >80% vs TRRUST/CollecTRI
       │
       ▼
  GRAPH MATERIALIZATION ──▶ Evidence nodes + InteractionContext
```

**Key resources:** PubTator Central (pre-annotated NER), BioRED (relation supervision), Docling (PDF/table/image conversion).