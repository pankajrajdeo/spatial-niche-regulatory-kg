---
title: "BaseSerialized"
description: "Base class for serialized objects."
source: "https://reference.langchain.com/python/langchain-core/load/serializable/BaseSerialized"
category: "reference"
tags: [reference, langchain-core, load, serializable, baseserialized]
---

# BaseSerialized

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/load/serializable/BaseSerialized)

Base class for serialized objects.

## Signature

```python
BaseSerialized()
```

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    lc: int,
    id: list[str],
    name: NotRequired[str],
    graph: NotRequired[dict[str, Any]],
)
```

| Name | Type |
|------|------|
| `lc` | `int` |
| `id` | `list[str]` |
| `name` | `NotRequired[str]` |
| `graph` | `NotRequired[dict[str, Any]]` |

## Properties

- `lc`
- `id`
- `name`
- `graph`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/load/serializable.py#L21)
