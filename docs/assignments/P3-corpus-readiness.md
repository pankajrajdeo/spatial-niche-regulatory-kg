# P3 extension — complete advisor corpus and extraction readiness

Requested by the user on 2026-09-22. Status: **PLANNED; NOT IMPLEMENTED OR ACCEPTED**.
This extends P3 before live P4; it does not create a new package or invalidate
accepted P1 and the historical AT1 P2 baseline. Expanded manuscript candidate
coverage now uses the accepted P2 extension `mcandidates-c278c6625ff7c537`
([review](../reviews/P2-manuscript.md)). Preserve the accepted original P3 repair baseline. Read AGENTS.md,
plan.md §9, and docs/reviews/P3.md first. Workers do not change acceptance boxes.

**File interpretation clarification, 2026-09-22:** also follow
[P3-file-readiness.md](P3-file-readiness.md). It specifies format edge cases,
library choices, numerical meaning, context across files, and fail-closed
readiness checks. These refine this assignment; they do not require a parser for
every possible format or authorize new raw-data analyses. Successful parsing
alone must not make a file eligible for scientific extraction.

**Agent boundary clarification:** [the P4 evidence-assembly contract](P4-evidence-assembly-agent.md)
adds adaptive source navigation after P3 review and user model/budget selection.
Do not implement/run that agent in this P3 assignment. Preserve parsed source
registries, ready bundles and separately identified context-investigation items.
Report assembly token/call allowances separately in the inference budget. A pending
investigation is not ready extraction evidence; missing files, parsing/identity
failures and new-analysis requirements still need explicit repair/disposition.
P4 may publish validated child bundles over the frozen sources; original P3
manifests stay immutable. This clarifies the freeze contract below.

## Required outcome

Account for every publication in the accepted P2 `seed_publications.parquet`
(currently 110 unique PMIDs and 117 list memberships). Acquire and process all
available advisor papers, regardless of title/abstract candidate-name matches.
An advisor recommendation is corpus membership, not proof of a regulatory claim
or proof of relevance to a particular manuscript claim. Preserve off-context and non-regulatory papers with
their actual disposition; do not manufacture findings to achieve coverage.

Screen every paper, but do not force every paper through paid regulatory
extraction. Record provisional paper roles (multiple allowed), with source and
review status: `PRIMARY_REGULATORY_EVIDENCE`, `BIOLOGICAL_CONTEXT`,
`RESOURCE_OR_METHOD`, `OTHER_CONTEXT`, or `UNCERTAIN`. Resolve roles using the
actual abstract/full text, not an inherited tier alone. Roles prioritize work;
eligibility ultimately belongs to an individual finding/experiment. A resource
paper can contain an original experiment, and a primary paper can cite reviews.
Lead-reviewed background-only papers remain covered without invented LLM calls.
Retain available full texts for screening, but put missing background/reference
assets in a lower-priority section rather than making all of them prerequisites
for manuscript extraction. Do not add all referenced databases to the project scope.

For interpretation: expression atlases do not establish TF-target regulation;
protein interactions do not establish transcriptional regulation; database
articles and their underlying studies are not independent replications; and
lung-cancer/other-cell-type findings must retain their context. Preserve negative
and contradictory findings under the same relevance rules as positive findings.

The execution target is the [current manuscript scope](../manuscript_scope.md):
AT1, alveolar macrophages, KRT5−/KRT17+ epithelial cells, and activated fibrotic
fibroblasts, with lineage-specific regulators and comparisons. No lineage has
automatic priority. Audit all advisor papers against all manuscript cases and
retain roles/context at the finding level. A macrophage paper is not off-topic
merely because it lacks AT1 biology. Keep missing nonessential background assets
from blocking a verified batch, while making every lineage's pending work visible.

Use `candidates-ad74f8d35867b7f3` for the accepted advisor seed inventory and the
original AT1 repair regression; do not use `candidates-20f8d10eba674ebc`. For new
manuscript-wide retrieval, consume the **reviewed expanded P2 candidate manifest**
`mcandidates-c278c6625ff7c537` from plan.md P2.11–P2.13. The old artifact alone
does not cover the manuscript. Adapt the P3 input contract to the accepted
`p2-manuscript-1` schema, preserving lineage associations and old-schema replay.
Do not generate expanded evidence bundles from guessed candidates.
Recompute counts from the source; fail reconciliation on missing/extra seed IDs
instead of hard-coding an expected success count. Search discoveries are an
additional corpus route and must not displace advisor papers.

