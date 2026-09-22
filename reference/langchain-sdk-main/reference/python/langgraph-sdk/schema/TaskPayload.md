---
title: "TaskPayload"
description: "Payload for a task start event."
source: "https://reference.langchain.com/python/langgraph-sdk/schema/TaskPayload"
category: "reference"
tags: [reference, langgraph-sdk, schema, taskpayload]
---

# TaskPayload

> **Class** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/schema/TaskPayload)

Payload for a task start event.

## Signature

```python
TaskPayload()
```

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    id: str,
    name: str,
    input: Any,
    triggers: list[str],
)
```

| Name | Type |
|------|------|
| `id` | `str` |
| `name` | `str` |
| `input` | `Any` |
| `triggers` | `list[str]` |

## Properties

- `id`
- `name`
- `input`
- `triggers`

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/d5f4b2aa960940effc8430165ab3604038e817af/libs/sdk-py/langgraph_sdk/schema.py#L617)
