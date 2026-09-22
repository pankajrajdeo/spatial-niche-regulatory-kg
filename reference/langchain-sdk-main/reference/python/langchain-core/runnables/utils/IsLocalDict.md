---
title: "IsLocalDict"
description: "Check if a name is a local dict."
source: "https://reference.langchain.com/python/langchain-core/runnables/utils/IsLocalDict"
category: "reference"
tags: [reference, langchain-core, runnables, utils, islocaldict]
---

# IsLocalDict

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/utils/IsLocalDict)

Check if a name is a local dict.

## Signature

```python
IsLocalDict(
    self,
    name: str,
    keys: set[str],
)
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `name` | `str` | Yes | The name to check. |
| `keys` | `set[str]` | Yes | The keys to populate. |

## Extends

- `ast.NodeVisitor`

## Constructors

```python
__init__(
    self,
    name: str,
    keys: set[str],
) -> None
```

| Name | Type |
|------|------|
| `name` | `str` |
| `keys` | `set[str]` |

## Properties

- `name`
- `keys`

## Methods

- [`visit_Subscript()`](https://reference.langchain.com/python/langchain-core/runnables/utils/IsLocalDict/visit_Subscript)
- [`visit_Call()`](https://reference.langchain.com/python/langchain-core/runnables/utils/IsLocalDict/visit_Call)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/runnables/utils.py#L161)
