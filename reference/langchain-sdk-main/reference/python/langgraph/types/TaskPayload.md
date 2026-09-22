---
title: "TaskPayload"
description: "Payload for a task start event."
source: "https://reference.langchain.com/python/langgraph/types/TaskPayload"
category: "reference"
tags: [reference, langgraph, types, taskpayload]
---

# TaskPayload

> **Class** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/types/TaskPayload)

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
    metadata: NotRequired[dict[str, Any]],
)
```

| Name | Type |
|------|------|
| `id` | `str` |
| `name` | `str` |
| `input` | `Any` |
| `triggers` | `list[str]` |
| `metadata` | `NotRequired[dict[str, Any]]` |

## Properties

- `id`
- `name`
- `input`
- `triggers`
- `metadata`

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/644815f9e5bc52ad8f7a5227a456227e9c3e639b/libs/langgraph/langgraph/types.py#L144)
