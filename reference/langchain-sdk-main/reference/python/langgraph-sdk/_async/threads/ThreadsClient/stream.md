---
title: "stream"
description: "Open a v3 thread-centric streaming session."
source: "https://reference.langchain.com/python/langgraph-sdk/_async/threads/ThreadsClient/stream"
category: "reference"
tags: [reference, langgraph-sdk, async, threads, threadsclient, stream]
---

# stream

> **Method** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/_async/threads/ThreadsClient/stream)

Open a v3 thread-centric streaming session.

When `thread_id` is None, a fresh UUIDv4 is minted client-side and
included in the URL of subsequent `POST /threads/{thread_id}/...`
calls. The server creates the thread row lazily on the first
`run.start` (internal server detail — the SDK does not send any
`if_not_exists` flag). The v3 protocol response carries only
`run_id`, never `thread_id` — that's why the SDK mints the id
client-side.

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
) -> AsyncThreadStream
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `thread_id` | `str \| None` | No | optional explicit thread identifier. Defaults to a fresh UUIDv4. (default: `None`) |
| `assistant_id` | `str` | Yes | assistant the run will use. Required. |
| `headers` | `Mapping[str, str] \| None` | No | optional headers forwarded on every command and event request for this stream session. (default: `None`) |
| `run_start_timeout` | `float \| None` | No | optional seconds to wait for an in-flight `run.start` before subscribing operations raise `asyncio.TimeoutError`. Defaults to `None` (wait forever). (default: `None`) |
| `transport` | `Literal['sse', 'websocket']` | No | event transport to use — `"sse"` (default) or `"websocket"`. (default: `'sse'`) |

## Returns

`AsyncThreadStream`

An `AsyncThreadStream` to use as an async context manager.

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/d5f4b2aa960940effc8430165ab3604038e817af/libs/sdk-py/langgraph_sdk/_async/threads.py#L739)
