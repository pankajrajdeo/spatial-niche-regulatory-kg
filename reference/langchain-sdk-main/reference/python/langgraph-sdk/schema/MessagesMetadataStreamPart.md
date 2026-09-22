---
title: "MessagesMetadataStreamPart"
description: "Stream part emitted for message metadata (messages/metadata)."
source: "https://reference.langchain.com/python/langgraph-sdk/schema/MessagesMetadataStreamPart"
category: "reference"
tags: [reference, langgraph-sdk, schema, messagesmetadatastreampart]
---

# MessagesMetadataStreamPart

> **Class** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/schema/MessagesMetadataStreamPart)

Stream part emitted for message metadata (`messages/metadata`).

## Signature

```python
MessagesMetadataStreamPart()
```

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    type: Literal['messages/metadata'],
    ns: list[str],
    data: dict[str, Any],
)
```

| Name | Type |
|------|------|
| `type` | `Literal['messages/metadata']` |
| `ns` | `list[str]` |
| `data` | `dict[str, Any]` |

## Properties

- `type`
- `ns`
- `data`

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/d5f4b2aa960940effc8430165ab3604038e817af/libs/sdk-py/langgraph_sdk/schema.py#L779)
