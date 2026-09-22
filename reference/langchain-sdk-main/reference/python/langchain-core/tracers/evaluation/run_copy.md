---
title: "run_copy"
description: "Copy run, compatible with both Pydantic v1 and v2."
source: "https://reference.langchain.com/python/langchain-core/tracers/evaluation/run_copy"
category: "reference"
tags: [reference, langchain-core, tracers, evaluation, run_copy]
---

# run_copy

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/tracers/_compat/run_copy)

Copy run, compatible with both Pydantic v1 and v2.

## Signature

```python
run_copy(
    run: Run,
    **kwargs: Any = {},
) -> Run
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `run` | `Run` | Yes | The run to copy. |
| `**kwargs` | `Any` | No | Additional arguments passed to `model_copy`/`copy`. (default: `{}`) |

## Returns

`Run`

A copy of the run.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/tracers/_compat.py#L39)
