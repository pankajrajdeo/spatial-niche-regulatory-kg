---
title: "signal_paused"
description: "Wake every active subscription iterator on interrupt (run pause)."
source: "https://reference.langchain.com/python/langgraph-sdk/stream/sync_controller/SyncStreamController/signal_paused"
category: "reference"
tags: [reference, langgraph-sdk, stream, sync_controller, syncstreamcontroller, signal_paused]
---

# signal_paused

> **Method** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/stream/sync_controller/SyncStreamController/signal_paused)

Wake every active subscription iterator on interrupt (run pause).

Pushes the terminal sentinel (`None`) into every subscription queue.
Iterators see `None` and return; the shared SSE keeps running so
re-iteration after `run.respond(...)` registers a fresh subscription
and resumes.

## Signature

```python
signal_paused(
    self,
) -> None
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/d5f4b2aa960940effc8430165ab3604038e817af/libs/sdk-py/langgraph_sdk/stream/sync_controller.py#L106)
