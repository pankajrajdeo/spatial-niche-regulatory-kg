---
title: "list"
description: "List runs."
source: "https://reference.langchain.com/python/langgraph-sdk/_async/runs/RunsClient/list"
category: "reference"
tags: [reference, langgraph-sdk, async, runs, runsclient, list]
---

# list

> **Method** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/_async/runs/RunsClient/list)

List runs.

## Signature

```python
list(
    self,
    thread_id: str,
    *,
    limit: int = 10,
    offset: int = 0,
    status: RunStatus | None = None,
    select: builtins.list[RunSelectField] | None = None,
    headers: Mapping[str, str] | None = None,
    params: QueryParamTypes | None = None,
) -> builtins.list[Run]
```

## Description

???+ example "Example Usage"

```python
client = get_client(url="http://localhost:2024")
await client.runs.list(
    thread_id="thread_id",
    limit=5,
    offset=5,
)
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `thread_id` | `str` | Yes | The thread ID to list runs for. |
| `limit` | `int` | No | The maximum number of results to return. (default: `10`) |
| `offset` | `int` | No | The number of results to skip. (default: `0`) |
| `status` | `RunStatus \| None` | No | The status of the run to filter by. (default: `None`) |
| `headers` | `Mapping[str, str] \| None` | No | Optional custom headers to include with the request. (default: `None`) |
| `params` | `QueryParamTypes \| None` | No | Optional query parameters to include with the request. (default: `None`) |

## Returns

`builtins.list[Run]`

The runs for the thread.

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/d5f4b2aa960940effc8430165ab3604038e817af/libs/sdk-py/langgraph_sdk/_async/runs.py#L854)
