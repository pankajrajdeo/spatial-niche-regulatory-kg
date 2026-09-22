# Lead review: P3 corpus correction pass

Latest continuation: [P3 scope-closure review](P3-scope-closure.md). Follow its source-gap completion assignment; earlier repair instructions below are historical.

Date: 2026-09-22. Latest decision: **per-TF identity repair accepted; scope/disposition closure and revised validation selection pending.**

## Latest lead review — `litcorpus-f8a11dd187098a3d`

**Decision: per-TF identity repair ACCEPTED. Proposed pilot NOT APPROVED unchanged. Expanded P3 still needs scope/disposition closure; no live calls authorized.**

- [x] Per-TF aggregation repair inspected: computation follows merged associations, manifests preserve individual identities, and mixed-identity regressions pass.
- [x] Independently ran 194 tests (passed; two existing Docling deprecation warnings) and Ruff (passed). Verified all 91 output checksums.
- [x] Independently checked all 1,066 ready bundles: 189 papers, 402 all-TF source-ID-consistent bundles, no unsupported per-TF upgrades in the checked records.
- [ ] Manuscript corpus scope/dispositions and validation selection approved.

The 12-bundle/10-paper proposal is a useful diagnostic, not adequate manuscript coverage. Inspected all 12 anchor texts. Examples: PMID 37732539 is lung-cancer MECOM work selected under AT1; PMID 38374140 is cardiac fibroblast TEAD1 work, including explicitly mouse experiments; PMID 37577627 concerns KAT6A in dermal fibroblasts; PMID 33872194 contains a schematic STAT6–EGR2 account that needs primary/secondary attribution review. PMID 39535362 describes SPI1 experiments in tumor/HEK293T cells in a macrophage-crosstalk paper, not automatically regulation inside alveolar macrophages. These can be useful context-discrimination tests, but cannot count as direct evidence for the assigned manuscript cell population.

The strict human-source-ID gate is a pilot selection choice, not a scientific requirement for extraction. It may exclude informative nonhuman or unresolved mentions. Conversely, an annotation mapping to a human ID does not make an explicitly mouse experiment human. Preserve both the annotation and source-stated experimental species; do not use `scorable_as_resolved_human` alone to approve a finding. The accepted fix addresses cross-TF contamination, not experiment-level species validation.

Next action is [P3 scope closure and validation selection](../assignments/P3-scope-closure.md). No further broad parser/corpus redesign is requested. The full finish line is unchanged: one complete manuscript-ready project; validation subsets are checkpoints, never an MVP or justification to drop required work. This review changed documentation only, not source code, artifacts, environment or credentials. Historical verification commands reported by the worker were not independently rerun in this pass.

## Follow-up lead review — artifact `litcorpus-0f330e3ec37fc790`

Decision: **one targeted identity repair remains; corpus not frozen; no P4/live inference authorization.** This follow-up supersedes the previous broad repair status below.

Independently reran the full suite: **190 passed**, two Docling/Pydantic deprecation warnings; Ruff passed. Verified all **91** manifest output checksums. Recounted **1,066 ready bundles from 189 papers**, maximum 5,997 serialized characters and three parts. The supplement registry now records 57 acquired assets, preserving partial/failed parses, with the oversized unacquired archive explicitly excluded. Reviewed the revised screening, bounded local-source navigation, ontology hashing and budget outputs. The earlier R1–R5 repair pass has made substantial progress; do not repeat the broad crawl or parser overhaul.

### Remaining identity defect — fix before scope selection

`src/regkg/workflows/corpus_ready.py:388` reduces all anchor TF mentions to one status: any consistent source identifier makes the bundle human-scorable unless a conflicting/ambiguous mention is present. This incorrectly upgrades other name-only TFs in the same bundle. An independent artifact check found three ready bundles marked `scorable_as_resolved_human: true` without consistent source identifiers for every associated TF:

- `payload:32b7b525429e3d523a9d`: unsupported by consistent source identifier for `HGNC:11714`.
- `payload:5c4f9e13a9dee8b20608`: unsupported for `HGNC:6348`.
- `payload:af0f23fb130b2c18e8ef`: unsupported for `HGNC:3798`.

