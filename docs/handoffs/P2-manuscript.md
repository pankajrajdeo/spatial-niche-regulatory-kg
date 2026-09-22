# P2 manuscript-scope extension handoff (P2.11–P2.13)

Status: READY_FOR_REVIEW. The extension is pending lead review, and the manifest says so (`status: pending_lead_review`).

- **Assigned outcome:** plan §8 P2.11–P2.13 and [docs/manuscript_scope.md](../manuscript_scope.md). The four regulatory cases, their seeds and the six primary comparisons go through the existing P2 code. The output is a reconciled manuscript candidate manifest and fair, resumable query batches.
- **Inputs:**
  - accepted ingest `ingest-6f3b10c688adf3b6` (P1, reused and not re-ingested);
  - cached HGNC 2026-09-04 and CollecTRI 2.0 snapshots (0 network requests);
  - the two advisor CSVs (unchanged checksums).
- **Mode:** real project inputs. Fixture results exist only in pytest temporary directories.

**Result:** `data/processed/mcandidates-c278c6625ff7c537/` (schema `p2-manuscript-1`, scope `manuscript-scope-1`).
- `verify manuscript-candidates`: **33/33** checks passed.
- Replay: `REUSED`, 0 network requests.
- Reconciliation: 6 primary comparisons, 16 lineage–TF memberships, 13 unique named TFs (expected 6/16/13).
- Size: 57 candidates, 171 targets, 248 lineage-scoped queries in 13 batches, all `NOT_SEARCHED`.

The accepted AT1 baseline `candidates-ad74f8d35867b7f3` is byte-unchanged and still verifies 29/29.

## Design

- **Scope configuration:** a new versioned file, [configs/manuscript_scope.yaml](../../configs/manuscript_scope.yaml). For each case it lists the exact source cell-type label, the seeds, the primary conditions, lineage-specific retrieval context terms and the draft interpretation (stored as text to assess, never used in scoring, filtering or direction). It also states the expected reconciliation counts (6/16/13) and the schedule (`p2-schedule-1`, 20 queries per batch). Loading fails if the lineages do not reconcile with the stated counts, a cell type is unknown, a condition is unknown, or a seed is duplicated.
  - `configs/project.yaml` (`at1_scope`) and `src/regkg/project_data/` are **unchanged**. Both feed the ingest key, so P1 is reused, not re-ingested.
- **One pipeline** ([src/regkg/analysis/manuscript.py](../../src/regkg/analysis/manuscript.py)). It loops over the lineages with the existing functions:
  - `resolve_symbols` (HGNC) and `parse_collectri`/`ulm_network` (prior);
  - `comparison_vectors` and `concordance_table` (both sign policies);
  - `resolve_seeds`, `select_candidates` (seeds plus ≤ 5 concordance extras per comparison), `project_evidence`, `select_targets` (≤ 3 per candidate);
  - `build_queue` and `query_names`.

  No per-lineage pipeline or copied logic was added.
- **Refactoring for sharing:** `stage.py` gained `shared_resources`, `shared_tables`, `both_policies`, `resource_record` and `execute_stage` (the publish-or-reuse runner). `verify.py` gained `schema_checks`, `shared_checks`, `connectivity_semantics` and `target_selection`. The baseline stage and verifier call the same functions, with identical check names and order.
- **Comparisons** (`lineage_comparisons`):
  - Every supplied signature comparison of a scoped lineage is listed.
  - The 6 manuscript comparisons are `primary_regulatory`. Control for `KRT5neg_KRT17pos` and `Activated_Fibrotic_FBs` is `signature_only_not_primary`, with `regulatory_context_status = none_supplied` (derived from the ingest `contexts.in_chromlinker`).
  - Observation-only comparisons get no concordance, candidates or queries. Their signature and expression observations stay in the ingest artifact and are not copied or dropped.
  - A scoped primary comparison without supplied signatures raises an error; no comparison is invented.
- **Lineage identity:**
  - **Tables:** candidates, targets, concordance and queue carry `cell_type` (and candidates and queue carry `scope_version`). The manuscript schemas extend the baseline schemas by appending columns; the baseline schemas are unchanged.
  - **Candidates:** candidate IDs come from the lineage-qualified `comparison_id`, so TEAD1 has 4 distinct candidates (AT1 Control and IPF, KRT IPF, FB IPF) with one gene identity (HGNC:11714).
  - **Queries:** query IDs include `{cell_type, scope_version}` through a new optional `scope` argument to `build_queue`. The baseline passes none, so its IDs are unchanged.
  - **Context terms:** each lineage's context queries use its own terms.
  - **Shared text:** 24 query rows share text with another lineage (same TF, target and assay terms). They stay separate lineage-scoped rows; an identical request reuses the P3 source cache when executed.
