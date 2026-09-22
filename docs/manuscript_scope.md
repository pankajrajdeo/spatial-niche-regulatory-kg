# Manuscript requirements for the regulatory evidence KG

Source: the current Spatial NicheLinker manuscript draft supplied by the user
on 2026-09-22. This scope supersedes older AT1-first implementation framing.
Status: requirements, not independently verified manuscript results.

## Scientific question and contribution

Spatial NicheLinker asks whether cells of the same annotated type in different
cellular neighborhoods exhibit different transcriptional and regulatory states,
and whether these differences vary with disease condition. The manuscript spans
epithelial, immune, and mesenchymal lineages. AT1 is a detailed example in the
narrative, not the boundary of the KG or an exclusive literature priority.

The KG contribution is to connect supplied neighborhood, expression, and
ChromLinker observations to source-grounded experimental findings, contextual
evidence, contradictions, and explicit gaps for the regulatory results below.
Literature can contextualize a manuscript interpretation without independently
demonstrating a Spatial NicheLinker-defined niche or its disease-dependent pattern.
The KG must not present literature about general cell identity as validation of
an algorithm-derived niche assignment.

The graph has a general, reusable biological schema and a bounded manuscript
corpus. It must preserve cell types, dataset-qualified neighborhood states,
biological contexts, project measurements, inferred connections, publications,
source passages, experimental findings, and claim/evidence links. All supplied
input observations remain available in files; graph materialization is an
explicit selection across the manuscript cases, not a universal lung atlas.

| Manuscript question | KG responsibility and evidence boundary |
|---|---|
| Do same-type cells occupy different neighborhoods? | Represent supplied focal-cell/niche definitions and neighbor profiles; link the corresponding manuscript claims. Do not recompute clustering or spatial abundance from missing cell-level inputs. |
| Do neighborhood states differ transcriptionally? | Link available niche-expression signatures and expression observations with their true units and provenance; do not invent DE statistics or enrichment results. |
| Do states correspond across independent datasets? | Distinguish spatially observed niches from transcriptionally mapped niche-like populations; link supplied mapping/validation artifacts when available. Missing cross-dataset validation stays explicit. |
| Do regulatory states vary with neighborhood and disease? | Represent lineage-specific ChromLinker predictions and literature findings for all four regulatory cases; distinguish within-condition contrasts from unverified disease-interaction interpretations. |
| What supports the biological interpretations? | Link exact experimental/contextual evidence, contradictions, limitations, and missing inputs to manuscript claims, not just to a ranked TF list. |

Include claims without validation inputs in the manuscript coverage report as
unverified; do not manufacture graph results to fill those gaps. Reuse existing
entity/observation contracts and add only minimal typed claim/provenance fields
where needed. This does not require reimplementing Spatial NicheLinker, cell-state
mapping, or ChromLinker itself.

## Required regulatory cases

| Case / source cell-type label | Required manuscript regulators | Primary comparisons | Draft interpretation to assess |
|---|---|---|---|
| AT1 / `AT1` | TEAD1, KLF5, GATA6, FOXA2, ETV1 | Niche2 versus Niche1 separately in Control and IPF | Niche1 structural program; ETV1-associated remodeling; condition-dependent FOXA2 pattern |
| Alveolar macrophages / `Alveolar_Macrophages` | SPI1, EGR2, BHLHE41, TFEC, IRF8, CEBPB | Niche2 versus Niche1 separately in Control and IPF | Resident macrophage program, its attenuation/redistribution, and a condition-dependent CEBPB pattern |
| KRT5−/KRT17+ epithelial cells / `KRT5neg_KRT17pos` | TEAD1, KLF5, RFX2 | IPF Niche2 versus Niche1 | Junction/adhesion and epithelial regulatory redistribution; no required focal Niche2 gain |
| Activated fibrotic fibroblasts / `Activated_Fibrotic_FBs` | FOSB, TEAD1 | IPF Niche2 versus Niche1 | Cytoskeletal/adhesion/stromal program attenuation or redistribution |

These are six primary lineage/condition comparisons, 16 lineage–TF memberships,
and 13 unique named regulators. Resolve exact source labels through the audited
mapping; do not manufacture absent contexts. Supplied Control expression/signature
data for the latter two lineages remain preserved, but do not substitute for their
missing Control niche ChromLinker observations or establish disease interactions.

The manuscript also describes neighborhood analysis across 47 annotated types
and clear separation in ten. This does not authorize inventing regulatory data
for all 47 or require 47 independent literature/extraction pipelines. All four
regulatory cases above are required for this KG delivery, not deferred expansion.

## Evidence roles and relevance

Account for all 110 advisor PMIDs and all original memberships. Screen their
content against all four cases and named regulators, with bounded targeted
discovery filling gaps. A macrophage study can be highly relevant to the
macrophage case; it is not globally off-topic because it is not AT1.

