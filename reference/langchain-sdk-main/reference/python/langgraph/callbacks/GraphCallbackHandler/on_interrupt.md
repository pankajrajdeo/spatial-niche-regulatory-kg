---
title: "on_interrupt"
description: "Run when graph execution pauses due to one or more interrupts."
source: "https://reference.langchain.com/python/langgraph/callbacks/GraphCallbackHandler/on_interrupt"
category: "reference"
tags: [reference, langgraph, callbacks, graphcallbackhandler, on_interrupt]
---

# on_interrupt

> **Method** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/callbacks/GraphCallbackHandler/on_interrupt)

Run when graph execution pauses due to one or more interrupts.

## Signature

```python
on_interrupt(
    self,
    event: GraphInterruptEvent,
) -> Any
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `event` | `GraphInterruptEvent` | Yes | Interrupt lifecycle event payload. |

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/644815f9e5bc52ad8f7a5227a456227e9c3e639b/libs/langgraph/langgraph/callbacks.py#L99)
