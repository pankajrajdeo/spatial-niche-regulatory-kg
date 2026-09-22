---
title: "on_llm_error"
description: "Run when LLM errors."
source: "https://reference.langchain.com/python/langchain-core/callbacks/base/LLMManagerMixin/on_llm_error"
category: "reference"
tags: [reference, langchain-core, callbacks, base, llmmanagermixin, on_llm_error]
---

# on_llm_error

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/callbacks/base/LLMManagerMixin/on_llm_error)

Run when LLM errors.

## Signature

```python
on_llm_error(
    self,
    error: BaseException,
    *,
    run_id: UUID,
    parent_run_id: UUID | None = None,
    tags: list[str] | None = None,
    **kwargs: Any = {},
) -> Any
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `error` | `BaseException` | Yes | The error that occurred. |
| `run_id` | `UUID` | Yes | The ID of the current run. |
| `parent_run_id` | `UUID \| None` | No | The ID of the parent run. (default: `None`) |
| `tags` | `list[str] \| None` | No | The tags. (default: `None`) |
| `**kwargs` | `Any` | No | Additional keyword arguments. (default: `{}`) |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/callbacks/base.py#L109)
