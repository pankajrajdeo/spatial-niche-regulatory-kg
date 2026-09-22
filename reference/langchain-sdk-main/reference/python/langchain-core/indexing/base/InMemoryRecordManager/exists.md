---
title: "exists"
description: "Check if the provided keys exist in the database."
source: "https://reference.langchain.com/python/langchain-core/indexing/base/InMemoryRecordManager/exists"
category: "reference"
tags: [reference, langchain-core, indexing, base, inmemoryrecordmanager, exists]
---

# exists

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/indexing/base/InMemoryRecordManager/exists)

Check if the provided keys exist in the database.

## Signature

```python
exists(
    self,
    keys: Sequence[str],
) -> list[bool]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `keys` | `Sequence[str]` | Yes | A list of keys to check. |

## Returns

`list[bool]`

A list of boolean values indicating the existence of each key.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/indexing/base.py#L330)
