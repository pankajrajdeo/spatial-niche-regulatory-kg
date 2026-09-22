---
title: "on_chain_end"
description: "End a trace for a chain run."
source: "https://reference.langchain.com/python/langchain-core/tracers/base/BaseTracer/on_chain_end"
category: "reference"
tags: [reference, langchain-core, tracers, base, basetracer, on_chain_end]
---

# on_chain_end

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/tracers/base/BaseTracer/on_chain_end)

End a trace for a chain run.

## Signature

```python
on_chain_end(
    self,
    outputs: dict[str, Any],
    *,
    run_id: UUID,
    inputs: dict[str, Any] | None = None,
    **kwargs: Any = {},
) -> Run
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `outputs` | `dict[str, Any]` | Yes | The outputs for the chain. |
| `run_id` | `UUID` | Yes | The run ID. |
| `inputs` | `dict[str, Any] \| None` | No | The inputs for the chain. (default: `None`) |
| `**kwargs` | `Any` | No | Additional arguments. (default: `{}`) |

## Returns

`Run`

The run.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/tracers/base.py#L305)
