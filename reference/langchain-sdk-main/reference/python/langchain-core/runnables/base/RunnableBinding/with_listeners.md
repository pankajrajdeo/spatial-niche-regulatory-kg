---
title: "with_listeners"
description: "Bind lifecycle listeners to a Runnable, returning a new Runnable."
source: "https://reference.langchain.com/python/langchain-core/runnables/base/RunnableBinding/with_listeners"
category: "reference"
tags: [reference, langchain-core, runnables, base, runnablebinding, with_listeners]
---

# with_listeners

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/base/RunnableBinding/with_listeners)

Bind lifecycle listeners to a `Runnable`, returning a new `Runnable`.

The `Run` object contains information about the run, including its `id`,
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

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/runnables/base.py#L6467)
