# DPI Knowledge Graph — Final Schema
## Provenance-First, Context-Normalized, Dual-Resolution Regulatory Evidence Graph

> **Finalized design:** This document supersedes the earlier `InteractionContext` / generic `Evidence` / global `BINDS_AT` schema. The core philosophy is unchanged: a clean gene-level regulatory proposition is backed by context-specific, locus-level, experiment-traceable observations. The redesign makes context, provenance, TF identity, locus-to-gene assignment, regulatory effect, and model scoring explicit before large-scale ingestion begins.

## Concrete Example: MYC → BCL2 in A549

Read left to right. The graph distinguishes a **canonical proposition** from a **context-specific statement**, then traces the statement to the observations and experiments that support or refute it.

```text
Gene:TF (MYC) ──REGULATES_VIA──▶ RegulatoryInteraction ──TARGETS──▶ Gene (BCL2)
                                      │
                                HAS_STATEMENT
                                      ▼
                              ContextualStatement
                              context_coherence: matched
                              direction:
                                p_activating: 0.78
                                p_repressing: 0.05
                                p_no_effect: 0.07
                              epistemic_uncertainty: 0.10
                              B/L/R: B2 / L1 / R2
                                      │
                                IN_CONTEXT
                                      ▼
                              BiologicalContext
                              human / A549 / lung-derived
                              cell_line / NSCLC

Measured TF occupancy:                     Regulatory effect:
Gene:TF (MYC)                              PerturbationEffectObservation
      │ BINDER_IN                                      │
      ▼                                                ├──PERTURBED_TF──▶ MYC
BindingObservation                                  ├──AFFECTS_GENE──▶ BCL2
      │ AT_LOCUS                                      └──IN_CONTEXT──▶ context
      ▼
RegulatoryLocus ── participates in ──▶ LocusGeneLink ──TO_GENE──▶ BCL2
      │                                     │
      └── locus activity observation        └── IN_CONTEXT ──▶ context

Every observation is supported/refuted by typed EvidenceAssertion nodes:
EvidenceAssertion ──ASSERTS{polarity}──▶ Observation/Statement
       │
    FROM_RUN
       ▼
AnalysisRun ──USES_EXPERIMENT──▶ Experiment ──PART_OF──▶ Study ──REPORTED_IN──▶ Publication
EvidenceAssertion ──REPORTED_IN──▶ Publication        [optional for literature/curated claims]
```

The key semantic distinction is:

- `RegulatoryInteraction` = the proposition that MYC directly regulates BCL2 in at least one biological context.
- `ContextualStatement` = what is supported in one harmonized biological context.
- `BindingObservation`, `LocusGeneLink`, and `PerturbationEffectObservation` = the biological observations contributing to the B/L/R evidence axes.
- `EvidenceAssertion` = a source/run-specific claim about one observation or statement; it may point directly to a source publication and does not require an `Experiment` when the evidence is literature- or computation-derived.
- `ConfidenceScore` = a versioned model output, never an unexplained float on the interaction.

---

## Abstract Schema

