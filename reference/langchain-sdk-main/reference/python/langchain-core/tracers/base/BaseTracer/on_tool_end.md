---
title: "on_tool_end"
description: "End a trace for a tool run."
source: "https://reference.langchain.com/python/langchain-core/tracers/base/BaseTracer/on_tool_end"
category: "reference"
tags: [reference, langchain-core, tracers, base, basetracer, on_tool_end]
---

# on_tool_end

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/tracers/base/BaseTracer/on_tool_end)

End a trace for a tool run.

## Signature

```python
on_tool_end(
    self,
    output: Any,
    *,
    run_id: UUID,
    **kwargs: Any = {},
) -> Run
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `output` | `Any` | Yes | The output for the tool. |
| `run_id` | `UUID` | Yes | The run ID. |
| `**kwargs` | `Any` | No | Additional arguments. (default: `{}`) |

## Returns

`Run`

The run.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/tracers/base.py#L407)
