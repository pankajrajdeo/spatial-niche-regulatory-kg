---
title: "maximal_marginal_relevance"
description: "Calculate maximal marginal relevance."
source: "https://reference.langchain.com/python/langchain-core/vectorstores/in_memory/maximal_marginal_relevance"
category: "reference"
tags: [reference, langchain-core, vectorstores, in_memory, maximal_marginal_relevance]
---

# maximal_marginal_relevance

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/vectorstores/utils/maximal_marginal_relevance)

Calculate maximal marginal relevance.

## Signature

```python
maximal_marginal_relevance(
    query_embedding: npt.NDArray[np.floating],
    embedding_list: list[list[float]],
    lambda_mult: float = 0.5,
    k: int = 4,
) -> list[int]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `query_embedding` | `npt.NDArray[np.floating]` | Yes | The query embedding. |
| `embedding_list` | `list[list[float]]` | Yes | A list of embeddings. |
| `lambda_mult` | `float` | No | The lambda parameter for MMR. (default: `0.5`) |
| `k` | `int` | No | The number of embeddings to return. (default: `4`) |

## Returns

`list[int]`

A list of indices of the embeddings to return.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/vectorstores/utils.py#L112)