```text
═══════════════════════════════════════════════════════════════════════════════
CORE BIOLOGICAL ENTITIES
═══════════════════════════════════════════════════════════════════════════════

Gene(:TF)                         Motif ──MOTIF_OF──▶ MotifFamily / TFClass
[species-scoped Ensembl ID]                              │
      │                                                   └──CANDIDATE_BINDER──▶ Gene(:TF)
      │
      └──ORTHOLOG_OF────────────────────────────────────▶ Gene (other species)

RegulatoryLocus
[registry-anchored, chr/start/end/assembly]

BiologicalContext
[species, system_type, cell_type, tissue, disease, dev_stage, resolution]

Variant [assembly:chr:pos:ref:alt]
GWASStudy / CredibleSet
RegulatoryComplex
Drug                                                     [Optional]

═══════════════════════════════════════════════════════════════════════════════
PROPOSITION LAYER
═══════════════════════════════════════════════════════════════════════════════

Gene:TF ──REGULATES_VIA──▶ RegulatoryInteraction ──TARGETS──▶ Gene
                                  │
                            HAS_STATEMENT
                                  ▼
                         ContextualStatement ──IN_CONTEXT──▶ BiologicalContext
                         [B/L/R tiers, edge_class,
                          direction posterior,
                          disagreement, status,
                          context coherence]

═══════════════════════════════════════════════════════════════════════════════
OBSERVATION LAYER
═══════════════════════════════════════════════════════════════════════════════

Gene:TF or MotifFamily ──BINDER_IN──▶ BindingObservation
                                         │ AT_LOCUS
                                         ▼
                                  RegulatoryLocus
                                         │
                                         └──IN_CONTEXT──▶ BiologicalContext

RegulatoryLocus ──FROM_LOCUS◀── LocusGeneLink ──TO_GENE──▶ Gene
                                   │
                                   └──IN_CONTEXT──▶ BiologicalContext

RegulatoryLocus ◀──OF_LOCUS── LocusActivityObservation
                                   │
                                   └──IN_CONTEXT──▶ BiologicalContext

Gene:TF ◀──PERTURBED_TF── PerturbationEffectObservation ──AFFECTS_GENE──▶ Gene
                                   │
                                   └──IN_CONTEXT──▶ BiologicalContext

Gene ◀──OF_GENE── ExpressionObservation ──IN_CONTEXT──▶ BiologicalContext

Variant ──OVERLAPS──▶ RegulatoryLocus
Variant ──IN_CREDIBLE_SET{pip}──▶ CredibleSet ──FOR_STUDY──▶ GWASStudy
GWASAssociation ──OF_VARIANT──▶ Variant ──IN_STUDY──▶ GWASStudy
Gene ──DE_IN{logFC,se,q,tested}──▶ DEAnalysis

AllelicEffectObservation / MolecularQTL / ColocalizationEvidence
ComplexObservation / Cross-species locus mapping

═══════════════════════════════════════════════════════════════════════════════
EVIDENCE + PROVENANCE
═══════════════════════════════════════════════════════════════════════════════

EvidenceAssertion ──ASSERTS{polarity}──▶ Observation or ContextualStatement
       │
    FROM_RUN
       ▼
AnalysisRun ──USES_EXPERIMENT──▶ Experiment ──PART_OF──▶ Study ──REPORTED_IN──▶ Publication
EvidenceAssertion ──REPORTED_IN──▶ Publication        [optional; no Experiment required]

ConfidenceScore ──SCORES──▶ ContextualStatement / RegulatoryInteraction
[score, interval, model version, feature version, training snapshot,
 calibration, code commit, timestamp; append-only]

═══════════════════════════════════════════════════════════════════════════════
OUTSIDE THE GRAPH
═══════════════════════════════════════════════════════════════════════════════
raw peaks • per-base attributions • full matrices • raw motif hits •
full GWAS/QTL summary statistics • immutable feature snapshots • model artifacts
```

---

## 1. Node Types

### 1.1 Regulatory, context, observation, and provenance nodes