## Execution order

1. The original R1–R4 and F1/F2 repair baseline is accepted in docs/reviews/P3.md,
   with current retrieval `litretrieval-6a092b32d5f87020`. Preserve all prior
   artifacts and use this as the regression baseline; do not redo the repair
   assignment. Record baseline and expanded-corpus evidence separately.
2. Consume the accepted manuscript queue: 248 queries in 13 batches, all initially
   NOT_SEARCHED. The fixed queue is assigned for execution in resumable batches of
   at most 20 queries, with at most 10 papers per acquisition batch. Keep the
   rotating equal-share lineage schedule and validate PubMed/Europe PMC query
   translations for punctuated KRT5/KRT17 terms before bulk execution. If needed,
   version adapter normalization and record actual queries; do not mutate the P2
   artifact. Discovery phrases do not establish cell-type equivalence. Reuse
   identical requests, unify publication identities across routes, and retain all
   deferred papers/passages instead of dropping them at per-batch selection caps.
   Stop at this fixed discovery frontier; report evidence gaps for a later bounded
   assignment instead of launching a universal crawl.
3. Build the advisor coverage ledger from the accepted P2 artifact and reconcile
   source memberships. Reuse existing metadata/source caches with content hashes.
4. Audit full-text availability for every advisor PMID. Fetch eligible structured
   full text first, using resumable batches of at most 10 publications. Persist
   batch progress after each batch. Direct lookup of the fixed advisor list is
   not a new keyword search or a universal crawl. Keep at most 20 discovery queries per assigned batch and track the unexecuted queue.
5. Publish the coverage ledger and manual-download report immediately after the
   audit, before waiting for user PDFs or finishing the PDF adapter. Include exact
   artifact paths in a short progress update so the user can download in parallel.
6. Implement local document intake, Docling PDF parsing, and necessary supplement
   readers behind the existing canonical-document contract. No duplicate parser
   framework. Do not touch worker-unrelated source files or alter original inputs.
7. Parse all available advisor full texts, inspect real outputs, construct bounded
   retrieval batches, and publish the readiness report. Missing files and failed
   parsing stay pending; they do not silently become completed abstract reviews.
8. Run focused tests and existing P1/P2 replay/regression checks, update the P3
   handoff, and stop for lead review. No P4 chat calls, Neo4j writes, or Git push.

## Coverage ledger

Write immutable `advisor_coverage.parquet` and a readable `advisor_coverage.csv`
under `data/processed/<corpus_key>/`. One publication row per advisor PMID; keep
all original list memberships and their source hashes, tiers, and annotations.
Use a linked asset table for multiple article/supplement versions. Required fields:

- Publication ID, PMID, PMCID/DOI when verified, title, year, source memberships,
  metadata-conflict/retraction status, and acquisition priority with reason.
- PubMed URL, PMC URL when known, DOI resolver URL when known, and returned
  publisher/full-text/supplement URLs with discovery source and timestamp.
- Access status and checked sources; separate acquisition state such as
  `NOT_CHECKED`, `FULL_TEXT_ACQUIRED`, `ABSTRACT_ONLY`, `MANUAL_DOWNLOAD_NEEDED`,
  `FETCH_FAILED`, `IDENTITY_REVIEW_REQUIRED`, or `UNAVAILABLE_CONFIRMED`.
- Asset IDs/checksums, local paths, article version, format, parser/config/version,
  and parsing state `NOT_PARSED`, `PARSED`, `PARSE_FAILED`, or `PARTIAL`.
- Main-text/caption/table/supplement coverage and explicit missing components.
- Screening disposition and reason/source: `NOT_SCREENED`,
  `CANDIDATE_PASSAGES_FOUND`, `NO_CANDIDATE_PASSAGES`, or `CONTEXT_ONLY`.
  No candidate passage is a retrieval result, not a negative experiment or proof
  the complete paper contains no useful evidence. Retractions remain visible and
  cannot contribute primary support.
