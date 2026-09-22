# DPI Knowledge Graph Architecture
## Provenance-First, Context-Normalized, Dual-Resolution Regulatory Evidence Graph

> **Status: FINAL ARCHITECTURE.** The original dual-resolution concept is retained, but the implementation is revised before large-scale ingestion: shared `BiologicalContext` nodes replace per-interaction context blobs; global TF→locus and locus→gene edges are reified as context-bearing observations; an experiment/study/publication provenance spine prevents evidence double-counting; sequence-model outputs remain motif-family-level until TF identity is independently supported; differential expression is represented as an explicit contrast; and learned scores are versioned ranking/predictive outputs rather than bare probabilities of biological truth.

## Google Doc set-up by Dr. Nathan Salomonis: https://docs.google.com/document/d/1fAB6dKGWf_7ttOPLId5pacNGNUT7ED_yY31BvuE8368/edit?usp=sharing
---

## 1. Design Principles

### The One-Sentence Version

A **dual-resolution, provenance-first, context-normalized regulatory evidence graph** in which a canonical TF→Gene proposition is backed by context-specific observations of binding, locus activity, locus→gene assignment, and regulatory effect. Every assertion is traceable to an exact analysis/extraction run and, where applicable, to its underlying experiment/study and/or source publication. The graph remains gene-level for ordinary querying while preserving registry-anchored regulatory loci for variant/GWAS and mechanism queries.

### Core Requirements

1. **Regulatory propositions are not generic associations.** The graph must distinguish TF occupancy, locus→gene assignment, regulatory effect, correlation, disease expression, variant association, and druggability rather than collapsing them into one score.

2. **A canonical TF→Gene proposition is context-free; support is context-specific.** `RegulatoryInteraction` stores the proposition, while `ContextualStatement` stores what is supported in a reusable `BiologicalContext`.

3. **Context is shared and normalized.** Cell type, tissue, disease, species, system type, and developmental stage belong to shared `BiologicalContext` nodes. Experimental details such as assay remain on observations; treatment/time/dose/genotype may remain observation-level or nullable context dimensions depending on query needs.

4. **TF occupancy is an observation, not a global edge.** Replace authoritative `TF -[:BINDS_AT]-> locus` facts with `BindingObservation` nodes tied to a context and evidence provenance.

5. **Locus→gene assignment is an observation, not a global fact.** Distal enhancer-target links require a reified `LocusGeneLink` with method, context, statistics, and provenance. Proximity is annotation, not proof.

6. **Motif family ≠ TF identity.** ChromBPNet/seqlet/motif evidence may identify a sequence family without resolving paralogs. Represent `Motif`/`MotifFamily` explicitly and make specific TF assignment evidence-bearing.

7. **Measured evidence must be deduplicated by experiment/study, not by database.** CistromeDB, ChIP-Atlas, UniBind, GTRD, and similar resources may reprocess the same underlying public experiments. `Experiment`/`Study` identity is required before counting independent support.

8. **Direction is not one scalar label.** Signed correlation, curated direction, and perturbation effect remain distinct observations. A `ContextualStatement` carries a direction posterior plus uncertainty/disagreement.

9. **Direct regulation is defined by three evidence axes.** Binding/occupancy (B), locus→gene assignment (L), and regulatory effect (R) are scored separately in compatible contexts. A TF perturbation without binding is not direct regulation; binding without effect is not regulation.

10. **DE is an overlay with an explicit contrast.** Replace `DEGSet` with `DEAnalysis`; disease expression never supports a TF→Gene edge.

11. **Variant overlap is not variant mechanism.** Coordinate overlap is a geometric fact; allelic effects on accessibility/binding/methylation are separate observations. Fine-mapped credible sets are preferred over index-SNP-only interpretation.

12. **Scores are reproducible model outputs.** No bare `base_confidence` or `context_confidence` floats. `ConfidenceScore` records model/feature/training/calibration/code versions and uncertainty.

13. **Graph ≠ raw warehouse.** Store stable entities, summarized observations, evidence assertions, provenance, and scores in the KG; raw peaks, matrices, per-base attributions, summary statistics, feature snapshots, and model artifacts remain in a columnar/object store.

14. **Learned scores are not hand-tuned and are not automatically P(real).** The system produces ranking/predictive scores evaluated on leakage-safe, orthogonal gold sets; calibrated probabilities are reserved for observable endpoints.

### The Critical Distinction from STRING

| | STRING | DPI-KG |
|---|---|---|
| **Meaning** | Broad association across heterogeneous evidence classes | Explicit regulatory proposition plus typed observations |
| **Binding** | Not necessarily represented | TF/motif-family occupancy is a dedicated observation |
| **Regulatory effect** | Mixed with other signals | Separate perturbation/correlation observations |
| **Cell context** | Limited / not the organizing principle | Shared, ontology-grounded biological contexts |
| **Genomic locus** | No mechanism-oriented locus layer | Registry-anchored loci with activity, binding, and variant observations |
| **Provenance** | Source-level | Experiment/study/publication/analysis-run traceability |

## 2. Graph Schema

### 2.1 The Actual Schema

The final design has four logical layers: **biological entities**, **regulatory propositions**, **context-specific observations**, and **evidence/provenance**. Disease/variant/application overlays attach without changing the semantics of the core regulatory evidence.

```text
CORE ENTITIES
═════════════
Gene(:TF)      Motif ──MOTIF_OF──▶ MotifFamily/TFClass      RegulatoryLocus
   │                                  │                          │
   │                                  └──CANDIDATE_BINDER──▶ TF │
   └──ORTHOLOG_OF──▶ Gene(other species)              │

BiologicalContext
[species, system_type, cell_type, tissue, disease, dev_stage, resolution]

PROPOSITION LAYER
═════════════════
Gene(:TF) ──REGULATES_VIA──▶ RegulatoryInteraction ──TARGETS──▶ Gene
                                  │
                            HAS_STATEMENT
                                  ▼
                         ContextualStatement ──IN_CONTEXT──▶ BiologicalContext
                         [B/L/R tiers, edge_class,
                          direction posterior,
                          disagreement/status,
                          context coherence]

OBSERVATION LAYER
═════════════════
TF or MotifFamily ──BINDER_IN──▶ BindingObservation ──AT_LOCUS──▶ RegulatoryLocus
                                      └──IN_CONTEXT──▶ BiologicalContext

LocusActivityObservation ──OF_LOCUS──▶ RegulatoryLocus
          └──IN_CONTEXT──────────────▶ BiologicalContext

LocusGeneLink ──FROM_LOCUS──▶ RegulatoryLocus
      ├──TO_GENE────────────▶ Gene
      └──IN_CONTEXT─────────▶ BiologicalContext

PerturbationEffectObservation ──PERTURBED_TF──▶ Gene:TF
             ├──AFFECTS_GENE─────────────────▶ Gene
             └──IN_CONTEXT───────────────────▶ BiologicalContext

ExpressionObservation ──OF_GENE──▶ Gene
        └──IN_CONTEXT────────────▶ BiologicalContext

EVIDENCE + PROVENANCE
═════════════════════
EvidenceAssertion ──ASSERTS{polarity}──▶ Observation / ContextualStatement
      │ FROM_RUN
      ▼
AnalysisRun ──USES_EXPERIMENT──▶ Experiment ──PART_OF──▶ Study ──REPORTED_IN──▶ Publication
EvidenceAssertion ──REPORTED_IN──▶ Publication  [optional for literature/curated assertions]

ConfidenceScore ──SCORES──▶ ContextualStatement / RegulatoryInteraction
```

