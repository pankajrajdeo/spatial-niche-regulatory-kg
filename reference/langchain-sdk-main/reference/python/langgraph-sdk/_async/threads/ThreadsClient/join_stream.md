---
title: "join_stream"
description: "Get a stream of events for a thread."
source: "https://reference.langchain.com/python/langgraph-sdk/_async/threads/ThreadsClient/join_stream"
category: "reference"
tags: [reference, langgraph-sdk, async, threads, threadsclient, join_stream]
---

# join_stream

> **Method** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/_async/threads/ThreadsClient/join_stream)

Get a stream of events for a thread.

## Signature

```python
join_stream(
    self,
    thread_id: str,
    *,
    last_event_id: str | None = None,
    stream_mode: ThreadStreamMode | Sequence[ThreadStreamMode] = 'run_modes',
    headers: Mapping[str, str] | None = None,
    params: QueryParamTypes | None = None,
) -> AsyncIterator[StreamPart]
```

## Description

???+ example "Example Usage"

```python

for chunk in client.threads.join_stream(
    thread_id="my_thread_id",
    last_event_id="my_event_id",
):
    print(chunk)
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `thread_id` | `str` | Yes | The ID of the thread to get the stream for. |
| `last_event_id` | `str \| None` | No | The ID of the last event to get. (default: `None`) |
| `headers` | `Mapping[str, str] \| None` | No | Optional custom headers to include with the request. (default: `None`) |
| `params` | `QueryParamTypes \| None` | No | Optional query parameters to include with the request. (default: `None`) |

## Returns

`AsyncIterator[StreamPart]`

An iterator of stream parts.

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/d5f4b2aa960940effc8430165ab3604038e817af/libs/sdk-py/langgraph_sdk/_async/threads.py#L785)
