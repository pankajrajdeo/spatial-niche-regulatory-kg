---
title: "RecordManager"
description: "Abstract base class representing the interface for a record manager."
source: "https://reference.langchain.com/python/langchain-core/indexing/base/RecordManager"
category: "reference"
tags: [reference, langchain-core, indexing, base, recordmanager]
---

# RecordManager

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/indexing/base/RecordManager)

Abstract base class representing the interface for a record manager.

The record manager abstraction is used by the langchain indexing API.

The record manager keeps track of which documents have been
written into a `VectorStore` and when they were written.

The indexing API computes hashes for each document and stores the hash
together with the write time and the source id in the record manager.

On subsequent indexing runs, the indexing API can check the record manager
to determine which documents have already been indexed and which have not.

This allows the indexing API to avoid re-indexing documents that have
already been indexed, and to only index new documents.

The main benefit of this abstraction is that it works across many vectorstores.
To be supported, a `VectorStore` needs to only support the ability to add and
delete documents by ID. Using the record manager, the indexing API will
be able to delete outdated documents and avoid redundant indexing of documents
that have already been indexed.

The main constraints of this abstraction are:

1. It relies on the time-stamps to determine which documents have been
    indexed and which have not. This means that the time-stamps must be
    monotonically increasing. The timestamp should be the timestamp
    as measured by the server to minimize issues.
2. The record manager is currently implemented separately from the
    vectorstore, which means that the overall system becomes distributed
    and may create issues with consistency. For example, writing to
    record manager succeeds, but corresponding writing to `VectorStore` fails.

## Signature

```python
RecordManager(
    self,
    namespace: str,
)
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `namespace` | `str` | Yes | The namespace for the record manager. |

## Extends

- `ABC`

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

- `namespace`

## Methods

- [`create_schema()`](https://reference.langchain.com/python/langchain-core/indexing/base/RecordManager/create_schema)
- [`acreate_schema()`](https://reference.langchain.com/python/langchain-core/indexing/base/RecordManager/acreate_schema)
- [`get_time()`](https://reference.langchain.com/python/langchain-core/indexing/base/RecordManager/get_time)
- [`aget_time()`](https://reference.langchain.com/python/langchain-core/indexing/base/RecordManager/aget_time)
- [`update()`](https://reference.langchain.com/python/langchain-core/indexing/base/RecordManager/update)
- [`aupdate()`](https://reference.langchain.com/python/langchain-core/indexing/base/RecordManager/aupdate)
- [`exists()`](https://reference.langchain.com/python/langchain-core/indexing/base/RecordManager/exists)
- [`aexists()`](https://reference.langchain.com/python/langchain-core/indexing/base/RecordManager/aexists)
- [`list_keys()`](https://reference.langchain.com/python/langchain-core/indexing/base/RecordManager/list_keys)
- [`alist_keys()`](https://reference.langchain.com/python/langchain-core/indexing/base/RecordManager/alist_keys)
- [`delete_keys()`](https://reference.langchain.com/python/langchain-core/indexing/base/RecordManager/delete_keys)
- [`adelete_keys()`](https://reference.langchain.com/python/langchain-core/indexing/base/RecordManager/adelete_keys)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/indexing/base.py#L22)
