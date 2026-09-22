---
title: "MessagesTupleStreamPart"
description: "Stream part emitted for stream_mode=\"messages\" (raw message+metadata pair)."
source: "https://reference.langchain.com/python/langgraph-sdk/schema/MessagesTupleStreamPart"
category: "reference"
tags: [reference, langgraph-sdk, schema, messagestuplestreampart]
---

# MessagesTupleStreamPart

> **Class** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/schema/MessagesTupleStreamPart)

Stream part emitted for `stream_mode="messages"` (raw message+metadata pair).

## Signature

```python
MessagesTupleStreamPart()
```

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    type: Literal['messages'],
    ns: list[str],
    data: list[dict[str, Any]],
)
```

| Name | Type |
|------|------|
| `type` | `Literal['messages']` |
| `ns` | `list[str]` |
| `data` | `list[dict[str, Any]]` |

## Properties

- `type`
- `ns`
- `data`

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/d5f4b2aa960940effc8430165ab3604038e817af/libs/sdk-py/langgraph_sdk/schema.py#L790)