Keep paper roles explicit: primary regulatory experiments, biological context,
resource/method background, other-context evidence, or uncertain. Multiple roles
can apply to one paper. Match each finding to a specific lineage/condition/claim;
do not store a universal AT1-relative relevance score on the publication.
Do not require literal seed symbols in titles/abstracts to admit advisor papers.
Keep assay, species, cell type, tissue, model system, disease, direction, and
directness separate; unknown context cannot become an exact match.

Examples of appropriate scope:

- Lung/alveolar expression atlases support cell-state interpretation, not by
  themselves direct TF-target regulation.
- Primary EGR2/SPI1 macrophage evidence and fibroblast regulatory evidence belong
  to the manuscript scope alongside epithelial evidence.
- Cancer and non-lung experiments may illuminate a mechanism with limited context
  transfer; preserve their limitations instead of dropping or relabelling them.
- Resource articles document provenance; their reused studies are not independent
  replications. Do not ingest every referenced database just because it is listed.
- Null results, repression, loss of connectivity, and redistribution are useful
  outcomes. Neither candidate selection nor reporting requires a Niche2 TF gain.

## Manuscript claims versus available measurements

The draft is the authority for which questions to address. It is not a substitute
for source measurements, score definitions, experimental metadata, or validation.

- Preserve the existing descriptive Yale pooled niche-expression signature units.
  Draft wording about differential expression across datasets does not provide
  sample-aware DE statistics, donor-resolved data, or cross-platform input files.
- ChromLinker transform, zero semantics, and TF aggregation remain unconfirmed
  until a documented definition and relevant aggregation inputs are supplied.
  Store the draft's directional assertions as manuscript claims to assess, not
  computed facts or confirmed causal regulation. Do not hard-code the reported
  direction into candidate scores or search filters.
- For AT1/macrophages, show the two within-condition contrasts separately.
  Comparing those descriptively does not constitute a statistical disease-by-niche
  interaction test. For KRT/fibroblasts, keep the manuscript's IPF-only regulatory
  comparison unless additional appropriate measurements and design are supplied.
- Sample representation, spatial abundance, cross-dataset reproducibility, and
  enrichment claims in the draft need their own underlying results to be verified.
  Do not overwrite currently null donor fields from narrative counts. Preserve
  these as supplied claims with missing validation inputs where applicable.
- Functional annotations/pathway statements must cite existing supplied enrichment
  results or remain unverified. Do not generate pathway membership using an LLM
  or silently add a new enrichment-analysis project to fill narrative gaps.

## Implementation delta and review ownership

The accepted P1 artifact already ingests the supplied four-lineage inputs. The
accepted P2 and original P3 demonstration cover AT1 only. Preserve those results
and review evidence; their acceptance does not establish four-lineage completion.

Before new manuscript-wide retrieval, implement and review a bounded **P2 scope
extension** using the existing code:

1. Replace the active AT1-only scope/config assumptions with an explicit mapping
   of the four cases, their TF seeds, and six primary comparisons. Keep the old
   config/run reproducible; version changed configuration/contracts. Avoid changes
   to ingestion semantics or duplication of source data just for scope migration.
2. Reuse HGNC, CollecTRI, resolver, signed-concordance, and candidate code. Seed
   inclusion must work with absent prior coverage or no eligible targets. Include
   per-lineage TF seeds and the existing bounded additional-candidate route.
3. Make focal cell type and comparison identity explicit throughout candidates,
   target selections, query rows, coverage, and later evidence associations. A TF
   occurring in several cases has one gene identity but distinct nomination
   contexts. Do not leak one lineage's seed set or evidence into another.
4. Emit a reconciled manuscript candidate/coverage manifest. Test all six primary
   comparisons, shared TEAD1/KLF5 identities, absent Control regulatory contexts,
   sparse/empty results, preservation of negatives, and replay. Keep the old AT1
   baseline reproducible. Mark the extension pending until the lead reviews it.
5. Build resumable discovery/retrieval batches with explicit coverage scheduling
   across all four cases. A global top-k must not starve later lineages. Batch
   budgets remain enforced; missing support is reported rather than fabricated.

P3 repairs may finish against their original regression corpus in parallel with
these requirements being documented; no second agent is implied. Advisor metadata
audit/download reporting can proceed independently. New manuscript-specific
retrieval depends on the reviewed expanded candidate manifest. Continue with the
existing P3 corpus-readiness assignment, then P4 extraction, P5 file-first export
and import, and P6 manuscript evidence reports.

P6 must produce one coverage/evidence summary for each of the four cases and an
integrated manuscript claim-to-evidence table. Each row links the draft claim,
lineage/condition, project observations, exact literature findings, context match,
support/contradiction/uncertainty, and missing inputs. Do not equate a working AT1
example, all-paper metadata coverage, or a positive LLM response with completion
of the manuscript contribution.

## Pre-P4 corpus and provider decision

The user requires completion/review of corpus preparation before P4 starts, then
will choose the LLM provider/model/key. Follow plan.md P3.17: freeze the corpus,
resolve or explicitly disposition missing assets, and present actual coverage and
estimated inference tokens/costs. Local parsing/retrieval need no chat API calls.
Ready individual batches do not bypass this corpus-wide checkpoint.
