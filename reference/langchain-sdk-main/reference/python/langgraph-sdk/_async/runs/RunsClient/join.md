---
title: "join"
description: "Block until a run is done. Returns the final state of the thread."
source: "https://reference.langchain.com/python/langgraph-sdk/_async/runs/RunsClient/join"
category: "reference"
tags: [reference, langgraph-sdk, async, runs, runsclient, join]
---

# join

> **Method** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/_async/runs/RunsClient/join)

Block until a run is done. Returns the final state of the thread.

## Signature

```python
join(
    self,
    thread_id: str,
    run_id: str,
    *,
    headers: Mapping[str, str] | None = None,
    params: QueryParamTypes | None = None,
) -> dict
```

## Description

???+ example "Example Usage"

```python
client = get_client(url="http://localhost:2024")
result =await client.runs.join(
    thread_id="thread_id_to_join",
    run_id="run_id_to_join"
)
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `thread_id` | `str` | Yes | The thread ID to join. |
| `run_id` | `str` | Yes | The run ID to join. |
| `headers` | `Mapping[str, str] \| None` | No | Optional custom headers to include with the request. (default: `None`) |
| `params` | `QueryParamTypes \| None` | No | Optional query parameters to include with the request. (default: `None`) |

## Returns

`dict`

`None`

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/d5f4b2aa960940effc8430165ab3604038e817af/libs/sdk-py/langgraph_sdk/_async/runs.py#L1060)
