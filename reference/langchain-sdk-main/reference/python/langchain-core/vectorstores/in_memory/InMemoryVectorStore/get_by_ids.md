---
title: "get_by_ids"
description: "Get documents by their ids."
source: "https://reference.langchain.com/python/langchain-core/vectorstores/in_memory/InMemoryVectorStore/get_by_ids"
category: "reference"
tags: [reference, langchain-core, vectorstores, in_memory, inmemoryvectorstore, get_by_ids]
---

# get_by_ids

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/vectorstores/in_memory/InMemoryVectorStore/get_by_ids)

Get documents by their ids.

## Signature

```python
get_by_ids(
    self,
    ids: Sequence[str],
    /,
) -> list[Document]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `ids` | `Sequence[str]` | Yes | The IDs of the documents to get. |

## Returns

`list[Document]`

A list of `Document` objects.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/vectorstores/in_memory.py#L255)
