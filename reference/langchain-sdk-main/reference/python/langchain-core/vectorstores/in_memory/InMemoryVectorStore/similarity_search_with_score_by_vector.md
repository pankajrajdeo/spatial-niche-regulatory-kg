---
title: "similarity_search_with_score_by_vector"
description: "Search for the most similar documents to the given embedding."
source: "https://reference.langchain.com/python/langchain-core/vectorstores/in_memory/InMemoryVectorStore/similarity_search_with_score_by_vector"
category: "reference"
tags: [reference, langchain-core, vectorstores, in_memory, inmemoryvectorstore, similarity_search_with_score_by_vector]
---

# similarity_search_with_score_by_vector

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/vectorstores/in_memory/InMemoryVectorStore/similarity_search_with_score_by_vector)

Search for the most similar documents to the given embedding.

## Signature

```python
similarity_search_with_score_by_vector(
    self,
    embedding: list[float],
    k: int = 4,
    filter: Callable[[Document], bool] | None = None,
    **_kwargs: Any = {},
) -> list[tuple[Document, float]]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `embedding` | `list[float]` | Yes | The embedding to search for. |
| `k` | `int` | No | The number of documents to return. (default: `4`) |
| `filter` | `Callable[[Document], bool] \| None` | No | A function to filter the documents. (default: `None`) |

## Returns

`list[tuple[Document, float]]`

A list of tuples of `Document` objects and their similarity scores.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/vectorstores/in_memory.py#L334)
