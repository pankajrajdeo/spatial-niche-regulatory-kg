# Lead review: P3 source-gap completion

Date: 2026-09-22. Reviewed worker handoff, current relevant code/configuration and artifact `litcorpus-301a27a43b316dd7`.

**Decision: source acquisition/search progress accepted; cache repair and freeze reconciliation required before acceptance of the frozen corpus. No P4/live calls authorized.**

## Independently checked

- [x] 201 tests passed, two existing Docling warnings; Ruff passed.
- [x] All 92 corpus output checksums match.
- [x] 1,078 ready bundles from 192 papers, maximum 5,997 serialized evidence characters.
- [x] No previously covered PMID from `litcorpus-f8a11dd187098a3d/paper_coverage.csv` was lost in the final artifact.
- [x] Delimited parser visits later rows and preserves selective-materialization/PARTIAL status; this is useful progress.
- [ ] Cache identity includes the effective row selection and parse limits.
- [ ] Freeze obligations match the actual reports and source readiness.

## Blocking cache defect (reproduced)

`RowSelector.fingerprint()` in `literature/files.py` stores only counts. More fundamentally, `corpus_parse.parse_cached()` hashes asset bytes, route, publication and static rules, but does not hash the selector or effective limits passed through the parse closure. A temporary three-row CSV with selector A followed by selector B returns the cached A row on the second call. Both selector fingerprints and cache keys match. Changing selection or row limits can therefore silently lose required rows.

Fix the cache input contract for the affected routes: include canonical sorted selector contents (or their cryptographic digest), row/column/materialization limits, and relevant effective parser options. Propagate selection identity into canonical parsed-document identity where passage content depends on it. Test same-count A-to-B selector replacement, changed limits and identical-settings reuse. Invalidate affected caches through versioned keys; preserve old outputs and reuse unaffected routes. This is a correctness repair, not permission to redesign caching globally.

The parser still accepts the entire asset as bytes and creates a decoded string/StringIO. It bounds materialized row objects, not total memory independently of file size. Correct the handoff wording; existing bounded asset sizes are acceptable for this assignment. Do not claim disk streaming unless implemented.

## Freeze/report corrections

The on-disk `scope_closure.json` has six outstanding obligations and omits the PMID 42327275 automated full-text retry present in `actionable_downloads.csv`; the handoff claims seven. Its selection hash also differs from the handoff snapshot. Generate references/counts from the final stored records and link the retry to a stable task ID. Do not silently treat a JATS record with no body as complete full text.

The 3,270 table-region obligations are not all Habermann rows and must not all be linked to `audit:32832598-table-meaning`. Preserve source-specific interpretation tasks and correct the unit label (regions, not rows). Report separately what blocks a particular bundle and what remains a manuscript completion obligation.

The table-semantics config calls GitHub `master` URLs versioned code. Pin the actual inspected commit and file hashes. Treat proposed direction/log-base mappings as supported interpretations only where the source file family and analysis version can be established. Do not propagate a script's direction to unrelated tables. Preserve unknowns rather than deciding biological semantics by preference. The methods/control-cell statement alone does not prove a within-control cell-type comparison filename contradictory: disease contrasts and within-condition cell-type contrasts are different questions.

## Authorized next worker action

Complete the cache fix and record corrections above, then finish these two source fetches in the same pass:

1. Acquire Habermann `aba1972_SM.pdf` (~32.9 MB) through the existing authorized OA path, with a named allowance up to 64 MiB. Parse and inspect the actual relevant legends/methods. Resolve only supported table semantics; if direction remains undocumented, retain the blocker and report exactly what was inspected. No need to ask the user again for this scoped acquisition.
2. Retry primary-source full text for PMID 42327275 through available authorized source routes. Bound attempts using existing retry limits. If no usable body is obtainable, record the source-specific failure and add an actionable user-download request; preserve the abstract's limited status. No need for another permission question or general search.

PMID 41997467 (SOX4) may stay background/relevance-review material; do not make its purchase/manual download a prerequisite merely to fill the fibroblast gap. Missing direct FOSB/TEAD1 literature support remains a reportable limitation, not a requirement to manufacture evidence.

Do not reopen broad discovery. Do not remove incomplete XLSX/table/context states to get a green result; keep them linked to their actual sources. Publish the repaired artifact and one internally consistent freeze proposal, preserving previous artifacts, then stop for review. This assignment authorizes no paid chat calls, P4 implementation, commits, pushes or acceptance checkmarks. It concerns completion of the one manuscript-ready project.
