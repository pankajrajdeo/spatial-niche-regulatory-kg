---
title: "get_history"
description: "Get the state history of a thread."
source: "https://reference.langchain.com/python/langgraph-sdk/_sync/threads/SyncThreadsClient/get_history"
category: "reference"
tags: [reference, langgraph-sdk, sync, threads, syncthreadsclient, get_history]
---

# get_history

> **Method** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/_sync/threads/SyncThreadsClient/get_history)

Get the state history of a thread.

## Signature

```python
get_history(
    self,
    thread_id: str,
    *,
    limit: int = 10,
    before: str | Checkpoint | None = None,
    metadata: Mapping[str, Any] | None = None,
    checkpoint: Checkpoint | None = None,
    headers: Mapping[str, str] | None = None,
    params: QueryParamTypes | None = None,
) -> list[ThreadState]
```

## Description

???+ example "Example Usage"

```python

thread_state = client.threads.get_history(
    thread_id="my_thread_id",
    limit=5,
    before="my_timestamp",
    metadata={"name":"my_name"}
)
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `thread_id` | `str` | Yes | The ID of the thread to get the state history for. |
| `checkpoint` | `Checkpoint \| None` | No | Return states for this subgraph. If empty defaults to root. (default: `None`) |
| `limit` | `int` | No | The maximum number of states to return. (default: `10`) |
| `before` | `str \| Checkpoint \| None` | No | Return states before this checkpoint. (default: `None`) |
| `metadata` | `Mapping[str, Any] \| None` | No | Filter states by metadata key-value pairs. (default: `None`) |
| `headers` | `Mapping[str, str] \| None` | No | Optional custom headers to include with the request. (default: `None`) |

## Returns

`list[ThreadState]`

The state history of the `Thread`.

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/d5f4b2aa960940effc8430165ab3604038e817af/libs/sdk-py/langgraph_sdk/_sync/threads.py#L674)
