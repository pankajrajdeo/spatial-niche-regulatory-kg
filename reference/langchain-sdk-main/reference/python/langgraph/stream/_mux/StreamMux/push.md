---
title: "push"
description: "Route an event through all transformers, then append to the main log."
source: "https://reference.langchain.com/python/langgraph/stream/_mux/StreamMux/push"
category: "reference"
tags: [reference, langgraph, stream, mux, streammux, push]
---

# push

> **Method** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/stream/_mux/StreamMux/push)

Route an event through all transformers, then append to the main log.

Each transformer's `process()` is called in registration order.
If any transformer returns False, the event is suppressed from
the main log, but transformers that already saw it keep their
side effects.

On the root mux, `seq` is assigned right before an event enters
the main log, not before the transformer pipeline runs. This
ensures that events auto-forwarded from StreamChannels during
`process()` get earlier seq numbers than the original event,
preserving monotonic ordering in the root log. Child muxes do
not assign `seq`, so subgraph forwarding can share event objects
without mutating their envelopes.

## Signature

```python
push(
    self,
    event: ProtocolEvent,
) -> None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `event` | `ProtocolEvent` | Yes | The protocol event to dispatch. |

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/644815f9e5bc52ad8f7a5227a456227e9c3e639b/libs/langgraph/langgraph/stream/_mux.py#L269)
