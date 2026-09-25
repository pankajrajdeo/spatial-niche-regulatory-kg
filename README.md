# Spatial NicheLinker Regulatory Evidence KG

A biomedical evidence knowledge graph for investigating transcriptional regulation in spatial lung niches, across the epithelial, immune, and mesenchymal regulatory cases in the Spatial NicheLinker IPF manuscript.

**Continue here:** [current checkpoint](docs/CONTINUE_HERE.md) and [restore/setup instructions](docs/RESUME.md). P4 extraction is paused for architecture review after bounded GLM/Kimi diagnostics; scientific accuracy and manuscript completion remain unvalidated. Code, configuration, tests and the plan are tracked. The Git LFS snapshot under `transfer/` captures the earlier 2026-09-22 migration state, not subsequent runtime results or reference additions. This laptop already has restored sources; follow the restore instructions only when preparing another checkout. P4–P6 remain unfinished.

## Repository contents

- [plan.md](plan.md): detailed implementation packages, acceptance checklists, provider configuration, and worker handoff instructions.
- [AGENTS.md](AGENTS.md): project coding practices and scientific invariants. `CLAUDE.md` is a relative symlink to this file.
- [Final synthesis](reference/chatgpt/chatgpt_final_synthesis.md): scientific design and project-data interpretation.
- [LangChain synthesis](reference/chatgpt/chatgpt_langchain_synthesis.md): literature-processing and integration design.
- `files/`: supplied ChromLinker scores, pseudobulk expression, pooled niche-expression signatures, neighborhood profiles, and literature seed material. Legacy literature scripts require adaptation before use.
- `reference/`: design conversations and earlier research notes. The current local implementation references are `reference/GitHub/openwiki/`, `reference/GitHub/graphrag/`, and `reference/GitHub/langchain-sdk-main/`. These ignored local directories are not included by a code push; the LangChain mirror is documentation, not an installable SDK.

## Planned workflow

1. Normalize supplied project data into typed files with stable identities and provenance.
2. Generate candidates for AT1, alveolar macrophages, KRT5−/KRT17+ epithelial cells, and activated fibrotic fibroblasts; account for all advisor papers and retrieve evidence in bounded batches.
3. Extract and verify source-grounded findings through structured LLM calls.
4. Review Parquet/JSON artifacts and export a validated CSV graph bundle.
5. Import that bundle into Neo4j in a separate step.
6. Produce per-lineage nomination/evidence reports and a manuscript claim-to-evidence matrix, including contradictory findings and coverage gaps.

Working files remain the source of truth. Neo4j is a rebuildable query representation. The pooled niche-expression signatures are descriptive; they are not sample-aware differential-expression results. Predictions, experimental findings, and nominations retain distinct meanings.

LLM adapters support LiteLLM proxy, OpenRouter, and Groq. Optional retrieval embeddings use Ollama or Sentence Transformers. Models are configured as `provider:model_name`; see the plan for environment variables and exact contracts. Credentials belong in local environment settings and must not be committed.

## Local model configuration

Use the existing LiteLLM configuration as described in CONTINUE_HERE.md. The extractor inherits `LLM_MODEL` from the local environment, currently `litellm:prescient.glm-5.3-flash`; [configs/extraction.yaml](configs/extraction.yaml) selects `litellm:prescient.kimi-k3` for verification. Preserve the local `.env`. The OpenRouter defaults below describe the original laptop's example file.

Root [.env.example](.env.example) contains historical OpenRouter defaults and empty credential placeholders. On a fresh clone, copy it to `.env` only if `.env` does not already exist, then explicitly configure the selected provider. LiteLLM uses `LITELLM_BASE_URL` (or `LITELLM_API_BASE`) and `LITELLM_API_KEY`; do not configure another provider merely because it appears in the example.

