---
title: "with_fallbacks"
description: "Add fallbacks to a Runnable, returning a new Runnable."
source: "https://reference.langchain.com/python/langchain-core/runnables/base/Runnable/with_fallbacks"
category: "reference"
tags: [reference, langchain-core, runnables, base, runnable, with_fallbacks]
---

# with_fallbacks

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/base/Runnable/with_fallbacks)

Add fallbacks to a `Runnable`, returning a new `Runnable`.

The new `Runnable` will try the original `Runnable`, and then each fallback
in order, upon failures.

## Signature

```python
with_fallbacks(
    self,
    fallbacks: Sequence[Runnable[Input, Output]],
    *,
    exceptions_to_handle: tuple[type[BaseException], ...] = (Exception,),
    exception_key: str | None = None,
) -> RunnableWithFallbacksT[Input, Output]
```

## Description

**Example:**

```python
from typing import Iterator

from langchain_core.runnables import RunnableGenerator

def _generate_immediate_error(input: Iterator) -> Iterator[str]:
    raise ValueError()
    yield ""

def _generate(input: Iterator) -> Iterator[str]:
    yield from "foo bar"

runnable = RunnableGenerator(_generate_immediate_error).with_fallbacks(
    [RunnableGenerator(_generate)]
)
print("".join(runnable.stream({})))  # foo bar
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `fallbacks` | `Sequence[Runnable[Input, Output]]` | Yes | A sequence of runnables to try if the original `Runnable` fails. |
| `exceptions_to_handle` | `tuple[type[BaseException], ...]` | No | A tuple of exception types to handle. (default: `(Exception,)`) |
| `exception_key` | `str \| None` | No | If `string` is specified then handled exceptions will be passed to fallbacks as part of the input under the specified key.  If `None`, exceptions will not be passed to fallbacks.  If used, the base `Runnable` and its fallbacks must accept a dictionary as input. (default: `None`) |
| `fallbacks` | `Sequence[Runnable[Input, Output]]` | Yes | A sequence of runnables to try if the original `Runnable` fails. |
| `exceptions_to_handle` | `tuple[type[BaseException], ...]` | No | A tuple of exception types to handle. (default: `(Exception,)`) |
| `exception_key` | `str \| None` | No | If `string` is specified then handled exceptions will be passed to fallbacks as part of the input under the specified key.  If `None`, exceptions will not be passed to fallbacks.  If used, the base `Runnable` and its fallbacks must accept a dictionary as input. (default: `None`) |

## Returns

`RunnableWithFallbacksT[Input, Output]`

A new `Runnable` that will try the original `Runnable`, and then each
Fallback in order, upon failures.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/runnables/base.py#L2188)
