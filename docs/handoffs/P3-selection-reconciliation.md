# P3 selection reconciliation — 2026-09-22

Status: **source-ready subset verified; P3 corpus freeze NOT accepted**. The current user requested P3 completion and removal of unnecessary storage. No P4 extraction or graph write ran. The remaining asset/interpretation states below are not success states.

## Current result

Current artifact: `data/processed/p3selection-89efefdd214ee16e/`. It consumes the accepted project/manuscript candidates, `litcorpus-68fea35a393fe816`, and completed `litellm_repaired` screening. This is the only retained selection artifact from this pass; superseded drafts were deleted after verification.

- 2,235 screening records remain accounted for; all 110 advisor PMIDs have linked screening dispositions.
- 169 positive screening records became **156 extraction-selected records**, **11 background/commentary records**, and **2 linked preprint/journal study versions**. Original screening decisions and versions remain preserved.
- The WT1 preprint explicitly links its published DOI through the bioRxiv API. The macrophage preprint/journal pair was reviewed against source records: identical ordered seven-author list, matching 116 scRNAseq/119 bulkseq/five scATACseq cohort, and shared CXCL12/CXCR4/ERK and TF-footprinting results. Its abstract changed between versions; both sources remain stored and cannot count as independent studies.
- PMID 40464702 remains selected despite its PubMed Review label: its abstract explicitly reports its own ATAC/RNA/ChIP, CUT&RUN and reporter experiments. Publication type alone was not used as an exclusion gate.
- **115 selected papers have usable main text and at least one ready bundle. 41 need full text or an explicit limited/unavailable-source disposition.** The latter comprise 39 PMID articles and two DOI-only preprints whose official XML endpoint returned HTTP 429 on bounded attempts; these are not diagnosed as paywalled.
- **1,133 ready bundles**, **57 batches** of at most 10 papers/20 bundles/40 scheduled extraction-verification calls. Every scheduled part was checked against its canonical source text, offsets, locator and asset identity; serialized evidence remains at most 6,000 characters/3 parts.
- 3,879 candidate bundles overall: 858 NEEDS_CONTEXT, 1,142 NEEDS_SCREENING_REVIEW, 667 NEEDS_ASSET, 79 NEEDS_PARSE_REPAIR, 1,133 READY_FULL_TEXT. These are overlapping work across papers, not additional paper counts. 986 bounded context investigations are separate preparation records, not completed extraction or guaranteed successful repairs.

## Source work actually performed

Audited the 74 newly selected discovery records with PMIDs through existing adapters, in batches of ten; reused HTTP/source caches. 52 returned structured-full-text routes, but readiness independently required usable body text. Three unlinked bioRxiv preprints received source/version checks; one yielded parsed JATS and two remained rate-limited. No new keyword crawl or repeat screening/embedding run occurred.

Rebuilt screening-selected candidate passages through existing source serialization/readiness checks. Newly acquired papers and selected zero-ready papers contribute all Results/caption candidates without an exact-TF/top-k gate. Methods and other unselected source regions remain in the source frontier; this is not a claim of exhaustive finding extraction.

Fetched 28 specifically referenced supplements (25 initially, one additional 0.54 MB archive, and two targeted size-limit repairs) using existing bounded adapters, then parsed eligible content. No pending `to_acquire` items remain in this evaluated queue. Unresolvable references, image-only content, unsupported legacy Office files, and incomplete table materialization remain explicitly blocked; this does not mean all source gaps are resolved. The full dependency ledger is in `supplement_dependencies.jsonl` and the original corpus frontiers remain authoritative for unsatisfied earlier obligations.

The final size-limit repairs acquired PMID 33320836 `jciinsight-6-144294-s076.zip` (31,883,133 bytes) and PMID 42549055 `MCO2-7-e70887-s001.docx` (62,895,168 bytes), using named 64 MiB allowances rather than increasing the global limit. The DOCX parsed; supported ZIP members parsed while unsupported members remain explicitly NOT_PARSED. Twelve asset-blocked bundles moved to context/attribution review, not automatically to ready. The reconciliation cache key now includes effective corpus configuration.