- **Memberships:** `lineage_tf_memberships.parquet` has one row per named lineage–TF pair (16). Each row gives the HGNC ID, primary comparisons, candidate IDs, prior presence, concordance-eligible comparisons, ChromLinker presence, target and query counts, and missing-component reasons.
- **Fair, resumable batches** (`queue.schedule_queries`, `queue.next_pending`):
  - Lineages are interleaved round-robin, keeping each lineage's own order (the baseline interleaving: first query of every TF, seeds before extras, and so on). The first lineage rotates each round, so no lineage has standing priority.
  - `priority = schedule_position`, and `batch_index = ceil(position / 20)`; `in_initial_live_slice` is batch 1. `next_pending(schedule, searched_ids, limit)` resumes a partially executed batch in schedule order.
  - Batches 1–7 carry 5 queries from each lineage. Fibroblast queries end in batch 7 and KRT5−/KRT17+ queries in batch 8, after which AT1 and macrophage queries fill the batches (13 batches in all).
  - No query was executed. Executing batches remains P3 corpus-readiness work under its per-batch budget.
- **Manifest:** `manuscript_manifest.json` holds, per lineage, its comparisons with context status, candidate/seed/extra/eligible/target counts, observation-only entries, queries and first-batch share. It also holds the shared TFs, the batch table and the scientific-boundary notes.

## Changes

- **New:**
  - `configs/manuscript_scope.yaml`
  - `src/regkg/analysis/manuscript.py`: scope functions, stage, manifest, verification
  - `tests/test_manuscript.py`: 8 tests
  - `docs/handoffs/P2-manuscript.md`
- **Modified:**
  - `src/regkg/config.py`: `LineageScopeConfig`, `ExpectedScopeCounts`, `QueryScheduleConfig`, `ManuscriptScopeConfig`, `load_manuscript_scope`
  - `src/regkg/analysis/schemas.py`: `MANUSCRIPT_SCHEMA_VERSION`, `M_*` schemas, `LINEAGE_TF_MEMBERSHIPS`, `MANUSCRIPT_TABLE_SCHEMAS`; baseline schemas unchanged
  - `src/regkg/analysis/queue.py`: optional `scope` in query identity, `schedule_queries`, `next_pending`
  - `src/regkg/analysis/stage.py`: shared helpers and `execute_stage`, with a schema-version parameter
  - `src/regkg/analysis/verify.py`: reusable check functions; `artifact_integrity(…, schema_version)` defaults to the baseline schema
  - `src/regkg/cli.py`: `regkg manuscript-candidates` and `regkg verify manuscript-candidates`
- No dependency, P1 ingestion, P3 literature, plan or review files were changed.

## Actual verification

| Command | Exit/result |
|---|---|
| `.venv/bin/python -m pip check` | 0: `No broken requirements found.` (no dependency change) |
| `.venv/bin/python -m ruff check src tests` | 0: `All checks passed!` |
| `uv lock --check --python .venv/bin/python` | 0: `Resolved 133 packages` |
| `.venv/bin/python -m pytest -q tests/test_manuscript.py` | 0: `8 passed` |
| `.venv/bin/python -m pytest -q` | 0: `155 passed in 10.83s` (147 previous + 8 new) |
| `regkg manuscript-candidates --run ingest-6f3b10c688adf3b6` | 0: `SUCCEEDED mcandidates-c278c6625ff7c537`, execution `manuscript-candidates-20260922T045557Z-64e83b46`, `network_requests: 0` |
| `regkg verify manuscript-candidates --run mcandidates-c278c6625ff7c537` | 0: `PASSED (33/33 checks passed)` |
| Replay of `regkg manuscript-candidates --run ingest-6f3b10c688adf3b6` | 0: `REUSED mcandidates-c278c6625ff7c537`, execution `manuscript-candidates-20260922T045943Z-9f90cc28`, `network_requests: 0` |
| `regkg ingest --config configs/project.yaml` / `verify project-data --run ingest-6f3b10c688adf3b6` | 0: `REUSED ingest-6f3b10c688adf3b6` / `PASSED (56/56)` |
| `regkg verify candidates --run candidates-ad74f8d35867b7f3` (accepted baseline, verified with the refactored code) | 0: `PASSED (29/29)`, same check names |
| `regkg candidates --run ingest-6f3b10c688adf3b6 --cell-type AT1` (baseline reproducibility) | 0: `SUCCEEDED candidates-2780383528325761`, execution `candidates-20260922T050029Z-7cc52ae4`, 0 network requests. The key is new because the analysis code fingerprint changed; **all 12 data files are byte-identical to `candidates-ad74f8d35867b7f3`** (only `manifest.json` differs). `verify candidates`: 29/29 |
| `regkg verify literature --run litretrieval-6a092b32d5f87020` (accepted P3 chain) | 0: `PASSED (18/18)` |
| SHA-256 of every file in all 14 pre-existing `data/processed/` artifacts, before vs after | identical; the only new artifacts are `mcandidates-c278c6625ff7c537` and `candidates-2780383528325761` |

