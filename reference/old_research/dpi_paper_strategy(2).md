# DPI-KG Paper Strategy

> Consensus from critical analysis. Build toward this, not around it.

## Survivable Claim

**"A context-specific, locus-backed TF-target evidence prior improves regulatory subnetwork prioritization in lung disease, enabling variant-aware and literature-aware interpretation."**

This is NOT:
- "We built a knowledge graph"
- "We built an agent for regulatory biology"
- "We combined graph + GNN + agent"
- "First agentic system for TF-target analysis"

---

## Required Results

| # | Result | What it proves |
|---|---|---|
| 1 | Graph ranks direct TF-target edges better than generic priors (CollecTRI, DoRothEA, SCENIC+) in lung-relevant contexts | The evidence integration adds value over existing resources |
| 2 | A perturbation model using this prior outperforms the same model without it | The prior has predictive utility, not just descriptive |
| 3 | Gains are strongest in cross-context transfer or low-data settings | The InteractionContext design specifically helps |
| 4 | Small set of prospective perturbations validates the ranking improvement | It works in practice, not just retrospectively |
| 5 | GWAS variant overlap with regulatory loci identifies biologically plausible TF-target disruptions in IPF AT2 | The dual-resolution (gene + locus) design enables variant-aware subnetwork prioritization |

---

## Baselines to Beat

| Baseline | What it represents |
|---|---|
| **No prior** | Perturbation model with no GRN information |
| **CollecTRI/DoRothEA** | Best existing curated TF-target prior |
| **SCENIC+ GRN** | Best existing inferred cell-type-specific GRN |
| **CellOracle GRN** | Best existing perturbation-oriented GRN |
| **GEARS (no prior)** | Strong perturbation prediction baseline |
| **GEARS + generic prior** | Shows whether context-specific prior beats generic |

## Key Metrics

- Precision-recall for direct TF-target edges
- Sign accuracy (activator/repressor)
- Perturbation DE correlation (predicted vs. observed)
- Top-DE gene overlap
- Unseen perturbation generalization
- Unseen cell context generalization
- GWAS variant overlap with regulatory loci (number of GWAS-supported edges in subnetwork)
- DEG enrichment in GRN subnetworks

---

## Critical Warnings

1. **Leakage:** If TRRUST/CollecTRI are features in your weight-learning model, they CANNOT also be your main evaluation truth. Must do a clean source split.
2. **Don't over-scope:** Stay in lung. Don't claim this works for all biology.
3. **Agent is last:** Build graph → benchmark predictor → then add agent. Agent without good predictions is a chatbot over uncertainty.
4. **Explainability supports, doesn't lead:** Provenance is a feature, not the headline.
5. **IPF AT2 is the primary motivating use case.** All use cases from the advisor discussion (core GRN, DEG enrichment, druggable targets, GWAS overlap, mouse conservation) should be demonstrable.
6. **Drug-target mapping:** Use DGIdb, Open Targets, or ChEMBL. DrugBank is licensed.

---

## Venue Ladder

| Venue | What you need | Realistic citations (3yr) |
|---|---|---|
| **Bioinformatics / NAR Gen & Bioinf** | Results 1-2 plus IPF AT2 use case demonstration | 30-80 |
| **Genome Biology** | Results 1-3 plus variant-aware IPF AT2 prioritization | 80-150 |
| **Nature Communications** | Results 1-5 plus prospective validation | 150-300 |
| **Nature Methods** | All of the above + generalization beyond lung + strong baselines across multiple datasets | 300+ (unlikely without very strong results) |

---

## What Exists (Competitive Landscape)

| Tool | Published | What it does | Key difference from DPI-KG |
|---|---|---|---|
| SCENIC+ | Nat Methods 2023 | scATAC → enhancer-driven GRNs | One GRN per cell type, no unified multi-context graph |
| CellOracle | Nature 2022 | GRN inference + in silico perturbation | No multi-source evidence, no provenance |
| GRaNIE | Bioconductor | Cell-type-specific enhancer GRNs | Single data modality, no evidence weighting |
| GEARS | Nat Biotech 2023 | Graph-informed perturbation prediction | No GRN construction — needs priors from elsewhere |
| GRAND | Database | Tissue/cancer/cell-line regulatory networks | Static database, no learned weights |
| DoRothEA/CollecTRI | Resource | Curated signed TF-target interactions | Context-free, no cell-type specificity |

DPI-KG's actual differentiator: **context-specific, multi-source, evidence-weighted, provenance-preserving, dual-resolution (gene + locus)** — but this only matters if it translates to better predictions and variant-aware interpretation.

---

## Execution Order

1. Build core graph (ChromLinker/ChromBPNet + ChIP-seq + motifs + RegulatoryLocus nodes) — **this is where you are now**
2. GWAS/Variant overlay + GTEx eQTLs (variant interpretation needs eQTL support early)
3. Benchmark edge quality against CollecTRI/DoRothEA
4. Initial weight learning (Stage 1: structured DB labels)
5. Corpus selection + text extraction, validate against TRRUST (precision >80%)
6. Table/supplement extraction
7. Revised weight learning (Stage 2: with literature features)
8. Perturbation prediction benchmark (GEARS + your prior vs. baselines)
9. Cross-context transfer experiments
10. Context assembly (BOND, InteractionContext, DEG/Drug overlays) + IPF AT2 demonstration
11. Figure/vision extraction (enhancement layer, build last)
12. Prospective validation (if aiming above Bioinformatics)
13. Agent layer (last)

---

## The Bottom Line

The graph is not the paper. The paper is the claim you can defend with it. Build the graph as infrastructure, benchmark it as science, and keep the claim narrow enough that reviewers can't dismiss it as packaging.
