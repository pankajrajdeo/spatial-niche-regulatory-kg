---
title: "search"
description: "Search for threads."
source: "https://reference.langchain.com/python/langgraph-sdk/_sync/threads/SyncThreadsClient/search"
category: "reference"
tags: [reference, langgraph-sdk, sync, threads, syncthreadsclient, search]
---

# search

> **Method** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/_sync/threads/SyncThreadsClient/search)

Search for threads.

## Signature

```python
search(
    self,
    *,
    metadata: Json = None,
    values: Json = None,
    ids: Sequence[str] | None = None,
    status: ThreadStatus | None = None,
    limit: int = 10,
    offset: int = 0,
    sort_by: ThreadSortBy | None = None,
    sort_order: SortOrder | None = None,
    select: list[ThreadSelectField] | None = None,
    extract: dict[str, str] | None = None,
    headers: Mapping[str, str] | None = None,
    params: QueryParamTypes | None = None,
) -> list[Thread]
```

## Description

???+ example "Example Usage"

```python
client = get_sync_client(url="http://localhost:2024")
threads = client.threads.search(
    metadata={"number":1},
    status="interrupted",
    limit=15,
    offset=5
)
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `metadata` | `Json` | No | Thread metadata to filter on. (default: `None`) |
| `values` | `Json` | No | State values to filter on. (default: `None`) |
| `ids` | `Sequence[str] \| None` | No | List of thread IDs to filter by. (default: `None`) |
| `status` | `ThreadStatus \| None` | No | Thread status to filter on. Must be one of 'idle', 'busy', 'interrupted' or 'error'. (default: `None`) |
| `limit` | `int` | No | Limit on number of threads to return. (default: `10`) |
| `offset` | `int` | No | Offset in threads table to start search from. (default: `0`) |
| `sort_by` | `ThreadSortBy \| None` | No | Sort by field. (default: `None`) |
| `sort_order` | `SortOrder \| None` | No | Sort order. (default: `None`) |
| `select` | `list[ThreadSelectField] \| None` | No | List of fields to include in the response. (default: `None`) |
| `extract` | `dict[str, str] \| None` | No | Dictionary mapping aliases to JSONB paths to extract from thread data. Paths use dot notation for nested keys and bracket notation for array indices (e.g., `{"last_msg": "values.messages[-1]"}`). Extracted values are returned in an `extracted` field on each thread. Maximum 10 paths per request. (default: `None`) |
| `headers` | `Mapping[str, str] \| None` | No | Optional custom headers to include with the request. (default: `None`) |
| `params` | `QueryParamTypes \| None` | No | Optional query parameters to include with the request. (default: `None`) |

## Returns

`list[Thread]`

List of the threads matching the search parameters.

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/d5f4b2aa960940effc8430165ab3604038e817af/libs/sdk-py/langgraph_sdk/_sync/threads.py#L292)
