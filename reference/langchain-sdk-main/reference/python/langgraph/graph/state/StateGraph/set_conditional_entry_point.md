---
title: "set_conditional_entry_point"
description: "Sets a conditional entry point in the graph."
source: "https://reference.langchain.com/python/langgraph/graph/state/StateGraph/set_conditional_entry_point"
category: "reference"
tags: [reference, langgraph, graph, state, stategraph, set_conditional_entry_point]
---

# set_conditional_entry_point

> **Method** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/graph/state/StateGraph/set_conditional_entry_point)

Sets a conditional entry point in the graph.

## Signature

```python
set_conditional_entry_point(
    self,
    path: Callable[..., Hashable | Sequence[Hashable]] | Callable[..., Awaitable[Hashable | Sequence[Hashable]]] | Runnable[Any, Hashable | Sequence[Hashable]],
    path_map: dict[Hashable, str] | list[str] | None = None,
) -> Self
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `path` | `Callable[..., Hashable \| Sequence[Hashable]] \| Callable[..., Awaitable[Hashable \| Sequence[Hashable]]] \| Runnable[Any, Hashable \| Sequence[Hashable]]` | Yes | The callable that determines the next node or nodes.  If not specifying `path_map` it should return one or more nodes.  If it returns END, the graph will stop execution. |
| `path_map` | `dict[Hashable, str] \| list[str] \| None` | No | Optional mapping of paths to node names.  If omitted the paths returned by `path` should be node names. (default: `None`) |

## Returns

`Self`

The instance of the graph, allowing for method chaining.

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/644815f9e5bc52ad8f7a5227a456227e9c3e639b/libs/langgraph/langgraph/graph/state.py#L1092)
