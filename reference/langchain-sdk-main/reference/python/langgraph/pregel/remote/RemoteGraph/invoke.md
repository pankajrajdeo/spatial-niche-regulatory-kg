---
title: "invoke"
description: "Create a run, wait until it finishes and return the final state."
source: "https://reference.langchain.com/python/langgraph/pregel/remote/RemoteGraph/invoke"
category: "reference"
tags: [reference, langgraph, pregel, remote, remotegraph, invoke]
---

# invoke

> **Method** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/pregel/remote/RemoteGraph/invoke)

Create a run, wait until it finishes and return the final state.

## Signature

```python
invoke(
    self,
    input: dict[str, Any] | Any,
    config: RunnableConfig | None = None,
    *,
    context: Context | None = None,
    interrupt_before: All | Sequence[str] | None = None,
    interrupt_after: All | Sequence[str] | None = None,
    headers: dict[str, str] | None = None,
    params: QueryParamTypes | None = None,
    version: Literal['v1', 'v2'] = 'v1',
    **kwargs: Any = {},
) -> dict[str, Any] | Any
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `input` | `dict[str, Any] \| Any` | Yes | Input to the graph. |
| `config` | `RunnableConfig \| None` | No | A `RunnableConfig` for graph invocation. (default: `None`) |
| `interrupt_before` | `All \| Sequence[str] \| None` | No | Interrupt the graph before these nodes. (default: `None`) |
| `interrupt_after` | `All \| Sequence[str] \| None` | No | Interrupt the graph after these nodes. (default: `None`) |
| `headers` | `dict[str, str] \| None` | No | Additional headers to pass to the request. (default: `None`) |
| `version` | `Literal['v1', 'v2']` | No | The streaming format version. `"v1"` (default) returns the traditional format, `"v2"` returns `StreamPart` typed dicts. (default: `'v1'`) |
| `**kwargs` | `Any` | No | Additional params to pass to RemoteGraph.stream. (default: `{}`) |

## Returns

`dict[str, Any] | Any`

The output of the graph.

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/644815f9e5bc52ad8f7a5227a456227e9c3e639b/libs/langgraph/langgraph/pregel/remote.py#L1162)
