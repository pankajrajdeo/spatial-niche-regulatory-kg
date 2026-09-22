# DPI-KG Paper Strategy — Final

> **Final framing:** the knowledge graph is infrastructure. The paper must demonstrate that a provenance-first, context-specific, locus-backed regulatory evidence prior improves scientifically meaningful ranking or prediction and supports auditable disease-mechanism hypotheses. The revised plan explicitly separates measured binding, locus→gene assignment, regulatory effect, disease expression, and variant evidence, and uses leakage-safe evaluation.

## Survivable Claim

**Primary claim:**

> **A context-specific, locus-backed TF-target evidence prior improves regulatory subnetwork prioritization in lung disease and enables auditable variant-aware and literature-aware interpretation.**

Do **not** lead with:

- “we built a knowledge graph”;
- “we built an agent”;
- “we combined graph + GNN + LLM”;
- “first agentic system for TF-target analysis”;
- or a universal claim that a stored score is the probability an interaction is biologically true.

The contribution should be the combination of **better ranking/prediction + explicit evidence decomposition + reproducible provenance + a convincing lung/IPF use case**.

---

## Required Results

| # | Result | What it must prove |
|---|---|---|
| **1** | DPI-KG ranks context-specific TF-target candidates better than matched generic/curated priors on **orthogonal gold sets** | Evidence integration adds value beyond well-studiedness and existing priors |
| **2** | A perturbation-response model using the DPI-KG prior outperforms the same model without it and with a matched generic prior | The prior has downstream predictive utility, not just descriptive appeal |
| **3** | Performance remains useful under held-out TF/TF-family/context or low-data transfer settings | The context-aware evidence design contributes real generalization value; partial pooling is an optional modeling choice, not a required assumption |
| **4** | The locus→gene layer predicts/recovers experimentally tested CRE→gene relationships better than proximity-only baselines | The dual-resolution architecture is validatable rather than decorative |
| **5** | Fine-mapped IPF/related-trait variants can be assembled into **mechanistically plausible, uncertainty-labeled** regulatory hypotheses in relevant lung epithelial compartments | Variant-aware interpretation is useful without overstating causality |
| **6** | A small prospective or targeted experimental validation supports a subset of high-ranked novel statements, if aiming for a higher-impact venue | Demonstrates practical value beyond retrospective benchmarking |

### Important adjustment to the original Result 5

Do **not** make “IPF GWAS regulatory-edge enrichment” the sole headline statistic. The flagship variant layer should be evaluated as a **mechanism-prioritization task** with fine-mapped variants, matched nulls where appropriate, explicit link tiers, and case studies whose weakest mechanistic link is visible.

---

## Baselines to Beat

Use the same inputs/contexts wherever possible and state each baseline's intended use fairly.

| Baseline | Why it is needed |
|---|---|
| **Popularity-only baseline** | Mandatory diagnostic: TF publication count + target publication count + expression/coverage. Shows DPI-KG is not merely a well-studiedness detector. |
| **No prior** | Perturbation model without GRN information |
| **CollecTRI / DoRothEA** | Strong curated/context-free regulatory priors; treat them as a correlated resource block, not independent gold standards |
| **SCENIC+** | Cell-type-specific enhancer-driven GRN baseline |
| **CellOracle** | Perturbation-oriented GRN baseline |
| **GEARS / perturbation model without DPI-KG prior** | Strong downstream prediction baseline |
| **Same perturbation model + matched generic prior** | Tests whether context/locus evidence adds value rather than any graph prior helping |
| **Nearest-gene / promoter-distance locus→gene baseline** | Essential baseline for the dual-resolution locus layer |
| **ABC/rE2G or other appropriate E-G baseline** | Strong enhancer→gene comparison where inputs are available |

Do not use TRRUST vs CollecTRI vs DoRothEA as if they are cleanly independent train/test resources without publication/source de-overlap.

---

## Key Metrics

### TF-target / regulatory-effect ranking

- AUPRC / precision-recall on orthogonal perturbation or direct-regulation gold sets
- partial AUC / precision at high-recall or high-precision operating regions
- sign accuracy **conditioned on a measurable effect existing**
- effect-size correlation for perturbation response
- calibration metrics only for observable endpoints that genuinely support probability interpretation

### Generalization

- held-out TF performance
- held-out TF-family performance
- held-out target performance
- held-out biological-context performance
- temporal holdout performance
- lightly studied vs well-studied gene strata

### Locus→gene layer

