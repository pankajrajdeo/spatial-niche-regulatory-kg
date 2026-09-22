---
title: "on_chain_start"
description: "Start a trace for a chain run."
source: "https://reference.langchain.com/python/langchain-core/tracers/base/BaseTracer/on_chain_start"
category: "reference"
tags: [reference, langchain-core, tracers, base, basetracer, on_chain_start]
---

# on_chain_start

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/tracers/base/BaseTracer/on_chain_start)

Start a trace for a chain run.

## Signature

```python
on_chain_start(
    self,
    serialized: dict[str, Any],
    inputs: dict[str, Any],
    *,
    run_id: UUID,
    tags: list[str] | None = None,
    parent_run_id: UUID | None = None,
    metadata: dict[str, Any] | None = None,
    run_type: str | None = None,
    name: str | None = None,
    **kwargs: Any = {},
) -> Run
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `serialized` | `dict[str, Any]` | Yes | The serialized chain. |
| `inputs` | `dict[str, Any]` | Yes | The inputs for the chain. |
| `run_id` | `UUID` | Yes | The run ID. |
| `tags` | `list[str] \| None` | No | The tags for the run. (default: `None`) |
| `parent_run_id` | `UUID \| None` | No | The parent run ID. (default: `None`) |
| `metadata` | `dict[str, Any] \| None` | No | The metadata for the run. (default: `None`) |
| `run_type` | `str \| None` | No | The type of the run. (default: `None`) |
| `name` | `str \| None` | No | The name of the run. (default: `None`) |
| `**kwargs` | `Any` | No | Additional arguments. (default: `{}`) |

## Returns

`Run`

The run.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/tracers/base.py#L260)
