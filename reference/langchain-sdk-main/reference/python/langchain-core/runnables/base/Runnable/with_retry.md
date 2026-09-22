---
title: "with_retry"
description: "Create a new Runnable that retries the original Runnable on exceptions."
source: "https://reference.langchain.com/python/langchain-core/runnables/base/Runnable/with_retry"
category: "reference"
tags: [reference, langchain-core, runnables, base, runnable, with_retry]
---

# with_retry

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/base/Runnable/with_retry)

Create a new `Runnable` that retries the original `Runnable` on exceptions.

## Signature

```python
with_retry(
    self,
    *,
    retry_if_exception_type: tuple[type[BaseException], ...] = (Exception,),
    wait_exponential_jitter: bool = True,
    exponential_jitter_params: ExponentialJitterParams | None = None,
    stop_after_attempt: int = 3,
) -> Runnable[Input, Output]
```

## Description

**Example:**

```python
from langchain_core.runnables import RunnableLambda

count = 0

def _lambda(x: int) -> None:
    global count
    count = count + 1
    if x == 1:
        raise ValueError("x is 1")
    else:
        pass

runnable = RunnableLambda(_lambda)
try:
    runnable.with_retry(
        stop_after_attempt=2,
        retry_if_exception_type=(ValueError,),
    ).invoke(1)
except ValueError:
    pass

assert count == 2
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `retry_if_exception_type` | `tuple[type[BaseException], ...]` | No | A tuple of exception types to retry on. (default: `(Exception,)`) |
| `wait_exponential_jitter` | `bool` | No | Whether to add jitter to the wait time between retries. (default: `True`) |
| `stop_after_attempt` | `int` | No | The maximum number of attempts to make before giving up. (default: `3`) |
| `exponential_jitter_params` | `ExponentialJitterParams \| None` | No | Parameters for `tenacity.wait_exponential_jitter`. Namely: `initial`, `max`, `exp_base`, and `jitter` (all `float` values). (default: `None`) |

## Returns

`Runnable[Input, Output]`

A new `Runnable` that retries the original `Runnable` on exceptions.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/runnables/base.py#L2101)
