---
title: "cancel"
description: "Get a run."
source: "https://reference.langchain.com/python/langgraph-sdk/_sync/runs/SyncRunsClient/cancel"
category: "reference"
tags: [reference, langgraph-sdk, sync, runs, syncrunsclient, cancel]
---

# cancel

> **Method** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/_sync/runs/SyncRunsClient/cancel)

Get a run.

## Signature

```python
cancel(
    self,
    thread_id: str,
    run_id: str,
    *,
    wait: bool = False,
    action: CancelAction = 'interrupt',
    headers: Mapping[str, str] | None = None,
    params: QueryParamTypes | None = None,
) -> None
```

## Description

???+ example "Example Usage"

```python
client = get_sync_client(url="http://localhost:2024")
client.runs.cancel(
    thread_id="thread_id_to_cancel",
    run_id="run_id_to_cancel",
    wait=True,
    action="interrupt"
)
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `thread_id` | `str` | Yes | The thread ID to cancel. |
| `run_id` | `str` | Yes | The run ID to cancel. |
| `wait` | `bool` | No | Whether to wait until run has completed. (default: `False`) |
| `action` | `CancelAction` | No | Action to take when cancelling the run. Possible values are `interrupt` or `rollback`. Default is `interrupt`. (default: `'interrupt'`) |
| `headers` | `Mapping[str, str] \| None` | No | Optional custom headers to include with the request. (default: `None`) |
| `params` | `QueryParamTypes \| None` | No | Optional query parameters to include with the request. (default: `None`) |

## Returns

`None`

`None`

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/d5f4b2aa960940effc8430165ab3604038e817af/libs/sdk-py/langgraph_sdk/_sync/runs.py#L925)
