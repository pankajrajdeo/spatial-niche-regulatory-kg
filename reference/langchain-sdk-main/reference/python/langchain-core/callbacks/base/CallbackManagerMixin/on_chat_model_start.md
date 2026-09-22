---
title: "on_chat_model_start"
description: "Run when a chat model starts running."
source: "https://reference.langchain.com/python/langchain-core/callbacks/base/CallbackManagerMixin/on_chat_model_start"
category: "reference"
tags: [reference, langchain-core, callbacks, base, callbackmanagermixin, on_chat_model_start]
---

# on_chat_model_start

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/callbacks/base/CallbackManagerMixin/on_chat_model_start)

Run when a chat model starts running.

!!! warning

    This method is called for chat models. If you're implementing a handler for
    a non-chat model, you should use `on_llm_start` instead.

!!! note

    When overriding this method, the signature **must** include the two
    required positional arguments `serialized` and `messages`.  Avoid
    using `*args` in your override — doing so causes an `IndexError`
    in the fallback path when the callback system converts `messages`
    to prompt strings for `on_llm_start`.  Always declare the
    signature explicitly:

    .. code-block:: python

        def on_chat_model_start(
            self,
            serialized: dict[str, Any],
            messages: list[list[BaseMessage]],
            **kwargs: Any,
        ) -> None:
            raise NotImplementedError  # triggers fallback to on_llm_start

## Signature

```python
on_chat_model_start(
    self,
    serialized: dict[str, Any],
    messages: list[list[BaseMessage]],
    *,
    run_id: UUID,
    parent_run_id: UUID | None = None,
    tags: list[str] | None = None,
    metadata: dict[str, Any] | None = None,
    **kwargs: Any = {},
) -> Any
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `serialized` | `dict[str, Any]` | Yes | The serialized chat model. |
| `messages` | `list[list[BaseMessage]]` | Yes | The messages. Must be a list of message lists — this is a required positional argument and must be present in any override. |
| `run_id` | `UUID` | Yes | The ID of the current run. |
| `parent_run_id` | `UUID \| None` | No | The ID of the parent run. (default: `None`) |
| `tags` | `list[str] \| None` | No | The tags. (default: `None`) |
| `metadata` | `dict[str, Any] \| None` | No | The metadata. (default: `None`) |
| `**kwargs` | `Any` | No | Additional keyword arguments. (default: `{}`) |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/callbacks/base.py#L311)
