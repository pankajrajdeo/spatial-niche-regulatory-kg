---
title: "search"
description: "Return docs most similar to query using a specified search type."
source: "https://reference.langchain.com/python/langchain-core/vectorstores/base/VectorStore/search"
category: "reference"
tags: [reference, langchain-core, vectorstores, base, vectorstore, search]
---

# search

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/vectorstores/base/VectorStore/search)

Return docs most similar to query using a specified search type.

## Signature

```python
search(
    self,
    query: str,
    search_type: str,
    **kwargs: Any = {},
) -> list[Document]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `query` | `str` | Yes | Input text. |
| `search_type` | `str` | Yes | Type of search to perform.  Can be `'similarity'`, `'mmr'`, or `'similarity_score_threshold'`. |
| `**kwargs` | `Any` | No | Arguments to pass to the search method. (default: `{}`) |

## Returns

`list[Document]`

List of `Document` objects most similar to the query.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/vectorstores/base.py#L293)
