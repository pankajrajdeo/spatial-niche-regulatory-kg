---
title: "on_stream_event"
description: "Run on each protocol event from stream_events(version=\"v3\")."
source: "https://reference.langchain.com/python/langchain-core/callbacks/manager/CallbackManagerForLLMRun/on_stream_event"
category: "reference"
tags: [reference, langchain-core, callbacks, manager, callbackmanagerforllmrun, on_stream_event]
---

# on_stream_event

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/callbacks/manager/CallbackManagerForLLMRun/on_stream_event)

Run on each protocol event from `stream_events(version="v3")`.

## Signature

```python
on_stream_event(
    self,
    event: MessagesData,
    **kwargs: Any = {},
) -> None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `event` | `MessagesData` | Yes | The protocol event. |
| `**kwargs` | `Any` | No | Additional keyword arguments. (default: `{}`) |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/callbacks/manager.py#L785)
