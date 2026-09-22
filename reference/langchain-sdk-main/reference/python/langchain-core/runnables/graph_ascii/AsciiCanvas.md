---
title: "AsciiCanvas"
description: "Class for drawing in ASCII."
source: "https://reference.langchain.com/python/langchain-core/runnables/graph_ascii/AsciiCanvas"
category: "reference"
tags: [reference, langchain-core, runnables, graph_ascii, asciicanvas]
---

# AsciiCanvas

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/graph_ascii/AsciiCanvas)

Class for drawing in ASCII.

## Signature

```python
AsciiCanvas(
    self,
    cols: int,
    lines: int,
)
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `cols` | `int` | Yes | number of columns in the canvas. Should be `> 1`. |
| `lines` | `int` | Yes | number of lines in the canvas. Should be `> 1`. |

## Constructors

```python
__init__(
    self,
    cols: int,
    lines: int,
) -> None
```

| Name | Type |
|------|------|
| `cols` | `int` |
| `lines` | `int` |

## Properties

- `TIMEOUT`
- `cols`
- `lines`
- `canvas`

## Methods

- [`draw()`](https://reference.langchain.com/python/langchain-core/runnables/graph_ascii/AsciiCanvas/draw)
- [`point()`](https://reference.langchain.com/python/langchain-core/runnables/graph_ascii/AsciiCanvas/point)
- [`line()`](https://reference.langchain.com/python/langchain-core/runnables/graph_ascii/AsciiCanvas/line)
- [`text()`](https://reference.langchain.com/python/langchain-core/runnables/graph_ascii/AsciiCanvas/text)
- [`box()`](https://reference.langchain.com/python/langchain-core/runnables/graph_ascii/AsciiCanvas/box)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/runnables/graph_ascii.py#L57)
