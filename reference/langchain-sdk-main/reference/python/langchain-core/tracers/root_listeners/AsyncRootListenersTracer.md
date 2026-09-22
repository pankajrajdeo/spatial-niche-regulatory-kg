---
title: "AsyncRootListenersTracer"
description: "Async tracer that calls listeners on run start, end, and error."
source: "https://reference.langchain.com/python/langchain-core/tracers/root_listeners/AsyncRootListenersTracer"
category: "reference"
tags: [reference, langchain-core, tracers, root_listeners, asyncrootlistenerstracer]
---

# AsyncRootListenersTracer

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/tracers/root_listeners/AsyncRootListenersTracer)

Async tracer that calls listeners on run start, end, and error.

## Signature

```python
AsyncRootListenersTracer(
    self,
    *,
    config: RunnableConfig,
    on_start: AsyncListener | None,
    on_end: AsyncListener | None,
    on_error: AsyncListener | None,
)
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `config` | `RunnableConfig` | Yes | The runnable config. |
| `on_start` | `AsyncListener \| None` | Yes | The listener to call on run start. |
| `on_end` | `AsyncListener \| None` | Yes | The listener to call on run end. |
| `on_error` | `AsyncListener \| None` | Yes | The listener to call on run error |

## Extends

- `AsyncBaseTracer`

## Constructors

```python
__init__(
    self,
    *,
    config: RunnableConfig,
    on_start: AsyncListener | None,
    on_end: AsyncListener | None,
    on_error: AsyncListener | None,
) -> None
```

| Name | Type |
|------|------|
| `config` | `RunnableConfig` |
| `on_start` | `AsyncListener \| None` |
| `on_end` | `AsyncListener \| None` |
| `on_error` | `AsyncListener \| None` |

## Properties

- `log_missing_parent`
- `config`
- `root_id`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/tracers/root_listeners.py#L78)
