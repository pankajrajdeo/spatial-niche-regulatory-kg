---
title: "add_edge"
description: "Add a directed edge from the start node (or list of start nodes) to the end node."
source: "https://reference.langchain.com/python/langgraph/graph/state/StateGraph/add_edge"
category: "reference"
tags: [reference, langgraph, graph, state, stategraph, add_edge]
---

# add_edge

> **Method** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/graph/state/StateGraph/add_edge)

Add a directed edge from the start node (or list of start nodes) to the end node.

When a single start node is provided, the graph will wait for that node to complete
before executing the end node. When multiple start nodes are provided,
the graph will wait for ALL of the start nodes to complete before executing the end node.

## Signature

```python
add_edge(
    self,
    start_key: str | list[str],
    end_key: str,
) -> Self
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `start_key` | `str \| list[str]` | Yes | The key(s) of the start node(s) of the edge. |
| `end_key` | `str` | Yes | The key of the end node of the edge. |

## Returns

`Self`

The instance of the `StateGraph`, allowing for method chaining.

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/644815f9e5bc52ad8f7a5227a456227e9c3e639b/libs/langgraph/langgraph/graph/state.py#L928)