- Readiness state `READY_FULL_TEXT`, `READY_ABSTRACT_ONLY`, `NEEDS_ASSET`,
  `NEEDS_PARSE_REPAIR`, `NEEDS_CONTEXT`, `NEEDS_SCREENING_REVIEW`, or
  `NO_ELIGIBLE_BUNDLE_REVIEWED`, with reasons and exact bundle IDs if ready.
- A separate downstream extraction status, initially `NOT_RUN`; later distinguish
  queued/running/completed/no-relation/failed and extraction run IDs. Metadata,
  parsing, or one extracted bundle must not imply whole-paper extraction complete.

Keep these dimensions separate. For example, a successfully parsed paper can
still lack the supplement needed to interpret a particular result. Preserve
title/abstract and indexed species as metadata, not experiment-level identity.

## Manual-download report and return path

Generate `manual_downloads.csv` and `manual_downloads.md` with one actionable row
per needed asset, grouped by publication. Save checksummed copies alongside the
ledger, with an optional regenerated convenience copy in
`reports/literature/<corpus_key>/`. Include:

- PMID/DOI, title/year, advisor-list membership, priority and reason.
- Needed item: article PDF, named supplementary PDF/table, or another identified
  asset; expected filename and relative inbox destination.
- Evidence role and whether the asset is required for a proposed extraction
  bundle, needed to resolve screening uncertainty, or optional background reading.
  Keep all outstanding items visible, but distinguish the user's immediate
  download tasks from lower-priority background/reference material.
- Clickable PubMed, verified PMC, DOI/publisher, and discovered asset links.
  DOI links are landing/resolver links, not promises of downloadable PDFs.
  Do not invent direct PDF URLs or a university-specific proxy/login URL.
- Why user action is needed, which automatic routes were checked, last-check time,
  and state (`NEEDED`, `RECEIVED`, `IDENTITY_REVIEW_REQUIRED`, `INGESTED`).
- Optional user note/unavailable disposition and the resulting local asset hash.

Keep a separate `acquisition_failures` section/table for timeouts, malformed API
responses, and parsing failures. Do not call those papers paywalled. Where a
manual alternative is useful, label it as a fallback, not the diagnosed cause.
The report must cover all outstanding advisor assets, not only the 10-paper test
slice. Preserve resolved rows/history so new reports show what changed.

Use ignored `data/papers/manual_inbox/` as the proposed local intake location:
`<PMID>/article.pdf`, `<PMID>/supplement-<source-name>.<ext>`, plus a small
`intake.csv` mapping files to publication/asset IDs, URLs, and acquisition dates.
No login cookies, passwords, or library session URLs belong in that manifest.
Use existing ignore rules; add a narrow rule only if necessary.

On intake, verify file signature, size, nonempty content, and declared identity
against available DOI/title/PMID text. A filename is a mapping hint, not identity
proof. Flag inconsistent or unconfirmable documents for review. Reject paths
escaping the inbox, and do not follow external symlinks or execute file content.
Copy accepted bytes into the existing checksummed asset store; leave originals
unchanged. Deduplicate identical bytes and retain distinct versions. Regenerate
coverage/download reports. Reprocess only changed assets and dependent bundles.

## Parsing capability required before live extraction

Apply the format matrix and acceptance checklist in
[the file-readiness specification](P3-file-readiness.md). Record asset integrity,
parse completeness, scientific meaning, and bundle readiness separately. Table
regions need known column/contrast/unit meaning for the proposed claim; new
calculations require explicit code/provenance and raw-data reanalysis remains
outside this assignment. Preserve source-reported values and unknowns.

When a row needs a legend or methods from another asset, verify the publication,
version, table and experiment linkage. Extend the bundle contract to carry each
part's own hash/document/locator when implementing this path. Until that path is
implemented and tested, keep such bundles `NEEDS_CONTEXT`. Do not concatenate
unrelated documents or apply one document's offsets to another. Count serialized
table content as well as prose against bundle limits and inference estimates.

- Keep structured JATS/BioC as the preferred available source; use the existing
  safe XML/JSON parsers with repaired table and species handling.
