---
title: "Qdrant integrations"
description: "Integrate with Qdrant using LangChain Python."
source: "https://docs.langchain.com/oss/python/integrations/providers/qdrant"
category: "docs"
tags: [docs, integrations, providers, qdrant]
---

# Qdrant integrations

> Integrate with Qdrant using LangChain Python.

> [Qdrant](https://qdrant.tech/documentation/) (read: quadrant) is a vector similarity search engine.
> It provides a production-ready service with a convenient API to store, search, and manage
> points - vectors with an additional payload. `Qdrant` is tailored to extended filtering support.

## Installation and setup

Install the Python partner package:

**pip**

```bash
pip install langchain-qdrant
```

**uv**

```bash
uv add langchain-qdrant
```

## Embedding models

### FastEmbedSparse

```python
from langchain_qdrant import FastEmbedSparse
```

### SparseEmbeddings

```python
from langchain_qdrant import SparseEmbeddings
```

## Vector store

There exists a wrapper around `Qdrant` indexes, allowing you to use it as a vectorstore,
whether for semantic search or example selection.

To import this vectorstore:

```python
from langchain_qdrant import QdrantVectorStore
```

For a more detailed walkthrough of the Qdrant wrapper, see [this notebook](../vectorstores/qdrant.md)

***

> [!NOTE]
> [Connect these docs](../../use-these-docs.md) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/providers/qdrant.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
