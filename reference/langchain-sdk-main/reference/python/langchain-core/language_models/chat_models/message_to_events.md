---
title: "message_to_events"
description: "Replay a finalized message as a synthetic event lifecycle."
source: "https://reference.langchain.com/python/langchain-core/language_models/chat_models/message_to_events"
category: "reference"
tags: [reference, langchain-core, language_models, chat_models, message_to_events]
---

# message_to_events

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/language_models/_compat_bridge/message_to_events)

Replay a finalized message as a synthetic event lifecycle.

For a message returned whole (from a graph node, checkpoint, or
cache), produce the same `message-start` / per-block /
`message-finish` event stream a live call would produce.  Consumers
downstream see a uniform event shape regardless of source.

Text and reasoning blocks emit a single `content-block-delta` with
the full accumulated content.  Already-finalized blocks (tool_call,
server_tool_call, image, etc.) skip the delta and rely on the
`content-block-finish` event alone.

## Signature

```python
message_to_events(
    msg: BaseMessage,
    *,
    message_id: str | None = None,
) -> Iterator[MessagesData]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `msg` | `BaseMessage` | Yes | The finalized message — typically an `AIMessage`. |
| `message_id` | `str \| None` | No | Optional stable message ID; falls back to `msg.id`. (default: `None`) |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/language_models/_compat_bridge.py#L776)
