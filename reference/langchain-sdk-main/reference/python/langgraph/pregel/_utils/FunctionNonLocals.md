---
title: "FunctionNonLocals"
description: "Get the nonlocal variables accessed of a function."
source: "https://reference.langchain.com/python/langgraph/pregel/_utils/FunctionNonLocals"
category: "reference"
tags: [reference, langgraph, pregel, utils, functionnonlocals]
---

# FunctionNonLocals

> **Class** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/pregel/_utils/FunctionNonLocals)

Get the nonlocal variables accessed of a function.

## Signature

```python
FunctionNonLocals(
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

- `nonlocals`

## Methods

- [`visit_FunctionDef()`](https://reference.langchain.com/python/langgraph/pregel/_utils/FunctionNonLocals/visit_FunctionDef)
- [`visit_AsyncFunctionDef()`](https://reference.langchain.com/python/langgraph/pregel/_utils/FunctionNonLocals/visit_AsyncFunctionDef)
- [`visit_Lambda()`](https://reference.langchain.com/python/langgraph/pregel/_utils/FunctionNonLocals/visit_Lambda)

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/644815f9e5bc52ad8f7a5227a456227e9c3e639b/libs/langgraph/langgraph/pregel/_utils.py#L183)