| Node | Purpose | Key properties |
|---|---|---|
| **Gene** (`:TF` label when appropriate) | Species-specific gene entity | `ensembl_gene_id` (stable root ID), `species`, `symbol`, `hgnc_id`/`mgi_id`, `entrez_id`, `biotype`, `strand`, `annotation_release`, `gene_model_version`, `tss_positions[]`, `is_tf`, `tf_census_source` |
| **Motif** | PWM / motif identity | `jaspar_id`, `version`, `name`, `information_content` |
| **MotifFamily / TFClass** | Family-level sequence specificity | `family_id`, `name`, `dbd_type` |
| **RegulatoryLocus** | Stable regulatory coordinate | `locus_id`, `chr`, `start`, `end`, `assembly`, `registry`, `registry_version`, `ccre_class`, `mappability`, `blacklist_flag`, `liftover_status` |
| **BiologicalContext** | Shared harmonized biological situation | `context_id`, `species`, `system_type`, `cell_type`, `cell_line`, `tissue`, `disease`, `dev_stage`, `resolution`, `label_raw[]`, `bond_version`; the ID hash excludes treatment/dose/time/genotype/perturbation/donor fields, which belong to observations or analysis-specific metadata |
| **RegulatoryInteraction** | Canonical TF→Gene proposition | `interaction_id`, `species`, `first_asserted`; optional derived summaries only |
| **ContextualStatement** | Interaction × context statement | `statement_id`, `tier_B`, `tier_L`, `tier_R`, `edge_class`, `p_activating`, `p_repressing`, `p_no_effect`, `epistemic_uncertainty`, `direction_basis`, `disagreement`, `status`, `context_coherence`; independent-study counts are derived/cached, not authoritative |
| **BindingObservation** | TF- or motif-family occupancy observation | `obs_id`, `assay`, `occupancy_statistic`, `motif_supported`, `origin` (`measured`/`predicted`), `allele_specific`, optional treatment/dose/time/genotype/donor metadata |
| **LocusActivityObservation** | Context-specific activity/accessibility of a locus | `obs_id`, `assay`, `activity_statistic`, `active_call`, `origin` (`measured`/`predicted`), optional treatment/dose/time/genotype/donor metadata |
| **LocusGeneLink** | Locus→gene assignment | `link_id`, `method`, `link_tier`, `score`, `distance_bp`, `q_value`, `origin` (`annotation`/`predicted`/`measured`/`validated`) |
| **PerturbationEffectObservation** | Regulatory-effect observation following TF perturbation | `obs_id`, `perturbation_type`, `effect_size`, `effect_unit`, `p_value`, `q_value`, `time_point`, `origin` (`measured`/`inferred`), optional dose/genotype/donor metadata |
| **ExpressionObservation** | Gene expression in a context | `obs_id`, `mean_expr`, `pct_cells`, `assay`, `dataset_id` |
| **EvidenceAssertion** | Typed, polarity-bearing source assertion | `assertion_id`, `evidence_type`, `directness`, `evidence_origin` (`measured`/`predicted`/`inferred`/`curated`/`reported`/`annotation`), `statistic_name`, `statistic_value`, `threshold_used`, `detection_power`, `independence_resolvable`, `ingest_version` |
| **AnalysisRun** | One processing/extraction/model run | `run_id`, `source_db`, `pipeline`, `version`, `parameters_hash`, `access_date`, optional `source_snapshot_id`, `input_artifact_refs[]`, `model_artifact_ref`; an AnalysisRun may use zero, one, or many experiments |
| **Experiment** | Deduplication unit for experimental evidence | `experiment_id`, `assay`, `target`, `antibody`, `biosample_raw`, `lab`, `platform`, `qc_flags`, `external_accessions[]` |
| **Study** | Groups experiments/datasets | `study_id`, `external_accessions[]`, `title`, `submission_date` |
| **Publication** | Publication provenance | `pmid`, `doi`, `year`, `journal`, `retraction_status` |
| **ConfidenceScore** | Versioned score/ranking output | `score`, `lower`, `upper`, `score_type`, `prediction_target`, `endpoint_definition`, `calibrated`, `model_name`, `model_version`, `feature_set_version`, `training_snapshot_id`, `training_cutoff`, `calibration_id`, `code_commit`, `created_at`, `superseded_by` |

### 1.2 Disease-genetics and differential-expression nodes

| Node | Purpose | Key properties |
|---|---|---|
| **Variant** | Normalized genomic variant | `variant_key` = `assembly:chr:pos:ref:alt`, `rsids[]`, `variant_type`, `liftover_status`, optional population AF annotations |
| **GWASStudy** | GWAS study provenance | `study_accession`, `trait_efo`, `trait_mondo`, `n_cases`, `n_controls`, `ancestry`, `pmid`, `sumstats_available` |
| **GWASAssociation** | Study-specific variant association | `p_value`, `beta` or `odds_ratio`, `se`, `effect_allele`, `imputation_quality` |
| **CredibleSet** | Fine-mapped signal | `credible_set_id`, `method`, `coverage` |
| **DEAnalysis** | Explicit differential-expression contrast | `analysis_id`, `contrast`, `assay`, `pipeline`, `n_case`, `n_control`, `covariates`, `multiple_testing_method`; case/control contexts are first-class graph relations, not only ID properties |

### 1.3 Additional final-schema nodes

| Node | Purpose |
|---|---|
| **AllelicEffectObservation** | Variant changes locus accessibility/activity/binding/methylation; measured or predicted |
| **MolecularQTL** | eQTL/caQTL/sQTL observation with tissue/context and study provenance |
| **ColocalizationEvidence** | Shared causal-signal evidence between GWAS and QTL signals |
| **RegulatoryComplex** | Canonical known TF/cofactor complex |
| **ComplexObservation** | Complex/co-occupancy at a locus in a context |
| **MechanisticHypothesis** | Ordered, explicitly labeled hypothesis path with weakest link and competing alternatives |
| **Drug / DrugTargetAssertion** | Optional tractability overlay; external/query-time first |

