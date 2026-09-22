---
title: "ahandle_event"
description: "Async generic event handler for AsyncCallbackManager."
source: "https://reference.langchain.com/python/langchain-core/callbacks/manager/ahandle_event"
category: "reference"
tags: [reference, langchain-core, callbacks, manager, ahandle_event]
---

# ahandle_event

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/callbacks/manager/ahandle_event)

Async generic event handler for `AsyncCallbackManager`.

## Signature

```python
ahandle_event(
    handlers: list[BaseCallbackHandler],
    event_name: str,
    ignore_condition_name: str | None,
    *args: Any = (),
    **kwargs: Any = {},
) -> None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `handlers` | `list[BaseCallbackHandler]` | Yes | The list of handlers that will handle the event. |
| `event_name` | `str` | Yes | The name of the event (e.g., `'on_llm_start'`). |
| `ignore_condition_name` | `str \| None` | Yes | Name of the attribute defined on handler that if `True` will cause the handler to be skipped for the given event. |
| `*args` | `Any` | No | The arguments to pass to the event handler. (default: `()`) |
| `**kwargs` | `Any` | No | The keyword arguments to pass to the event handler. (default: `{}`) |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/callbacks/manager.py#L453)