The local Docling model assets were required by these new PDFs and are now available. Fixed the metadata reader to record the table model's actual configured `v2.3.0` ref instead of looking only for `main`. Existing parse records are preserved; older records with missing model revision are not relabelled retroactively.

## User download list and remaining boundary

- [Actionable article list](../../reports/literature/p3selection-89efefdd214ee16e/manual_downloads.md)
- [CSV download list](../../reports/literature/p3selection-89efefdd214ee16e/manual_downloads.csv)
- [All selected/background/version records](../../data/processed/p3selection-89efefdd214ee16e/paper_selection.csv)
- [Lineage/regulator screening coverage](../../data/processed/p3selection-89efefdd214ee16e/lineage_regulator_coverage.csv)
- [Readiness and blockers](../../data/processed/p3selection-89efefdd214ee16e/extraction_readiness.json)

Priority requests remain PMID 41386231 (alveolar macrophage inflammatory switch), 42555354 (CEBPB–IPO4–FASN–MAVS), and 42327275 (KLF5/basal metaplasia). The expanded list now includes newly selected sources, rather than silently retaining the old three-paper-only list. Save files in the listed `data/papers/manual_inbox/<PMID>/article.pdf` paths; DOI-only papers have distinct publication-ID directories.

P3 cannot honestly be marked fully complete/frozen: requested full texts remain absent, source-specific meaning/attribution and partial/unsupported parsing remain unresolved for blocked evidence. A downloaded/parsed file alone does not resolve those scientific checks. Ready batches are verified preparation artifacts, not authorization to extract incomplete bundles. Preserve manuscript-required missingness, source conflicts and negative findings. No user unavailable/abstract-only disposition has been invented.

## Budget and checks

`inference_budget.json` contains separate extractor/verifier input estimates, repeated source context, verifier extraction-output overhead, retry and reasoning assumptions, and separate assembly scenarios. For current ready bundles: 1,133 extractor calls and up to 1,133 verifier calls before schema checks/retries/assembly. Typical source/prompt input estimates are 3,581,875 extractor tokens and 3,808,475 verifier tokens. Final P4 prompts/tokenizer/output caps still require calibration. LiteLLM proxy dollar cost is unknown; inherited OpenRouter examples are explicitly illustrative and are not selected-provider prices or request settings.

Commands/results:

```text
.venv/bin/python -m regkg.workflows.p3_selection --corpus litcorpus-68fea35a393fe816
  produced current selection; all 1,133 scheduled bundles source-checked
same command again
  REUSED_VERIFIED; no network/model calls and no duplicate artifact
.venv/bin/python -m pytest tests/test_p3_selection.py tests/test_corpus.py -q
  52 passed; two Docling deprecation warnings
.venv/bin/python -m pytest -q
  224 passed; two Docling deprecation warnings; live PDF test no longer skipped
.venv/bin/python -m ruff check src/regkg/workflows/p3_selection.py src/regkg/literature/files.py tests/test_p3_selection.py
  passed
```

All 72 current artifact output hashes verified. `.env` hash unchanged. Logs, source-adapter invocation scripts, and verification receipts are retained under `reports/continuation/p3-final/`; acquisition/parse receipts are under `data/work/corpus-c700d6e584b7bccf/p3-final-*`. Old accepted corpus artifacts were not overwritten. No commit/push.

## Storage

Reverified all 31,110 restored snapshot files, then returned the redundant working-tree transfer archive to its exact Git LFS pointers. Verified local LFS objects remain available. Recovered 3,199,611,824 archive bytes plus 168,690,776 bytes of superseded selection drafts. `git lfs checkout transfer/` can rehydrate the archive if a deliberate restoration is needed; ordinary continuation must not redownload it. Source/parsed/LLM caches remain because they prevent expensive recomputation. The new reports contain references instead of copying full nonselected screening records. No blanket cache pruning or source deletion occurred.
