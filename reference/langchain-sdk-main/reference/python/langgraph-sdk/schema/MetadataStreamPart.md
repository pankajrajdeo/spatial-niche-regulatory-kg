---
title: "MetadataStreamPart"
description: "Control event with run_id and other run metadata."
source: "https://reference.langchain.com/python/langgraph-sdk/schema/MetadataStreamPart"
category: "reference"
tags: [reference, langgraph-sdk, schema, metadatastreampart]
---

# MetadataStreamPart

> **Class** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/schema/MetadataStreamPart)

Control event with `run_id` and other run metadata.

## Signature

```python
MetadataStreamPart()
```

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    type: Literal['metadata'],
    ns: list[str],
    data: RunMetadataPayload,
)
```

| Name | Type |
|------|------|
| `type` | `Literal['metadata']` |
| `ns` | `list[str]` |
| `data` | `RunMetadataPayload` |

## Properties

- `type`
- `ns`
- `data`

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/d5f4b2aa960940effc8430165ab3604038e817af/libs/sdk-py/langgraph_sdk/schema.py#L845)
