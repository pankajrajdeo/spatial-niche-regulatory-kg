---
title: "asimilarity_search_with_relevance_scores"
description: "Async return docs and relevance scores in the range [0, 1]."
source: "https://reference.langchain.com/python/langchain-core/vectorstores/base/VectorStore/asimilarity_search_with_relevance_scores"
category: "reference"
tags: [reference, langchain-core, vectorstores, base, vectorstore, asimilarity_search_with_relevance_scores]
---

# asimilarity_search_with_relevance_scores

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/vectorstores/base/VectorStore/asimilarity_search_with_relevance_scores)

Async return docs and relevance scores in the range `[0, 1]`.

`0` is dissimilar, `1` is most similar.

## Signature

```python
asimilarity_search_with_relevance_scores(
    self,
    query: str,
    k: int = 4,
    **kwargs: Any = {},
) -> list[tuple[Document, float]]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `query` | `str` | Yes | Input text. |
| `k` | `int` | No | Number of `Document` objects to return. (default: `4`) |
| `**kwargs` | `Any` | No | Kwargs to be passed to similarity search.  Should include `score_threshold`, an optional floating point value between `0` to `1` to filter the resulting set of retrieved docs. (default: `{}`) |

## Returns

`list[tuple[Document, float]]`

List of tuples of `(doc, similarity_score)`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/vectorstores/base.py#L556)