Variant/disease overlays:

```text
Variant ──OVERLAPS──▶ RegulatoryLocus
Variant ──IN_CREDIBLE_SET{pip}──▶ CredibleSet ──FOR_STUDY──▶ GWASStudy
GWASAssociation ──OF_VARIANT──▶ Variant ──IN_STUDY──▶ GWASStudy
Gene ──DE_IN{logFC,se,q,tested}──▶ DEAnalysis
AllelicEffectObservation ──OF_VARIANT──▶ Variant ──ON_LOCUS──▶ RegulatoryLocus
MolecularQTL / ColocalizationEvidence
RegulatoryComplex / ComplexObservation
```

### 2.2 Node Definitions

#### Regulatory, context, observation, and provenance entities

| Node Type | Key Properties | Notes |
|---|---|---|
| **Gene** | `ensembl_gene_id`, `species`, `symbol`, `hgnc_id`/`mgi_id`, `entrez_id`, `annotation_release`, `gene_model_version`, `tss_positions[]`, `strand`, `is_tf`, `tf_census_source` | Species-specific. Use the Ensembl stable root ID as identity; store version/release separately. TFs retain an additional `:TF` label. |
| **Motif** | `jaspar_id`, `version`, `name` | PWM identity; not equivalent to measured occupancy. |
| **MotifFamily / TFClass** | `family_id`, `name`, `dbd_type` | Explicitly carries paralog ambiguity for sequence-model evidence. |
| **RegulatoryLocus** | `locus_id`, `chr`, `start`, `end`, `assembly`, `registry`, `registry_version`, `ccre_class`, `liftover_status` | Stable registry coordinate; do not mint one node per experiment peak. |
| **BiologicalContext** | `context_id`, `species`, `system_type`, `cell_type`, `cell_line`, `tissue`, `disease`, `dev_stage`, `resolution`, `label_raw[]`, `bond_version` | Shared, deduplicated biological situation. The context hash excludes treatment/dose/time/genotype/perturbation/donor fields. |
| **RegulatoryInteraction** | `interaction_id`, `species`, `first_asserted` | Canonical proposition only. Scores/tiers live elsewhere. |
| **ContextualStatement** | `statement_id`, `tier_B`, `tier_L`, `tier_R`, `edge_class`, `p_activating`, `p_repressing`, `p_no_effect`, `epistemic_uncertainty`, `direction_basis`, `disagreement`, `status`, `context_coherence` | Authoritative context-specific interpretation. Independent-study counts are derived/cached from provenance, not authoritative fields. |
| **BindingObservation** | `obs_id`, `assay`, `occupancy_statistic`, `motif_supported`, `origin` (`measured`/`predicted`), `allele_specific` | Binder is linked as a TF or MotifFamily node, not stored only as a string. Treatment/dose/time/genotype/donor are observation-level dimensions. |
| **LocusActivityObservation** | `obs_id`, `assay`, `activity_statistic`, `active_call`, `origin` (`measured`/`predicted`) | Separates “locus exists” from “locus active in this context.” |
| **LocusGeneLink** | `link_id`, `method`, `link_tier`, `score`, `distance_bp`, `q_value`, `origin` (`annotation`/`predicted`/`measured`/`validated`) | Distal links are context-specific; proximity is weak annotation. |
| **PerturbationEffectObservation** | `obs_id`, `perturbation_type`, `effect_size`, `effect_unit`, `p_value`, `q_value`, `time_point`, `origin` (`measured`/`inferred`) | Provides R-axis regulatory-effect evidence. |
| **ExpressionObservation** | `obs_id`, `mean_expr`, `pct_cells`, `assay`, `dataset_id` | Required for context activity and TF paralog plausibility. |
| **EvidenceAssertion** | `assertion_id`, `evidence_type`, `directness`, `evidence_origin` (`measured`/`predicted`/`inferred`/`curated`/`reported`/`annotation`), `statistic_name`, `statistic_value`, `threshold_used`, `detection_power`, `independence_resolvable`, `ingest_version` | Typed assertion with polarity on `:ASSERTS`; feature-bearing values must not live only in a free JSON blob. |
| **AnalysisRun** | `run_id`, `source_db`, `pipeline`, `version`, `parameters_hash`, `access_date`, optional `source_snapshot_id`, `input_artifact_refs[]`, `model_artifact_ref` | A processing/extraction/model run. It may use zero, one, or many `Experiment` nodes; literature/computational assertions do not require an Experiment. |
| **Experiment** | `experiment_id`, `external_accessions[]`, `assay`, `target`, `antibody`, `biosample_raw`, `lab`, `platform`, `qc_flags` | Primary deduplication unit for measured evidence. External accessions require crosswalks rather than assuming GSM/SRX/ENCSR/ENCFF are interchangeable levels. |
| **Study** | `study_id`, `external_accessions[]`, `title`, `submission_date` | Groups experiments; independence generally counted at Study or stricter lab/antibody level. |
| **Publication** | `pmid`, `doi`, `year`, `journal`, `retraction_status` | Publication-level dedup and leakage-safe splitting. |
| **ConfidenceScore** | `score`, `lower`, `upper`, `score_type`, `prediction_target`, `endpoint_definition`, `calibrated`, `model_name`, `model_version`, `feature_set_version`, `training_snapshot_id`, `training_cutoff`, `calibration_id`, `code_commit`, `created_at`, `superseded_by` | Append-only model output. Context-specific scores attach primarily to `ContextualStatement`; interaction-level scores are explicit derived aggregations. |

#### Disease-genetics and differential-expression entities

| Node Type | Key Properties | Notes |
|---|---|---|
| **Variant** | normalized `variant_key=assembly:chr:pos:ref:alt`, `rsids[]`, `variant_type`, `liftover_status` | rsID is an alias, not the sole identity. |
| **GWASStudy** | `study_accession`, `trait_efo`, `trait_mondo`, `n_cases`, `n_controls`, `ancestry`, `pmid`, `sumstats_available` | Study provenance separated from association statistic. |
| **GWASAssociation** | `p_value`, `beta`/`odds_ratio`, `se`, `effect_allele`, `imputation_quality` | Effect allele is required. |
| **CredibleSet** | `credible_set_id`, `method`, `coverage` | Fine-mapped signal; membership carries PIP. |
| **DEAnalysis** | `analysis_id`, `contrast`, `assay`, `pipeline`, `n_case`, `n_control`, `covariates` | Explicit contrast replaces `DEGSet`; case and control are connected to `BiologicalContext` by `CASE_CONTEXT` / `CONTROL_CONTEXT`. |

