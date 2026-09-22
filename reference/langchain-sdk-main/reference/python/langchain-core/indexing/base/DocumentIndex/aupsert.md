---
title: "aupsert"
description: "Add or update documents in the VectorStore. Async version of upsert."
source: "https://reference.langchain.com/python/langchain-core/indexing/base/DocumentIndex/aupsert"
category: "reference"
tags: [reference, langchain-core, indexing, base, documentindex, aupsert]
---

# aupsert

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/indexing/base/DocumentIndex/aupsert)

Add or update documents in the `VectorStore`. Async version of `upsert`.

The upsert functionality should utilize the ID field of the item
if it is provided. If the ID is not provided, the upsert method is free
to generate an ID for the item.

When an ID is specified and the item already exists in the `VectorStore`,
the upsert method should update the item with the new data. If the item
does not exist, the upsert method should add the item to the `VectorStore`.

## Signature

```python
aupsert(
    self,
    items: Sequence[Document],
    /,
    **kwargs: Any = {},
) -> UpsertResponse
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `items` | `Sequence[Document]` | Yes | Sequence of documents to add to the `VectorStore`. |
| `**kwargs` | `Any` | No | Additional keyword arguments. (default: `{}`) |

## Returns

`UpsertResponse`

A response object that contains the list of IDs that were

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/indexing/base.py#L535)
