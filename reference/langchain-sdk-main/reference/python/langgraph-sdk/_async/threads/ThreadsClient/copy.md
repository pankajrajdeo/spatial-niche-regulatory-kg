---
title: "copy"
description: "Copy a thread."
source: "https://reference.langchain.com/python/langgraph-sdk/_async/threads/ThreadsClient/copy"
category: "reference"
tags: [reference, langgraph-sdk, async, threads, threadsclient, copy]
---

# copy

> **Method** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/_async/threads/ThreadsClient/copy)

Copy a thread.

## Signature

```python
copy(
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
client = get_client(url="http://localhost:2024)
await client.threads.copy(
    thread_id="my_thread_id"
)
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `thread_id` | `str` | Yes | The ID of the thread to copy. |
| `headers` | `Mapping[str, str] \| None` | No | Optional custom headers to include with the request. (default: `None`) |
| `params` | `QueryParamTypes \| None` | No | Optional query parameters to include with the request. (default: `None`) |

## Returns

`None`

`None`

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/d5f4b2aa960940effc8430165ab3604038e817af/libs/sdk-py/langgraph_sdk/_async/threads.py#L410)
