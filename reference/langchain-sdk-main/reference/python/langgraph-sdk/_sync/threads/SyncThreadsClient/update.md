---
title: "update"
description: "Update a thread."
source: "https://reference.langchain.com/python/langgraph-sdk/_sync/threads/SyncThreadsClient/update"
category: "reference"
tags: [reference, langgraph-sdk, sync, threads, syncthreadsclient, update]
---

# update

> **Method** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/_sync/threads/SyncThreadsClient/update)

Update a thread.

## Signature

```python
update(
    self,
    thread_id: str,
    *,
    metadata: Mapping[str, Any],
    ttl: int | Mapping[str, Any] | None = None,
    return_minimal: bool = False,
    headers: Mapping[str, str] | None = None,
    params: QueryParamTypes | None = None,
) -> Thread | None
```

## Description

???+ example "Example Usage"

```python
client = get_sync_client(url="http://localhost:2024")
thread = client.threads.update(
    thread_id="my-thread-id",
    metadata={"number":1},
    ttl=43_200,
)
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `thread_id` | `str` | Yes | ID of thread to update. |
| `metadata` | `Mapping[str, Any]` | Yes | Metadata to merge with existing thread metadata. |
| `ttl` | `int \| Mapping[str, Any] \| None` | No | Optional time-to-live in minutes for the thread. You can pass an integer (minutes) or a mapping with keys `ttl` and optional `strategy` (defaults to "delete"). (default: `None`) |
| `return_minimal` | `bool` | No | If `True`, request a 204 response with no body. (default: `False`) |
| `headers` | `Mapping[str, str] \| None` | No | Optional custom headers to include with the request. (default: `None`) |
| `params` | `QueryParamTypes \| None` | No | Optional query parameters to include with the request. (default: `None`) |

## Returns

`Thread | None`

The updated `Thread`, or `None` when `return_minimal=True`.

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/d5f4b2aa960940effc8430165ab3604038e817af/libs/sdk-py/langgraph_sdk/_sync/threads.py#L210)
