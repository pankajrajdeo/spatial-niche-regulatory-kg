---
title: "on_llm_end"
description: "End a trace for an LLM or chat model run."
source: "https://reference.langchain.com/python/langchain-core/tracers/base/BaseTracer/on_llm_end"
category: "reference"
tags: [reference, langchain-core, tracers, base, basetracer, on_llm_end]
---

# on_llm_end

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/tracers/base/BaseTracer/on_llm_end)

End a trace for an LLM or chat model run.

## Signature

```python
on_llm_end(
    self,
    response: LLMResult,
    *,
    run_id: UUID,
    **kwargs: Any = {},
) -> Run
```

## Description

**Note:**

This is the end callback for both run types. Chat models start with
`on_chat_model_start`, but there is no `on_chat_model_end`;
completion is routed here for callback API compatibility.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `response` | `LLMResult` | Yes | The response. |
| `run_id` | `UUID` | Yes | The run ID. |
| `**kwargs` | `Any` | No | Additional arguments. (default: `{}`) |

## Returns

`Run`

The run.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/tracers/base.py#L207)