#### Additional final-schema entities

`AllelicEffectObservation`, `MolecularQTL`, `ColocalizationEvidence`, `RegulatoryComplex`, `ComplexObservation`, `MechanisticHypothesis`, cross-species conservation relations, and typed drug-target assertions.

### 2.3 Context Model

`BiologicalContext` is a reusable node, not one node per interaction. Recommended first-class dimensions:

| Dimension | Representation | Requirement |
|---|---|---|
| `species` | NCBITaxon | Mandatory |
| `system_type` | closed enum: primary tissue/cell, cell line, organoid, ALI, iPSC-derived, in vivo, ex vivo | Mandatory |
| `cell_type` | Cell Ontology (CL) | Required for cell-resolved contexts; nullable for bulk tissue |
| `cell_line` | Cellosaurus | Nullable |
| `tissue` | UBERON | Required where anatomy matters |
| `disease` | MONDO | Nullable for healthy |
| `dev_stage` | controlled vocabulary | Recommended |
| `resolution` | bulk/sorted/single-cell/spatial | Recommended |

`context_id` is locked to stable biological dimensions: species, system type, cell type/cell line, tissue, disease, developmental stage, and resolution. Treatment, perturbation, dose, time, genotype, sex, and donor/cohort belong to observations or analysis metadata and do **not** change the shared context identity. Do not put `assay` in the biological context key: assay describes an observation, not the biological situation.

BOND should retain the raw labels and `bond_version` so harmonization can be audited/re-run.

> [!IMPORTANT]
> **Genome assembly is mandatory** on every coordinate-bearing object. Adopt one canonical graph assembly per species and store liftOver provenance/status for imports.

### 2.4 Evidence Attachment Rule

Evidence attaches to the **thing it actually measures**:

- ChIP/CUT&RUN peak → `BindingObservation`
- ATAC/DNase/histone activity → `LocusActivityObservation`
- ABC/contact/CRISPRi enhancer assignment → `LocusGeneLink`
- TF perturbation → `PerturbationEffectObservation` and/or resulting `ContextualStatement`
- curated/literature regulatory claim → `ContextualStatement`
- variant allelic activity → `AllelicEffectObservation`

This replaces the old rule that all `Evidence` nodes point only to an interaction context.

### 2.5 Edge Types (Complete Core)

| Edge | From → To | Purpose |
|---|---|---|
| `:REGULATES_VIA` | Gene:TF → RegulatoryInteraction | Canonical regulator |
| `:TARGETS` | RegulatoryInteraction → Gene | Canonical target |
| `:HAS_STATEMENT` | RegulatoryInteraction → ContextualStatement | Context-specific claim |
| `:IN_CONTEXT` | Observation/Statement → BiologicalContext | Biological situation |
| `:BINDER_IN` | Gene:TF or MotifFamily → BindingObservation | Binder identity/resolution |
| `:AT_LOCUS` | BindingObservation → RegulatoryLocus | Binding position |
| `:OF_LOCUS` | LocusActivityObservation → RegulatoryLocus | Locus activity observation |
| `:FROM_LOCUS` | LocusGeneLink → RegulatoryLocus | Locus side of assignment |
| `:TO_GENE` | LocusGeneLink → Gene | Gene side of assignment |
| `:PERTURBED_TF` | PerturbationEffectObservation → Gene:TF | Perturbed regulator |
| `:AFFECTS_GENE` | PerturbationEffectObservation → Gene | Measured downstream effect |
| `:OF_GENE` | ExpressionObservation → Gene | Expression measurement |
| `:ASSERTS` | EvidenceAssertion → Observation/Statement | Carries `polarity=supports/refutes/inconclusive` |
| `:FROM_RUN` | EvidenceAssertion → AnalysisRun | Processing provenance |
| `:USES_EXPERIMENT` | AnalysisRun → Experiment | Optional experimental input(s); zero-or-many allowed |
| `:PART_OF` | Experiment → Study | Study grouping |
| `:REPORTED_IN` | EvidenceAssertion/Study/Experiment → Publication | Source/publication provenance; literature claims may connect directly |
| `:SCORES` | ConfidenceScore → Interaction/Statement | Versioned model output |
| `:MOTIF_OF` | Motif → MotifFamily | Motif taxonomy |
| `:CANDIDATE_BINDER` | MotifFamily → Gene:TF | Compatible paralogs |
| `:OVERLAPS` | Variant → RegulatoryLocus | Coordinate containment |
| `:OF_VARIANT` | GWASAssociation → Variant | Variant association |
| `:IN_STUDY` | GWASAssociation → GWASStudy | Study provenance |
| `:IN_CREDIBLE_SET` | Variant → CredibleSet | Carries PIP |
| `:FOR_STUDY` | CredibleSet → GWASStudy | Fine-mapping provenance |
| `:DE_IN` | Gene → DEAnalysis | Differential-expression result |
| `:CASE_CONTEXT` | DEAnalysis → BiologicalContext | Case context |
| `:CONTROL_CONTEXT` | DEAnalysis → BiologicalContext | Control context |

Derived shortcut edges may be materialized for performance but must be rebuildable and clearly marked derived.

## 3. The Co-Factor Problem

### Current approach to avoid: String concatenation

`"MYC_MAX" → BCL2` remains incorrect because it destroys the identity of the participating TFs and cannot distinguish canonical complexes from locus/context-specific co-occupancy.

### Final approach: Canonical RegulatoryComplex + optional ComplexObservation

```text
Gene:TF ──MEMBER_OF{role}──▶ RegulatoryComplex
Gene:TF ──MEMBER_OF{role}──▶ RegulatoryComplex

ContextualStatement ──MEDIATED_BY──▶ RegulatoryComplex
ComplexObservation ──OF_COMPLEX──▶ RegulatoryComplex
ComplexObservation ──AT_LOCUS────▶ RegulatoryLocus
ComplexObservation ──IN_CONTEXT──▶ BiologicalContext
```

Use `requirement ∈ {obligate, facilitating, competing, unknown}` and a biological `complex_class` rather than simple `AND/OR`. BioGRID is a weak PPI prior, not sufficient proof that the TFs jointly regulate a target at one locus. Prefer canonical complex resources and locus/context-specific co-occupancy where available.

Independent TFs that happen to regulate the same gene remain separate regulatory interactions.

## 4. Data Source Inventory

The source strategy is now organized by **what biological layer a source measures** and by **independence of the underlying experiments**, not by counting databases as independent votes.

### 4.1 Core binding / locus / context sources

