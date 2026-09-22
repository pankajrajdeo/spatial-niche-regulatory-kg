---
title: "InMemoryRecordManager"
description: "An in-memory record manager for testing purposes."
source: "https://reference.langchain.com/python/langchain-core/indexing/base/InMemoryRecordManager"
category: "reference"
tags: [reference, langchain-core, indexing, base, inmemoryrecordmanager]
---

# InMemoryRecordManager

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/indexing/base/InMemoryRecordManager)

An in-memory record manager for testing purposes.

## Signature

```python
InMemoryRecordManager(
    self,
    namespace: str,
)
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `namespace` | `str` | Yes | The namespace for the record manager. |

## Extends

- `RecordManager`

## Constructors

```python
__init__(
    self,
    namespace: str,
) -> None
```

| Name | Type |
|------|------|
| `namespace` | `str` |

## Properties

- `records`
- `namespace`

## Methods

- [`create_schema()`](https://reference.langchain.com/python/langchain-core/indexing/base/InMemoryRecordManager/create_schema)
- [`acreate_schema()`](https://reference.langchain.com/python/langchain-core/indexing/base/InMemoryRecordManager/acreate_schema)
- [`get_time()`](https://reference.langchain.com/python/langchain-core/indexing/base/InMemoryRecordManager/get_time)
- [`aget_time()`](https://reference.langchain.com/python/langchain-core/indexing/base/InMemoryRecordManager/aget_time)
- [`update()`](https://reference.langchain.com/python/langchain-core/indexing/base/InMemoryRecordManager/update)
- [`aupdate()`](https://reference.langchain.com/python/langchain-core/indexing/base/InMemoryRecordManager/aupdate)
- [`exists()`](https://reference.langchain.com/python/langchain-core/indexing/base/InMemoryRecordManager/exists)
- [`aexists()`](https://reference.langchain.com/python/langchain-core/indexing/base/InMemoryRecordManager/aexists)
- [`list_keys()`](https://reference.langchain.com/python/langchain-core/indexing/base/InMemoryRecordManager/list_keys)
- [`alist_keys()`](https://reference.langchain.com/python/langchain-core/indexing/base/InMemoryRecordManager/alist_keys)
- [`delete_keys()`](https://reference.langchain.com/python/langchain-core/indexing/base/InMemoryRecordManager/delete_keys)
- [`adelete_keys()`](https://reference.langchain.com/python/langchain-core/indexing/base/InMemoryRecordManager/adelete_keys)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/indexing/base.py#L240)
