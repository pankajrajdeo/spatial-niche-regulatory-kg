---
title: "StructuredQuery"
description: "Structured query."
source: "https://reference.langchain.com/python/langchain-core/structured_query/StructuredQuery"
category: "reference"
tags: [reference, langchain-core, structured_query, structuredquery]
---

# StructuredQuery

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/structured_query/StructuredQuery)

Structured query.

## Signature

```python
StructuredQuery(
    self,
    query: str,
    filter: FilterDirective | None,
    limit: int | None = None,
    **kwargs: Any = {},
)
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `query` | `str` | Yes | The query string. |
| `filter` | `FilterDirective \| None` | Yes | The filtering expression. |
| `limit` | `int \| None` | No | The limit on the number of results. (default: `None`) |

## Extends

- `Expr`

## Constructors

```python
__init__(
    self,
    query: str,
    filter: FilterDirective | None,
    limit: int | None = None,
    **kwargs: Any = {},
) -> None
```

| Name | Type |
|------|------|
| `query` | `str` |
| `filter` | `FilterDirective \| None` |
| `limit` | `int \| None` |

## Properties

- `query`
- `filter`
- `limit`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/structured_query.py#L176)