| Source | Final role | Key rule |
|---|---|---|
| **ChromLinker / ChromBPNet** (internal/lab pipeline) | Core predicted accessibility/motif-family/candidate regulatory evidence | Version/freeze every run. Do not convert motif-family attribution directly into a TF-specific binding fact. |
| **CistromeDB** | Core ChIP/ATAC/DNase experiment-linked evidence + QC | Use peaks/QC; do not ingest derived target-gene proximity tables as direct TF-target truth. |
| **ChIP-Atlas** | Core TF-specific measured binding | Use experiment-linked peaks; target-gene tables encode proximity and are excluded as direct-regulation evidence. |
| **UniBind** | Core high-stringency motif-supported ChIP binding | Link to the parent ChIP experiment; it is added processing/stringency, not a fully independent experiment. |
| **GTRD / ReMap** | Secondary ChIP-derived binding | Alternative processing/coverage; deduplicate by experiment/study. |
| **JASPAR** | Core motif/PWM definitions | Motif plausibility/family identity only. |
| **ENCODE SCREEN** | Core regulatory-locus registry / cCRE annotation | Registry existence is not context activity; activity is a separate observation. |
| **Project lung ATAC consensus** | Core complementary locus registry/context activity | Version the registry; retain raw per-experiment peaks in warehouse. |
| **Lung single-cell/single-nucleus expression/accessibility atlases** | Core context/expression/locus-activity layer | Required for context matching, TF expression filtering, and lung/IPF use cases. |
| **TF census + TFClass** | Core identity utility | Defines TF status and family/paralog relationships with provenance. |

### 4.2 Locus→gene / regulatory-effect validation sources

| Source | Final role | Key rule |
|---|---|---|
| **ABC / ENCODE rE2G** | Strong predicted locus→gene links | Store as predicted `LocusGeneLink`; benchmark against CRE perturbation. |
| **CRISPRi/CRISPRa enhancer-gene perturbation** | Core validation for locus→gene links | Highest-value orthogonal validation for the dual-resolution claim. |
| **Promoter capture Hi-C / HiChIP** | Secondary/strong context-specific linkage | Physical contact is supportive, not automatically regulatory effect. |
| **Perturb-seq / TF KO/KD/OE/degron datasets** | Core regulatory-effect validation | TF perturbation is causal for perturbation but target effects can be indirect; store explicit observations/time. |

### 4.3 Curated TF-target resources — correlated validation block

| Source | Final use |
|---|---|
| **TRRUST** | Validation/baseline resource; publication-resolved assertions may enter scoring only under leakage-safe evaluation |
| **CollecTRI** | Validation/baseline; treat as overlapping with other curated resources |
| **DoRothEA** | Baseline/validation; not an independent vote from the same curated lineage |

Do not train on one curated resource and claim independent validation on another without publication/source de-overlap.

### 4.4 Literature

| Source / tool | Role |
|---|---|
| **PubMed / PMC** | Secondary regulatory assertions, direction/context/directness, after manual QC gate |
| **PubTator Central** | Entity recognition/normalization utility; not evidence |
| **BioRED** | Optional relation-extraction supervision; not a TF-target benchmark |
| **Docling** | PDF/table fallback when structured full text is unavailable |

### 4.5 Variant / QTL sources

| Source | Final role |
|---|---|
| **GWAS Catalog** | Core variant-trait/study associations |
| **Open Targets** | Credible sets/colocalization where useful; L2G is validation/annotation, not a circular scoring feature |
| **GTEx** | Core tissue eQTL source with bulk-mixture caveat |
| **eQTL Catalogue** | Strongly recommended harmonized multi-study QTL source |
| **caQTL / allele-specific ATAC/ChIP** | Strong variant→locus activity evidence |
| **RegulomeDB** | Optional composite annotation |
| **ClinVar** | Optional; not core to the noncoding IPF mechanism claim |

### 4.6 Drugs and complexes

| Source | Final role |
|---|---|
| **ChEMBL / Open Targets drugs / DGIdb** | Optional/query-time tractability layer; type the mechanism if materialized |
| **BioGRID** | Optional weak PPI prior for co-factors |
| **CORUM / Complex Portal** | Prefer for canonical complex definitions |

> [!IMPORTANT]
> **Evidence independence rule:** build an accession crosswalk across ChIP aggregators before feature engineering. Count distinct experiments/studies (or stricter lab/antibody units where justified), never distinct databases. Where provenance cannot be resolved, that source may support an assertion but cannot increase an “independent studies” count.

### 4.7 Cell-System Harmonization

Use **BOND** early to map raw cell-system labels to CL/Cellosaurus and disease labels to MONDO while retaining raw labels and the BOND version. Add UBERON tissue/anatomy and `system_type` so cancer cell lines cannot silently stand in for primary lung biology.

## 5. Evidence Integration & Weight Learning

### 5.1 First classify the evidence: B / L / R

Before fitting any model, every `ContextualStatement` receives transparent evidence tiers.

**B — binding/occupancy:** B0 motif only; B1 predicted/family-level context support; B2 measured TF-specific occupancy; B3 strong context-matched occupancy from ≥2 independent studies.

**L — locus→gene assignment:** L0 distance/nearest gene; L1 promoter-proximal or weak link; L2 context-matched ABC/rE2G/contact/colocalization; L3 CRE-perturbation validated.

**R — regulatory effect:** R0 none; R1 correlation only; R2 TF perturbation effect; R3 strong context-matched evidence for a primary/direct effect.

Named edge classes are derived from these tiers. For promoter regulation, L1 may be sufficient when promoter identity is unambiguous and B≥2/R≥2. For distal regulation, require L≥2 before assigning a `SUPPORTED_DIRECT_*` evidence class. These classes mean that the evidence supports a direct-regulation proposition; they are not proof of a complete causal mechanism.

### 5.2 Why the old two-score model is retired

The former `base_confidence = P(real TF-target edge)` is not an identifiable universal probability when positives are publication-curated and negatives are mostly unlabeled. It also invites popularity leakage if literature counts are features. Adding or multiplying a separate context probability is not principled when the feature sets overlap.

The final design therefore separates:

1. **transparent evidence class/tier** (B/L/R + context coherence), and
2. **learned ranking/predictive score** stored in a versioned `ConfidenceScore` node.

### 5.3 Scoring target

Start with a pragmatic, experiment-deduplicated logistic/gradient-boosted model that ranks context-specific candidate statements. Calibrate probabilities only for an observable event with explicit labels, e.g. target response above a threshold after TF perturbation.

Recommended feature blocks:

```python
class ContextualStatementFeatures:
    # Binding block — aggregated by independent study, not source database
    n_binding_studies: int
    n_context_matched_binding_studies: int
    best_binding_qvalue: float | None
    measured_tf_occupancy: bool
    motif_family_support: bool
    predicted_binding_score: float | None

    # Locus activity / identity
    locus_active_in_context: bool | None
    tf_expressed_in_context: bool | None
    tf_expression: float | None

    # Locus-gene block
    promoter_link: bool
    best_locus_gene_tier: int
    abc_or_re2g_score: float | None
    contact_supported: bool
    crispri_validated_link: bool

    # Regulatory effect block
    perturbation_effect_supported: bool
    perturbation_effect_size: float | None
    perturbation_qvalue: float | None
    correlation_score: float | None

    # Curated/literature block — only when leakage-safe for the split
    curated_support: bool
    literature_claims_independent_pmids: int
    direction_agreement: float | None

    # Missingness/provenance
    n_independent_studies_total: int
    n_refuting_studies: int
    unresolved_provenance_count: int
```

