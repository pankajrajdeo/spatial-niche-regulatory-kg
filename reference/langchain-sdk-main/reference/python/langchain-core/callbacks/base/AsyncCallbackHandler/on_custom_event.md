---
title: "on_custom_event"
description: "Override to define a handler for custom events."
source: "https://reference.langchain.com/python/langchain-core/callbacks/base/AsyncCallbackHandler/on_custom_event"
category: "reference"
tags: [reference, langchain-core, callbacks, base, asynccallbackhandler, on_custom_event]
---

# on_custom_event

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/callbacks/base/AsyncCallbackHandler/on_custom_event)

Override to define a handler for custom events.

## Signature

```python
on_custom_event(
    self,
    name: str,
    data: Any,
    *,
    run_id: UUID,
    tags: list[str] | None = None,
    metadata: dict[str, Any] | None = None,
    **kwargs: Any = {},
) -> None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `name` | `str` | Yes | The name of the custom event. |
| `data` | `Any` | Yes | The data for the custom event.  Format will match the format specified by the user. |
| `run_id` | `UUID` | Yes | The ID of the run. |
| `tags` | `list[str] \| None` | No | The tags associated with the custom event (includes inherited tags). (default: `None`) |
| `metadata` | `dict[str, Any] \| None` | No | The metadata associated with the custom event (includes inherited metadata). (default: `None`) |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/callbacks/base.py#L980)
