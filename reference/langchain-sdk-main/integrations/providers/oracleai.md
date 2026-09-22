---
title: "OracleAI vector search integrations"
description: "Integrate with OracleAI vector search using LangChain Python."
source: "https://docs.langchain.com/oss/python/integrations/providers/oracleai"
category: "docs"
tags: [docs, integrations, providers, oracleai]
---

# OracleAI vector search integrations

> Integrate with OracleAI vector search using LangChain Python.

Oracle AI Database is built for AI workloads where you query data by **meaning** (semantics), not just keywords. It combines **semantic search over unstructured content** with **relational filtering over business data** in one system—so you can build AI retrieval workflows (like RAG) without introducing a separate vector database and fragmenting data across multiple platforms.

### Why it matters

* **One system for AI + business data:** vectors and operational data live together.
* **Less fragmentation:** fewer moving parts than a separate vector store.
* **Database-grade guarantees:** apply security, transactions, scale, and availability to the same AI workload.

## Prerequisites

Install `langchain-oracledb`. The `python-oracledb` driver will be installed automatically as a dependency.

**pip**

```bash
pip install -qU langchain-oracledb
```

**uv**

```bash
uv add langchain-oracledb
```

## Document loaders

Please check the [usage example](../document_loaders/oracleai.md).

```python
from langchain_oracledb.document_loaders.oracleai import OracleDocLoader
```

## Text splitter

Please check the [usage example](../document_loaders/oracleai.md).

```python
from langchain_oracledb.document_loaders.oracleai import OracleTextSplitter
```

## Embeddings

Please check the [usage example](../embeddings/oracleai.md).

```python
from langchain_oracledb.embeddings.oracleai import OracleEmbeddings
```

## Summary

Please check the [usage example](../tools/oracleai.md).

```python
from langchain_oracledb.utilities.oracleai import OracleSummary
```

## Vector store

Please check the [usage example](../vectorstores/oracle.md).

```python
from langchain_oracledb.vectorstores.oraclevs import OracleVS
```

## End to end demo

Please check the [Oracle AI Vector Search End-to-End Demo Guide](https://github.com/langchain-ai/langchain/blob/v0.3/cookbook/oracleai_demo.ipynb).

## Additional resources

* [GitHub repository](https://github.com/oracle/langchain-oracle) — the official `oracle/langchain-oracle` monorepo, which also ships [`langgraph-oracledb`](https://github.com/oracle/langchain-oracle/tree/main/libs/langgraph-oracledb) (LangGraph checkpointers and stores backed by Oracle Database) and [`@oracle/langchain-oracledb`](https://github.com/oracle/langchain-oracle/tree/main/libs/js/langchain-oracledb) for LangChain.js
* [Samples](https://github.com/oracle/langchain-oracle/tree/main/samples) — a numbered learning path covering chat, agents, tool calling, structured output, embeddings, and RAG with Oracle datastores
* [`langchain-oracledb` package documentation](https://github.com/oracle/langchain-oracle/tree/main/libs/oracledb)

***

> [!NOTE]
> [Connect these docs](../../use-these-docs.md) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/providers/oracleai.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
