---
title: "get"
description: "Get a thread by ID."
source: "https://reference.langchain.com/python/langgraph-sdk/_sync/threads/SyncThreadsClient/get"
category: "reference"
tags: [reference, langgraph-sdk, sync, threads, syncthreadsclient, get]
---

# get

> **Method** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/_sync/threads/SyncThreadsClient/get)

Get a thread by ID.

## Signature

```python
get(
    self,
    thread_id: str,
    *,
    include: Sequence[str] | None = None,
    headers: Mapping[str, str] | None = None,
    params: QueryParamTypes | None = None,
) -> Thread
```

## Description

???+ example "Example Usage"

```python
client = get_sync_client(url="http://localhost:2024")
thread = client.threads.get(
    thread_id="my_thread_id"
)
print(thread)
```
```shell
-----------------------------------------------------

{
    'thread_id': 'my_thread_id',
    'created_at': '2024-07-18T18:35:15.540834+00:00',
    'updated_at': '2024-07-18T18:35:15.540834+00:00',
    'metadata': {'graph_id': 'agent'}
}
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `thread_id` | `str` | Yes | The ID of the thread to get. |
| `include` | `Sequence[str] \| None` | No | Additional fields to include in the response. Supported values: `"ttl"`. (default: `None`) |
| `headers` | `Mapping[str, str] \| None` | No | Optional custom headers to include with the request. (default: `None`) |
| `params` | `QueryParamTypes \| None` | No | Optional query parameters to include with the request. (default: `None`) |

## Returns

`Thread`

`Thread` object.

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/d5f4b2aa960940effc8430165ab3604038e817af/libs/sdk-py/langgraph_sdk/_sync/threads.py#L47)
