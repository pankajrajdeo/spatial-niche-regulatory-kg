---
title: "UpdatesStreamPart"
description: "Stream part emitted for stream_mode=\"updates\"."
source: "https://reference.langchain.com/python/langgraph/types/UpdatesStreamPart"
category: "reference"
tags: [reference, langgraph, types, updatesstreampart]
---

# UpdatesStreamPart

> **Class** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/types/UpdatesStreamPart)

Stream part emitted for `stream_mode="updates"`.

`data` maps node names to their outputs. May also contain
`__interrupt__` (tuple of `Interrupt` dicts) and `__metadata__` keys.

## Signature

```python
UpdatesStreamPart()
```

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    type: Literal['updates'],
    ns: tuple[str, ...],
    data: dict[str, Any],
)
```

| Name | Type |
|------|------|
| `type` | `Literal['updates']` |
| `ns` | `tuple[str, ...]` |
| `data` | `dict[str, Any]` |

## Properties

- `type`
- `ns`
- `data`

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/644815f9e5bc52ad8f7a5227a456227e9c3e639b/libs/langgraph/langgraph/types.py#L276)