Never use `number_of_ChIP_databases` as a feature.

### 5.4 Negative sampling and uncertainty

- Random zero-evidence pairs are development-only easy negatives.
- Prefer expression/popularity/degree/distance-matched negatives.
- Include hard negatives where TF and target are expressed and the locus is accessible/motif-compatible but measured occupancy/effect is absent.
- Reserve verified perturbation-null and CRE-perturbation-null pairs as high-value evaluation negatives.
- Missing data is not negative evidence; explicit negative experiments need detection-power metadata.
- Preserve contradictory assertions. Store `p_activating`, `p_repressing`, and `p_no_effect` as biological probabilities; store `epistemic_uncertainty` and disagreement/entropy separately.

### 5.5 Reproducible score storage

```text
ConfidenceScore
  score
  lower / upper
  score_type
  prediction_target / endpoint_definition
  calibrated
  model_name / model_version
  feature_set_version
  training_snapshot_id / training_cutoff
  calibration_id
  code_commit
  created_at
  superseded_by
```

Scores are append-only. Re-training creates a new score rather than overwriting history.

### 5.6 Leakage-Safe Evaluation Strategy

> [!CRITICAL]
> **Fold-specific evidence masking:** for every evaluation fold, first remove all assertions/observations from the held-out gold source(s), then recompute B/L/R tiers, `edge_class`, aggregate evidence counts, and the immutable feature snapshot. A Perturb-seq test observation cannot contribute to R-tier/features for the same test statement; a CRISPRi E-G test result cannot contribute to L-tier/features. Apply masking before training, calibration, and scoring.


Treat source dependencies explicitly:

- curated TF-target databases are a correlated block;
- public ChIP aggregators are a correlated block over shared experiments;
- curated resources and literature share publications;
- motif-filtered ChIP and motif features are not fully independent;
- ChromBPNet features cannot be evaluated against accessibility labels derived from the exact same training data.

Use three evaluation tiers:

1. **Grouped internal CV** with separate held-out TF, TF-family, target, study/publication, and context analyses.
2. **Temporal holdout**: freeze source data at a date and evaluate relationships first established after the cutoff date.
3. **Orthogonal headline gold sets**: TF perturbation for regulatory effect, CRE perturbation for locus→gene links, allele-specific/caQTL for variant→locus activity.

Mandatory diagnostic: a popularity-only baseline using TF/target publication counts and expression. The full model must beat it, especially on lightly studied genes.

## 6. Corpus and Evidence Processing Pipeline

The graph schema defines **what** the graph stores. This section defines **how** evidence gets there.

```
retrieve broadly → triage aggressively → route assets → extract by modality
→ ground/contextualize → validate → score → materialize
```

### 6.1 Pipeline Overview

The build order is provenance-first because experiment identity, context identity, and locus identity are expensive to retrofit after ingestion.

```text
FINAL SCHEMA + CLOSED VOCABULARIES + BOND
        ↓
EXPERIMENT / STUDY / PUBLICATION REGISTRY
        ↓
ACCESSION CROSSWALK ACROSS CISTROME / ChIP-ATLAS / UNIBIND / GTRD / REMAP
        ↓
LOCUS REGISTRY (ENCODE cCRE + lung ATAC consensus; canonical assembly)
        ↓
EXPRESSION + LOCUS-ACTIVITY CONTEXT LAYER
        ↓
MEASURED BINDING OBSERVATIONS
        ↓
MOTIF / TFCLASS + PREDICTED BINDING
(family-level unless TF identity is independently resolved)
        ↓
LOCUS→GENE LINKS + CRE-PERTURBATION BENCHMARK
        ↓
LEAKAGE AUDIT + BASELINES BEFORE LEARNED SCORING
        ↓
CONFIDENCE / RANKING MODEL
        ↓
GWAS + CREDIBLE SETS + VARIANT OVERLAP
        ↓
QTL / COLOCALIZATION / ALLELIC EFFECTS
        ↓
DEAnalysis disease overlays
        ↓
PERTURBATION-PREDICTION UTILITY BENCHMARK
        ↓
LITERATURE QC HARNESS → CORPUS → EXTRACTION → MANUAL GATE
        ↓
COMPLEXES / CROSS-SPECIES / DRUG / AGENT CAPABILITIES
```

The raw-data warehouse remains separate from the graph. Only stable entities, summarized observations, assertions, provenance, scores, and retained disease/variant objects are materialized in Neo4j.

### 6.2 Corpus Selection

Do **not** process all of PubMed uniformly. Use gene-seeded retrieval:

