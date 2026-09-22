---
title: "add_conditional_edges"
description: "Add a conditional edge from the starting node to any number of destination nodes."
source: "https://reference.langchain.com/python/langgraph/graph/state/StateGraph/add_conditional_edges"
category: "reference"
tags: [reference, langgraph, graph, state, stategraph, add_conditional_edges]
---

# add_conditional_edges

> **Method** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/graph/state/StateGraph/add_conditional_edges)

Add a conditional edge from the starting node to any number of destination nodes.

## Signature

```python
add_conditional_edges(
    self,
    source: str,
    path: Callable[..., Hashable | Sequence[Hashable]] | Callable[..., Awaitable[Hashable | Sequence[Hashable]]] | Runnable[Any, Hashable | Sequence[Hashable]],
    path_map: dict[Hashable, str] | list[str] | None = None,
) -> Self
```

## Description

!!! warning
Without type hints on the `path` function's return value (e.g., `-> Literal["foo", "__end__"]:`)
or a path_map, the graph visualization assumes the edge could transition to any node in the graph.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `source` | `str` | Yes | The starting node. This conditional edge will run when exiting this node. |
| `path` | `Callable[..., Hashable \| Sequence[Hashable]] \| Callable[..., Awaitable[Hashable \| Sequence[Hashable]]] \| Runnable[Any, Hashable \| Sequence[Hashable]]` | Yes | The callable that determines the next node or nodes.  If not specifying `path_map` it should return one or more nodes.  If it returns `'END'`, the graph will stop execution. |
| `path_map` | `dict[Hashable, str] \| list[str] \| None` | No | Optional mapping of paths to node names.  If omitted the paths returned by `path` should be node names. (default: `None`) |

## Returns

`Self`

The instance of the graph, allowing for method chaining.

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/644815f9e5bc52ad8f7a5227a456227e9c3e639b/libs/langgraph/langgraph/graph/state.py#L982)
