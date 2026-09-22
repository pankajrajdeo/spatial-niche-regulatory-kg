---
title: "draw_mermaid"
description: "Draws a Mermaid graph using the provided graph data."
source: "https://reference.langchain.com/python/langchain-core/runnables/graph_mermaid/draw_mermaid"
category: "reference"
tags: [reference, langchain-core, runnables, graph_mermaid, draw_mermaid]
---

# draw_mermaid

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/graph_mermaid/draw_mermaid)

Draws a Mermaid graph using the provided graph data.

## Signature

```python
draw_mermaid(
    nodes: dict[str, Node],
    edges: list[Edge],
    *,
    first_node: str | None = None,
    last_node: str | None = None,
    with_styles: bool = True,
    curve_style: CurveStyle = CurveStyle.LINEAR,
    node_styles: NodeStyles | None = None,
    wrap_label_n_words: int = 9,
    frontmatter_config: dict[str, Any] | None = None,
) -> str
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `nodes` | `dict[str, Node]` | Yes | List of node ids. |
| `edges` | `list[Edge]` | Yes | List of edges, object with a source, target and data. |
| `first_node` | `str \| None` | No | Id of the first node. (default: `None`) |
| `last_node` | `str \| None` | No | Id of the last node. (default: `None`) |
| `with_styles` | `bool` | No | Whether to include styles in the graph. (default: `True`) |
| `curve_style` | `CurveStyle` | No | Curve style for the edges. (default: `CurveStyle.LINEAR`) |
| `node_styles` | `NodeStyles \| None` | No | Node colors for different types. (default: `None`) |
| `wrap_label_n_words` | `int` | No | Words to wrap the edge labels. (default: `9`) |
| `frontmatter_config` | `dict[str, Any] \| None` | No | Mermaid frontmatter config. Can be used to customize theme and styles. Will be converted to YAML and added to the beginning of the mermaid graph.  See more here: https://mermaid.js.org/config/configuration.html.  Example config:  ```python {     "config": {         "theme": "neutral",         "look": "handDrawn",         "themeVariables": {"primaryColor": "#e2e2e2"},     } } ``` (default: `None`) |

## Returns

`str`

Mermaid graph syntax.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/runnables/graph_mermaid.py#L45)