```
Corpus step 1: SEED (~500-2000 papers)
════════════════════════════════
Input: GRN gene list from ChromLinker (200 TFs + 2000 targets)

Query PubMed/PMC for each TF-Gene pair:
  "{TF}[Title/Abstract] AND {Gene}[Title/Abstract]
   AND (regulates OR activates OR represses OR ChIP OR knockdown)"

Filter: primary research, human/mouse, not retracted
Expected: ~500-2000 papers, mostly relevant

Corpus step 2: EXPAND (~1000 more)
═════════════════════════════
Forward/backward citations from seed-corpus hits
Filter: same TFs/genes mentioned

Corpus step 3: DB-LINKED
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
- **Tier 1:** Full text + tables/supplements; figures only for a small Tier-0/targeted set when measured positional evidence is otherwise unavailable
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
    direction: str              # "activator" | "repressor" | "dual" | "unknown"
    directness: str             # "direct_binding" | "regulatory_effect" | "unclear"
    cell_type: str | None       # "AT2 cells", "A549"
    species: str | None         # "human", "mouse"
    disease: str | None         # "IPF", "NSCLC"
    assay: str | None           # "ChIP-seq", "knockdown", "luciferase"
    pmid: str
    source_sentence: str        # Exact sentence from paper
    section: str                # "Results", "Abstract", etc.
    extraction_confidence: float # Extraction confidence; not biological edge confidence
    claim_status: str           # "measured" | "inferred" | "reported" | "schematic"
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
- "TF target genes from ChIP-seq" → parse the underlying peak/experiment where possible; do **not** automatically create direct-regulation edges from a target-gene table.
- "DEGs upon TF knockdown" → `PerturbationEffectObservation`; causal for the perturbation, not automatically direct TF→target regulation.
- "Gene expression across cell types" → `ExpressionObservation`; useful context evidence, not regulation.

### 6.6 Figure / Vision Layer

**Deferred / optional, not part of the core scoring evidence.** Figure extraction has high engineering cost and high semantic risk, while most scientifically important measured values should be recoverable from structured source files, tables, captions, or experiment repositories.

If used at all, restrict it to a small Tier-0 set of papers where a measured panel contains otherwise-unavailable positional evidence. A figure-derived assertion must be typed `measured` versus `schematic`, linked to its publication, and must never create a high-confidence regulatory statement without independent text/structured support.

Recommended default: **do not include figure/vision-derived evidence in scoring.**

### 6.7 Grounding and Context Harmonization

Use BOND and identifier normalization before graph insertion.

| Raw Mention | Grounded To | System |
|-------------|------------|--------|
| "AT2", "alveolar type II", "AEC2" | CL:0002063 | BOND / Cell Ontology |
| "A549" | Cellosaurus ID + `system_type=cell_line` | BOND / Cellosaurus |
| "lung", "respiratory bronchiole", anatomical compartment | UBERON | anatomy normalization |
| "lung fibrosis", "IPF" | MONDO:0005570 | MONDO |
| human / mouse | NCBITaxon | species normalization |
| gene symbols/aliases | species-scoped Ensembl stable gene ID + HGNC/MGI xrefs | gene crosswalk |
| hg19/mm10 coordinates | canonical assembly | LiftOver with provenance/status |

Do not make raw researcher labels the context identity. `BiologicalContext.context_id` is derived from harmonized fields; retain `label_raw[]` and `bond_version` for auditability.

### 6.8 Literature Validation Gate

The old single “>80% vs TRRUST/CollecTRI” gate is replaced by a manual, field-level evaluation because curated databases are themselves incomplete/correlated and do not define all context fields.

Before literature assertions affect scoring:

1. Build a held-out manually double-annotated sample stratified by paper section and extraction-confidence bin.
2. Report precision with confidence intervals for **relation existence**, **direction**, **directness**, **cell/tissue context**, **species**, and **measured-vs-inferred** separately.
3. Report inter-annotator agreement.
4. Select an operating threshold that gives high precision for the fields used in scoring; claims below threshold remain in the sidecar store.
5. Curated-resource agreement is a secondary diagnostic, not the sole ground truth.
6. Publication provenance is mandatory so evaluation PMIDs can be blacklisted from training/literature features in each fold.

Every accepted assertion is also checked for normalization, context compatibility, polarity, measured/predicted status, contradiction, and publication status. Contradictions are stored, not overwritten.

### 6.9 Edge Cases Checklist

| # | Edge Case | Mitigation |
|---|-----------|------------|
| 1 | Gene name collisions with English words | Context-aware NER + PubTator + species-scoped gene IDs |
| 2 | Motif family mistaken for a specific TF | Motif/MotifFamily nodes; specific TF assignment requires independent evidence |
| 3 | Same ChIP experiment in multiple databases | Experiment/study accession crosswalk; never count databases as independent |
| 4 | Indirect vs direct regulation | B/L/R tiers + typed directness; perturbation alone is `EFFECT_ONLY` |
| 5 | Absence of evidence vs tested negative | Assertion polarity + detection-power metadata |
| 6 | Reviews restating old claims | Publication/source type; seed discovery only unless primary source resolved |
| 7 | Species confusion | Species-scoped Gene nodes; explicit orthology layer |
| 8 | Cell line drift / cancer line used as normal lung | `system_type` + tissue/cell ontology; exclude incompatible contexts by default |
| 9 | Same TF-Gene, opposite direction across contexts | Separate `ContextualStatement` nodes + direction posterior/disagreement |
| 10 | Enhancer assigned to nearest gene | `LocusGeneLink`; proximity = L0/L1, distal direct claims require stronger evidence |
| 11 | Variant overlap treated as mechanism | Separate `OVERLAPS`, locus activity, allelic-effect, binding, and locus→gene evidence |
| 12 | Index SNP treated as causal | CredibleSet + PIP; retain GWAS study/effect allele |
| 13 | Excel gene-name corruption in supplements | Detect/correct during ingestion |
| 14 | Preprint→published duplicates/retractions | Publication dedup + status tracking |
| 15 | Dose/time-dependent effects | Store on perturbation/observation condition; do not collapse into global direction |
| 16 | Gene absent from DEG table interpreted as unchanged | `DE_IN.tested`; explicit analysis contrast/filtering |
| 17 | Annotation update changes Ensembl version | Stable root ID as entity identity; release/version stored separately |
| 18 | Raw peak explosion in graph | Registry loci + warehouse raw peaks; summarized observations only |

### 6.10 Build Order

| # | What | Why now |
|---|---|---|
| 1 | final schema + identifier/context vocabularies + BOND | Join keys and cardinalities are expensive to retrofit |
| 2 | Experiment/Study/Publication registry + ChIP accession crosswalk | Prevents evidence double-counting before any features exist |
| 3 | Versioned locus registry (cCRE + lung ATAC consensus) | Stable coordinate vocabulary; prevents per-peak graph explosion |
| 4 | Lung expression + locus-activity layer | Required for context matching and TF plausibility |
| 5 | Measured binding observations + Motif/TFClass | Establish measured reference before predicted evidence |
| 6 | ChromBPNet/ChromLinker predicted binding/candidates | Write family-level predictions honestly; version internal pipeline |
| 7 | LocusGeneLink layer (promoter + ABC/rE2G/contact) + CRISPRi benchmark | Makes the locus layer validatable |
| 8 | Designated perturbation-effect observations for the feature/training pool; reserve untouched perturbation gold sets | Makes R-axis evidence available without contaminating evaluation |
| 9 | Leakage audit + popularity baseline + benchmark harness + fold-specific evidence masking | Define evaluation before fitting scores |
| 10 | Confidence/ranking model | First scientifically interpretable ranked graph; score endpoint is explicit |
| 11 | GWAS + credible sets + variant overlap | disease genetics on stable loci |
| 12 | QTL/colocalization/allelic effects | Strengthens variant→gene mechanism |
| 13 | DEAnalysis disease overlays with CASE_CONTEXT/CONTROL_CONTEXT | Disease prioritization without causal leakage |
| 14 | Perturbation utility benchmark | Tests downstream predictive value on held-out data |
| 15 | Literature QC harness + extraction | Adds direction/context after core graph is testable |
| 16 | Cross-context transfer | Tests context-normalized design |
| 17 | Complexes, cross-species, prospective validation | Higher-order biology after core performance succeeds |
| 18 | Drug overlay and agent interface | Application layer last |

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

The following example illustrates the final schema shape; implementation loaders should use deterministic IDs and MERGE/upsert patterns rather than literal CREATE statements.

```cypher
// CORE ENTITIES
CREATE (myc:Gene:TF {
  ensembl_gene_id: 'ENSG00000136997',
  species: 'NCBITaxon:9606',
  symbol: 'MYC',
  hgnc_id: 'HGNC:7553'
});
CREATE (bcl2:Gene {
  ensembl_gene_id: 'ENSG00000171791',
  species: 'NCBITaxon:9606',
  symbol: 'BCL2',
  hgnc_id: 'HGNC:990'
});

CREATE (ctx:BiologicalContext {
  context_id: 'CTX:<hash>',
  species: 'NCBITaxon:9606',
  system_type: 'cell_line',
  cell_line: 'CVCL_0023',
  tissue: 'UBERON:0002048',
  disease: 'MONDO:0005233',
  resolution: 'bulk',
  bond_version: 'BOND:<version>'
});

