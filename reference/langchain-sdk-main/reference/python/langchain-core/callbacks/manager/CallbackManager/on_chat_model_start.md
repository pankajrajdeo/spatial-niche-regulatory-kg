---
title: "on_chat_model_start"
description: "Run when chat model starts running."
source: "https://reference.langchain.com/python/langchain-core/callbacks/manager/CallbackManager/on_chat_model_start"
category: "reference"
tags: [reference, langchain-core, callbacks, manager, callbackmanager, on_chat_model_start]
---

# on_chat_model_start

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/callbacks/manager/CallbackManager/on_chat_model_start)

Run when chat model starts running.

## Signature

```python
on_chat_model_start(
    self,
    serialized: dict[str, Any],
    messages: list[list[BaseMessage]],
    run_id: UUID | None = None,
    **kwargs: Any = {},
) -> list[CallbackManagerForLLMRun]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `serialized` | `dict[str, Any]` | Yes | The serialized LLM. |
| `messages` | `list[list[BaseMessage]]` | Yes | The list of messages. |
| `run_id` | `UUID \| None` | No | The ID of the run. (default: `None`) |
| `**kwargs` | `Any` | No | Additional keyword arguments. (default: `{}`) |

## Returns

`list[CallbackManagerForLLMRun]`

A callback manager for each list of messages as an LLM run.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/callbacks/manager.py#L1431)
