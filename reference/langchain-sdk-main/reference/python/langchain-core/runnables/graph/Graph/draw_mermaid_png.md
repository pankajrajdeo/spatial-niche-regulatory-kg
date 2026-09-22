---
title: "draw_mermaid_png"
description: "Draw the graph as a PNG image using Mermaid."
source: "https://reference.langchain.com/python/langchain-core/runnables/graph/Graph/draw_mermaid_png"
category: "reference"
tags: [reference, langchain-core, runnables, graph, draw_mermaid_png]
---

# draw_mermaid_png

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/graph/Graph/draw_mermaid_png)

Draw the graph as a PNG image using Mermaid.

## Signature

```python
draw_mermaid_png(
    self,
    *,
    curve_style: CurveStyle = CurveStyle.LINEAR,
    node_colors: NodeStyles | None = None,
    wrap_label_n_words: int = 9,
    output_file_path: str | None = None,
    draw_method: MermaidDrawMethod = MermaidDrawMethod.API,
    background_color: str = 'white',
    padding: int = 10,
    max_retries: int = 1,
    retry_delay: float = 1.0,
    frontmatter_config: dict[str, Any] | None = None,
    base_url: str | None = None,
    proxies: dict[str, str] | None = None,
) -> bytes
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `curve_style` | `CurveStyle` | No | The style of the edges. (default: `CurveStyle.LINEAR`) |
| `node_colors` | `NodeStyles \| None` | No | The colors of the nodes. (default: `None`) |
| `wrap_label_n_words` | `int` | No | The number of words to wrap the node labels at. (default: `9`) |
| `output_file_path` | `str \| None` | No | The path to save the image to. If `None`, the image is not saved. (default: `None`) |
| `draw_method` | `MermaidDrawMethod` | No | The method to use to draw the graph. (default: `MermaidDrawMethod.API`) |
| `background_color` | `str` | No | The color of the background. (default: `'white'`) |
| `padding` | `int` | No | The padding around the graph. (default: `10`) |
| `max_retries` | `int` | No | The maximum number of retries (`MermaidDrawMethod.API`). (default: `1`) |
| `retry_delay` | `float` | No | The delay between retries (`MermaidDrawMethod.API`). (default: `1.0`) |
| `frontmatter_config` | `dict[str, Any] \| None` | No | Mermaid frontmatter config. Can be used to customize theme and styles. Will be converted to YAML and added to the beginning of the mermaid graph.  See more here: https://mermaid.js.org/config/configuration.html.  Example config:  ```python {     "config": {         "theme": "neutral",         "look": "handDrawn",         "themeVariables": {"primaryColor": "#e2e2e2"},     } } ``` (default: `None`) |
| `base_url` | `str \| None` | No | The base URL of the Mermaid server for rendering via API. (default: `None`) |
| `proxies` | `dict[str, str] \| None` | No | HTTP/HTTPS proxies for requests (e.g. `{"http": "http://127.0.0.1:7890"}`). (default: `None`) |

## Returns

`bytes`

The PNG image as bytes.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/runnables/graph.py#L632)
