---
title: "count"
description: "Count threads matching filters."
source: "https://reference.langchain.com/python/langgraph-sdk/_async/threads/ThreadsClient/count"
category: "reference"
tags: [reference, langgraph-sdk, async, threads, threadsclient, count]
---

# count

> **Method** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/_async/threads/ThreadsClient/count)

Count threads matching filters.

## Signature

```python
count(
    self,
    *,
    metadata: Json = None,
    values: Json = None,
    status: ThreadStatus | None = None,
    headers: Mapping[str, str] | None = None,
    params: QueryParamTypes | None = None,
) -> int
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `metadata` | `Json` | No | Thread metadata to filter on. (default: `None`) |
| `values` | `Json` | No | State values to filter on. (default: `None`) |
| `status` | `ThreadStatus \| None` | No | Thread status to filter on. (default: `None`) |
| `headers` | `Mapping[str, str] \| None` | No | Optional custom headers to include with the request. (default: `None`) |
| `params` | `QueryParamTypes \| None` | No | Optional query parameters to include with the request. (default: `None`) |

## Returns

`int`

Number of threads matching the criteria.

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/d5f4b2aa960940effc8430165ab3604038e817af/libs/sdk-py/langgraph_sdk/_async/threads.py#L378)
