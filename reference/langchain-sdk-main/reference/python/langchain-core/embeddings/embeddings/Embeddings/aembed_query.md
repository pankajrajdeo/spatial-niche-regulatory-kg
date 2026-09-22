---
title: "aembed_query"
description: "Asynchronous Embed query text."
source: "https://reference.langchain.com/python/langchain-core/embeddings/embeddings/Embeddings/aembed_query"
category: "reference"
tags: [reference, langchain-core, embeddings, aembed_query]
---

# aembed_query

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/embeddings/embeddings/Embeddings/aembed_query)

Asynchronous Embed query text.

## Signature

```python
aembed_query(
    self,
    text: str,
) -> list[float]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `text` | `str` | Yes | Text to embed. |

## Returns

`list[float]`

Embedding.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/embeddings/embeddings.py#L69)