Required: preserve identity status and original source identifiers per candidate TF/association, not just per bundle. A resolved TF must not upgrade another unresolved TF. If retaining a bundle-level all-resolved flag, require every relevant TF to satisfy it. Compute from the complete merged association set. Carry the per-TF result into ready manifests; preserve unresolved/nonhuman candidates without inventing human identity. Add a mixed resolved/name-only two-TF regression and a mixed resolved/conflicting regression. Refresh dependent reports/manifests through normal artifact publication with appropriate rule-version invalidation, reusing downloads, parses and embeddings. Do not rewrite existing artifacts or repeat broad acquisition.

### Scope and handoff corrections

- The 405 identity-consistent bundles are a proposed pool, **not an approved pilot or 405 verified findings**. Following the fix, propose at most 10 papers/20 bundles covering all four manuscript lineages where eligible evidence exists. Include explicit gaps and a selection rationale; source-ID consistency alone does not establish experimental species, cell context or valid regulatory evidence.
- Current manual-download report separates **two candidate-evidence article requests** from 64 potentially useful articles, 110 background articles, 443 identification tasks and 42 size/parse repairs. Two is not a guarantee that no further files will be needed after scope review.
- Budget rows remain estimates. The actual report has **4,145** hypothetical split children, not the handoff's 4,144; use the stored report. Only the assembly call caps are configured bounds; the overall row named ceiling is not an enforced total extraction spending cap.
- Ontology labels remain screening hints, not exact scientific equivalences. In particular generic activated fibroblasts/CTHRC1-positive cells and aberrant basaloid labels must not automatically establish the exact manuscript population during extraction.
- Keep proposed deferrals visible for review. Do not silently discard the screening/table/context frontier or force all advisor papers through extraction.

Next worker scope: the targeted identity correction, accurate handoff counts and a small proposed pilot manifest only. No paid calls, P4 implementation, new corpus expansion, commits, pushes or acceptance checkmarks. The lead will review scope/dispositions before freezing P3. This review changed documentation only; it did not alter code, artifacts or secrets.

## Earlier review — `litcorpus-1ed92d41df5cb075`

Decision at that review: **CHANGES_REQUIRED; no P4/live inference authorization.**

Reviewed the full worker transcript supplied in attachment b376f498-5d35-41c9-a9ea-eaf6dc45b123, current code, handoff and artifact `litcorpus-1ed92d41df5cb075`. The transcript includes a later explicit user request to consider cell-type/disease synonyms and ontology files; the ontology work is therefore authorized, despite the earlier plan placing hierarchy work in P5/P6. Synonym-based P3 screening/search and P5/P6 hierarchy export remain separate capabilities.

## Independently checked progress

- Full test suite: 183 passed, 2 Docling/Pydantic deprecation warnings (21.90 seconds). Ruff: all checks passed.
- All 86 output checksums in the current artifact manifest match. This establishes current stored-output integrity, not correctness or historical immutability.
- 1,029 ready bundles from 185 papers; all fit 3 parts/6,000 serialized evidence characters. Maximum observed ready size: 5,979 characters.
- Per-paper candidate enumeration replaces the global top-10 exclusion. Historical query-association counts are now labeled correctly. The expanded ledger, separate investigation queue and versioned resource snapshots are useful.
- Source files/code were inspected; no source code, source inputs, environment variables or artifacts were changed by this review. No chat calls, bulk reprocessing, commits or pushes were performed. Historical baseline verification reported by the worker was not independently rerun in this review.

## Required repairs

### R1 — Newly acquired supplements are absent from the published corpus registry (high)

`workflows/corpus_prepare.py` builds documents/meta/parse inventory and screening before `_parse_needed`. That helper discards returned documents and only updates dependency state. `_all_audits` does not merge needed-supplement acquisition records. All **55** acquired needed-supplement assets are absent by SHA-256 from BOTH `coverage_assets.parquet` and `parse_inventory.parquet` in the published artifact. They are consequently not covered by the claimed per-document screening/registry, even though dependency rows point to them.

`_parse_needed` and `_dependency_state` also collapse PARTIAL into `available_parsed`, including mixed archive-member outcomes. `investigations()` permits only matched dependency hashes plus the anchor; **159 cross-asset investigations permit only one asset**, so an unidentified reference can prevent navigation to local candidate supplements.

