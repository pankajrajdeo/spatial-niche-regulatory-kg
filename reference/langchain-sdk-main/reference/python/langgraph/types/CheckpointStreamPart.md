---
title: "CheckpointStreamPart"
description: "Stream part emitted for stream_mode=\"checkpoints\"."
source: "https://reference.langchain.com/python/langgraph/types/CheckpointStreamPart"
category: "reference"
tags: [reference, langgraph, types, checkpointstreampart]
---

# CheckpointStreamPart

> **Class** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/types/CheckpointStreamPart)

Stream part emitted for `stream_mode="checkpoints"`.

## Signature

```python
CheckpointStreamPart()
```

## Extends

- `TypedDict`
- `Generic[StateT]`

## Constructors

```python
__init__(
    type: Literal['checkpoints'],
    ns: tuple[str, ...],
    data: CheckpointPayload[StateT],
)
```

| Name | Type |
|------|------|
| `type` | `Literal['checkpoints']` |
| `ns` | `tuple[str, ...]` |
| `data` | `CheckpointPayload[StateT]` |

## Properties

- `type`
- `ns`
- `data`

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/644815f9e5bc52ad8f7a5227a456227e9c3e639b/libs/langgraph/langgraph/types.py#L312)
