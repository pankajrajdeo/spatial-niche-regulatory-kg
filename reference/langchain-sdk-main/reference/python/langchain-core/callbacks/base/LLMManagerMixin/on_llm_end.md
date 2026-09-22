---
title: "on_llm_end"
description: "Run when LLM ends running."
source: "https://reference.langchain.com/python/langchain-core/callbacks/base/LLMManagerMixin/on_llm_end"
category: "reference"
tags: [reference, langchain-core, callbacks, base, llmmanagermixin, on_llm_end]
---

# on_llm_end

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/callbacks/base/LLMManagerMixin/on_llm_end)

Run when LLM ends running.

## Signature

```python
on_llm_end(
    self,
    response: LLMResult,
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
| `response` | `LLMResult` | Yes | The response which was generated. |
| `run_id` | `UUID` | Yes | The ID of the current run. |
| `parent_run_id` | `UUID \| None` | No | The ID of the parent run. (default: `None`) |
| `tags` | `list[str] \| None` | No | The tags. (default: `None`) |
| `**kwargs` | `Any` | No | Additional keyword arguments. (default: `{}`) |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/callbacks/base.py#L90)