- Correct `_bioc_kind` so generic BioC footnotes (including supplementary URL
  lists) are not automatically table footnotes. Associate table footnotes only
  when the source supports table membership. Preserve text/locators, version
  changed parsing rules, test both cases, and correct table-count reporting.
  The accepted baseline contains 13 misclassified generic footnote passages;
  they are not 13 genuine tables and were not selected as table-row bundles.
- Implement the planned local Docling adapter now for advisor PDFs. Pin the
  compatible PDF extra/lock and record necessary model assets/revisions. Keep
  conversion local; no remote VLM or scientific interpretation of figure pixels.
  Bound pages, OCR, file size, runtime, and memory. Oversized/unsupported inputs
  receive explicit partial/failure statuses rather than silent truncation.
- Preserve canonical text with exact offsets, section/item identifiers, and PDF
  page/item/bounding-box provenance where available. Keep source checksums and
  parser/normalization versions in document, passage, and bundle identity.
- Retain paragraphs, captions, table cells, headers, captions, and footnotes.
  Validate merged/multirow headers and context completeness. Ambiguous tables
  remain inspectable but cannot supply falsely precise quantitative findings.
- Preserve figure identity/caption/source references. For PDFs, retain available
  figure crops or page references for inspection; record the distinction between
  preserved image assets and interpreted evidence. No chart/blot/microscopy
  conclusions from pixels. Figure-only evidence requires manual review.
- Inventory all discoverable supplementary links/items. Acquire accessible
  supplements for advisor papers and include missing/restricted items in the
  user report. Parse supplementary PDFs through the same adapter; support actual
  supplied CSV/TSV/XLSX tables with sheet/row/column/header/unit provenance. Never
  execute spreadsheet formulas/macros; preserve formulas and distinguish cached
  values/missing values. Binary datasets, videos, and other unsupported assets
  remain inventoried with explicit disposition, not marked parsed.
- If a supplementary table is indispensable to a bundle, absence/unsupported
  parsing blocks that bundle. It need not block unrelated well-grounded findings
  from the same paper. Never join experiments only by nearby layout or gene name.
- Select one canonical article version and retain alternatives; avoid duplicate
  evidence from XML and PDF of the same study. Supplements link to their parent.

Demonstrate the PDF branch on at least one real accessible/supplied advisor PDF
if available. If none is accessible yet, implement/test the branch and report
live PDF validation pending; do not claim full PDF readiness using fixtures alone.
Inspect representative real prose, a figure caption, a table with header/footnote
context, and a supplement when available, comparing parser output to the source.

## Batching and P4 boundary

The 10-paper/20-bundle/40-scheduled-call values are **per live extraction batch**,
not a cap on the advisor corpus. Retain at most 3 passages/6,000 characters per
bundle and existing retry/token/provider price controls. Keep the original P3
regression batch limits unchanged. Use a deterministic remaining-work queue so
global per-TF/per-paper caps do not permanently starve later papers or passages.
Record deferred eligible bundles and an explicit processing frontier; do not
claim exhaustive extraction from top-k retrieval.

Generate a corpus-level `extraction_readiness.json` and readable report containing:
source seed count and reconciled membership count; acquisition/parsing/screening
counts; asset and bundle blockers; ready batch manifests; pending queue; and the
number of papers still awaiting user files. Include per-lineage, named-regulator, and primary-comparison coverage so a globally successful batch cannot hide an unprocessed manuscript case. Each batch manifest pins publication,
asset, document, passage, and bundle hashes plus context-completeness results.

**User checkpoint — 2026-09-22:** complete the manuscript-scope P1–P3 preparation
before starting P4. Do not begin P4 development, smoke tests, extraction, or
verification calls merely because an individual batch is ready. Finish the
four-lineage candidate extension, whole-advisor audit, assigned targeted discovery,
manual-download reconciliation, parsing/context review, retrieval, and corpus-wide
readiness/budget reports first. Present remaining inaccessible/unsupported assets
and unresolved review items explicitly; they require a recorded user disposition
before the corpus can be frozen as ready. Never label them processed.

Freeze the approved corpus and extraction queue, then wait for the user to select
the LLM provider/model and supply or confirm its credential configuration. The
existing `.env` and earlier smoke-call authorization do not authorize the newly
expanded extraction run. Preserve `.env`; do not inspect or print key values.
P4 must validate the frozen readiness manifest and refuse failed, unverified, or
context-incomplete bundles. Abstract-only scope requires an explicit recorded
disposition and never counts as full-text coverage.

