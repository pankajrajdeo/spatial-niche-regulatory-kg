---
title: "pipe"
description: "Pipe Runnable objects."
source: "https://reference.langchain.com/python/langchain-core/runnables/base/Runnable/pipe"
category: "reference"
tags: [reference, langchain-core, runnables, base, runnable, pipe]
---

# pipe

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/base/Runnable/pipe)

Pipe `Runnable` objects.

Compose this `Runnable` with `Runnable`-like objects to make a
`RunnableSequence`.

Equivalent to `RunnableSequence(self, *others)` or `self | others[0] | ...`

## Signature

```python
pipe(
    self,
    *others: Runnable[Any, Other] | Callable[[Any], Other] = (),
    name: str | None = None,
) -> RunnableSerializable[Input, Other]
```

## Description

**Example:**

```python
from langchain_core.runnables import RunnableLambda

def add_one(x: int) -> int:
    return x + 1

def mul_two(x: int) -> int:
    return x * 2

runnable_1 = RunnableLambda(add_one)
runnable_2 = RunnableLambda(mul_two)
sequence = runnable_1.pipe(runnable_2)
# Or equivalently:
# sequence = runnable_1 | runnable_2
# sequence = RunnableSequence(first=runnable_1, last=runnable_2)
sequence.invoke(1)
await sequence.ainvoke(1)
# -> 4

sequence.batch([1, 2, 3])
await sequence.abatch([1, 2, 3])
# -> [4, 6, 8]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `*others` | `Runnable[Any, Other] \| Callable[[Any], Other]` | No | Other `Runnable` or `Runnable`-like objects to compose (default: `()`) |
| `name` | `str \| None` | No | An optional name for the resulting `RunnableSequence`. (default: `None`) |

## Returns

`RunnableSerializable[Input, Other]`

A new `Runnable`.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/runnables/base.py#L724)