> **Gene identity rule:** use the species-scoped Ensembl stable gene identifier (without relying on the version suffix as permanent identity). Record the annotation release and gene-model version separately. HGNC/MGI/Entrez/symbols are searchable cross-references, not join keys.

> **Coordinate rule:** every coordinate-bearing object must carry genome assembly. Adopt one canonical assembly per species for graph materialization (e.g. hg38 and mm39); imported coordinates retain liftOver provenance/status.

> **Context identity rule:** `context_id` is a deterministic hash of stable biological dimensions only: species, system type, cell type/cell line, tissue, disease, developmental stage, and resolution. Treatment, perturbation, dose, time, genotype, sex, donor, and cohort are observation/analysis dimensions and do **not** alter the shared biological-context identity.

---

## 2. Edge Types

| Edge | From → To | Meaning | Context-specific? |
|---|---|---|---|
| `:REGULATES_VIA` | Gene:TF → RegulatoryInteraction | This TF is the regulator in the canonical proposition | No |
| `:TARGETS` | RegulatoryInteraction → Gene | This gene is the target | No |
| `:HAS_STATEMENT` | RegulatoryInteraction → ContextualStatement | Context-specific interpretation of the proposition | — |
| `:IN_CONTEXT` | Observation/ContextualStatement → BiologicalContext | Situates the observation/statement | Yes |
| `:BINDER_IN` | Gene:TF or MotifFamily → BindingObservation | Specific measured TF or family-level predicted binder | Via observation |
| `:AT_LOCUS` | BindingObservation → RegulatoryLocus | Where occupancy/binding evidence occurs | Via observation |
| `:OF_LOCUS` | LocusActivityObservation → RegulatoryLocus | Locus whose activity is measured/predicted | Via observation |
| `:FROM_LOCUS` | LocusGeneLink → RegulatoryLocus | Source regulatory element | Usually context-specific for distal links |
| `:TO_GENE` | LocusGeneLink → Gene | Candidate/validated target gene | Usually context-specific for distal links |
| `:PERTURBED_TF` | PerturbationEffectObservation → Gene:TF | Perturbed regulator | Yes |
| `:AFFECTS_GENE` | PerturbationEffectObservation → Gene | Measured downstream expression effect | Yes |
| `:OF_GENE` | ExpressionObservation → Gene | Expression measurement | Yes |
| `:ASSERTS` | EvidenceAssertion → Observation/ContextualStatement | Evidence supports/refutes/is inconclusive about the target | Inherited; carries `polarity` |
| `:FROM_RUN` | EvidenceAssertion → AnalysisRun | Processing that produced the assertion | No |
| `:USES_EXPERIMENT` | AnalysisRun → Experiment | Optional experimental input(s) used by the run; zero-or-many allowed | No |
| `:PART_OF` | Experiment → Study | Experiment grouping | No |
| `:REPORTED_IN` | EvidenceAssertion/Study/Experiment → Publication | Source/publication provenance; literature assertions may connect directly without an Experiment | No |
| `:SCORES` | ConfidenceScore → ContextualStatement/RegulatoryInteraction | Versioned model output | No |
| `:MOTIF_OF` | Motif → MotifFamily | Motif taxonomy | No |
| `:CANDIDATE_BINDER` | MotifFamily → Gene:TF | TFs compatible with family motif | No |
| `:OVERLAPS` | Variant → RegulatoryLocus | Coordinate containment | No |
| `:OF_VARIANT` | GWASAssociation → Variant | GWAS association statistic | No |
| `:IN_STUDY` | GWASAssociation → GWASStudy | Study provenance | No |
| `:IN_CREDIBLE_SET` | Variant → CredibleSet | Fine-mapping membership; carries `pip` | No |
| `:FOR_STUDY` | CredibleSet → GWASStudy | Signal provenance | No |
| `:DE_IN` | Gene → DEAnalysis | Gene result in a defined case-control contrast | Via contexts |
| `:CASE_CONTEXT` | DEAnalysis → BiologicalContext | Case biological context | Yes |
| `:CONTROL_CONTEXT` | DEAnalysis → BiologicalContext | Control biological context | Yes |
| `:MEMBER_OF` | Gene:TF → RegulatoryComplex | Complex membership; carries member role | No |
| `:MEDIATED_BY` | ContextualStatement → RegulatoryComplex | Complex is implicated in this context | Yes |
| `:ORTHOLOG_OF` | Gene → Gene | Cross-species correspondence; carries cardinality/confidence | No |
| `:CONSERVED_WITH` | RegulatoryInteraction → RegulatoryInteraction | Explicit cross-species conservation assertion | No |
| `:SYNTENIC_WITH` | RegulatoryLocus → RegulatoryLocus | Cross-species locus mapping | No |