Before that checkpoint, generate `inference_budget.json` and
`inference_budget.md` beside the readiness report, without calling a chat model:

- Actual counts of unique papers audited, full texts parsed, contextual/resource
  papers, extraction-eligible papers, bundles, batches, and pending items, split
  by manuscript lineage/comparison and evidence role.
- Text/structured-context sizes of every proposed bundle, including table cells,
  headers, captions, and grounding metadata actually intended for the prompt.
  Do not count only the anchor paragraph. Deduplicate shared bundles across
  candidate/lineage associations where the extraction payload is identical.
- Estimated extractor and verifier input separately; verifier input includes
  source context plus extractor findings. Include explicit prompt/schema overhead
  assumptions until P4 prompts are finalized. No-relation results may avoid a
  verifier call, but budget up to two scheduled calls per bundle.
- Separate assembly estimates: investigation counts, bounded repeated model inputs including tool schemas/history/results, final output/reasoning and retry allowances. Show bypass/cached cases separately and preserve the user-approved total cap; the old 40-call limit is extractor/verifier only.
- Estimated output and billable reasoning tokens, timeout/retry assumptions,
  schema preflight allowance, scheduled-call count, attempt ceiling, and cumulative
  corpus totals. Show a typical scenario and a conservative runtime-cap scenario;
  do not mistake a 25% planning reserve for an enforced ceiling.
- Provider-agnostic token estimates plus a rate-parameterized cost table. State
  currency and USD per million-token units; split input/output/cache/other charges
  when applicable. No assumed caching discount. Clearly label illustrative rates;
  verify actual selected-model/provider rates only after selection.
- Exact tokens depend on the selected tokenizer and final prompts. Label current
  estimates as estimates; P4 must repeat a no-inference dry run with the selected
  model and implemented prompts before the first live call. Source preparation
  and the first cost comparison do not require an LLM API key.

Preparation uses existing public source adapters, local parsing/Docling, lexical
retrieval, and the selected local Ollama embedding model. It makes **no chat API
calls**; do not add paid OCR, remote VLM parsing, or LLM screening to P3.

Coverage acceptance has three distinct numbers: papers accounted for, full texts
processed, and papers/bundles extracted. All advisor IDs must be accounted for;
every available advisor full text must be parsed/screened; unresolved access or
review items prevent a claim of complete corpus processing. An unavailable paper
may have a documented reviewed disposition but is never labelled extracted.
Scope/context/no-eligible-bundle exclusions require lead review and remain listed.

## Acceptance evidence

- Address the relevant checks in [P3-file-readiness.md](P3-file-readiness.md) in
  the handoff: observed formats, validated adapters, table meanings, unresolved
  semantics, partial coverage, cross-asset links, and required review items. Keep
  unsupported formats explicit instead of claiming universal parser support.

- Reconciliation covers every seed PMID and original membership; duplicates across
  source routes are unified. An advisor paper without an exact title/abstract TF
  mention still enters acquisition and full-text screening.
- Advisor membership is computed from authoritative P2 IDs, not a search-route
  flag. A lead cross-check on 2026-09-22 found PMID 37067057 in both the original
  selected 10 papers and the advisor list, contrary to the old handoff's claim
  of zero advisor papers selected. Preserve both routes and correct that report.
- Tests cover cached/full-text success, true unavailability vs network failure,
  missing supplement, intake identity mismatch, duplicate and changed bytes,
  PDF provenance, table context, safe spreadsheet handling when implemented, and
  resumable queues without dropped papers or repeated successful work.
- Readiness rejects unparsed/failed/incomplete bundles and reports pending corpus
  items. Per-batch limits do not masquerade as whole-corpus completion.
- Include real coverage/download/readiness report paths, acquired/parsed counts,
  format-specific checks, actual network/embedding counts, and deferred items in
  `docs/handoffs/P3.md`. Re-run relevant checks after code changes. Stop for review.

The CLI should expose corpus audit, manual intake, coverage/download report,
and ready-batch generation through the existing literature command group. These
are capabilities to implement, not claims that such commands already exist.
