---
title: "Comparison"
description: "Comparison to a value."
source: "https://reference.langchain.com/python/langchain-core/structured_query/Comparison"
category: "reference"
tags: [reference, langchain-core, structured_query, comparison]
---

# Comparison

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/structured_query/Comparison)

Comparison to a value.

## Signature

```python
Comparison(
    self,
    comparator: Comparator,
    attribute: str,
    value: Any,
    **kwargs: Any = {},
)
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `comparator` | `Comparator` | Yes | The comparator to use. |
| `attribute` | `str` | Yes | The attribute to compare. |
| `value` | `Any` | Yes | The value to compare to. |

## Extends

- `FilterDirective`

## Constructors

```python
__init__(
    self,
    comparator: Comparator,
    attribute: str,
    value: Any,
    **kwargs: Any = {},
) -> None
```

| Name | Type |
|------|------|
| `comparator` | `Comparator` |
| `attribute` | `str` |
| `value` | `Any` |

## Properties

- `comparator`
- `attribute`
- `value`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/structured_query.py#L126)
