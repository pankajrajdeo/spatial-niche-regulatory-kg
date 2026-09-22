---
title: "stream"
description: "Open a v3 thread-centric streaming session."
source: "https://reference.langchain.com/python/langgraph-sdk/_sync/threads/SyncThreadsClient/stream"
category: "reference"
tags: [reference, langgraph-sdk, sync, threads, syncthreadsclient, stream]
---

# stream

> **Method** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/_sync/threads/SyncThreadsClient/stream)

Open a v3 thread-centric streaming session.

## Signature

```python
stream(
    self,
    thread_id: str | None = None,
    *,
    assistant_id: str,
    headers: Mapping[str, str] | None = None,
    run_start_timeout: float | None = None,
    transport: Literal['sse', 'websocket'] = 'sse',
) -> SyncThreadStream
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `thread_id` | `str \| None` | No | optional explicit thread identifier. Defaults to a fresh UUIDv4. (default: `None`) |
| `assistant_id` | `str` | Yes | assistant the run will use. Required. |
| `headers` | `Mapping[str, str] \| None` | No | optional headers forwarded on every command and SSE request for this stream session. (default: `None`) |
| `transport` | `Literal['sse', 'websocket']` | No | event transport to use, `"sse"` (default) or `"websocket"`. (default: `'sse'`) |

## Returns

`SyncThreadStream`

A `SyncThreadStream` to use as a context manager.

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/d5f4b2aa960940effc8430165ab3604038e817af/libs/sdk-py/langgraph_sdk/_sync/threads.py#L727)
