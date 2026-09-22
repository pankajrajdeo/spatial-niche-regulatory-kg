---
title: "ValuesStreamPart"
description: "Stream part emitted for stream_mode=\"values\"."
source: "https://reference.langchain.com/python/langgraph/types/ValuesStreamPart"
category: "reference"
tags: [reference, langgraph, types, valuesstreampart]
---

# ValuesStreamPart

> **Class** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/types/ValuesStreamPart)

Stream part emitted for `stream_mode="values"`.

`data` contains the full state after each step, as returned by `read_channels()`.

## Signature

```python
ValuesStreamPart()
```

## Extends

- `TypedDict`
- `Generic[OutputT]`

## Constructors

```python
__init__(
    type: Literal['values'],
    ns: tuple[str, ...],
    data: OutputT,
    interrupts: tuple[Interrupt, ...],
)
```

| Name | Type |
|------|------|
| `type` | `Literal['values']` |
| `ns` | `tuple[str, ...]` |
| `data` | `OutputT` |
| `interrupts` | `tuple[Interrupt, ...]` |

## Properties

- `type`
- `ns`
- `data`
- `interrupts`

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/644815f9e5bc52ad8f7a5227a456227e9c3e639b/libs/langgraph/langgraph/types.py#L264)
