---
title: "on_stream_event"
description: "Run on each protocol event from stream_events(version=\"v3\")."
source: "https://reference.langchain.com/python/langchain-core/callbacks/base/LLMManagerMixin/on_stream_event"
category: "reference"
tags: [reference, langchain-core, callbacks, base, llmmanagermixin, on_stream_event]
---

# on_stream_event

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/callbacks/base/LLMManagerMixin/on_stream_event)

Run on each protocol event from `stream_events(version="v3")`.

Also fires for the async equivalent
(`astream_events(version="v3")`).

Fires once per `MessagesData` event — `message-start`, per-block
`content-block-start` / `content-block-delta` /
`content-block-finish`, and `message-finish`. Analogous to
`on_llm_new_token` in v1 streaming, but at event granularity rather
than chunk: a single chunk can map to multiple events (e.g. a
`content-block-start` plus its first `content-block-delta`), and
lifecycle boundaries are explicit.

Fires uniformly whether the provider emits events natively via
`_stream_chat_model_events` or goes through the chunk-to-event
compat bridge. Observers see the same event stream regardless of
how the underlying model produces output.

Not fired from v1 `stream()` / `astream()`; for those, keep using
`on_llm_new_token`. Purely additive — `on_chat_model_start`,
`on_llm_end`, and `on_llm_error` still fire around a v2 call as
they do around a v1 call.

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
) -> Any
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

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/callbacks/base.py#L128)
