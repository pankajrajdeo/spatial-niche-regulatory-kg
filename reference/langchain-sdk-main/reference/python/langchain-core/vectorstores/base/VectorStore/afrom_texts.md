---
title: "afrom_texts"
description: "Async return VectorStore initialized from texts and embeddings."
source: "https://reference.langchain.com/python/langchain-core/vectorstores/base/VectorStore/afrom_texts"
category: "reference"
tags: [reference, langchain-core, vectorstores, base, vectorstore, afrom_texts]
---

# afrom_texts

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/vectorstores/base/VectorStore/afrom_texts)

Async return `VectorStore` initialized from texts and embeddings.

## Signature

```python
afrom_texts(
    cls,
    texts: list[str],
    embedding: Embeddings,
    metadatas: list[dict[str, Any]] | None = None,
    *,
    ids: list[str] | None = None,
    **kwargs: Any = {},
) -> Self
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `texts` | `list[str]` | Yes | Texts to add to the `VectorStore`. |
| `embedding` | `Embeddings` | Yes | Embedding function to use. |
| `metadatas` | `list[dict[str, Any]] \| None` | No | Optional list of metadatas associated with the texts. (default: `None`) |
| `ids` | `list[str] \| None` | No | Optional list of IDs associated with the texts. (default: `None`) |
| `**kwargs` | `Any` | No | Additional keyword arguments. (default: `{}`) |

## Returns

`Self`

`VectorStore` initialized from texts and embeddings.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/vectorstores/base.py#L870)
