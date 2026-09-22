---
title: "adelete"
description: "Delete by IDs or other criteria. Async variant."
source: "https://reference.langchain.com/python/langchain-core/indexing/base/DocumentIndex/adelete"
category: "reference"
tags: [reference, langchain-core, indexing, base, documentindex, adelete]
---

# adelete

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/indexing/base/DocumentIndex/adelete)

Delete by IDs or other criteria. Async variant.

Calling adelete without any input parameters should raise a ValueError!

## Signature

```python
adelete(
    self,
    ids: list[str] | None = None,
    **kwargs: Any = {},
) -> DeleteResponse
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `ids` | `list[str] \| None` | No | List of IDs to delete. (default: `None`) |
| `**kwargs` | `Any` | No | Additional keyword arguments. This is up to the implementation. For example, can include an option to delete the entire index. (default: `{}`) |

## Returns

`DeleteResponse`

A response object that contains the list of IDs that were

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/indexing/base.py#L581)