// CANONICAL PROPOSITION + CONTEXTUAL STATEMENT
CREATE (ri:RegulatoryInteraction {
  interaction_id: 'RI:<deterministic_hash>',
  species: 'NCBITaxon:9606'
});
CREATE (myc)-[:REGULATES_VIA]->(ri);
CREATE (ri)-[:TARGETS]->(bcl2);

CREATE (st:ContextualStatement {
  statement_id: 'ST:<deterministic_hash>',
  tier_B: 2,
  tier_L: 1,
  tier_R: 2,
  edge_class: 'SUPPORTED_DIRECT_PROMOTER',
  p_activating:0.78, p_repressing:0.05, p_no_effect:0.07,
  epistemic_uncertainty:0.10,
  context_coherence: 'matched',
  status: 'supported'
});
CREATE (ri)-[:HAS_STATEMENT]->(st);
CREATE (st)-[:IN_CONTEXT]->(ctx);

// LOCUS + BINDING OBSERVATION
CREATE (locus:RegulatoryLocus {
  locus_id: 'L:<registry_id>', chr:'18', start:63100100, end:63100450,
  assembly:'hg38', registry:'project_lung_registry', registry_version:'2026-08-12'
});
CREATE (bo:BindingObservation {
  obs_id:'BO:<hash>', assay:'ChIP-seq', origin:'measured',
  occupancy_statistic:245.3, motif_supported:true
});
CREATE (myc)-[:BINDER_IN]->(bo);
CREATE (bo)-[:AT_LOCUS]->(locus);
CREATE (bo)-[:IN_CONTEXT]->(ctx);

// LOCUS→GENE LINK
CREATE (lg:LocusGeneLink {
  link_id:'LG:<hash>', method:'promoter', link_tier:1, distance_bp:0,
  origin:'annotation'
});
CREATE (lg)-[:FROM_LOCUS]->(locus);
CREATE (lg)-[:TO_GENE]->(bcl2);
CREATE (lg)-[:IN_CONTEXT]->(ctx);

// PROVENANCE
CREATE (exp:Experiment {experiment_id:'EXP:<internal>', external_accessions:['SRX3456789'], assay:'ChIP-seq'});
CREATE (run:AnalysisRun {run_id:'RUN:<hash>', source_db:'ChIP-Atlas', pipeline:'<pipeline>', version:'<version>'});
CREATE (ea:EvidenceAssertion {
  assertion_id:'EA:<hash>', evidence_type:'chip_peak', directness:'direct_binding',
  evidence_origin:'measured', statistic_name:'q_value', statistic_value:1e-12
});
CREATE (ea)-[:FROM_RUN]->(run);
CREATE (run)-[:USES_EXPERIMENT]->(exp);
CREATE (ea)-[:ASSERTS {polarity:'supports'}]->(bo);

// VERSIONED SCORE
CREATE (cs:ConfidenceScore {
  score:0.81, lower:0.72, upper:0.88,
  score_type:'ranking', prediction_target:'contextual_tf_target_priority',
  endpoint_definition:'orthogonal regulatory-effect ranking', calibrated:false,
  model_name:'dpi_ranker', model_version:'git:<commit>', feature_set_version:'sha256:<feature_snapshot>',
  training_snapshot_id:'train1', training_cutoff:'<date>',
  calibration_id:null, code_commit:'<git_sha>'
});
CREATE (cs)-[:SCORES]->(st);

