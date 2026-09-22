---
title: "aget_state_history"
description: "Get the state history of a thread."
source: "https://reference.langchain.com/python/langgraph/pregel/remote/RemoteGraph/aget_state_history"
category: "reference"
tags: [reference, langgraph, pregel, remote, remotegraph, aget_state_history]
---

# aget_state_history

> **Method** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/pregel/remote/RemoteGraph/aget_state_history)

Get the state history of a thread.

This method calls `POST /threads/{thread_id}/history`.

## Signature

```python
aget_state_history(
    self,
    config: RunnableConfig,
    *,
    filter: dict[str, Any] | None = None,
    before: RunnableConfig | None = None,
    limit: int | None = None,
    headers: dict[str, str] | None = None,
    params: QueryParamTypes | None = None,
) -> AsyncIterator[StateSnapshot]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `config` | `RunnableConfig` | Yes | A `RunnableConfig` that includes `thread_id` in the `configurable` field. |
| `filter` | `dict[str, Any] \| None` | No | Metadata to filter on. (default: `None`) |
| `before` | `RunnableConfig \| None` | No | A `RunnableConfig` that includes checkpoint metadata. (default: `None`) |
| `limit` | `int \| None` | No | Max number of states to return. (default: `None`) |
| `headers` | `dict[str, str] \| None` | No | Optional custom headers to include with the request. (default: `None`) |
| `params` | `QueryParamTypes \| None` | No | Optional query parameters to include with the request. (default: `None`) |

## Returns

`AsyncIterator[StateSnapshot]`

States of the thread.

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/644815f9e5bc52ad8f7a5227a456227e9c3e639b/libs/langgraph/langgraph/pregel/remote.py#L547)
