---
title: "max_marginal_relevance_search"
description: "Return docs selected using the maximal marginal relevance."
source: "https://reference.langchain.com/python/langchain-core/vectorstores/base/VectorStore/max_marginal_relevance_search"
category: "reference"
tags: [reference, langchain-core, vectorstores, base, vectorstore, max_marginal_relevance_search]
---

# max_marginal_relevance_search

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/vectorstores/base/VectorStore/max_marginal_relevance_search)

Return docs selected using the maximal marginal relevance.

Maximal marginal relevance optimizes for similarity to query AND diversity
among selected documents.

## Signature

```python
max_marginal_relevance_search(
    self,
    query: str,
    k: int = 4,
    fetch_k: int = 20,
    lambda_mult: float = 0.5,
    **kwargs: Any = {},
) -> list[Document]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `query` | `str` | Yes | Text to look up documents similar to. |
| `k` | `int` | No | Number of `Document` objects to return. (default: `4`) |
| `fetch_k` | `int` | No | Number of `Document` objects to fetch to pass to MMR algorithm. (default: `20`) |
| `lambda_mult` | `float` | No | Number between `0` and `1` that determines the degree of diversity among the results with `0` corresponding to maximum diversity and `1` to minimum diversity. (default: `0.5`) |
| `**kwargs` | `Any` | No | Arguments to pass to the search method. (default: `{}`) |

## Returns

`list[Document]`

List of `Document` objects selected by maximal marginal relevance.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/vectorstores/base.py#L659)