The verifier's manuscript-specific checks:
- **`scope:primary_comparisons_and_missing_contexts`:** comparisons are recomputed from the ingest artifact. There are exactly the 6 expected lineage/condition pairs, plus 2 observation-only comparisons: `KRT5neg_KRT17pos/Control` and `Activated_Fibrotic_FBs/Control`, both `none_supplied`.
- **`scope:lineage_tf_memberships`:** 16 memberships and 13 unique TFs, recomputed. Each seed is a candidate in every primary comparison of its lineage, and each symbol has one HGNC and gene ID. Shared: TEAD1 (AT1, KRT, FB) and KLF5 (AT1, KRT).
- **`candidates:lineage_isolation_and_selection`:**
  - The per-lineage recomputation is identical.
  - Seed reasons appear only for a lineage's own seeds, and every candidate sits in its own lineage's primary comparison.
  - There are ≤ 5 extras per comparison, and concordance exists only for primary comparisons.
- **`targets:bounded_selection`:** targets are bounded, resolved, route-linked and ordered, and each lies in its candidate's lineage and comparison.
- **`queue:lineage_queues_reproducible`:** the rebuild is identical. Every query's candidates come from its own lineage, every lineage–TF candidate is queued, and all rows are `NOT_SEARCHED` with no date restriction.
- **`queue:fair_cross_lineage_schedule`:** positions are 1…248, batches have ≤ 20 queries, and each lineage keeps its order. No lineage with pending queries is missing from any batch.
- **Shared with the baseline:** mapping, indirect-name, provenance, prior, advisor-metadata and concordance-coverage checks, plus `no_connectivity_rank`.

## Run/artifact identity

| Artifact | Key | Notes |
|---|---|---|
| Manuscript candidates (new) | `mcandidates-c278c6625ff7c537` | schema `p2-manuscript-1`; scope file sha256 `72a54d4f04334720…`; code fingerprint `36616dd43057ede0…`; decoupler 2.2.0 |
| Accepted AT1 baseline (preserved) | `candidates-ad74f8d35867b7f3` | unchanged; still used by the accepted P3 chain |
| AT1 baseline reproduced with current code | `candidates-2780383528325761` | byte-identical data files; evidence only, not a replacement |
| Accepted ingest (reused) | `ingest-6f3b10c688adf3b6` | unchanged |

Outputs of `mcandidates-c278c6625ff7c537`:

| File | Rows |
|---|---|
| `comparisons.parquet` | 8 |
| `comparison_vectors.parquet` | 131,244 (6 × 21,874) |
| `concordance.parquet` | 13,008 |
| `candidates.parquet` | 57 |
| `candidate_chromlinker_observations.parquet` | 17,036 |
| `candidate_targets.parquet` | 171 |
| `retrieval_queue.parquet` | 248 |
| `lineage_tf_memberships.parquet` | 16 |
| `gene_mappings.parquet` | 36,610 |
| `prior_interactions.parquet` | 43,175 |
| `seed_publications.parquet` | 110 |

It also contains `coverage_report.json`, `manuscript_manifest.json`, `resources.json` and `manifest.json`.

## Scientific checks

**Primary comparisons.** Each has signatures and both case and reference ChromLinker contexts supplied. All have 32,191 signature genes, of which 21,874 are resolved and finite.

| Lineage | Condition | Candidates | Seeds | Concordance extras (direction, ULM t) |
|---|---|---|---|---|
| AT1 | Control | 10 | 5 | NCOA2 (+, 6.87), TRPS1 (−, −5.73), SREBF2 (+, 5.59), FOXF2 (+, 5.58), SREBF1 (+, 4.37) |
| AT1 | IPF | 10 | 5 | NCOA2 (+, 6.49), MKX (+, 5.90), MECOM (−, −4.77), YAP1 (−, −4.60), WWTR1 (−, −4.31) |
| Alveolar_Macrophages | Control | 11 | 6 | IRF4 (+, 5.22), SMARCA4 (−, −4.94), KLF17 (−, −4.52), ZNF202 (+, 4.51), FOSL2 (+, 4.35) |
| Alveolar_Macrophages | IPF | 11 | 6 | JUND (+, 7.96), FOSL2 (+, 7.73), IRF4 (+, 7.54), ASXL1 (−, −6.87), WT1 (+, 6.74) |
| KRT5neg_KRT17pos | IPF | 8 | 3 | MKX (+, 6.00), IRX1 (+, 5.43), WWTR1 (−, −5.33), KLF4 (−, −5.07), PPARD (−, −4.96) |
| Activated_Fibrotic_FBs | IPF | 7 | 2 | MKX (+, 9.70), HOXA5 (+, 9.49), LMO2 (−, −8.69), SIX1 (+, 8.40), KAT6A (+, 7.96) |