- CRE perturbation positive/negative discrimination
- performance against nearest-gene baseline
- performance stratified by promoter vs distal regulation
- fraction of retained links at L0/L1/L2/L3

### Variant / disease layer

- proportion of prioritized variants with fine-mapped credible-set support
- context-active regulatory-locus support
- allelic-effect support where available
- strength/tier of TF occupancy and locus→gene assignment
- disease DE/cell-compartment relevance as an **association overlay**
- matched-null enrichment only where statistical power is adequate

### Reproducibility / auditability

- accession overlap matrix across ChIP aggregators
- number of **independent studies**, not number of databases
- fraction of assertions with resolvable experiment/publication provenance
- score reproducibility from released feature/model snapshots

---

## Leakage-Safe Evaluation Plan

This is a main-methods requirement, not a supplementary detail.

### Dependency blocks

Treat these as correlated unless provenance proves otherwise:

- curated TF-target resources with overlapping publications/resources;
- GEO/SRA/ENCODE-derived ChIP aggregators;
- curated databases and literature extraction that cite the same publications;
- motif features and motif-filtered ChIP-derived resources;
- ChromBPNet/accessibility features and any labels derived from the same ATAC data.

### Evaluation tiers

**Non-negotiable fold construction rule:** held-out gold evidence is removed **before** B/L/R tiers, `edge_class`, aggregate evidence counts, and feature snapshots are computed. Perturb-seq observations held out for R-axis evaluation cannot contribute to R-tier/features in that fold; CRISPRi enhancer-gene observations held out for L-axis evaluation cannot contribute to L-tier/features. Recompute all derived statement fields after masking.

**Tier 1 — grouped internal development CV**

Report separate held-out analyses for TF, TF family, target, publication/study, and context. Do not average them into one misleading “generalization” score.

**Tier 2 — temporal holdout**

Freeze all features/source snapshots at a cutoff date and evaluate relationships first supported after that date. This is a strong retrospective proxy for prospective discovery.

**Tier 3 — orthogonal headline gold sets**

- TF perturbation / degron data for regulatory-effect prediction;
- CRE perturbation for locus→gene validation;
- caQTL / allele-specific accessibility or occupancy for variant→locus activity;
- downstream perturbation prediction with vs without the prior.

### Negative sets

Use:

- matched negatives on TF/target degree, expression, publication exposure, and locus distance;
- hard negatives with plausible accessible/motif-compatible loci but no measured occupancy/effect;
- verified perturbation-null or CRE-perturbation-null examples for high-quality evaluation.

Random zero-evidence TF-gene pairs are too easy to be the primary negative set.

---

## Critical Warnings

1. **Evidence double-counting:** CistromeDB, ChIP-Atlas, UniBind, GTRD/ReMap may reprocess the same experiment. The unit of independence is experiment/study, never database count.
2. **TF identity from motif/ChromBPNet:** motif-family attribution does not automatically identify a specific paralog. Specific TF claims need expression and preferably TF-specific occupancy.
3. **Binding ≠ regulation:** measured occupancy alone is B-axis evidence, not proof of regulatory effect.
4. **Perturbation ≠ directness:** TF KO/KD can affect genes indirectly. Direct regulation needs compatible binding + locus→gene + effect evidence.
5. **Nearest gene ≠ target gene:** distal links require explicit `LocusGeneLink` evidence and should be benchmarked against CRE perturbation.
6. **eQTL overlap ≠ colocalization:** do not use simple overlap as a causal target assignment.
7. **DE ≠ TF causality:** `DEAnalysis` is a disease prioritization overlay only.
8. **Cell lines ≠ primary lung:** `system_type` must be explicit; cancer-line evidence should not silently support primary-lung claims.
9. **Curated-resource leakage:** TRRUST/CollecTRI/DoRothEA are not cleanly independent gold standards.
10. **Popularity bias:** literature counts and curated positives can make a model rank famous genes. Always report the popularity-only baseline and study-stratified performance.
11. **Score semantics:** retire “probability this relationship is real” unless the target is actually observable/calibratable. Use ranking/predictive score + uncertainty + model provenance.
12. **MUC5B/rs35705950:** use as a complex mechanistic-hypothesis demonstration, not a pre-resolved “FOXA2 motif disruption in AT2” fact. Preserve airway/secretory vs AT2 compartment evidence and competing mechanisms.
13. **Lung vs perturbation-benchmark context:** large public Perturb-seq datasets may not be lung. Label generic perturbation utility separately from lung-specific claims; obtain/generate lung-relevant perturbation evidence if the paper depends on a lung-specific predictive claim.
14. **Internal ChromLinker reproducibility:** freeze/version the internal pipeline and provide ablations so the paper's contribution is not inseparable from an opaque input.
15. **Agent last:** an agent over an unvalidated prior is not a scientific contribution.

