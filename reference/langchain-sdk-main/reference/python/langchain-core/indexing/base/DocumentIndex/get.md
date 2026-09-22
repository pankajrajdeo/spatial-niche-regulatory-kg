---
title: "get"
description: "Get documents by id."
source: "https://reference.langchain.com/python/langchain-core/indexing/base/DocumentIndex/get"
category: "reference"
tags: [reference, langchain-core, indexing, base, documentindex, get]
---

# get

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/indexing/base/DocumentIndex/get)

Get documents by id.

Fewer documents may be returned than requested if some IDs are not found or
if there are duplicated IDs.

Users should not assume that the order of the returned documents matches
the order of the input IDs. Instead, users should rely on the ID field of the
returned documents.

This method should **NOT** raise exceptions if no documents are found for
some IDs.

## Signature

```python
get(
    self,
    ids: Sequence[str],
    /,
    **kwargs: Any = {},
) -> list[Document]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `ids` | `Sequence[str]` | Yes | List of IDs to get. |
| `**kwargs` | `Any` | No | Additional keyword arguments. These are up to the implementation. (default: `{}`) |

## Returns

`list[Document]`

List of documents that were found.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/indexing/base.py#L604)
