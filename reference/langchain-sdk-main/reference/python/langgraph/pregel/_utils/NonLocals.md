---
title: "NonLocals"
description: "Get nonlocal variables accessed."
source: "https://reference.langchain.com/python/langgraph/pregel/_utils/NonLocals"
category: "reference"
tags: [reference, langgraph, pregel, utils, nonlocals]
---

# NonLocals

> **Class** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/pregel/_utils/NonLocals)

Get nonlocal variables accessed.

## Signature

```python
NonLocals(
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

- `loads`
- `stores`

## Methods

- [`visit_Name()`](https://reference.langchain.com/python/langgraph/pregel/_utils/NonLocals/visit_Name)
- [`visit_Attribute()`](https://reference.langchain.com/python/langgraph/pregel/_utils/NonLocals/visit_Attribute)

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/644815f9e5bc52ad8f7a5227a456227e9c3e639b/libs/langgraph/langgraph/pregel/_utils.py#L232)
