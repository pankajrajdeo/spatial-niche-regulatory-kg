---
title: "map"
description: "Return a new Runnable that maps a list of inputs to a list of outputs."
source: "https://reference.langchain.com/python/langchain-core/runnables/base/Runnable/map"
category: "reference"
tags: [reference, langchain-core, runnables, base, runnable, map]
---

# map

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/base/Runnable/map)

Return a new `Runnable` that maps a list of inputs to a list of outputs.

Calls `invoke` with each input.

## Signature

```python
map(
    self,
) -> Runnable[Sequence[Input], list[Output]]
```

## Description

**Example:**

```python
from langchain_core.runnables import RunnableLambda

def _lambda(x: int) -> int:
    return x + 1

runnable = RunnableLambda(_lambda)
print(runnable.map().invoke([1, 2, 3]))  # [2, 3, 4]
```

## Returns

`Runnable[Sequence[Input], list[Output]]`

A new `Runnable` that maps a list of inputs to a list of outputs.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/runnables/base.py#L2165)
