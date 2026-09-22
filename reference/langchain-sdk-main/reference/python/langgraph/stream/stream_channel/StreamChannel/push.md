---
title: "push"
description: "Append an item. Auto-forwards if wired."
source: "https://reference.langchain.com/python/langgraph/stream/stream_channel/StreamChannel/push"
category: "reference"
tags: [reference, langgraph, stream, stream_channel, streamchannel, push]
---

# push

> **Method** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/stream/stream_channel/StreamChannel/push)

Append an item. Auto-forwards if wired.

The local buffer append is a no-op when no subscriber is
registered, but auto-forwarding always fires so wired events
reach the main event log regardless of subscription state.

Items are stored as `(stamp, item)` tuples where stamp is a
monotonic counter from the owning mux. Stamps are stripped by
the default cursors; raw stamped tuples are visible on `_items`.

## Signature

```python
push(
    self,
    item: T,
) -> None
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/644815f9e5bc52ad8f7a5227a456227e9c3e639b/libs/langgraph/langgraph/stream/stream_channel.py#L120)
