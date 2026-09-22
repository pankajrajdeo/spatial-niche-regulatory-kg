---
title: "subscribe"
description: "Open a typed subscription against the shared SSE."
source: "https://reference.langchain.com/python/langgraph-sdk/_async/stream/AsyncThreadStream/subscribe"
category: "reference"
tags: [reference, langgraph-sdk, async, stream, asyncthreadstream, subscribe]
---

# subscribe

> **Method** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/_async/stream/AsyncThreadStream/subscribe)

Open a typed subscription against the shared SSE.

Returns an async iterator that yields raw `Event` dicts matching the
given filter. Multiple concurrent subscribes share one HTTP connection
whose union expands or rotates as subscriptions come and go.

## Signature

```python
subscribe(
    self,
    channels: list[str],
    *,
    namespaces: list[list[str]] | None = None,
    depth: int | None = None,
) -> AsyncIterator[Event]
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/d5f4b2aa960940effc8430165ab3604038e817af/libs/sdk-py/langgraph_sdk/_async/stream.py#L1397)
