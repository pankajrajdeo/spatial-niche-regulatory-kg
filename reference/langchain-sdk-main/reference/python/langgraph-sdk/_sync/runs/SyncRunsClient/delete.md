---
title: "delete"
description: "Delete a run."
source: "https://reference.langchain.com/python/langgraph-sdk/_sync/runs/SyncRunsClient/delete"
category: "reference"
tags: [reference, langgraph-sdk, sync, runs, syncrunsclient, delete]
---

# delete

> **Method** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/_sync/runs/SyncRunsClient/delete)

Delete a run.

## Signature

```python
delete(
    self,
    thread_id: str,
    run_id: str,
    *,
    headers: Mapping[str, str] | None = None,
    params: QueryParamTypes | None = None,
) -> None
```

## Description

???+ example "Example Usage"

```python
client = get_sync_client(url="http://localhost:2024")
client.runs.delete(
    thread_id="thread_id_to_delete",
    run_id="run_id_to_delete"
)
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `thread_id` | `str` | Yes | The thread ID to delete. |
| `run_id` | `str` | Yes | The run ID to delete. |
| `headers` | `Mapping[str, str] \| None` | No | Optional custom headers to include with the request. (default: `None`) |
| `params` | `QueryParamTypes \| None` | No | Optional query parameters to include with the request. (default: `None`) |

## Returns

`None`

`None`

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/d5f4b2aa960940effc8430165ab3604038e817af/libs/sdk-py/langgraph_sdk/_sync/runs.py#L1137)
