---
title: "on_retriever_start"
description: "Run when the Retriever starts running."
source: "https://reference.langchain.com/python/langchain-core/tracers/base/BaseTracer/on_retriever_start"
category: "reference"
tags: [reference, langchain-core, tracers, base, basetracer, on_retriever_start]
---

# on_retriever_start

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/tracers/base/BaseTracer/on_retriever_start)

Run when the `Retriever` starts running.

## Signature

```python
on_retriever_start(
    self,
    serialized: dict[str, Any],
    query: str,
    *,
    run_id: UUID,
    parent_run_id: UUID | None = None,
    tags: list[str] | None = None,
    metadata: dict[str, Any] | None = None,
    name: str | None = None,
    **kwargs: Any = {},
) -> Run
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `serialized` | `dict[str, Any]` | Yes | The serialized retriever. |
| `query` | `str` | Yes | The query. |
| `run_id` | `UUID` | Yes | The run ID. |
| `parent_run_id` | `UUID \| None` | No | The parent run ID. (default: `None`) |
| `tags` | `list[str] \| None` | No | The tags for the run. (default: `None`) |
| `metadata` | `dict[str, Any] \| None` | No | The metadata for the run. (default: `None`) |
| `name` | `str \| None` | No | The name of the run. (default: `None`) |
| `**kwargs` | `Any` | No | Additional arguments. (default: `{}`) |

## Returns

`Run`

The run.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/tracers/base.py#L453)