Required: merge acquired supplements and archive children into a checksummed publication/document/asset registry, inventory and applicable screening before final publication. Preserve each member's document ID, locator, parse status, parent linkage and remaining frontier. PARTIAL is not complete capture. Permit bounded navigation among eligible same-publication/version local sources when locating unresolved references; do not declare an experiment link from common publication alone. Merge anchor IDs when investigations are deduplicated. Missing/failed/uninterpretable sources remain blocked, not extraction-ready. Cache existing parses/vectors; do not redownload everything.

Verification: each of the 55 assets and its child documents is represented or explicitly excluded with a reason; new supplement prose/table regions have screening records or a retained unprocessed disposition; partial members stay visible; a synthetic missing-label reference can discover an existing local supplement without getting arbitrary filesystem access.

### R2 — Title/abstract heuristics still decide passage eligibility and overstate context (high)

`_relevance` uses only title/abstract; `screen` prevents bundle creation when those provisional labels are irrelevant for every associated lineage. Full-text regulatory findings can still be lost because the abstract lacks assay/regulation words. `_excluded_sample` labels absence of a TF name as likely outside scope, repeating the original exclusion rather than independently assessing it. `gene_matcher` is case-sensitive and ignores PubTator identifiers when enumerating anchors: a direct probe with EGR2 configured finds nothing in `Egr2 deletion affects alveolar macrophages.` Do not fix this by indiscriminately treating all case-insensitive words as human genes.

Context probes against the real ontology mapping reproduce false direct labels:
- `TEAD1 regulates alveolar type 1 fibroblast cells in lung tissue.` -> AT1 direct;
- `KLF5 regulates basaloid cells in lung cancer.` -> KRT5neg/KRT17pos direct;
- `We investigated activated fibroblasts in skin injury and lung epithelial cells.` -> activated fibrotic lung fibroblasts direct.

Required: paper-level labels prioritize; passage/linked-source evidence determines candidate disposition. Preserve unresolved candidates when the only exclusion is a title/abstract heuristic. Use validated aliases and source-ID-backed mentions/species-aware case variants as retrieval hints; retain unresolved species/entity identity rather than converting orthologs into human IDs. Resolve competing longer cell-type mentions and keep generic basaloid, IPF-fibroblast and mixed-context mentions broader/unresolved unless the source establishes the target state. Keep exact cell-type, species, disease and experimental attribution as separate dimensions. Unknowns do not need a new NLP model or forced resolution.

The paper-context label is not experiment-local biological evidence. Report current numbers as **provisional screened-context counts**, not proof that relevant literature is absent. Independent recount: ready bundles labeled direct are AT1 2, alveolar macrophages 33, KRT 0, fibroblasts 0; the reported 192 macrophage figure covers all labeled bundles, not 192 ready findings.

Verification: full-text relevant result survives misleading/underspecified abstract; probes above do not become exact direct context; null/negative evidence survives; source-backed nonhuman/case variants remain candidates without invented human identities. Revisit the 24 excluded-paper sample and preserve insufficient evidence as unresolved.

### R3 — Manual-download report confuses unresolved references with identified missing files (high)

Of 75 `required_evidence_asset` rows, **70 use `supplement-unidentified`**, three are article PDFs and two identify supplement filenames. Only five rows have a verified file link. `_download_row` keys requests by PMID plus filename, so all unidentified references for a paper collapse into one request/destination. One real row contains 17 cited items; they are not known to be one file.

Required: separate local source-navigation/identification tasks, identified missing files, parse/size-limit repairs and background dispositions. Keep a distinct unresolved-reference ID until multiple references are proven to share one asset. Only verified same-asset requests should share a download destination. Preserve all affected bundle IDs and publication/version links; do not send users an extensionless placeholder as though it were an actionable file. Report actual missing article/file counts separately from papers with unresolved context. Do not make all unidentified references mandatory manual downloads.

Verification: two unknown references from one paper remain independently resolvable; verified identical assets deduplicate; an existing local candidate goes to source navigation, not download; intake resolution cannot mark unrelated references satisfied.

