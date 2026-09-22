---
title: "aupdate_state"
description: "Update the state of a thread."
source: "https://reference.langchain.com/python/langgraph/pregel/remote/RemoteGraph/aupdate_state"
category: "reference"
tags: [reference, langgraph, pregel, remote, remotegraph, aupdate_state]
---

# aupdate_state

> **Method** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/pregel/remote/RemoteGraph/aupdate_state)

Update the state of a thread.

This method calls `POST /threads/{thread_id}/state`.

## Signature

```python
aupdate_state(
    self,
    config: RunnableConfig,
    values: dict[str, Any] | Any | None,
    as_node: str | None = None,
    *,
    headers: dict[str, str] | None = None,
    params: QueryParamTypes | None = None,
) -> RunnableConfig
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `config` | `RunnableConfig` | Yes | A `RunnableConfig` that includes `thread_id` in the `configurable` field. |
| `values` | `dict[str, Any] \| Any \| None` | Yes | Values to update to the state. |
| `as_node` | `str \| None` | No | Update the state as if this node had just executed. (default: `None`) |

## Returns

`RunnableConfig`

`RunnableConfig` for the updated thread.

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/644815f9e5bc52ad8f7a5227a456227e9c3e639b/libs/langgraph/langgraph/pregel/remote.py#L637)
