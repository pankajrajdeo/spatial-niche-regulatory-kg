---
title: "on_stream_event"
description: "Forward a protocol event from stream_events(version=\"v3\") as a messages stream part."
source: "https://reference.langchain.com/python/langgraph/pregel/_messages/StreamMessagesHandlerV2/on_stream_event"
category: "reference"
tags: [reference, langgraph, pregel, messages, streammessageshandlerv2, on_stream_event]
---

# on_stream_event

> **Method** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/pregel/_messages/StreamMessagesHandlerV2/on_stream_event)

Forward a protocol event from `stream_events(version="v3")` as a messages stream part.

Fires once per `MessagesData` event (`message-start`, per-block
`content-block-*`, `message-finish`). The transformer layer
correlates events back to a single `ChatModelStream` via
`metadata["run_id"]` — attached here so the v1
`stream_mode="messages"` output (which emits
`(AIMessageChunk, metadata)` via `on_llm_new_token`) keeps its
original metadata shape.

Lives on the v2 handler rather than the v1 base: content-block
events are a v2-only concept, and forwarding them only when the
v2 handler is attached keeps the message channel's shape
predictable for v1 callers.

## Signature

```python
on_stream_event(
    self,
    event: dict[str, Any],
    *,
    run_id: UUID,
    parent_run_id: UUID | None = None,
    tags: list[str] | None = None,
    **kwargs: Any = {},
) -> Any
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/644815f9e5bc52ad8f7a5227a456227e9c3e639b/libs/langgraph/langgraph/pregel/_messages.py#L373)
