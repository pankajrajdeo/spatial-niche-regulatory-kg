---
title: "get_by_ids"
description: "Get documents by their IDs."
source: "https://reference.langchain.com/python/langchain-core/vectorstores/base/VectorStore/get_by_ids"
category: "reference"
tags: [reference, langchain-core, vectorstores, base, vectorstore, get_by_ids]
---

# get_by_ids

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/vectorstores/base/VectorStore/get_by_ids)

Get documents by their IDs.

The returned documents are expected to have the ID field set to the ID of the
document in the vector store.

Fewer documents may be returned than requested if some IDs are not found or
if there are duplicated IDs.

Users should not assume that the order of the returned documents matches
the order of the input IDs. Instead, users should rely on the ID field of the
returned documents.

This method should **NOT** raise exceptions if no documents are found for
some IDs.

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
| `ids` | `Sequence[str]` | Yes | List of IDs to retrieve. |

## Returns

`list[Document]`

List of `Document` objects.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/vectorstores/base.py#L122)
