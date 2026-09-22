---
title: "extend"
description: "Add all nodes and edges from another graph."
source: "https://reference.langchain.com/python/langchain-core/runnables/graph/Graph/extend"
category: "reference"
tags: [reference, langchain-core, runnables, graph, extend]
---

# extend

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/graph/Graph/extend)

Add all nodes and edges from another graph.

Note this doesn't check for duplicates, nor does it connect the graphs.

## Signature

```python
extend(
    self,
    graph: Graph,
    *,
    prefix: str = '',
) -> tuple[Node | None, Node | None]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `graph` | `Graph` | Yes | The graph to add. |
| `prefix` | `str` | No | The prefix to add to the node ids. (default: `''`) |

## Returns

`tuple[Node | None, Node | None]`

A tuple of the first and last nodes of the subgraph.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/runnables/graph.py#L386)
