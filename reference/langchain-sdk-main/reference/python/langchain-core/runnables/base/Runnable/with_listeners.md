---
title: "with_listeners"
description: "Bind lifecycle listeners to a Runnable, returning a new Runnable."
source: "https://reference.langchain.com/python/langchain-core/runnables/base/Runnable/with_listeners"
category: "reference"
tags: [reference, langchain-core, runnables, base, runnable, with_listeners]
---

# with_listeners

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/base/Runnable/with_listeners)

Bind lifecycle listeners to a `Runnable`, returning a new `Runnable`.

The Run object contains information about the run, including its `id`,
`type`, `input`, `output`, `error`, `start_time`, `end_time`, and
any tags or metadata added to the run.

## Signature

```python
with_listeners(
    self,
    *,
    on_start: Callable[[Run], None] | Callable[[Run, RunnableConfig], None] | None = None,
    on_end: Callable[[Run], None] | Callable[[Run, RunnableConfig], None] | None = None,
    on_error: Callable[[Run], None] | Callable[[Run, RunnableConfig], None] | None = None,
) -> Runnable[Input, Output]
```

## Description

**Example:**

```python
from langchain_core.runnables import RunnableLambda
from langchain_core.tracers.schemas import Run

import time

def test_runnable(time_to_sleep: int):
    time.sleep(time_to_sleep)

def fn_start(run_obj: Run):
    print("start_time:", run_obj.start_time)

def fn_end(run_obj: Run):
    print("end_time:", run_obj.end_time)

chain = RunnableLambda(test_runnable).with_listeners(
    on_start=fn_start, on_end=fn_end
)
chain.invoke(2)
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `on_start` | `Callable[[Run], None] \| Callable[[Run, RunnableConfig], None] \| None` | No | Called before the `Runnable` starts running, with the `Run` object. (default: `None`) |
| `on_end` | `Callable[[Run], None] \| Callable[[Run, RunnableConfig], None] \| None` | No | Called after the `Runnable` finishes running, with the `Run` object. (default: `None`) |
| `on_error` | `Callable[[Run], None] \| Callable[[Run, RunnableConfig], None] \| None` | No | Called if the `Runnable` throws an error, with the `Run` object. (default: `None`) |

## Returns

`Runnable[Input, Output]`

A new `Runnable` with the listeners bound.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/runnables/base.py#L1910)
