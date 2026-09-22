---
title: "Graph RAG integrations"
description: "Integrate with Graph RAG using LangChain Python."
source: "https://docs.langchain.com/oss/python/integrations/providers/graph_rag"
category: "docs"
tags: [docs, integrations, providers, graph_rag]
---

# Graph RAG integrations

> Integrate with Graph RAG using LangChain Python.

## Overview

[Graph RAG](https://datastax.github.io/graph-rag/) provides a retriever interface
that combines **unstructured** similarity search on vectors with **structured**
traversal of metadata properties. This enables graph-based retrieval over **existing**
vector stores.

## Installation and setup

**pip**

```bash
pip install langchain-graph-retriever
```

**uv**

```bash
uv add langchain-graph-retriever
```

## Retrievers

```python
from langchain_graph_retriever import GraphRetriever
```

For more information, see the [Graph RAG Integration Guide](../retrievers/graph_rag.md).

***

> [!NOTE]
> [Connect these docs](../../use-these-docs.md) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/providers/graph_rag.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