Derived performance edges such as `:BINDS_AT_ANY` may be materialized for query speed, but they must be rebuildable from observation nodes and must never become the authoritative source.

---

## 3. Property / Semantic Split

| Layer | What lives here | Question answered |
|---|---|---|
| **RegulatoryInteraction** | TF-target proposition | “Could this TF directly regulate this gene in at least one context?” |
| **ContextualStatement** | B/L/R evidence tiers, direction probabilities, epistemic uncertainty, context coherence, status | “What is supported in this biological context?” |
| **BindingObservation** | TF/motif-family occupancy at a locus | “Who or what sequence family appears to bind here?” |
| **LocusActivityObservation** | ATAC/DNase/histone activity | “Is this regulatory locus active in this context?” |
| **LocusGeneLink** | promoter/ABC/contact/coloc/CRISPRi assignment | “Why is this locus assigned to this gene?” |
| **PerturbationEffectObservation** | measured downstream effect | “Does perturbing the TF change this target?” |
| **EvidenceAssertion** | source-specific native statistic, polarity, directness, evidence origin | “Which source/run says this, and what exactly did it measure/report/infer?” |
| **Experiment / Study / Publication / AnalysisRun** | provenance and deduplication | “Are two pieces of evidence really independent?” |
| **ConfidenceScore** | versioned model/ranking result | “Which model produced this score and with what uncertainty?” |
| **DEAnalysis** | disease/cell contrast result | “Does this gene change in disease?” — annotation, never TF-edge evidence |

---

## 4. Evidence Sources and Their Roles

| Source | Role in final design | Independence / semantic rule |
|---|---|---|
| **ChromLinker / ChromBPNet** | Core predicted accessibility/motif-family and candidate regulatory evidence | Sequence attribution is not automatically a TF-specific occupancy claim. Specific TF assignment needs expression and preferably TF-specific occupancy evidence. Version every internal run. |
| **CistromeDB** | Core measured binding/QC source | Ingest experiment-linked peaks/QC. Do not treat target-gene abstractions as independent TF-target truth. |
| **ChIP-Atlas** | Core measured binding source | Ingest peak/experiment evidence; target-gene proximity tables are not direct-regulation evidence. |
| **UniBind** | Core high-stringency motif-supported binding evidence | Often derived from the same parent ChIP experiment; adds processing/stringency, not an independent biological experiment. |
| **GTRD / ReMap** | Secondary ChIP-derived binding | Useful alternative processing/coverage; deduplicate by experiment/study. |
| **JASPAR** | Core motif definitions | Motif plausibility / family identity, not occupancy. |
| **TF census / TFClass** | Core identity/taxonomy utility | Defines TF status and family/paralog relationships. |
| **TRRUST / CollecTRI / DoRothEA** | Validation/baseline block initially | Treat as correlated curated resources, not independent votes. Avoid train/evaluation leakage. |
| **Perturb-seq / TF perturbation data** | Core orthogonal regulatory-effect validation | Direct causal perturbation of TF, but downstream expression effects can still be indirect. Store as `PerturbationEffectObservation`. |
| **CRISPRi/CRISPRa CRE perturbation** | Core validation for locus→gene links | Highest-value validation for distal enhancer-gene assignment. |
| **ABC / ENCODE rE2G** | Core/strong locus→gene prediction | Store as predicted `LocusGeneLink`; validate against CRE perturbation. |
| **ENCODE SCREEN / project lung ATAC consensus** | Core locus registry/activity | Registry coordinates are not evidence that a locus is active in every context. Activity is a separate observation. |
| **PubMed / PMC** | Secondary, gated literature assertions | Direction/context/directness; publication-level dedup and held-out manual QC required before entering scoring. |
| **PubTator Central** | Core extraction utility | NER/normalization helper, not regulatory evidence. |
| **BioRED** | Optional extraction-model supervision | Not a TF-target gold-standard benchmark. |
| **GWAS Catalog** | Core variant-trait associations | Use study provenance and fine-mapping where available. |
| **Open Targets** | Core for credible sets/colocalization where appropriate; optional for drugs | Do not use L2G as a feature and then evaluate the same gene-assignment problem against it. |
| **GTEx + eQTL Catalogue** | QTL and colocalization support | Tissue/cell context matters; eQTL overlap is not equivalent to colocalization. |
| **ENCODE SCREEN / caQTL / allele-specific ATAC** | Variant→locus activity evidence | Distinguish coordinate overlap from functional allelic effect. |
| **DGIdb / ChEMBL / Open Targets drugs** | Optional application layer | Query-time/external first; drug-target mechanism should be typed if materialized. |

