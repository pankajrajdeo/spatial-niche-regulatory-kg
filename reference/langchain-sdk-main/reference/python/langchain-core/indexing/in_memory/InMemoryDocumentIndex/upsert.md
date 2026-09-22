---
title: "upsert"
description: "Upsert documents into the index."
source: "https://reference.langchain.com/python/langchain-core/indexing/in_memory/InMemoryDocumentIndex/upsert"
category: "reference"
tags: [reference, langchain-core, indexing, in_memory, inmemorydocumentindex, upsert]
---

# upsert

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/indexing/in_memory/InMemoryDocumentIndex/upsert)

Upsert documents into the index.

## Signature

```python
upsert(
    self,
    items: Sequence[Document],
    /,
    **kwargs: Any = {},
) -> UpsertResponse
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `items` | `Sequence[Document]` | Yes | Sequence of documents to add to the index. |
| `**kwargs` | `Any` | No | Additional keyword arguments. (default: `{}`) |

## Returns

`UpsertResponse`

A response object that contains the list of IDs that were

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/indexing/in_memory.py#L31)
