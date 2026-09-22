---
title: "add_node"
description: "Add a node to the graph and return it."
source: "https://reference.langchain.com/python/langchain-core/runnables/graph/Graph/add_node"
category: "reference"
tags: [reference, langchain-core, runnables, graph, add_node]
---

# add_node

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/graph/Graph/add_node)

Add a node to the graph and return it.

## Signature

```python
add_node(
    self,
    data: TypeBaseModel | RunnableType[Any, Any] | None,
    id: str | None = None,
    *,
    metadata: dict[str, Any] | None = None,
) -> Node
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `data` | `TypeBaseModel \| RunnableType[Any, Any] \| None` | Yes | The data of the node. |
| `id` | `str \| None` | No | The id of the node. (default: `None`) |
| `metadata` | `dict[str, Any] \| None` | No | Optional metadata for the node. (default: `None`) |

## Returns

`Node`

The node that was added to the graph.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/runnables/graph.py#L314)
