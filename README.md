# Spatial NicheLinker Regulatory Evidence KG

A biomedical evidence knowledge graph for investigating transcriptional regulation in spatial lung niches, with an initial focus on AT1 cells and idiopathic pulmonary fibrosis.

**Status:** design and execution plan prepared; pipeline implementation has not started. Commands in the plan describe work to implement, not an available application.

## Repository contents

- [plan.md](plan.md): detailed implementation packages, acceptance checklists, provider configuration, and worker handoff instructions.
- [AGENTS.md](AGENTS.md): project coding practices and scientific invariants. `CLAUDE.md` is a relative symlink to this file.
- [Final synthesis](reference/chatgpt/chatgpt_final_synthesis.md): scientific design and project-data interpretation.
- [LangChain synthesis](reference/chatgpt/chatgpt_langchain_synthesis.md): literature-processing and integration design.
- `files/`: supplied ChromLinker scores, pseudobulk expression, pooled niche-expression signatures, neighborhood profiles, and literature seed material. Legacy literature scripts require adaptation before use.
- `reference/`: design conversations, earlier research notes, and a local LangChain documentation mirror. The mirror is reference material, not the application SDK.

## Planned workflow

1. Normalize supplied project data into typed files with stable identities and provenance.
2. Generate AT1 candidates and retrieve a bounded literature corpus.
3. Extract and verify source-grounded findings through structured LLM calls.
4. Review Parquet/JSON artifacts and export a validated CSV graph bundle.
5. Import that bundle into Neo4j in a separate step.
6. Produce reproducible nomination tables and evidence reports.

Working files remain the source of truth. Neo4j is a rebuildable query representation. The pooled niche-expression signatures are descriptive; they are not sample-aware differential-expression results. Predictions, experimental findings, and nominations retain distinct meanings.

Planned LLM integrations are LiteLLM proxy, OpenRouter, and Groq. Optional retrieval embeddings use Ollama or Sentence Transformers. Models are configured as `provider:model_name`; see the plan for environment variables and exact contracts. Credentials belong in local environment settings and must not be committed.

## Starting implementation

Read the plan and assign **P1 only**. Workers submit evidence for lead review before advancing; implementation checkboxes remain unchecked until accepted. Generated artifacts, environments, and caches are ignored by Git. Supplied inputs and reference material are retained with their existing provenance and any applicable upstream terms; this repository does not grant new rights to third-party material.
