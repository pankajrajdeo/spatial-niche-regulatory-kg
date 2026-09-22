# DPI-KG Final — Revision Notes

These files are the single final DPI-KG design set and supersede all earlier drafts.

Major finalized changes applied consistently across the set:

- retained the dual-resolution gene + regulatory-locus architecture;
- split the old per-interaction context concept into shared `BiologicalContext` + `ContextualStatement`;
- replaced global TF→locus and locus→gene facts with context-bearing `BindingObservation` and `LocusGeneLink`;
- added `LocusActivityObservation`, `PerturbationEffectObservation`, and `ExpressionObservation`;
- added `Motif` / `MotifFamily` / TFClass handling so sequence-model evidence does not silently become a TF-specific occupancy fact;
- finalized the provenance spine so experimental, literature, curated, and computational assertions are all representable: `EvidenceAssertion → AnalysisRun`, optional `AnalysisRun → Experiment → Study → Publication`, and optional direct `EvidenceAssertion → Publication`;
- defined experimental independence at experiment/study level rather than database count;
- replaced generic Evidence metadata blobs with typed assertions and polarity/directness/measured-vs-predicted fields;
- replaced bare `base_confidence`/`context_confidence` semantics with transparent B/L/R evidence tiers plus versioned `ConfidenceScore` outputs;
- replaced `DEGSet` with explicit `DEAnalysis` case/control contrasts;
- added normalized Variant + GWASStudy + CredibleSet/PIP/effect-allele support;
- separated coordinate overlap from allelic functional effect;
- revised the MUC5B/rs35705950 example to be an uncertainty-preserving mechanistic hypothesis rather than a pre-resolved motif-disruption story;
- strengthened enhancer→gene validation with CRISPRi/CRISPRa CRE perturbation and ABC/rE2G/contact/QTL tiers;
- moved accession/provenance/locus registries and evaluation harness ahead of learned scoring;
- made literature secondary and manually gated; figure/vision extraction is excluded from scoring by default;
- kept drugs and the agent outside the core regulatory evidence path; retained complexes and cross-species conservation as defined capabilities of the final schema;
- added a graph/warehouse boundary so raw peaks/matrices/per-base data do not explode Neo4j;
- revised paper evaluation around leakage-safe grouped/temporal/orthogonal benchmarks and a mandatory popularity-only baseline.


## Final lock decisions

Before build start, the final review also locked these implementation-critical rules:

- `BiologicalContext` identity uses only stable biological dimensions; treatment, dose, time, genotype, perturbation, sex, donor, and cohort stay at observation/analysis level.
- Held-out evaluation evidence is masked **before** B/L/R tiers, edge classes, aggregate counts, and feature snapshots are computed.
- Perturbation observations used as model features/training data are explicitly separated from untouched perturbation gold sets.
- `ConfidenceScore` declares what the score predicts (`score_type`, `prediction_target`, `endpoint_definition`, calibration status), rather than exposing an ambiguous scalar.
- Direction stores biological probabilities separately from epistemic uncertainty.
- `DEAnalysis` connects to case/control `BiologicalContext` nodes through explicit relationships.
- Independent-study counts are derived from provenance and may be cached only as rebuildable values.
- The project has one final schema and one numbered build order.
