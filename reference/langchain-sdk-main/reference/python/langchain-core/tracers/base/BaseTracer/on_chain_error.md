---
title: "on_chain_error"
description: "Handle an error for a chain run."
source: "https://reference.langchain.com/python/langchain-core/tracers/base/BaseTracer/on_chain_error"
category: "reference"
tags: [reference, langchain-core, tracers, base, basetracer, on_chain_error]
---

# on_chain_error

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/tracers/base/BaseTracer/on_chain_error)

Handle an error for a chain run.

## Signature

```python
on_chain_error(
    self,
    error: BaseException,
    *,
    inputs: dict[str, Any] | None = None,
    run_id: UUID,
    **kwargs: Any = {},
) -> Run
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `error` | `BaseException` | Yes | The error. |
| `inputs` | `dict[str, Any] \| None` | No | The inputs for the chain. (default: `None`) |
| `run_id` | `UUID` | Yes | The run ID. |
| `**kwargs` | `Any` | No | Additional arguments. (default: `{}`) |

## Returns

`Run`

The run.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/tracers/base.py#L334)
