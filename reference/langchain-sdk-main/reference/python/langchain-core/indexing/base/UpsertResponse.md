---
title: "UpsertResponse"
description: "A generic response for upsert operations."
source: "https://reference.langchain.com/python/langchain-core/indexing/base/UpsertResponse"
category: "reference"
tags: [reference, langchain-core, indexing, base, upsertresponse]
---

# UpsertResponse

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/indexing/base/UpsertResponse)

A generic response for upsert operations.

The upsert response will be used by abstractions that implement an upsert
operation for content that can be upserted by ID.

Upsert APIs that accept inputs with IDs and generate IDs internally
will return a response that includes the IDs that succeeded and the IDs
that failed.

If there are no failures, the failed list will be empty, and the order
of the IDs in the succeeded list will match the order of the input documents.

If there are failures, the response becomes ill defined, and a user of the API
cannot determine which generated ID corresponds to which input document.

It is recommended for users explicitly attach the IDs to the items being
indexed to avoid this issue.

## Signature

```python
UpsertResponse()
```

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    succeeded: list[str],
    failed: list[str],
)
```

| Name | Type |
|------|------|
| `succeeded` | `list[str]` |
| `failed` | `list[str]` |

## Properties

- `succeeded`
- `failed`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/indexing/base.py#L434)
