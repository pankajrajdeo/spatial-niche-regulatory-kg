---
title: "GraphSchema"
description: "Defines the structure and properties of a graph."
source: "https://reference.langchain.com/python/langgraph-sdk/schema/GraphSchema"
category: "reference"
tags: [reference, langgraph-sdk, schema, graphschema]
---

# GraphSchema

> **Class** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/schema/GraphSchema)

Defines the structure and properties of a graph.

## Signature

```python
GraphSchema()
```

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    graph_id: str,
    input_schema: dict | None,
    output_schema: dict | None,
    state_schema: dict | None,
    config_schema: dict | None,
    context_schema: dict | None,
)
```

| Name | Type |
|------|------|
| `graph_id` | `str` |
| `input_schema` | `dict \| None` |
| `output_schema` | `dict \| None` |
| `state_schema` | `dict \| None` |
| `config_schema` | `dict \| None` |
| `context_schema` | `dict \| None` |

## Properties

- `graph_id`
- `input_schema`
- `output_schema`
- `state_schema`
- `config_schema`
- `context_schema`

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/d5f4b2aa960940effc8430165ab3604038e817af/libs/sdk-py/langgraph_sdk/schema.py#L221)