- **Concordance values are descriptive:** these are ULM t-values relating the signed CollecTRI prior to a descriptive pooled contrast. They are not TF activity, causal regulation or DE; directions are concordance signs, and no seed is also a top-5 concordance regulator.
- **Eligible regulators:** under the primary sign policy, 508 regulators are eligible in each comparison. The count is the same because every comparison has the same resolved gene universe.
- **AT1 lineage matches the accepted baseline:** candidate values, target and concordance tables, and query texts and lineage order are identical. The only difference is the stored dtype of `concordance_selection_rank`: other lineages have unranked seeds, so the combined column is stored as float.

**Seeds with sparse prior coverage:**
- TFEC in both macrophage comparisons, and RFX2 in KRT5−/KRT17+ IPF, have 1 observed prior target, below `min_targets = 5`.
- They remain seed candidates with null ULM scores and the reason `prior_target_coverage_below_minimum`. They still have targets from their supplied ChromLinker rows, plus lineage context queries.
- All 13 named TFs resolve exactly to approved HGNC symbols, appear as ChromLinker TFs and have CollecTRI records.

**Other scientific boundaries:**
- **Missing Control regulatory contexts:** KRT5−/KRT17+ and fibroblast Control are observation-only and `none_supplied`, with null context labels. Nothing is inferred from them, and no disease-interaction claim is made.
- **AT1/macrophages:** Control and IPF are separate within-condition comparisons. Nothing tests a disease-by-niche interaction.
- **ChromLinker:** `connectivity_rank` and `interpreted_connectivity_delta` are null for all 57 candidates, and semantics remain `unconfirmed`. Raw values, including zeros, are carried descriptively in `candidate_chromlinker_observations.parquet`.
- **Signatures:** effects remain `effect_niche2_minus_niche1` (descriptive pooled mean-log difference). No p-values, FDR or DEG labels were added.
- **Regulator scope caveat:** each candidate is an individual-gene CollecTRI regulator; DNA binding is not established. This is unchanged from the baseline.

## Limitations and blockers

No blocker. For review:

1. **Retrieval context phrases for the three new lineages are my choice.** They mirror the AT1 design (generic lung terms, cell-specific phrases, fibrosis phrases):
   - macrophage: "alveolar macrophage(s)", "lung/pulmonary/resident macrophage";
   - KRT5−/KRT17+: "aberrant basaloid", "basaloid cells", "KRT5-/KRT17+", "KRT17+ epithelial";
   - fibroblast: "fibroblast(s)", "myofibroblast", "activated/fibrotic/lung fibroblast".

   How each search service tokenizes "KRT5-/KRT17+" is untested. The phrases only select literature and assert nothing. Please confirm or adjust them before P3 executes these queries.
2. **The schedule is unweighted round-robin by lineage.** Each lineage gets an equal share per batch while it has queries, so smaller lineages finish earlier (fibroblasts by batch 7, KRT5−/KRT17+ by batch 8). Weighting by comparisons or TFs was not added. Running all 13 batches (248 queries) exceeds the current P3 per-batch bound of 20 queries, so batch execution and budget belong to P3 corpus readiness.
3. **P3 still consumes the baseline candidate schema.** The literature stages read the baseline `candidates-*` artifact. Running them on `mcandidates-*` (lineage-aware query rows, batches, per-lineage coverage) is the next P3 corpus-readiness adaptation and was not done here.
4. **The AT1 baseline command now publishes a new key** (`candidates-2780383528325761`), because the analysis code fingerprint changed. Its data files are byte-identical to the accepted artifact, which remains the referenced baseline.
5. **`ranking.yaml` still lists `cell_types: [AT1]`.** This is the old `regkg candidates` allowlist, kept for baseline reproducibility. The manuscript stage takes its lineages only from `manuscript_scope.yaml`.
6. **No concordance for observation-only comparisons.** Scoring the KRT5−/KRT17+ and fibroblast Control signatures against the prior would have been possible, but they are not manuscript regulatory comparisons, so this was deliberately left out.
7. **Not done, per scope:** no literature searches, advisor-paper screening, PDF work, P4, LLM calls, Neo4j or push. Plan checkboxes and review documents are unchanged, `.env` is untouched, and nothing was committed.

## Proposed review disposition

- Evidence is provided for P2.11–P2.13.
- If accepted, `mcandidates-c278c6625ff7c537` is the candidate manifest for manuscript-specific P3 retrieval.
- Stopping here for lead review.
