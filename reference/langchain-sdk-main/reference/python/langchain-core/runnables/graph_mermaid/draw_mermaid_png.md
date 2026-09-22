---
title: "draw_mermaid_png"
description: "Draws a Mermaid graph as PNG using provided syntax."
source: "https://reference.langchain.com/python/langchain-core/runnables/graph_mermaid/draw_mermaid_png"
category: "reference"
tags: [reference, langchain-core, runnables, graph_mermaid, draw_mermaid_png]
---

# draw_mermaid_png

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/graph_mermaid/draw_mermaid_png)

Draws a Mermaid graph as PNG using provided syntax.

## Signature

```python
draw_mermaid_png(
    mermaid_syntax: str,
    output_file_path: str | None = None,
    draw_method: MermaidDrawMethod = MermaidDrawMethod.API,
    background_color: str | None = 'white',
    padding: int = 10,
    max_retries: int = 1,
    retry_delay: float = 1.0,
    base_url: str | None = None,
    proxies: dict[str, str] | None = None,
) -> bytes
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `mermaid_syntax` | `str` | Yes | Mermaid graph syntax. |
| `output_file_path` | `str \| None` | No | Path to save the PNG image. (default: `None`) |
| `draw_method` | `MermaidDrawMethod` | No | Method to draw the graph. (default: `MermaidDrawMethod.API`) |
| `background_color` | `str \| None` | No | Background color of the image. (default: `'white'`) |
| `padding` | `int` | No | Padding around the image. (default: `10`) |
| `max_retries` | `int` | No | Maximum number of retries (MermaidDrawMethod.API). (default: `1`) |
| `retry_delay` | `float` | No | Delay between retries (MermaidDrawMethod.API). (default: `1.0`) |
| `base_url` | `str \| None` | No | Base URL for the Mermaid.ink API. (default: `None`) |
| `proxies` | `dict[str, str] \| None` | No | HTTP/HTTPS proxies for requests (e.g. `{"http": "http://127.0.0.1:7890"}`). (default: `None`) |

## Returns

`bytes`

PNG image bytes.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/runnables/graph_mermaid.py#L277)
