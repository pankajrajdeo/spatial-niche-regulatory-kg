---
title: "on_chat_model_start"
description: "Async run when LLM starts running."
source: "https://reference.langchain.com/python/langchain-core/callbacks/manager/AsyncCallbackManager/on_chat_model_start"
category: "reference"
tags: [reference, langchain-core, callbacks, manager, asynccallbackmanager, on_chat_model_start]
---

# on_chat_model_start

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/callbacks/manager/AsyncCallbackManager/on_chat_model_start)

Async run when LLM starts running.

## Signature

```python
on_chat_model_start(
    self,
    serialized: dict[str, Any],
    messages: list[list[BaseMessage]],
    run_id: UUID | None = None,
    **kwargs: Any = {},
) -> list[AsyncCallbackManagerForLLMRun]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `serialized` | `dict[str, Any]` | Yes | The serialized LLM. |
| `messages` | `list[list[BaseMessage]]` | Yes | The list of messages. |
| `run_id` | `UUID \| None` | No | The ID of the run. (default: `None`) |
| `**kwargs` | `Any` | No | Additional keyword arguments. (default: `{}`) |

## Returns

`list[AsyncCallbackManagerForLLMRun]`

The list of async callback managers, one for each LLM run corresponding to

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/callbacks/manager.py#L1955)
