---
title: "cancel_many"
description: "Cancel one or more runs."
source: "https://reference.langchain.com/python/langgraph-sdk/_sync/runs/SyncRunsClient/cancel_many"
category: "reference"
tags: [reference, langgraph-sdk, sync, runs, syncrunsclient, cancel_many]
---

# cancel_many

> **Method** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/_sync/runs/SyncRunsClient/cancel_many)

Cancel one or more runs.

Can cancel runs by thread ID and run IDs, or by status filter.

## Signature

```python
cancel_many(
    self,
    *,
    thread_id: str | None = None,
    run_ids: Sequence[str] | None = None,
    status: BulkCancelRunsStatus | None = None,
    action: CancelAction = 'interrupt',
    headers: Mapping[str, str] | None = None,
    params: QueryParamTypes | None = None,
) -> None
```

## Description

???+ example "Example Usage"

```python
client = get_sync_client(url="http://localhost:2024")
# Cancel all pending runs
client.runs.cancel_many(status="pending")
# Cancel specific runs on a thread
client.runs.cancel_many(
    thread_id="my_thread_id",
    run_ids=["run_1", "run_2"],
    action="rollback",
)
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `thread_id` | `str \| None` | No | The ID of the thread containing runs to cancel. (default: `None`) |
| `run_ids` | `Sequence[str] \| None` | No | List of run IDs to cancel. (default: `None`) |
| `status` | `BulkCancelRunsStatus \| None` | No | Filter runs by status to cancel. Must be one of `"pending"`, `"running"`, or `"all"`. (default: `None`) |
| `action` | `CancelAction` | No | Action to take when cancelling the run. Possible values are `"interrupt"` or `"rollback"`. Default is `"interrupt"`. (default: `'interrupt'`) |
| `headers` | `Mapping[str, str] \| None` | No | Optional custom headers to include with the request. (default: `None`) |
| `params` | `QueryParamTypes \| None` | No | Optional query parameters to include with the request. (default: `None`) |

## Returns

`None`

`None`

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/d5f4b2aa960940effc8430165ab3604038e817af/libs/sdk-py/langgraph_sdk/_sync/runs.py#L983)
