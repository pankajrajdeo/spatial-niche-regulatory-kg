---
title: "draw_mermaid"
description: "Draw the graph as a Mermaid syntax string."
source: "https://reference.langchain.com/python/langchain-core/runnables/graph/Graph/draw_mermaid"
category: "reference"
tags: [reference, langchain-core, runnables, graph, draw_mermaid]
---

# draw_mermaid

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/graph/Graph/draw_mermaid)

Draw the graph as a Mermaid syntax string.

## Signature

```python
draw_mermaid(
    self,
    *,
    with_styles: bool = True,
    curve_style: CurveStyle = CurveStyle.LINEAR,
    node_colors: NodeStyles | None = None,
    wrap_label_n_words: int = 9,
    frontmatter_config: dict[str, Any] | None = None,
) -> str
```

## Description

Returns:
The Mermaid syntax string.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `with_styles` | `bool` | No | Whether to include styles in the syntax. (default: `True`) |
| `curve_style` | `CurveStyle` | No | The style of the edges. (default: `CurveStyle.LINEAR`) |
| `node_colors` | `NodeStyles \| None` | No | The colors of the nodes. (default: `None`) |
| `wrap_label_n_words` | `int` | No | The number of words to wrap the node labels at. (default: `9`) |
| `frontmatter_config` | `dict[str, Any] \| None` | No | Mermaid frontmatter config. Can be used to customize theme and styles. Will be converted to YAML and added to the beginning of the mermaid graph.  See more here: https://mermaid.js.org/config/configuration.html.  Example config:  ```python {     "config": {         "theme": "neutral",         "look": "handDrawn",         "themeVariables": {"primaryColor": "#e2e2e2"},     } } ``` (default: `None`) |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/runnables/graph.py#L577)