---

## Venue Ladder

The venue should be chosen based on achieved evidence, not the ambition of the schema.

| Venue tier | What the project would need |
|---|---|
| **Bioinformatics / NAR Genomics & Bioinformatics-type paper** | Strong leakage-safe TF-target ranking + locus-layer validation + convincing lung/IPF demonstration |
| **Genome Biology-type paper** | Above + robust cross-context/low-data generalization + stronger disease-variant mechanism prioritization |
| **Nature Communications-type paper** | Above + downstream predictive utility + prospective/targeted biological validation |
| **Methods-level top-tier claim** | Broad multi-dataset generalization beyond lung, rigorous orthogonal benchmarks, reproducibility, and substantial prospective validation |

Do not use projected citation counts as a scientific planning criterion.

---

## What Exists (Competitive Landscape)

| Tool/resource | What it does | DPI-KG's intended difference |
|---|---|---|
| **SCENIC+** | enhancer-driven, cell-type-specific regulatory networks | DPI-KG adds experiment-level provenance, cross-context statements, explicit B/L/R evidence decomposition, and disease-variant layers |
| **CellOracle** | GRN inference + in silico perturbation | DPI-KG focuses on multi-source auditable evidence and locus/variant provenance |
| **GRaNIE** | enhancer-GRN inference | DPI-KG integrates multiple modalities and experiment-level evidence dependencies |
| **GEARS / perturbation predictors** | predict perturbation responses | DPI-KG supplies/test a regulatory prior rather than replacing the predictor |
| **GRAND / static regulatory resources** | precomputed networks | DPI-KG is context-normalized and provenance-aware |
| **DoRothEA / CollecTRI** | curated signed TF-target resources | DPI-KG adds cell/locus context and measured/predicted evidence separation |

The differentiator is only meaningful if it yields **better orthogonal prediction and more defensible mechanism prioritization**.

---

## Execution Order

1. **Adopt the final schema, identifiers, closed vocabularies, stable `BiologicalContext` identity, and BOND rules as the single implementation contract.**
2. **Build Experiment/Study/Publication registry and accession crosswalk** across the ChIP aggregators; measure overlap.
3. **Build the versioned locus registry** (cCRE + lung consensus as decided) and canonical assembly rules.
4. **Load lung expression and locus-activity observations.**
5. **Load measured binding observations** plus Motif/TFClass definitions.
6. **Load ChromBPNet/ChromLinker predicted evidence** at family-level where TF identity is unresolved.
7. **Build `LocusGeneLink`** from promoter + ABC/rE2G/contact evidence and establish the CRE-perturbation benchmark.
8. **Load designated perturbation-effect observations for the feature/training pool**, while reserving orthogonal perturbation datasets as untouched gold sets.
9. **Build leakage audit, popularity baseline, benchmark harness, and fold-specific evidence-masking pipeline before fitting any score.**
10. **Train the confidence/ranking model** using experiment-deduplicated features and hard/matched negatives; every score records its prediction target/endpoint.
11. **Load GWAS studies + credible sets + variants** and intersect with registry loci.
12. **Add QTL/colocalization/allelic-effect layer** where available.
13. **Load `DEAnalysis` disease contrasts** with explicit case/control context relations for relevant lung epithelial compartments.
14. **Run perturbation-prediction utility benchmark** with/without the prior.
15. **Build literature QC harness first, then corpus/extraction**, and only then promote accepted assertions into scoring.
16. **Run cross-context transfer experiments.**
17. **Add complexes / cross-species / prospective validation** as justified.
18. **Drug overlay and agent interface last.**

---

## The Bottom Line

The graph is still **not the paper**.

The final project should be described as:

> **A provenance-first, context-normalized evidence system that turns regulatory candidates into auditable, tiered TF-target propositions and tests whether those propositions improve prediction and disease-mechanism prioritization.**

The strongest paper will show that DPI-KG does something a carefully matched baseline cannot: it predicts or prioritizes regulatory biology better, under leakage-safe evaluation, while exposing exactly which experimental link makes each mechanism strong or weak.
