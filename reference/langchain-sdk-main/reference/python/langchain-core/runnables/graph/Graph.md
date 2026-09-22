---
title: "Graph"
description: "Graph of nodes and edges."
source: "https://reference.langchain.com/python/langchain-core/runnables/graph/Graph"
category: "reference"
tags: [reference, langchain-core, runnables, graph]
---

# Graph

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/graph/Graph)

Graph of nodes and edges.

## Signature

```python
Graph(
    self,
    nodes: dict[str, Node] = dict(),
    edges: list[Edge] = list(),
)
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `nodes` | `dict[str, Node]` | No | Dictionary of nodes in the graph. Defaults to an empty dictionary. (default: `dict()`) |
| `edges` | `list[Edge]` | No | List of edges in the graph. Defaults to an empty list. (default: `list()`) |

## Constructors

```python
__init__(
    self,
    nodes: dict[str, Node] = dict(),
    edges: list[Edge] = list(),
) -> None
```

| Name | Type |
|------|------|
| `nodes` | `dict[str, Node]` |
| `edges` | `list[Edge]` |

## Properties

- `nodes`
- `edges`

## Methods

- [`to_json()`](https://reference.langchain.com/python/langchain-core/runnables/graph/Graph/to_json)
- [`next_id()`](https://reference.langchain.com/python/langchain-core/runnables/graph/Graph/next_id)
- [`add_node()`](https://reference.langchain.com/python/langchain-core/runnables/graph/Graph/add_node)
- [`remove_node()`](https://reference.langchain.com/python/langchain-core/runnables/graph/Graph/remove_node)
- [`add_edge()`](https://reference.langchain.com/python/langchain-core/runnables/graph/Graph/add_edge)
- [`extend()`](https://reference.langchain.com/python/langchain-core/runnables/graph/Graph/extend)
- [`reid()`](https://reference.langchain.com/python/langchain-core/runnables/graph/Graph/reid)
- [`first_node()`](https://reference.langchain.com/python/langchain-core/runnables/graph/Graph/first_node)
- [`last_node()`](https://reference.langchain.com/python/langchain-core/runnables/graph/Graph/last_node)
- [`trim_first_node()`](https://reference.langchain.com/python/langchain-core/runnables/graph/Graph/trim_first_node)
- [`trim_last_node()`](https://reference.langchain.com/python/langchain-core/runnables/graph/Graph/trim_last_node)
- [`draw_ascii()`](https://reference.langchain.com/python/langchain-core/runnables/graph/Graph/draw_ascii)
- [`print_ascii()`](https://reference.langchain.com/python/langchain-core/runnables/graph/Graph/print_ascii)
- [`draw_png()`](https://reference.langchain.com/python/langchain-core/runnables/graph/Graph/draw_png)
- [`draw_mermaid()`](https://reference.langchain.com/python/langchain-core/runnables/graph/Graph/draw_mermaid)
- [`draw_mermaid_png()`](https://reference.langchain.com/python/langchain-core/runnables/graph/Graph/draw_mermaid_png)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/runnables/graph.py#L254)