### Evidence independence rule

**Never use “number of databases” as a proxy for independent evidence.** The unit of independence is the underlying experiment/study/publication as appropriate. Build and maintain an accession crosswalk across ChIP aggregators; unresolved provenance cannot contribute to independence-count features.

---

## 5. Direct-Regulation Evidence Tiers and Scoring

### 5.1 Three orthogonal evidence axes

#### B — Binding / occupancy

| Tier | Requirement |
|---|---|
| **B0** | Motif match only |
| **B1** | Sequence-model / footprint / accessibility-based family-level binding support in a matched context; specific TF may be unresolved |
| **B2** | Measured TF-specific occupancy (ChIP/CUT&RUN/CUT&Tag) at the locus in a compatible context |
| **B3** | Strong context-matched measured occupancy supported by ≥2 independent studies, ideally motif-consistent |

#### L — Locus→gene assignment

| Tier | Requirement |
|---|---|
| **L0** | Nearest-gene / distance annotation only |
| **L1** | Promoter-proximal assignment to an annotated TSS, or weak contextual link |
| **L2** | Context-matched ABC/rE2G, contact map, or properly supported QTL/colocalization evidence |
| **L3** | CRE perturbation validated in a matched/closely related system |

#### R — Regulatory effect

| Tier | Requirement |
|---|---|
| **R0** | No regulatory-effect evidence |
| **R1** | Correlational evidence only |
| **R2** | TF perturbation changes target expression, with appropriate statistical support |
| **R3** | Context-matched, temporally/experimentally strong evidence for a primary/direct effect or CRE perturbation consistent with TF effect |

### 5.2 Named edge classes

| Class | Typical requirement | Interpretation |
|---|---|---|
| `CANDIDATE` | B≤1 and/or weak L/R | Hypothesis-generation only |
| `BOUND_PROXIMAL` | B≥2, L≥1, R≤1 | TF occupies a target promoter/proximal region; binding claim, not necessarily regulation |
| `PUTATIVE_DIRECT` | B≥2, L≥2 for distal loci, R≤1 | Bound and credibly linked; regulatory effect not yet measured |
| `SUPPORTED_DIRECT_PROMOTER` | B≥2, **L≥1 promoter identity**, R≥2, context compatible | Evidence supports a promoter-mediated direct-regulation proposition; not proof of causal mechanism |
| `SUPPORTED_DIRECT_DISTAL` | B≥2, **L≥2**, R≥2, context compatible | Evidence supports a distal direct-regulation proposition; not proof of causal mechanism |
| `SUPPORTED_DIRECT_HIGH` | Strong B + strong L + R3, context matched | Highest-evidence prospective-validation tier |
| `EFFECT_ONLY` | R≥2 with B≤1 | TF perturbation affects gene, but direct binding mechanism is unresolved/likely indirect |
| `REFUTED` | Adequately powered negative evidence without compatible support | Tested negative in a defined context |

B/L/R tiers are properties of the **ContextualStatement**, not the global `RegulatoryInteraction`. A canonical interaction may cache derived summaries for performance, but context-specific evidence is authoritative.

### 5.3 Learned scores