// CONSTRAINTS / INDEXES
CREATE CONSTRAINT gene_id_unique IF NOT EXISTS FOR (g:Gene) REQUIRE (g.species, g.ensembl_gene_id) IS UNIQUE;
CREATE CONSTRAINT context_id_unique IF NOT EXISTS FOR (c:BiologicalContext) REQUIRE c.context_id IS UNIQUE;
CREATE CONSTRAINT interaction_id_unique IF NOT EXISTS FOR (r:RegulatoryInteraction) REQUIRE r.interaction_id IS UNIQUE;
CREATE CONSTRAINT statement_id_unique IF NOT EXISTS FOR (s:ContextualStatement) REQUIRE s.statement_id IS UNIQUE;
CREATE CONSTRAINT locus_id_unique IF NOT EXISTS FOR (l:RegulatoryLocus) REQUIRE l.locus_id IS UNIQUE;
CREATE CONSTRAINT experiment_id_unique IF NOT EXISTS FOR (e:Experiment) REQUIRE e.experiment_id IS UNIQUE;
```

## 8. How This Differs from MechGate

| Dimension | MechGate | DPI-KG |
|---|---|---|
| **Scope** | Broad mechanistic biology | Focused TF→Gene regulation with locus/variant support |
| **Primary backbone** | Literature-centric mechanistic claims | Structured experimental/computational observations first; literature supplementary |
| **Core semantic unit** | Mechanistic event/claim | Canonical regulatory proposition + context-specific observation/evidence chain |
| **Provenance** | Claim/source-centric | Experiment → Study → Publication + AnalysisRun + EvidenceAssertion |
| **Context** | Broad compatibility model | Shared ontology-grounded `BiologicalContext` + observation-specific assay/conditions |
| **Position resolution** | Variable | Registry-anchored `RegulatoryLocus` layer is first-class |
| **Scale control** | Large claim graph | Raw high-volume arrays stay in warehouse; graph stores summarized retained observations |
| **Primary scientific claim** | Mechanism extraction | Better regulatory prioritization/prediction and auditable variant-aware hypotheses |

## 9. Implementation Roadmap

The detailed build order is defined in §6.10. Summary:

| Stage | What |
|---|---|
| **Foundation** | Schema/IDs/context + provenance registry + locus registry |
| **Core observations** | Lung expression/locus activity + measured binding + motif/TFClass + predicted binding |
| **Mechanism linking** | LocusGeneLink + CRISPRi E-G benchmark |
| **Evaluation before scoring** | Leakage audit + popularity baseline + orthogonal benchmark harness |
| **Ranking model** | Experiment-deduplicated context-specific ranking/predictive score |
| **Disease genetics** | GWAS studies + credible sets + variant overlap + QTL/colocalization where available |
| **Disease expression** | DEAnalysis explicit contrasts |
| **Utility** | Perturbation prediction and cross-context transfer benchmarks |
| **Secondary enrichment** | Literature after manual QC gate |
| **Additional final capabilities** | Complexes, cross-species conservation, prospective validation, drugs, and agent interface |

## 10. Concrete Use Cases (IPF / Lung Epithelial Workflow)

> The original IPF/AT2 motivation remains, but the graph must preserve epithelial compartment and system-type uncertainty rather than forcing every mechanism into AT2.

**Use Case 1: Context-Specific Core Regulatory Statements**
> Show high-ranked regulatory statements for IPF-relevant lung epithelial contexts with measured/predicted binding, locus→gene, and effect tiers visible.

Path: `Gene:TF → RegulatoryInteraction → ContextualStatement → BiologicalContext`, returning B/L/R tiers and the evidence chain.

**Use Case 2: DEG Enrichment Without Causal Leakage**
> Are genes differentially expressed in IPF vs control in a specified epithelial compartment enriched among targets in the ranked network?

Path: `Gene -[:DE_IN]-> DEAnalysis` intersected with targets of context-compatible `ContextualStatement` nodes. `DEAnalysis` never supports the regulatory edge.

**Use Case 3: Experiment-Level Explanation**
> Why is a TF-target statement ranked highly, and are the supporting studies independent?

Path: `ContextualStatement <-[:ASSERTS]- EvidenceAssertion → AnalysisRun`, with optional `AnalysisRun → Experiment → Study → Publication` for experimental evidence or `EvidenceAssertion → Publication` for literature/curated evidence, plus `ConfidenceScore` provenance.

**Use Case 4: Underdocumented Regulators**
> Find central regulators with strong measured/predictive evidence but low publication exposure.

Use network centrality plus publication-resolved evidence counts; compare against a popularity-only baseline so “novel” does not simply mean undermeasured.

**Use Case 5: Variant-Aware Mechanistic Hypothesis**
> Which fine-mapped IPF variants overlap active regulatory loci, show allelic activity evidence, have TF occupancy, and link to disease-relevant genes?

Path: `CredibleSet ← Variant → RegulatoryLocus`, then locus activity, allelic effect [when available], binding observation, `LocusGeneLink`, and DE overlay. Return the weakest evidence tier rather than a single causal label.

**Use Case 6: TFs Implicated Across Multiple Variant-Affected Loci**
> Find TFs or motif families repeatedly implicated at credible-set-overlapping loci across multiple target genes.

Use `BindingObservation` rather than global `BINDS_AT`; preserve family-level identity where specific TF assignment is unresolved.

**Use Case 7: Perturbation Utility**
> If a TF is perturbed, does a model using the DPI-KG prior predict target responses better than matched baselines?

This is evaluated downstream and must be kept separate from graph-construction labels.

**Use Case 8: Cross-Species Conservation**
> Which human regulatory propositions have orthologous, evidence-supported mouse propositions in appropriate model contexts?

Human and mouse Gene/Interaction nodes remain species-specific; conservation is an explicit `CONSERVED_WITH` assertion with orthology and locus-synteny evidence, never a shared node or automatic confidence transfer.

## 11. Open Design Decisions

### Decided

- **Core architecture:** canonical `RegulatoryInteraction` + shared `BiologicalContext` + `ContextualStatement` + observation/evidence/provenance layers.
- **Position resolution:** dual resolution retained; loci are registry-anchored, raw peaks stay outside the graph.
- **Binding semantics:** authoritative TF occupancy is `BindingObservation`; sequence-model evidence may remain MotifFamily-level.
- **Locus→gene semantics:** reified `LocusGeneLink`; distal direct-regulation claims require stronger than nearest-gene evidence.
- **Evidence independence:** count experiments/studies, never databases.
- **Gene IDs:** species-scoped Ensembl stable root IDs; HGNC/MGI/symbols are xrefs; annotation version stored separately.
- **Context:** shared `BiologicalContext` with CL/Cellosaurus + UBERON + MONDO + NCBITaxon + `system_type`; BOND harmonization retained.
- **DE:** `DEAnalysis` explicit contrasts, never edge evidence.
- **Scoring:** B/L/R tiers + versioned ranking/predictive scores; retire `P(real edge)` language and bare score fields.
- **Variant:** normalized variant key + GWASStudy + CredibleSet/PIP; overlap is not mechanism.
- **Graph/warehouse boundary:** summarized observations/provenance in Neo4j, raw high-volume arrays in columnar/object storage.
- **Literature:** secondary and gated by manual field-level QC; not the backbone.
- **Vision:** deferred/optional, excluded from scoring by default.
- **Drug/agent:** application capabilities outside the core regulatory evidence path.

### Still Open / Requires Dataset-Specific Decision

1. **Starting biological systems:** which primary lung epithelial/AT2/airway contexts have sufficient ChromLinker/ChromBPNet and measured data to support the first benchmark?
2. **Exact locus registry construction:** ENCODE cCRE-only vs cCRE ∪ project lung consensus ATAC peaks; define merge rules/versioning.
3. **ChromLinker output contract:** whether it emits motif/site→gene, TF→gene, or both, and what specific TF assignment logic is used.
4. **Experiment accession crosswalk implementation:** mapping GEO/SRA/ENCODE identifiers and handling aggregators without resolvable accessions.
5. **Ranker:** logistic vs gradient boosting, with the same leakage-safe grouped evaluation harness.
6. **Context granularity:** which treatment/time/genotype fields belong in shared `BiologicalContext` versus observation-level experimental conditions for the first datasets.
7. **Best available lung CRE-perturbation / perturbation-response benchmarks:** determines how strongly the direct-regulation and utility claims can be tested in lung rather than only generic cell systems.
8. **Primary IPF demonstration compartment:** AT2 remains important, but MUC5B/rs35705950 should be modeled compartment-explicitly with airway/secretory and AT2 evidence rather than forced into an AT2-only mechanism.

## 12. Engineering Notes

- **Raw warehouse:** Parquet/DuckDB/ClickHouse/Postgres are appropriate for raw peaks, matrices, summary statistics, text spans, and feature snapshots. Neo4j should not be the raw analytical warehouse.
- **Graph as query-optimized evidence view:** materialize stable entities, normalized contexts, summarized observations, assertions, provenance, and score versions.
- **Locus registry:** do not create a node for every peak in every experiment. Registry loci are stable join targets; experiment-specific peak rows remain in the warehouse and summarize into `BindingObservation`/`LocusActivityObservation`.
- **Accession crosswalk before ingestion:** build a resolvable experiment/study identity layer across CistromeDB, ChIP-Atlas, UniBind, GTRD/ReMap, GEO/SRA/ENCODE. Measure overlap explicitly.
- **Idempotent ingestion:** node/assertion IDs should be deterministic hashes or stable internal IDs; re-ingesting the same release should not create duplicates.
- **EvidenceAssertion schema:** any property used by the feature pipeline must be typed/validated; free-form JSON may exist only for non-feature extras.
- **Ontology IDs from day one:** Ensembl gene IDs + HGNC/MGI xrefs, CL, Cellosaurus, UBERON, MONDO, NCBITaxon, EFO where useful for GWAS traits, and BOND audit version.
- **Genome assembly from day one:** canonical hg38/mm39 graph assemblies; liftOver status/provenance for imports.
- **Confidence reproducibility:** immutable feature snapshots + model artifacts + code commit + append-only `ConfidenceScore` nodes.
- **Source licensing:** keep DrugBank excluded; inspect redistribution/licensing of aggregators before exporting source-derived content.
- **Neo4j scale guardrail:** aim to keep the graph at summarized-observation scale. If materialization approaches raw-peak cardinality, move that layer back to the warehouse rather than scaling the ontology into billions of edges.

