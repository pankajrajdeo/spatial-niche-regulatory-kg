---
title: "get_state"
description: "Get the state of a thread."
source: "https://reference.langchain.com/python/langgraph/pregel/remote/RemoteGraph/get_state"
category: "reference"
tags: [reference, langgraph, pregel, remote, remotegraph, get_state]
---

# get_state

> **Method** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/pregel/remote/RemoteGraph/get_state)

Get the state of a thread.

This method calls `POST /threads/{thread_id}/state/checkpoint` if a
checkpoint is specified in the config or `GET /threads/{thread_id}/state`
if no checkpoint is specified.

## Signature

```python
get_state(
    self,
    config: RunnableConfig,
    *,
    subgraphs: bool = False,
    headers: dict[str, str] | None = None,
    params: QueryParamTypes | None = None,
) -> StateSnapshot
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `config` | `RunnableConfig` | Yes | A `RunnableConfig` that includes `thread_id` in the `configurable` field. |
| `subgraphs` | `bool` | No | Include subgraphs in the state. (default: `False`) |
| `headers` | `dict[str, str] \| None` | No | Optional custom headers to include with the request. (default: `None`) |
| `params` | `QueryParamTypes \| None` | No | Optional query parameters to include with the request. (default: `None`) |

## Returns

`StateSnapshot`

The latest state of the thread.

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/644815f9e5bc52ad8f7a5227a456227e9c3e639b/libs/langgraph/langgraph/pregel/remote.py#L436)
