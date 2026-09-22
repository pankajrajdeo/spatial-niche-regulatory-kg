---
title: "Chroma integrations"
description: "Integrate with Chroma using LangChain Python."
source: "https://docs.langchain.com/oss/python/integrations/providers/chroma"
category: "docs"
tags: [docs, integrations, providers, chroma]
---

# Chroma integrations

> Integrate with Chroma using LangChain Python.

> [Chroma](https://docs.trychroma.com/getting-started) is a database for building AI applications with embeddings.

## Installation and setup

**pip**

```bash
pip install langchain-chroma
```

**uv**

```bash
uv add langchain-chroma
```

## VectorStore

There exists a wrapper around Chroma vector databases, allowing you to use it as a vectorstore,
whether for semantic search or example selection.

```python
from langchain_chroma import Chroma
```

For a more detailed walkthrough of the Chroma wrapper, see [this notebook](../vectorstores/chroma.md).

## Retriever

```python
from langchain_classic.retrievers import SelfQueryRetriever
```

***

> [!NOTE]
> [Connect these docs](../../use-these-docs.md) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/providers/chroma.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
