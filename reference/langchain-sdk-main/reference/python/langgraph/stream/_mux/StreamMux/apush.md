---
title: "apush"
description: "Dispatch an event on the async lane."
source: "https://reference.langchain.com/python/langgraph/stream/_mux/StreamMux/apush"
category: "reference"
tags: [reference, langgraph, stream, mux, streammux, apush]
---

# apush

> **Method** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/stream/_mux/StreamMux/apush)

Dispatch an event on the async lane.

Awaits each transformer's `aprocess` in registration order
before appending to the main log. A slow `aprocess` serializes
the pipeline by design — that's the guarantee that lets a later
transformer (or a synchronous consumer) see the result of the
async work. For decoupled work, use `schedule()` from inside
`process` / `aprocess` instead.

The main log append is a non-blocking `push` — matching v1's
`put_nowait` shape. The root mux assigns `seq`; child muxes do
not, so forwarded subgraph events can be shared without copying.
Memory is bounded by caller pace via the caller-driven pump; see
`StreamChannel` for the full tradeoff story.

## Signature

```python
apush(
    self,
    event: ProtocolEvent,
) -> None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `event` | `ProtocolEvent` | Yes | The protocol event to dispatch. |

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/644815f9e5bc52ad8f7a5227a456227e9c3e639b/libs/langgraph/langgraph/stream/_mux.py#L351)
