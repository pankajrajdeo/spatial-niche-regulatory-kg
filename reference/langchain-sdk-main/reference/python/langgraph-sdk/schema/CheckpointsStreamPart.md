---
title: "CheckpointsStreamPart"
description: "Stream part emitted for stream_mode=\"checkpoints\"."
source: "https://reference.langchain.com/python/langgraph-sdk/schema/CheckpointsStreamPart"
category: "reference"
tags: [reference, langgraph-sdk, schema, checkpointsstreampart]
---

# CheckpointsStreamPart

> **Class** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/schema/CheckpointsStreamPart)

Stream part emitted for `stream_mode="checkpoints"`.

## Signature

```python
CheckpointsStreamPart()
```

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    type: Literal['checkpoints'],
    ns: list[str],
    data: CheckpointPayload,
)
```

| Name | Type |
|------|------|
| `type` | `Literal['checkpoints']` |
| `ns` | `list[str]` |
| `data` | `CheckpointPayload` |

## Properties

- `type`
- `ns`
- `data`

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/d5f4b2aa960940effc8430165ab3604038e817af/libs/sdk-py/langgraph_sdk/schema.py#L812)
