---
title: "on_llm_start"
description: "Run when the model starts running."
source: "https://reference.langchain.com/python/langchain-core/callbacks/base/AsyncCallbackHandler/on_llm_start"
category: "reference"
tags: [reference, langchain-core, callbacks, base, asynccallbackhandler, on_llm_start]
---

# on_llm_start

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/callbacks/base/AsyncCallbackHandler/on_llm_start)

Run when the model starts running.

!!! warning

    This method is called for non-chat models (regular text completion LLMs). If
    you're implementing a handler for a chat model, you should use
    `on_chat_model_start` instead.

## Signature

```python
on_llm_start(
    self,
    serialized: dict[str, Any],
    prompts: list[str],
    *,
    run_id: UUID,
    parent_run_id: UUID | None = None,
    tags: list[str] | None = None,
    metadata: dict[str, Any] | None = None,
    **kwargs: Any = {},
) -> None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `serialized` | `dict[str, Any]` | Yes | The serialized LLM. |
| `prompts` | `list[str]` | Yes | The prompts. |
| `run_id` | `UUID` | Yes | The ID of the current run. |
| `parent_run_id` | `UUID \| None` | No | The ID of the parent run. (default: `None`) |
| `tags` | `list[str] \| None` | No | The tags. (default: `None`) |
| `metadata` | `dict[str, Any] \| None` | No | The metadata. (default: `None`) |
| `**kwargs` | `Any` | No | Additional keyword arguments. (default: `{}`) |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/callbacks/base.py#L551)
