# LiteLLM continuation — 2026-09-22

Status: SCREENING EXECUTION AND FAILURE REPAIR COMPLETE. Final extraction/source-readiness acceptance remains pending. No P4 extraction or graph import has run.

## Latest repair result (supersedes the historical running status below)

- Initial run finished with 2,161 screened records, 16 partial, 57 unsuccessful, and one missing parsed document. Its 2,888 calls and original reports remain preserved.
- Audited all 74 invalid windows: mostly paraphrased quotations/wrong passage IDs, plus invalid JSON, wrong enum values, overlong missing-information arrays, and unsupported positive decisions without citations.
- Added `--repair-failed`: reads valid original caches unchanged and writes bounded repairs separately. Full JSON schema and specific diagnostics replace the ineffective generic retry instruction. All prior failure responses remain available.
- First repair: 63 of 74 windows validated. Five further windows were recovered without new calls by correcting a uniquely identifiable exact-quote passage pointer. Quotes were never rewritten, fuzzy-matched, or accepted when absent from the shown text; ambiguous pointers remain invalid.
- Final six windows passed after targeted instructions to preserve literal HTML/XML formatting and acronym parentheses in quotes. Separate `repairs-v2` caches link the first repair by SHA-256. These were new validated model responses, not relaxed quote checks.
- PMID 29446906 had no parsed article inventory but did have cached Europe PMC metadata. That source was screened with missing main text explicitly declared; no acquisition or parser rerun occurred.
- Final result: **2,235/2,235 unique records screened; zero invalid or unread windows; 169 provisional extraction selections**. This does not mean every paper has full text or resolved biological context.
- **106 additional model calls**, 2,994 cumulative calls in the full-run namespace. Dollar cost remains unknown; existing unknown-usage reservations remain conservative.
- All **2,579 base window-cache checksums** in the pre-repair audit (including the new metadata fallback) were unchanged. The original 2,504 successful full-run windows were not sent back to the model. `.env` remained unchanged.
- Identical full-pool replay passed with **zero additional model calls** and 2,235 screened records.
- Validation: **218 tests passed, 1 skipped**; targeted suite **53 passed**; Ruff passed. The skip concerns unavailable external PDF model assets, not screening.

Artifacts:

- `reports/literature/litcorpus-68fea35a393fe816/screening_summary_litellm_repaired.json`
- `reports/literature/litcorpus-68fea35a393fe816/screening_records_litellm_repaired.jsonl`
- `reports/literature/litcorpus-68fea35a393fe816/screening_ledger_litellm_repaired.csv`
- `reports/continuation/screening_failure_audit.json`
- `reports/continuation/screening_repair_verification.json`
- `data/work/corpus-c700d6e584b7bccf/screening/56f1a75cc8ed9a6a/{repairs-v1,repairs-v1/recovered,repairs-v2}/`

Repair command:

```bash
.venv/bin/python -u -m regkg literature screen-run --run mcandidates-c278c6625ff7c537 --corpus litcorpus-68fea35a393fe816 --pool all --repair-failed --label litellm_repaired
```

Remaining: review provisional biological selections, reconcile candidate regions with source/readiness gates, and create an accurate extraction plan before P4. Do not relabel screening as extracted/verified KG evidence.

The sections below preserve the earlier setup/run history; their running status and pending failure counts are superseded by this result.

## Verified restoration and configuration

- Installed Git LFS 3.8.0 from the official darwin-arm64 release after matching its published SHA-256; initialized only this repository and ran `git lfs pull`.
- `uv venv .venv --python 3.12 --seed`; `uv sync --locked --inexact --extra test --extra analysis --extra chat --extra embeddings-ollama --extra pdf` installed the locked environment. No model weights were downloaded and no acquisition, source parsing, or embedding pipeline was restarted.
- `.venv/bin/python scripts/restore_snapshot.py`: **31,110 files verified**. Restore streams verified archive chunks instead of making an extra multi-GB archive copy; a synthetic cross-chunk tar test passed.
- Latest `litcorpus-68fea35a393fe816` manifest: **92 output checksums verified**. Original ingestion, manuscript candidates, and all 96 OpenRouter screening cache JSON records are present.
- User-owned `.env` is unchanged (privately checked by hash). User's `.gitignore` addition for `certs/` is preserved.
- Selected model: `litellm:prescient.glm-5.3-flash`. `LITELLM_API_BASE` now aliases `LITELLM_BASE_URL`, respecting process-over-file precedence across spellings. No credentials are recorded here.
- User explicitly confirmed unlimited GLM quota and superseded the old OpenRouter $1/700-call allowance. The finite local corpus and two-attempt/window policy bound the work; a 10,000-call cumulative runaway guard remains. Proxy dollar cost stays unknown.

## Live validation and current run