Do **not** define a bare `base_confidence` as “P(the interaction is biologically real).” Curated positives and unlabeled TF-gene pairs do not provide an identifiable universal probability of truth.

For the final scoring implementation:

1. Produce a **ranking score** for context-specific candidate statements using experiment-deduplicated, group-aware features.
2. When possible, calibrate probabilities only for **observable endpoints**, e.g. `P(target changes above threshold after TF perturbation in a matched context)`.
3. Use hard/matched negatives and verified negatives; never rely only on random zero-evidence pairs.
4. Store the output in append-only `ConfidenceScore` nodes with uncertainty and full model provenance.
5. Keep direction separate: store `p_activating`, `p_repressing`, and `p_no_effect`; store `epistemic_uncertainty` and `disagreement` separately so ignorance is not treated as a biological outcome.
6. Every `ConfidenceScore` must declare `score_type`, `prediction_target`, `endpoint_definition`, and whether it is calibrated. Context-specific scores attach primarily to `ContextualStatement`; any interaction-level score is an explicitly derived aggregation.

A hierarchical/partially pooled model is an optional modeling choice after the baseline scorer is benchmarked; it is not required by the schema.

---

## 6. Co-Factor Representation

Keep a canonical `RegulatoryComplex` entity, but do not encode biological cooperativity as simple Boolean `AND/OR` logic.

```text
Gene:TF ──MEMBER_OF{role}──▶ RegulatoryComplex
Gene:TF ──MEMBER_OF{role}──▶ RegulatoryComplex

ContextualStatement ──MEDIATED_BY──▶ RegulatoryComplex
RegulatoryComplex ── observed through ──▶ ComplexObservation
ComplexObservation ──AT_LOCUS──▶ RegulatoryLocus
ComplexObservation ──IN_CONTEXT──▶ BiologicalContext
```

Recommended complex properties include `complex_class` and `requirement` such as `obligate`, `facilitating`, `competitive`, or `unknown`. BioGRID can be a weak PPI prior; canonical complex resources and locus/context-specific co-occupancy are stronger evidence.

---

## 7. GWAS / Variant Mechanism Example

The variant layer must represent a chain of distinct evidence classes rather than collapsing “overlap” into mechanism.

```text
GWASStudy
   ▲
FOR_STUDY
   │
CredibleSet ◀──IN_CREDIBLE_SET{pip}── Variant
                                          │
                                      OVERLAPS
                                          ▼
                                  RegulatoryLocus
                                    ▲       ▲
                                    │       │
                          locus activity   binding
                                    │       │
                       LocusActivityObs   BindingObservation
                                    │       │
                                    └──IN_CONTEXT──▶ BiologicalContext
                                          │
                                    LocusGeneLink
                                          │
                                       TO_GENE
                                          ▼
                                        Gene
                                          │
                                         DE_IN
                                          ▼
                                      DEAnalysis
```

For a path to be called **mechanistically plausible** rather than merely associated, require as much of the following as possible:

1. Fine-mapped credible-set membership with non-trivial PIP.
2. The locus is active in the relevant biological context.
3. Evidence that the allele affects locus activity/binding where available (`AllelicEffectObservation`), rather than assuming every overlap disrupts a motif.
4. TF-specific measured occupancy in a compatible context, or explicitly family-level predicted binder status.
5. A defensible locus→gene link; for distal loci, prefer L2/L3 evidence.
6. Disease expression/context overlays remain **associative**, never causal proof.

### MUC5B / rs35705950 use-case rule

Use the MUC5B/IPF locus as a **mechanistic hypothesis demonstration**, not as a pre-resolved “variant disrupts FOXA2 motif in AT2” fact. The graph must be able to represent variant association, locus activity, nearby/adjacent TF occupancy, methylation/accessibility effects, multiple epithelial compartments, competing mechanisms, and uncertainty about causal mediation. That complexity is a test of the schema, not a reason to simplify the biology.

---

## 8. Evidence Processing Pipeline (Final)

