---
title: "add_sequence"
description: "Add a sequence of nodes that will be executed in the provided order."
source: "https://reference.langchain.com/python/langgraph/graph/state/StateGraph/add_sequence"
category: "reference"
tags: [reference, langgraph, graph, state, stategraph, add_sequence]
---

# add_sequence

> **Method** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/graph/state/StateGraph/add_sequence)

Add a sequence of nodes that will be executed in the provided order.

## Signature

```python
add_sequence(
    self,
    nodes: Sequence[StateNode[NodeInputT, ContextT] | tuple[str, StateNode[NodeInputT, ContextT]]],
) -> Self
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `nodes` | `Sequence[StateNode[NodeInputT, ContextT] \| tuple[str, StateNode[NodeInputT, ContextT]]]` | Yes | A sequence of `StateNode` (callables that accept a `state` arg) or `(name, StateNode)` tuples.  If no names are provided, the name will be inferred from the node object (e.g. a `Runnable` or a `Callable` name).  Each node will be executed in the order provided. |

## Returns

`Self`

The instance of the `StateGraph`, allowing for method chaining.

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/644815f9e5bc52ad8f7a5227a456227e9c3e639b/libs/langgraph/langgraph/graph/state.py#L1032)
