---
title: "UIMessage"
description: "A message type for UI updates in LangGraph."
source: "https://reference.langchain.com/python/langgraph/graph/ui/UIMessage"
category: "reference"
tags: [reference, langgraph, graph, ui, uimessage]
---

# UIMessage

> **Class** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/graph/ui/UIMessage)

A message type for UI updates in LangGraph.

This TypedDict represents a UI message that can be sent to update the UI state.
It contains information about the UI component to render and its properties.

## Signature

```python
UIMessage()
```

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    type: Literal['ui'],
    id: str,
    name: str,
    props: dict[str, Any],
    metadata: dict[str, Any],
)
```

| Name | Type |
|------|------|
| `type` | `Literal['ui']` |
| `id` | `str` |
| `name` | `str` |
| `props` | `dict[str, Any]` |
| `metadata` | `dict[str, Any]` |

## Properties

- `type`
- `id`
- `name`
- `props`
- `metadata`

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/644815f9e5bc52ad8f7a5227a456227e9c3e639b/libs/langgraph/langgraph/graph/ui.py#L22)
