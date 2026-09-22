---
title: "on_custom_event"
description: "Dispatch an adhoc event to the handlers (async version)."
source: "https://reference.langchain.com/python/langchain-core/callbacks/manager/CallbackManager/on_custom_event"
category: "reference"
tags: [reference, langchain-core, callbacks, manager, callbackmanager, on_custom_event]
---

# on_custom_event

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/callbacks/manager/CallbackManager/on_custom_event)

Dispatch an adhoc event to the handlers (async version).

This event should NOT be used in any internal LangChain code. The event is meant
specifically for users of the library to dispatch custom events that are
tailored to their application.

## Signature

```python
on_custom_event(
    self,
    name: str,
    data: Any,
    run_id: UUID | None = None,
    **kwargs: Any = {},
) -> None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `name` | `str` | Yes | The name of the adhoc event. |
| `data` | `Any` | Yes | The data for the adhoc event. |
| `run_id` | `UUID \| None` | No | The ID of the run. (default: `None`) |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/callbacks/manager.py#L1638)
