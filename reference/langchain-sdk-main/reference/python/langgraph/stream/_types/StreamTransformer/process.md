---
title: "process"
description: "Handle an event on the sync lane."
source: "https://reference.langchain.com/python/langgraph/stream/_types/StreamTransformer/process"
category: "reference"
tags: [reference, langgraph, stream, types, streamtransformer, process]
---

# process

> **Method** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/stream/_types/StreamTransformer/process)

Handle an event on the sync lane.

Called for every event before it is appended to the main event
log. Subclasses must override either `process` or `aprocess`.
The default raises so a missing override fails loudly rather
than silently passing every event through.

## Signature

```python
process(
    self,
    event: ProtocolEvent,
) -> bool
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `event` | `ProtocolEvent` | Yes | The protocol event to observe. |

## Returns

`bool`

True to keep the event in the main log, False to suppress it.

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/644815f9e5bc52ad8f7a5227a456227e9c3e639b/libs/langgraph/langgraph/stream/_types.py#L148)
