---
title: "Checkpoint"
description: "Represents a checkpoint in the execution process."
source: "https://reference.langchain.com/python/langgraph-sdk/schema/Checkpoint"
category: "reference"
tags: [reference, langgraph-sdk, schema, checkpoint]
---

# Checkpoint

> **Class** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/schema/Checkpoint)

Represents a checkpoint in the execution process.

## Signature

```python
Checkpoint()
```

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    thread_id: str,
    checkpoint_ns: str,
    checkpoint_id: str | None,
    checkpoint_map: dict[str, Any] | None,
)
```

| Name | Type |
|------|------|
| `thread_id` | `str` |
| `checkpoint_ns` | `str` |
| `checkpoint_id` | `str \| None` |
| `checkpoint_map` | `dict[str, Any] \| None` |

## Properties

- `thread_id`
- `checkpoint_ns`
- `checkpoint_id`
- `checkpoint_map`

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/d5f4b2aa960940effc8430165ab3604038e817af/libs/sdk-py/langgraph_sdk/schema.py#L208)
