---
title: "TaskResultPayload"
description: "Payload for a task result event."
source: "https://reference.langchain.com/python/langgraph/types/TaskResultPayload"
category: "reference"
tags: [reference, langgraph, types, taskresultpayload]
---

# TaskResultPayload

> **Class** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/types/TaskResultPayload)

Payload for a task result event.

## Signature

```python
TaskResultPayload()
```

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    id: str,
    name: str,
    error: str | None,
    interrupts: list[dict],
    result: dict[str, Any],
)
```

| Name | Type |
|------|------|
| `id` | `str` |
| `name` | `str` |
| `error` | `str \| None` |
| `interrupts` | `list[dict]` |
| `result` | `dict[str, Any]` |

## Properties

- `id`
- `name`
- `error`
- `interrupts`
- `result`

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/644815f9e5bc52ad8f7a5227a456227e9c3e639b/libs/langgraph/langgraph/types.py#L167)
