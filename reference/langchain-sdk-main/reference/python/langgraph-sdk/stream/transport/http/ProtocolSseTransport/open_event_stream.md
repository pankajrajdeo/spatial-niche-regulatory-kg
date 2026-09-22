---
title: "open_event_stream"
description: "Open an independent filtered SSE event stream."
source: "https://reference.langchain.com/python/langgraph-sdk/stream/transport/http/ProtocolSseTransport/open_event_stream"
category: "reference"
tags: [reference, langgraph-sdk, stream, transport, http, protocolssetransport, open_event_stream]
---

# open_event_stream

> **Method** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/stream/transport/http/ProtocolSseTransport/open_event_stream)

Open an independent filtered SSE event stream.

Posts `params` as a SubscribeParams body to `/threads/{thread_id}/stream/events`.
Returns an `EventStreamHandle` whose `events` async iterator yields typed
`Event` dicts as the server emits them. `handle.ready` resolves on a 2xx
response (rejects on HTTP error or transport failure before headers).

Reconnect: pass `params["since"]` to filter outbound seqs server-side. The
cursor goes in the request body, not as a `Last-Event-ID` header.

## Signature

```python
open_event_stream(
    self,
    params: dict[str, Any],
) -> EventStreamHandle
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/d5f4b2aa960940effc8430165ab3604038e817af/libs/sdk-py/langgraph_sdk/stream/transport/http.py#L96)
