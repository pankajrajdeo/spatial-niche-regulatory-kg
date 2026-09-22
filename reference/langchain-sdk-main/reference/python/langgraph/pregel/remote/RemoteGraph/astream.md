---
title: "astream"
description: "Create a run and stream the results."
source: "https://reference.langchain.com/python/langgraph/pregel/remote/RemoteGraph/astream"
category: "reference"
tags: [reference, langgraph, pregel, remote, remotegraph, astream]
---

# astream

> **Method** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/pregel/remote/RemoteGraph/astream)

Create a run and stream the results.

This method calls `POST /threads/{thread_id}/runs/stream` if a `thread_id`
is specified in the `configurable` field of the config or
`POST /runs/stream` otherwise.

## Signature

```python
astream(
    self,
    input: dict[str, Any] | Any,
    config: RunnableConfig | None = None,
    *,
    context: Context | None = None,
    stream_mode: StreamMode | list[StreamMode] | None = None,
    interrupt_before: All | Sequence[str] | None = None,
    interrupt_after: All | Sequence[str] | None = None,
    subgraphs: bool = False,
    headers: dict[str, str] | None = None,
    params: QueryParamTypes | None = None,
    version: Literal['v1', 'v2'] = 'v1',
    **kwargs: Any = {},
) -> AsyncIterator[dict[str, Any] | Any]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `input` | `dict[str, Any] \| Any` | Yes | Input to the graph. |
| `config` | `RunnableConfig \| None` | No | A `RunnableConfig` for graph invocation. (default: `None`) |
| `stream_mode` | `StreamMode \| list[StreamMode] \| None` | No | Stream mode(s) to use. (default: `None`) |
| `interrupt_before` | `All \| Sequence[str] \| None` | No | Interrupt the graph before these nodes. (default: `None`) |
| `interrupt_after` | `All \| Sequence[str] \| None` | No | Interrupt the graph after these nodes. (default: `None`) |
| `subgraphs` | `bool` | No | Stream from subgraphs. (default: `False`) |
| `headers` | `dict[str, str] \| None` | No | Additional headers to pass to the request. (default: `None`) |
| `**kwargs` | `Any` | No | Additional params to pass to client.runs.stream. (default: `{}`) |

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/644815f9e5bc52ad8f7a5227a456227e9c3e639b/libs/langgraph/langgraph/pregel/remote.py#L912)
