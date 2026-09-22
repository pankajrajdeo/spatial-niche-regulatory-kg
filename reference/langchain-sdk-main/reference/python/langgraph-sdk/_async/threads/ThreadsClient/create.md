---
title: "create"
description: "Create a new thread."
source: "https://reference.langchain.com/python/langgraph-sdk/_async/threads/ThreadsClient/create"
category: "reference"
tags: [reference, langgraph-sdk, async, threads, threadsclient, create]
---

# create

> **Method** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/_async/threads/ThreadsClient/create)

Create a new thread.

## Signature

```python
create(
    self,
    *,
    metadata: Json = None,
    thread_id: str | None = None,
    if_exists: OnConflictBehavior | None = None,
    supersteps: Sequence[dict[str, Sequence[dict[str, Any]]]] | None = None,
    graph_id: str | None = None,
    ttl: int | Mapping[str, Any] | None = None,
    headers: Mapping[str, str] | None = None,
    params: QueryParamTypes | None = None,
) -> Thread
```

## Description

???+ example "Example Usage"

```python
client = get_client(url="http://localhost:2024")
thread = await client.threads.create(
    metadata={"number":1},
    thread_id="my-thread-id",
    if_exists="raise"
)
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `metadata` | `Json` | No | Metadata to add to thread. (default: `None`) |
| `thread_id` | `str \| None` | No | ID of thread. If `None`, ID will be a randomly generated UUID. (default: `None`) |
| `if_exists` | `OnConflictBehavior \| None` | No | How to handle duplicate creation. Defaults to 'raise' under the hood. Must be either 'raise' (raise error if duplicate), or 'do_nothing' (return existing thread). (default: `None`) |
| `supersteps` | `Sequence[dict[str, Sequence[dict[str, Any]]]] \| None` | No | Apply a list of supersteps when creating a thread, each containing a sequence of updates. Each update has `values` or `command` and `as_node`. Used for copying a thread between deployments. (default: `None`) |
| `graph_id` | `str \| None` | No | Optional graph ID to associate with the thread. (default: `None`) |
| `ttl` | `int \| Mapping[str, Any] \| None` | No | Optional time-to-live in minutes for the thread. You can pass an integer (minutes) or a mapping with keys `ttl` and optional `strategy` (defaults to "delete"). (default: `None`) |
| `headers` | `Mapping[str, str] \| None` | No | Optional custom headers to include with the request. (default: `None`) |
| `params` | `QueryParamTypes \| None` | No | Optional query parameters to include with the request. (default: `None`) |

## Returns

`Thread`

The created thread.

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/d5f4b2aa960940effc8430165ab3604038e817af/libs/sdk-py/langgraph_sdk/_async/threads.py#L101)
