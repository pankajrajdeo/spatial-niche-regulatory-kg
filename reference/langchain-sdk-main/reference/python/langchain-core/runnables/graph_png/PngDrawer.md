---
title: "PngDrawer"
description: "Helper class to draw a state graph into a PNG file."
source: "https://reference.langchain.com/python/langchain-core/runnables/graph_png/PngDrawer"
category: "reference"
tags: [reference, langchain-core, runnables, graph_png, pngdrawer]
---

# PngDrawer

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/graph_png/PngDrawer)

Helper class to draw a state graph into a PNG file.

It requires `graphviz` and `pygraphviz` to be installed.

## Signature

```python
PngDrawer(
    self,
    fontname: str | None = None,
    labels: LabelsDict | None = None,
)
```

## Description

**Example:**

```python
drawer = PngDrawer()
drawer.draw(state_graph, "graph.png")
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `fontname` | `str \| None` | No | The font to use for the labels. Defaults to "arial". (default: `None`) |
| `labels` | `LabelsDict \| None` | No | A dictionary of label overrides. The dictionary should have the following format: {     "nodes": {         "node1": "CustomLabel1",         "node2": "CustomLabel2",         "__end__": "End Node"     },     "edges": {         "continue": "ContinueLabel",         "end": "EndLabel"     } } The keys are the original labels, and the values are the new labels. (default: `None`) |

## Constructors

```python
__init__(
    self,
    fontname: str | None = None,
    labels: LabelsDict | None = None,
) -> None
```

| Name | Type |
|------|------|
| `fontname` | `str \| None` |
| `labels` | `LabelsDict \| None` |

## Properties

- `fontname`
- `labels`

## Methods

- [`get_node_label()`](https://reference.langchain.com/python/langchain-core/runnables/graph_png/PngDrawer/get_node_label)
- [`get_edge_label()`](https://reference.langchain.com/python/langchain-core/runnables/graph_png/PngDrawer/get_edge_label)
- [`add_node()`](https://reference.langchain.com/python/langchain-core/runnables/graph_png/PngDrawer/add_node)
- [`add_edge()`](https://reference.langchain.com/python/langchain-core/runnables/graph_png/PngDrawer/add_edge)
- [`draw()`](https://reference.langchain.com/python/langchain-core/runnables/graph_png/PngDrawer/draw)
- [`add_nodes()`](https://reference.langchain.com/python/langchain-core/runnables/graph_png/PngDrawer/add_nodes)
- [`add_subgraph()`](https://reference.langchain.com/python/langchain-core/runnables/graph_png/PngDrawer/add_subgraph)
- [`add_edges()`](https://reference.langchain.com/python/langchain-core/runnables/graph_png/PngDrawer/add_edges)
- [`update_styles()`](https://reference.langchain.com/python/langchain-core/runnables/graph_png/PngDrawer/update_styles)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/runnables/graph_png.py#L16)