- LLM: `openrouter:z-ai/glm-5.3-flash`; verification inherits this model by default.
- Embeddings: `ollama:pankajrajdeo/biomed-embeddings-16l-fp16:latest`.
- Ollama endpoint: `http://localhost:11434`.
- OpenRouter: reasoning `low`; prefer Morph, DeepInfra, Together, Baseten, then CoreWeave. Explicit order takes precedence over latency sorting. Same-model fallback is capped at $0.15 input / $0.50 output per million tokens.

Both extraction and verification share these OpenRouter settings when using `openrouter:`. LiteLLM and Groq do not use this host ordering, latency sorting, or other OpenRouter request options.

Environment loading, provider-specific request mapping, LangChain structured extraction/verification, and bounded local evidence assembly are implemented. Live diagnostics and fixture tests are recorded in [the P4 handoff](docs/handoffs/P4.md); they do not establish extraction precision or recall. The current checkpoint governs execution status and subsequent validation.

## Setup

Python 3.12 in a repository-local `.venv`, with dependencies pinned in [pyproject.toml](pyproject.toml) and locked in [uv.lock](uv.lock):

```bash
uv venv .venv --python 3.12 --seed        # --seed provides pip for `pip check`
uv sync --locked --extra test --inexact   # --inexact keeps the seeded pip
.venv/bin/python -m pip check
```

Without uv, `.venv/bin/python -m pip install -e '.[test]'` installs the same pinned direct dependencies (without lock hashes). Later packages add their extras to `pyproject.toml` and `uv.lock` together.

## Project-data ingestion (P1)

```bash
.venv/bin/python -m regkg ingest --config configs/project.yaml
.venv/bin/python -m regkg verify project-data --run <ingest_key printed above>
.venv/bin/python -m regkg verify config   # resolved model selections; key presence only, never values
```

[configs/project.yaml](configs/project.yaml) declares every source path, niche definition (k, resolution, pooled conditions), and curated cell-type display name; unknown fields are rejected. Ingestion reads all supplied quantitative inputs in `files/` (never modified) and publishes one immutable artifact at `data/processed/<ingest_key>/`:

| File | Contents |
|---|---|
| `chromlinker_observations.parquet` | Every supplied TF→gene score, zeros included, with `score_semantics_status=unconfirmed` |
| `expression_observations.parquet` | Every pseudobulk CPTT value as supplied |
| `niche_expression_signatures.parquet` | Descriptive Niche2−Niche1 pooled mean log-expression contrasts; no p-values or DE labels |
| `neighborhood_profiles.parquet` | Reported neighbor mean counts and count/k fractions; unreported categories have no rows |
| `genes.parquet` | One species-qualified local ID per exact source symbol; external IDs unresolved in P1 |
| `contexts.parquet`, `biological_contexts.parquet`, `cell_types.parquet`, `niche_states.parquet` | Context labels, condition-specific contexts, and condition-pooled niche states |
| `sampling_coverage.parquet` | Cell counts per compared niche group; donor counts null (not supplied) |
| `source_inventory.json`, `join_report.json`, `source_audit.md`, `manifest.json` | Hashes, counts, overlaps/unmatched sets, and provenance |

The key is derived from source hashes, result-affecting configuration, ingest code, and schema version. Publication is atomic; an identical rerun reports `REUSED` after checksum verification and never rewrites or duplicates rows. Each attempt writes `data/runs/<execution_id>/execution.json`.

Tests use tiny synthetic inputs only: `.venv/bin/python -m pytest -q`.

## Starting implementation

Read the current checkpoint, manuscript scope and plan §16. Preserve completed P1–P3 work and the paused P4 diagnostics. The P2 manuscript extension is accepted ([review](docs/reviews/P2-manuscript.md)); extraction validation, corpus expansion and manuscript-wide graph integration remain pending. Workers submit evidence for lead review before advancing; implementation checkboxes remain unchecked until accepted. Generated artifacts, environments, and caches are ignored by Git. Supplied inputs and reference material are retained with their existing provenance and any applicable upstream terms; this repository does not grant new rights to third-party material.
