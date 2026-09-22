---
title: "get"
description: "Get a run."
source: "https://reference.langchain.com/python/langgraph-sdk/_sync/runs/SyncRunsClient/get"
category: "reference"
tags: [reference, langgraph-sdk, sync, runs, syncrunsclient, get]
---

# get

> **Method** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/_sync/runs/SyncRunsClient/get)

Get a run.

## Signature

```python
get(
    self,
    thread_id: str,
    run_id: str,
    *,
    headers: Mapping[str, str] | None = None,
    params: QueryParamTypes | None = None,
) -> Run
```

## Description

???+ example "Example Usage"

```python

run = client.runs.get(
    thread_id="thread_id_to_delete",
    run_id="run_id_to_delete",
)
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `thread_id` | `str` | Yes | The thread ID to get. |
| `run_id` | `str` | Yes | The run ID to get. |
| `headers` | `Mapping[str, str] \| None` | No | Optional custom headers to include with the request. (default: `None`) |

## Returns

`Run`

`Run` object.

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/d5f4b2aa960940effc8430165ab3604038e817af/libs/sdk-py/langgraph_sdk/_sync/runs.py#L890)
