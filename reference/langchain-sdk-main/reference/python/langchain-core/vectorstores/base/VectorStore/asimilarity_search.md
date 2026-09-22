---
title: "asimilarity_search"
description: "Async return docs most similar to query."
source: "https://reference.langchain.com/python/langchain-core/vectorstores/base/VectorStore/asimilarity_search"
category: "reference"
tags: [reference, langchain-core, vectorstores, base, vectorstore, asimilarity_search]
---

# asimilarity_search

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/vectorstores/base/VectorStore/asimilarity_search)

Async return docs most similar to query.

## Signature

```python
asimilarity_search(
    self,
    query: str,
    k: int = 4,
    **kwargs: Any = {},
) -> list[Document]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `query` | `str` | Yes | Input text. |
| `k` | `int` | No | Number of `Document` objects to return. (default: `4`) |
| `**kwargs` | `Any` | No | Arguments to pass to the search method. (default: `{}`) |

## Returns

`list[Document]`

List of `Document` objects most similar to the query.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/vectorstores/base.py#L606)
