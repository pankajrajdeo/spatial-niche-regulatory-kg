---
title: "delete"
description: "Delete a thread."
source: "https://reference.langchain.com/python/langgraph-sdk/_sync/threads/SyncThreadsClient/delete"
category: "reference"
tags: [reference, langgraph-sdk, sync, threads, syncthreadsclient, delete]
---

# delete

> **Method** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/_sync/threads/SyncThreadsClient/delete)

Delete a thread.

## Signature

```python
delete(
    self,
    thread_id: str,
    *,
    headers: Mapping[str, str] | None = None,
    params: QueryParamTypes | None = None,
) -> None
```

## Description

???+ example "Example Usage"

```python
client.threads.delete(
    thread_id="my_thread_id"
)
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `thread_id` | `str` | Yes | The ID of the thread to delete. |
| `headers` | `Mapping[str, str] \| None` | No | Optional custom headers to include with the request. (default: `None`) |
| `params` | `QueryParamTypes \| None` | No | Optional query parameters to include with the request. (default: `None`) |

## Returns

`None`

`None`

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/d5f4b2aa960940effc8430165ab3604038e817af/libs/sdk-py/langgraph_sdk/_sync/threads.py#L262)
