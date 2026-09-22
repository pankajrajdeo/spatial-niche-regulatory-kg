---
title: "TimeoutPolicy"
description: "Configuration for timing out node attempts."
source: "https://reference.langchain.com/python/langgraph/types/TimeoutPolicy"
category: "reference"
tags: [reference, langgraph, types, timeoutpolicy]
---

# TimeoutPolicy

> **Class** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/types/TimeoutPolicy)

Configuration for timing out node attempts.

!!! note "Cooperative cancellation"

    Timeouts rely on asyncio cancellation. If your node uses synchronous
    time.sleep() or other CPU-bound work that blocks the GIL, the timeout will not
    be fired until after the event loop has been released.

!!! note "Inline callback dispatch"

    Under `refresh_on="auto"`, an internal handler refreshes the timeout on any
    callback event that occurs in the execution of the node or its nested descendants.

## Signature

```python
TimeoutPolicy(
    self,
    *,
    run_timeout: float | timedelta | None = None,
    idle_timeout: float | timedelta | None = None,
    refresh_on: Literal['auto', 'heartbeat'] = 'auto',
)
```

## Constructors

```python
__init__(
    self,
    *,
    run_timeout: float | timedelta | None = None,
    idle_timeout: float | timedelta | None = None,
    refresh_on: Literal['auto', 'heartbeat'] = 'auto',
) -> None
```

| Name | Type |
|------|------|
| `run_timeout` | `float \| timedelta \| None` |
| `idle_timeout` | `float \| timedelta \| None` |
| `refresh_on` | `Literal['auto', 'heartbeat']` |

## Properties

- `run_timeout`
- `idle_timeout`
- `refresh_on`

## Methods

- [`coerce()`](https://reference.langchain.com/python/langgraph/types/TimeoutPolicy/coerce)

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/644815f9e5bc52ad8f7a5227a456227e9c3e639b/libs/langgraph/langgraph/types.py#L451)
