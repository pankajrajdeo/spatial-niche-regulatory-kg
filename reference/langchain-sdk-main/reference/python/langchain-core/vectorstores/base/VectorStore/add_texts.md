---
title: "add_texts"
description: "Run more texts through the embeddings and add to the VectorStore."
source: "https://reference.langchain.com/python/langchain-core/vectorstores/base/VectorStore/add_texts"
category: "reference"
tags: [reference, langchain-core, vectorstores, base, vectorstore, add_texts]
---

# add_texts

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/vectorstores/base/VectorStore/add_texts)

Run more texts through the embeddings and add to the `VectorStore`.

## Signature

```python
add_texts(
    self,
    texts: Iterable[str],
    metadatas: list[dict[str, Any]] | None = None,
    *,
    ids: list[str] | None = None,
    **kwargs: Any = {},
) -> list[str]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `texts` | `Iterable[str]` | Yes | Iterable of strings to add to the `VectorStore`. |
| `metadatas` | `list[dict[str, Any]] \| None` | No | Optional list of metadatas associated with the texts. (default: `None`) |
| `ids` | `list[str] \| None` | No | Optional list of IDs associated with the texts. (default: `None`) |
| `**kwargs` | `Any` | No | `VectorStore` specific parameters.  One of the kwargs should be `ids` which is a list of ids associated with the texts. (default: `{}`) |

## Returns

`list[str]`

List of IDs from adding the texts into the `VectorStore`.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/vectorstores/base.py#L46)