```text
SCHEMA + IDENTIFIERS + CONTEXT VOCABULARIES
        ↓
EXPERIMENT / STUDY / PUBLICATION REGISTRY
        ↓
ACCESSION CROSSWALK ACROSS CHROMATIN DATABASES
        ↓
LOCUS REGISTRY (cCRE + lung ATAC consensus; canonical assembly)
        ↓
EXPRESSION + LOCUS-ACTIVITY CONTEXT LAYER
        ↓
MEASURED BINDING OBSERVATIONS
        ↓
MOTIF / TFCLASS + PREDICTED BINDING (family-level where unresolved)
        ↓
LOCUS→GENE LINKS + CRISPRi E-G BENCHMARK
        ↓
PERTURBATION-EFFECT OBSERVATIONS FOR FEATURE/TRAINING POOL
(designated gold datasets reserved and masked from features)
        ↓
LEAKAGE AUDIT + BASELINE BENCHMARK HARNESS
        ↓
CONFIDENCE / RANKING MODEL
        ↓
GWAS + CREDIBLE SETS + VARIANT OVERLAP
        ↓
QTL / COLOCALIZATION / ALLELIC EFFECTS
        ↓
DEAnalysis DISEASE OVERLAYS
        ↓
PERTURBATION UTILITY BENCHMARKS
        ↓
LITERATURE EXTRACTION WITH MANUAL QC GATE
        ↓
COMPLEXES / CROSS-SPECIES / DRUG / AGENT CAPABILITIES
```

### Graph / warehouse boundary

**Graph:** stable entities, normalized contexts, summarized observations, evidence assertions, provenance, scores, and selected disease/variant objects.

**Warehouse/object store:** raw peaks, per-base attribution tracks, full expression matrices, motif scan hits, full GWAS/QTL summary statistics, raw text spans, immutable feature snapshots, and model artifacts.

Do not mint one `RegulatoryLocus` node per peak per experiment. Use a versioned locus registry and materialize only loci participating in retained observations/links or disease-variant queries.

---

## 9. Leakage-Safe Evaluation Rules

1. Treat curated TF-target resources as one correlated evidence block unless source provenance proves otherwise.
2. Treat public ChIP aggregators as correlated processing layers over shared experiments; split/deduplicate by study/experiment.
3. Prevent publication leakage between curated labels and literature features.
4. Evaluate held-out TFs, TF families, targets, studies/publications, and biological contexts separately.
5. Add a temporal holdout when practical: freeze features before a date and evaluate relationships first established after that date.
6. Use orthogonal gold sets for headline claims:
   - TF perturbation for regulatory-effect prediction;
   - CRE perturbation for locus→gene links;
   - allele-specific/caQTL data for variant→locus activity.
7. Include a popularity-only baseline (TF/target publication counts and expression) to demonstrate that the model is not simply a well-studiedness detector.
8. Predefine the primary split/metric before final benchmark runs.
9. **Fold-specific evidence masking is mandatory:** before computing B/L/R, `edge_class`, aggregate counts, or model features for a test fold, remove all assertions/observations belonging to that fold's held-out gold data (e.g. Perturb-seq for R, CRISPRi for L, allele-specific data for variant effects), then recompute the statement and feature snapshot. Never let the evaluation answer leak into the evidence tiers being evaluated.

---

## 10. Final Scope and Materialization Rules

### Required final regulatory backbone

Non-negotiable pieces:

- species-scoped Gene IDs + Motif/TFClass;
- shared `BiologicalContext`;
- `RegulatoryInteraction` + `ContextualStatement`;
- `BindingObservation`, `LocusActivityObservation`, `LocusGeneLink`, `PerturbationEffectObservation`, `ExpressionObservation`;
- `EvidenceAssertion` + `AnalysisRun` + `Experiment` + `Study` + `Publication` provenance spine;
- versioned `ConfidenceScore`;
- versioned `RegulatoryLocus` registry;
- the perturbation-effect observation schema and reserved-gold masking rules;
- immutable, fold-specific feature snapshots for leakage-safe scoring.

### Required disease and variant layers

- explicit DE contrasts (`DEAnalysis`) with `CASE_CONTEXT` / `CONTROL_CONTEXT`;
- GWAS study + credible-set representation;
- variant ↔ locus overlap and disease-specific prioritization.

### Additional final-schema capabilities

- MolecularQTL + formal colocalization;
- allelic-effect observations;
- locus/context-specific complex observations;
- cross-species orthology + syntenic locus mapping;
- literature assertions promoted into scoring after manual QC;
- mechanistic-hypothesis objects;
- drug overlay;
- natural-language/agent interface last.

