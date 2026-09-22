# P2 manuscript extension — lead review

Reviewed: 2026-09-22 UTC. Disposition: **ACCEPTED** for plan P2.11–P2.13.
Accepted artifact: `mcandidates-c278c6625ff7c537` (`p2-manuscript-1`).
Scope: `manuscript-scope-1` in [manuscript_scope.yaml](../../configs/manuscript_scope.yaml).
Worker evidence: [handoff](../handoffs/P2-manuscript.md).

## Independently checked

The lead inspected the scope configuration, shared candidate-stage implementation,
lineage comparisons/candidates/memberships, queue scheduler, verifier, and behavioral
tests. There is one shared analysis pipeline with lineage-specific inputs.

- `.venv/bin/python -m pytest -q`: **155 passed**, including eight manuscript tests.
- `.venv/bin/python -m regkg verify manuscript-candidates --run mcandidates-c278c6625ff7c537`:
  **33/33 passed**, including P1 source artifact integrity and resource checksums.
- `.venv/bin/python -m regkg manuscript-candidates --run ingest-6f3b10c688adf3b6`:
  **REUSED**, zero network requests; execution
  `manuscript-candidates-20260922T050637Z-56e49614`.
- `.venv/bin/python -m regkg verify literature --run litretrieval-6a092b32d5f87020`:
  **18/18 passed**, including accepted search/parse/candidate output checksums.
- `pip check`, Ruff (`src tests`), and `uv lock --check --offline`: passed.
- Independent real-artifact comparison: AT1 candidates (20), targets (60), and
  concordance rows (4,336) match the accepted baseline on its existing columns
  (allowing the documented numeric dtype difference). All 12 data outputs of the
  legacy rerun `candidates-2780383528325761` are byte-identical to the accepted
  `candidates-ad74f8d35867b7f3`; the code fingerprint explains its new manifest/key.

## Reconciled scope and outputs

| Lineage | Primary comparisons | Candidates | Named seed records |
|---|---|---:|---:|
| AT1 | Control and IPF | 20 | 10 |
| Alveolar macrophages | Control and IPF | 22 | 12 |
| KRT5-negative/KRT17-positive epithelial cells | IPF | 8 | 3 |
| Activated fibrotic fibroblasts | IPF | 7 | 2 |

Six primary comparisons, 16 lineage–TF memberships, 13 unique named TFs,
57 candidate records, 171 candidate targets, and 248 queries in 13 batches.
All queries remain `NOT_SEARCHED`. Each of the first seven batches contains five
queries from each lineage. Later batches finish the remaining queues; no lineage
has standing priority. TEAD1/KLF5 retain shared gene identities with separate
lineage/comparison nomination contexts.

The two supplied Control signature comparisons for KRT5-negative/KRT17-positive
cells and fibroblasts remain observation-only, with absent ChromLinker contexts
and no fabricated regulatory comparisons. TFEC in both macrophage comparisons
and RFX2 in the epithelial IPF comparison retain seed status despite having only
one observed prior target, below the five-target concordance minimum. Their null
scores and missingness reasons are explicit. ChromLinker connectivity ranks and
interpreted deltas remain null; signature effects remain descriptive.

## Decisions and next boundary

No blocking finding. Accept equal-share rotating lineage scheduling. The new
context phrases are reasonable discovery terms, not assertions of biological
identity or evidence relevance. P3 must check source query translations for
punctuated KRT5/KRT17 phrases and record any versioned normalization before bulk
execution; ordinary word-based alternatives must remain available.

Keep `ranking.yaml` and the old AT1 command as the historical baseline. The new
manuscript command uses `configs/manuscript_scope.yaml`. P3's old-schema consumer
is intentionally not yet adapted; that belongs to the next assignment.

Assign [P3 corpus readiness](../assignments/P3-corpus-readiness.md) using this
accepted manuscript artifact. Account for all 110 advisor publications and all
117 memberships; prepare fair manuscript discovery, full-text/PDF/supplement
parsing, the manual-download list, readiness manifests, and the corpus-wide
inference budget. Carry forward the recorded generic BioC footnote correction.

This accepts candidate preparation, not literature completeness or biological
validation. P3 corpus readiness remains unaccepted. No P4 development or chat
calls until corpus preparation/dispositions are reviewed and the user chooses
the LLM provider/model/key. No credentials, immutable artifacts, source inputs,
or Git staging were changed by this review; no commit or push was made.

The immutable artifact's `pending_lead_review` field describes its publication
state. This review and plan checkmarks record subsequent acceptance; do not edit
that artifact in place.
