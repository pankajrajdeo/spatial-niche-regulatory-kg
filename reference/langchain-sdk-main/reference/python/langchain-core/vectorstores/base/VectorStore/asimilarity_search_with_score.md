---
title: "asimilarity_search_with_score"
description: "Async run similarity search with distance."
source: "https://reference.langchain.com/python/langchain-core/vectorstores/base/VectorStore/asimilarity_search_with_score"
category: "reference"
tags: [reference, langchain-core, vectorstores, base, vectorstore, asimilarity_search_with_score]
---

# asimilarity_search_with_score

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/vectorstores/base/VectorStore/asimilarity_search_with_score)

Async run similarity search with distance.

## Signature

```python
asimilarity_search_with_score(
    self,
    *args: Any = (),
    **kwargs: Any = {},
) -> list[tuple[Document, float]]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `*args` | `Any` | No | Arguments to pass to the search method. (default: `()`) |
| `**kwargs` | `Any` | No | Arguments to pass to the search method. (default: `{}`) |

## Returns

`list[tuple[Document, float]]`

List of tuples of `(doc, similarity_score)`.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/vectorstores/base.py#L431)
