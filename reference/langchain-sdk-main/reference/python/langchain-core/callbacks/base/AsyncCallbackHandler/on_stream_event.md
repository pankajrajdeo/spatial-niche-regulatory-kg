---
title: "on_stream_event"
description: "Run on each protocol event produced by astream_events(version=\"v3\")."
source: "https://reference.langchain.com/python/langchain-core/callbacks/base/AsyncCallbackHandler/on_stream_event"
category: "reference"
tags: [reference, langchain-core, callbacks, base, asynccallbackhandler, on_stream_event]
---

# on_stream_event

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/callbacks/base/AsyncCallbackHandler/on_stream_event)

Run on each protocol event produced by `astream_events(version="v3")`.

See :meth:`LLMManagerMixin.on_stream_event` for the full contract.
Fires once per `MessagesData` event at event granularity, uniformly
across native and compat-bridge providers, and is purely additive
to the existing `on_chat_model_start` / `on_llm_end` /
`on_llm_error` callbacks.

## Signature

```python
on_stream_event(
    self,
    event: MessagesData,
    *,
    run_id: UUID,
    parent_run_id: UUID | None = None,
    tags: list[str] | None = None,
    **kwargs: Any = {},
) -> None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `event` | `MessagesData` | Yes | The protocol event. |
| `run_id` | `UUID` | Yes | The ID of the current run. |
| `parent_run_id` | `UUID \| None` | No | The ID of the parent run. (default: `None`) |
| `tags` | `list[str] \| None` | No | The tags. (default: `None`) |
| `**kwargs` | `Any` | No | Additional keyword arguments. (default: `{}`) |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/callbacks/base.py#L696)
