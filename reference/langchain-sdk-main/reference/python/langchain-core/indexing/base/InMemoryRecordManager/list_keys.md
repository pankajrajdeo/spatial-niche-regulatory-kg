---
title: "list_keys"
description: "List records in the database based on the provided filters."
source: "https://reference.langchain.com/python/langchain-core/indexing/base/InMemoryRecordManager/list_keys"
category: "reference"
tags: [reference, langchain-core, indexing, base, inmemoryrecordmanager, list_keys]
---

# list_keys

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/indexing/base/InMemoryRecordManager/list_keys)

List records in the database based on the provided filters.

## Signature

```python
list_keys(
    self,
    *,
    before: float | None = None,
    after: float | None = None,
    group_ids: Sequence[str] | None = None,
    limit: int | None = None,
) -> list[str]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `before` | `float \| None` | No | Filter to list records updated before this time. (default: `None`) |
| `after` | `float \| None` | No | Filter to list records updated after this time. (default: `None`) |
| `group_ids` | `Sequence[str] \| None` | No | Filter to list records with specific group IDs. (default: `None`) |
| `limit` | `int \| None` | No | optional limit on the number of records to return. (default: `None`) |

## Returns

`list[str]`

A list of keys for the matching records.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/indexing/base.py#L352)
