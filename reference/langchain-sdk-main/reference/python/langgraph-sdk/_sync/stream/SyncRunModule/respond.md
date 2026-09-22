---
title: "respond"
description: "Reply to a server-side interrupt and resume the run."
source: "https://reference.langchain.com/python/langgraph-sdk/_sync/stream/SyncRunModule/respond"
category: "reference"
tags: [reference, langgraph-sdk, sync, stream, syncrunmodule, respond]
---

# respond

> **Method** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/_sync/stream/SyncRunModule/respond)

Reply to a server-side interrupt and resume the run.

## Signature

```python
respond(
    self,
    response: Any,
    *,
    interrupt_id: str | None = None,
) -> dict[str, Any]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `response` | `Any` | Yes | the response value forwarded as `params.response` on the wire. |
| `interrupt_id` | `str \| None` | No | optional explicit id. When omitted, requires exactly one outstanding interrupt. (default: `None`) |

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/d5f4b2aa960940effc8430165ab3604038e817af/libs/sdk-py/langgraph_sdk/_sync/stream.py#L237)
