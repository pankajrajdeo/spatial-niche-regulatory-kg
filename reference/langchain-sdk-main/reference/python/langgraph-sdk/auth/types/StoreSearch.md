---
title: "StoreSearch"
description: "Operation to search for items within a specified namespace hierarchy."
source: "https://reference.langchain.com/python/langgraph-sdk/auth/types/StoreSearch"
category: "reference"
tags: [reference, langgraph-sdk, auth, types, storesearch]
---

# StoreSearch

> **Class** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/auth/types/StoreSearch)

Operation to search for items within a specified namespace hierarchy.

This dict is mutable — auth handlers can modify `namespace` to enforce
access scoping (e.g., prepending the user's identity).

## Signature

```python
StoreSearch()
```

## Extends

- `typing.TypedDict`

## Constructors

```python
__init__(
    namespace: tuple[str, ...],
    filter: dict[str, typing.Any] | None,
    limit: int,
    offset: int,
    query: str | None,
)
```

| Name | Type |
|------|------|
| `namespace` | `tuple[str, ...]` |
| `filter` | `dict[str, typing.Any] \| None` |
| `limit` | `int` |
| `offset` | `int` |
| `query` | `str \| None` |

## Properties

- `namespace`
- `filter`
- `limit`
- `offset`
- `query`

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/d5f4b2aa960940effc8430165ab3604038e817af/libs/sdk-py/langgraph_sdk/auth/types.py#L879)