1. LiteLLM transport JSON test passed: 27 input / 224 output tokens, including 218 reasoning tokens; dollar cost unknown.
2. PMID 41116170 at the old 5,000-token output limit failed both attempts by hitting the length limit: 19,384 input / 10,000 output tokens total. Neither output became an accepted screening decision. Cache `b32b2102b8bb3af4` and `screening_summary_litellm_validation.json` preserve this failure. The old CLI incorrectly printed SUCCEEDED despite unread windows; the CLI status has since been corrected to PARTIAL in such cases.
3. Same paper with 12,000-token maximum passed source-quote checks in one call: 9,684 input / 7,743 output tokens, unknown dollars. Cache `805955098ba49296`; report `screening_summary_litellm_validation_12k.json`. This is paper selection, not a verified scientific finding.
4. User asked about disabling reasoning. Official Z.ai documentation says GLM-5.3-Flash forces thinking: https://docs.z.ai/guides/capabilities/thinking-mode . A separate proxy test with `reasoning_effort=low` returned valid JSON, 28 input / 7 output tokens (1 reasoning token). LiteLLM-specific low effort is now configured; it does not inherit OpenRouter routing/reasoning fields.
5. **Full screening is running**, four concurrent workers, cache namespace **`56f1a75cc8ed9a6a`**. New settings intentionally create a new namespace; previous OpenRouter/default-reasoning results retain their original provenance. Do not relabel or delete those caches.

Exact running command:

```bash
.venv/bin/python -u -m regkg literature screen-run --run mcandidates-c278c6625ff7c537 --corpus litcorpus-68fea35a393fe816 --pool all --label litellm_full > reports/continuation/screening-live.log 2>&1
```

Check the running process and these artifacts before restarting:

- `reports/continuation/screening-live.log`
- `data/work/corpus-c700d6e584b7bccf/screening/56f1a75cc8ed9a6a/budget.json`
- Same directory: atomic per-window JSON results and incrementally flushed `papers-*.jsonl` journals.
- Final reports, once the command finishes: `reports/literature/litcorpus-68fea35a393fe816/screening_{summary,ledger,records}_litellm_full.{json,csv,jsonl}` (matching extension per artifact).

A project-local process lock prevents concurrent screening invocations. Do not start a duplicate run. Interrupted reservations remain conservatively accounted; valid windows replay from cache. Failed windows remain explicit needs-review states, not silent exclusions. Existing failure records are not automatically retried on replay.

## Actual pool and call counts

- 452 acquired publications: 247 need one window, 123 two, 34 three, 36 four, 10 five, one six, and one has no parsed document. **795 windows**.
- 1,783 additional discovery records, all matched to existing cached metadata, **one window each**. One DOI-only record in the previous 1,784 count was source-linked to acquired PMID 42327275 and is now deduplicated.
- Total: **2,235 unique publications/records**, **2,578 initial window calls**, at most **5,156 attempts** if every window needed its one retry. Validation calls/settings are separate.
- Acquired section-group count ranges 1–13 for readable papers; those groups are packed into windows, not one call per section. Main text is available for 267; 184 have abstract/metadata-level inputs; one lacks a parsed document. Availability does not prove full-text completeness.
- Original dry-run output at `reports/continuation/screening_dry_run_litellm.json` predates the increased output cap and low-effort setting. Its discovery output-token estimate is inherited and too low; regenerate accurate token estimates before using it as a budget report. Window counts above were independently measured after fixing section splitting and discovery deduplication.

## Changes and checks

Changed: `scripts/restore_snapshot.py`, `src/regkg/config.py`, `src/regkg/cli.py`, `src/regkg/workflows/screening.py`, `src/regkg/literature/screening_llm.py`, `configs/literature.yaml`, `.env.example`, `tests/test_screening.py`, `tests/test_contracts.py`.

- Atomic reservation/settlement covers concurrent calls and every repair, with persistent crash accounting and explicit unknown token/cost reporting.
- Added actual discovery-metadata execution using frozen search responses; no new crawl.
- Removed the previous 1,800-character manuscript-scope truncation. All four lineage names/seeds/contexts are supplied, without draft interpretations or expected validation answers.
- Oversized sections split by passage; oversized passages use exact source-text slices. Every retained passage is represented. Bibliography and bounded table previews retain explicit omission policy.
- Source identity now hashes text and declared missingness. Ungrounded positive decisions fail validation; unassessed questions remain uncertain. Abstract-only negative decisions cannot exclude unseen full text.
- Reports no longer call runs with unread papers/windows successful.
- `.venv/bin/python -m pip check`: passed.
- Full suite: **216 passed, 1 skipped** in 45.52 seconds. PDF live-model test skipped because external model assets are absent; not claimed as passed.
- Focused suite after low-effort adapter change: **51 passed**. Ruff import ordering was corrected; rerun lint after subsequent edits.

## Remaining work

Let the active run finish; inspect invalid/unread outputs and a small stratified inclusion/exclusion sample, preserve negatives/context uncertainty, produce a reconciled selection ledger and accurate extraction dry-run budget, and rebuild newly selected candidate regions through existing source/readiness gates. The full screening output is not yet available and is not acceptance.

P4 implementation/tested extraction pipeline, explicit full-extraction run allowance, evidence assembly, offline graph export, separate Neo4j import, and manuscript reports remain pending. Do not claim a completed KG or restart old acquisition/parsing/embedding work. Three prior manual-download needs remain recorded in the restored actionable report. Preserve source uncertainty and the user's existing environment.
