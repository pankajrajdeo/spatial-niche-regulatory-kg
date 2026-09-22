---
title: "delete"
description: "Delete by IDs."
source: "https://reference.langchain.com/python/langchain-core/indexing/in_memory/InMemoryDocumentIndex/delete"
category: "reference"
tags: [reference, langchain-core, indexing, in_memory, inmemorydocumentindex, delete]
---

# delete

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/indexing/in_memory/InMemoryDocumentIndex/delete)

Delete by IDs.

## Signature

```python
delete(
    self,
    ids: list[str] | None = None,
    **kwargs: Any = {},
) -> DeleteResponse
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `ids` | `list[str] \| None` | No | List of IDs to delete. (default: `None`) |

## Returns

`DeleteResponse`

A response object that contains the list of IDs that were successfully

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/indexing/in_memory.py#L60)
