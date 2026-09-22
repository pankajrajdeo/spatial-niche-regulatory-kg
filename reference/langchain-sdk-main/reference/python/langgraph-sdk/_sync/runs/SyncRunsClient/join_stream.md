---
title: "join_stream"
description: "Stream output from a run in real-time, until the run is done. Output is not buffered, so any output produced before this call will not be received here."
source: "https://reference.langchain.com/python/langgraph-sdk/_sync/runs/SyncRunsClient/join_stream"
category: "reference"
tags: [reference, langgraph-sdk, sync, runs, syncrunsclient, join_stream]
---

# join_stream

> **Method** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/_sync/runs/SyncRunsClient/join_stream)

Stream output from a run in real-time, until the run is done.
Output is not buffered, so any output produced before this call will
not be received here.

## Signature

```python
join_stream(
    self,
    thread_id: str,
    run_id: str,
    *,
    cancel_on_disconnect: bool = False,
    stream_mode: StreamMode | Sequence[StreamMode] | None = None,
    headers: Mapping[str, str] | None = None,
    params: QueryParamTypes | None = None,
    last_event_id: str | None = None,
) -> Iterator[StreamPart]
```

## Description

???+ example "Example Usage"

```python
client = get_sync_client(url="http://localhost:2024")
client.runs.join_stream(
    thread_id="thread_id_to_join",
    run_id="run_id_to_join",
    stream_mode=["values", "debug"]
)
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `thread_id` | `str` | Yes | The thread ID to join. |
| `run_id` | `str` | Yes | The run ID to join. |
| `stream_mode` | `StreamMode \| Sequence[StreamMode] \| None` | No | The stream mode(s) to use. Must be a subset of the stream modes passed when creating the run. Background runs default to having the union of all stream modes. (default: `None`) |
| `cancel_on_disconnect` | `bool` | No | Whether to cancel the run when the stream is disconnected. (default: `False`) |
| `headers` | `Mapping[str, str] \| None` | No | Optional custom headers to include with the request. (default: `None`) |
| `params` | `QueryParamTypes \| None` | No | Optional query parameters to include with the request. (default: `None`) |
| `last_event_id` | `str \| None` | No | The last event ID to use for the stream. (default: `None`) |

## Returns

`Iterator[StreamPart]`

`None`

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/d5f4b2aa960940effc8430165ab3604038e817af/libs/sdk-py/langgraph_sdk/_sync/runs.py#L1079)
