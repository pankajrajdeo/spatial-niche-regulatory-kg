---
title: "Parallel integrations"
description: "Integrate with Parallel using LangChain Python."
source: "https://docs.langchain.com/oss/python/integrations/providers/parallel"
category: "docs"
tags: [docs, integrations, providers, parallel]
---

# Parallel integrations

> Integrate with Parallel using LangChain Python.

This page covers all LangChain integrations with [Parallel](https://platform.parallel.ai/).

## Installation and setup

The `Parallel` integration lives in its own [partner package](https://pypi.org/project/langchain-parallel/):

**pip**

```bash
pip install -U langchain-parallel
```

**uv**

```bash
uv add langchain-parallel
```

Set the `PARALLEL_API_KEY` environment variable to your Parallel API key. Sign up at [platform.parallel.ai](https://platform.parallel.ai) to obtain one.

## Chat models

#### [ChatParallel](../chat/parallel.md)
OpenAI-compatible chat model with optional web research and per-field citations on the research tiers.

## Tools

#### [ParallelSearchTool](../tools/parallel_search.md)
Search the web and get structured, LLM-optimized excerpts back.

#### [ParallelExtractTool](../tools/parallel_extract.md)
Extract clean markdown content from a list of URLs.

#### [ParallelFindAllTool](../tools/parallel_findall.md)
Discover entities that satisfy a set of boolean match conditions.

#### [Task API](../tools/parallel_task.md)
Run research-grade tasks: single ad-hoc, deep research, batch enrichment. `ParallelTaskRunTool`, `ParallelDeepResearch`, `ParallelTaskGroup`, `ParallelEnrichment`.

#### [ParallelMonitor](../tools/parallel_monitor.md)
Schedule a query on a recurring cadence and receive events when relevant new content shows up.

## Retrievers

#### [ParallelSearchRetriever](../retrievers/parallel.md)
`BaseRetriever` over Parallel Search. Returns `list[Document]` for drop-in use in any RAG pipeline.

***

> [!NOTE]
> [Connect these docs](../../use-these-docs.md) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/providers/parallel.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
