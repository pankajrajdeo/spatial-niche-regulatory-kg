---
title: "on_chat_model_start"
description: "Start a trace for a chat model run."
source: "https://reference.langchain.com/python/langchain-core/tracers/base/BaseTracer/on_chat_model_start"
category: "reference"
tags: [reference, langchain-core, tracers, base, basetracer, on_chat_model_start]
---

# on_chat_model_start

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/tracers/base/BaseTracer/on_chat_model_start)

Start a trace for a chat model run.

## Signature

```python
on_chat_model_start(
    self,
    serialized: dict[str, Any],
    messages: list[list[BaseMessage]],
    *,
    run_id: UUID,
    tags: list[str] | None = None,
    parent_run_id: UUID | None = None,
    metadata: dict[str, Any] | None = None,
    name: str | None = None,
    **kwargs: Any = {},
) -> Run
```

## Description

**Note:**

Naming can be confusing here: there is `on_chat_model_start`, but no
corresponding `on_chat_model_end` callback. Chat model completion is
routed through `on_llm_end` / `_on_llm_end`, which are shared with
text LLM runs.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `serialized` | `dict[str, Any]` | Yes | The serialized model. |
| `messages` | `list[list[BaseMessage]]` | Yes | The messages to start the chat with. |
| `run_id` | `UUID` | Yes | The run ID. |
| `tags` | `list[str] \| None` | No | The tags for the run. (default: `None`) |
| `parent_run_id` | `UUID \| None` | No | The parent run ID. (default: `None`) |
| `metadata` | `dict[str, Any] \| None` | No | The metadata for the run. (default: `None`) |
| `name` | `str \| None` | No | The name of the run. (default: `None`) |
| `**kwargs` | `Any` | No | Additional arguments. (default: `{}`) |

## Returns

`Run`

The run.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/tracers/base.py#L61)