### R4 — Budget is not an end-to-end bound (medium)

`budget()` charges ready bundles plus assembly, but does not charge extraction/verification of newly repaired child bundles in that scope. Its assembly conservative input sequence totals 26,000 tokens per investigation (4k+6k+8k+8k), below the actual allowed 4*8,000 = 32,000. Preflight calls also have fixed assumed sizes rather than an enforced worst case. The all-payloads case includes oversized blocked payloads without representing splitting into extra valid bundles.

Required: show current-ready-only, assembly-only, and assembly-plus-downstream scenarios; deduplicate repaired outputs by payload. Bound child bundle counts explicitly or mark the total dependent/unbounded until selection. Label modeled retry scenarios as scenarios; show a separate genuine configured ceiling where one exists, counting output/reasoning consistently with the assembly contract. Do not send oversized evidence as-is in a hypothetical ready scenario. No model calls to compute this report.

Verification: one successful investigation adds separately counted downstream extraction/verification; shared repairs are not double charged; true assembly input ceiling covers four 8k calls; rejected/no-result paths are distinguished.

### R5 — Ontology mapping changes are not fully included in replay identity (medium)

`build_context().record` stores versions/checksums and phrase COUNTS, not mapping bytes or effective phrase contents. A temporary-copy probe replacing one manuscript alias with another yields different phrase dictionaries but an identical record. Preparation hashes this record and payload ID/status, so a semantic mapping/query-gap change can reuse stale reports when counts/statuses do not change. `build_context` also assumes cached pinned resources exist; acquisition currently relies on the worker's ad hoc script.

Required: hash the validated mapping contents and effective phrase tables, plus source release checksums, in artifact identity. Validate configured IDs across CL/UBERON/MONDO and preserve ambiguous synonym-to-multiple-ID matches instead of silently choosing the first. Record missing/obsolete/unsupported mappings. Provide a documented reproducible acquisition path for the exact pinned releases (or verified transferred snapshots); do not silently fetch a future latest release. Ensure changes in needed-supplement bytes/parser config/outputs invalidate dependent artifacts as well. Keep proposed ontology matches explicitly provisional until reviewed.

Verification: same-count synonym edit changes artifact identity; unchanged replay reuses; cached-resource corruption is rejected; missing pinned resources have a reproducible setup action. No full ontology reasoning or migration of accepted local IDs required.

## Other dispositions

- There are 148 ready bundles with a TF/source-identifier conflict flag. This is not automatically 148 bad findings: some may reflect nonhuman orthologs. Preserve original external identifiers and species uncertainty, and demonstrate that P4 cannot score a conflicting name-only human association as resolved. The handoff's claim that ambiguous TF identity blocks readiness is stronger than the actual readiness function; correct that statement or implement the documented gate for genuinely ambiguous identities.
- The known JATS `<br/>` word-joining issue must not silently change header interpretation. Fix with parser-version invalidation and a focused regression or mark affected evidence for interpretation review. Avoid claiming a table's numerical meaning was verified from text overlap.
- No requirement to manually review all 1,465 attribution-unresolved bundles or all 2,486 table regions before any possible pilot. Record a scientifically defensible approved scope and explicit deferrals; essential unknowns in a selected bundle remain blockers. Permitted P4 investigations are pending work for P4, not something P3 must execute.
- The 14 synonym queries are a reasonable bounded follow-up to the user's synonym request, **after** mapping/context repairs. Preserve the accepted P2 queue and publish a separate versioned supplemental queue with exact terms, translations/results and overlap. Do not claim gaps from substring matching alone; broader original queries may already retrieve the same papers. Use existing request/acquisition limits, report incremental yield, and do not auto-acquire every result or expand into an unbounded search.

## Worker next action and stopping point

Repair R1–R5 in the existing modules, add focused behavioral regressions, regenerate a new artifact using caches, and submit a new P3 handoff referencing this review. Include before/after evidence and exact source registry/download/budget counts. Do not rebuild the application or loosen semantic gates for more ready bundles. Preserve `litcorpus-1ed92d41df5cb075` and prior artifacts. P4 and paid calls remain unstarted; only the lead checks acceptance. No acceptance boxes changed in this review.
