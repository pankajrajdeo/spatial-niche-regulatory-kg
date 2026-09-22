---
title: "IsFunctionArgDict"
description: "Check if the first argument of a function is a dict."
source: "https://reference.langchain.com/python/langchain-core/runnables/utils/IsFunctionArgDict"
category: "reference"
tags: [reference, langchain-core, runnables, utils, isfunctionargdict]
---

# IsFunctionArgDict

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/utils/IsFunctionArgDict)

Check if the first argument of a function is a dict.

## Signature

```python
IsFunctionArgDict(
    self,
)
```

## Extends

- `ast.NodeVisitor`

## Constructors

```python
__init__(
    self,
) -> None
```

## Properties

- `keys`

## Methods

- [`visit_Lambda()`](https://reference.langchain.com/python/langchain-core/runnables/utils/IsFunctionArgDict/visit_Lambda)
- [`visit_FunctionDef()`](https://reference.langchain.com/python/langchain-core/runnables/utils/IsFunctionArgDict/visit_FunctionDef)
- [`visit_AsyncFunctionDef()`](https://reference.langchain.com/python/langchain-core/runnables/utils/IsFunctionArgDict/visit_AsyncFunctionDef)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/runnables/utils.py#L211)
