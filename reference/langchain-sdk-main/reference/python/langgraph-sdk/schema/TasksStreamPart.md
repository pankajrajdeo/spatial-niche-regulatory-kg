---
title: "TasksStreamPart"
description: "Stream part emitted for stream_mode=\"tasks\"."
source: "https://reference.langchain.com/python/langgraph-sdk/schema/TasksStreamPart"
category: "reference"
tags: [reference, langgraph-sdk, schema, tasksstreampart]
---

# TasksStreamPart

> **Class** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/schema/TasksStreamPart)

Stream part emitted for `stream_mode="tasks"`.

## Signature

```python
TasksStreamPart()
```

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    type: Literal['tasks'],
    ns: list[str],
    data: TaskPayload | TaskResultPayload,
)
```

| Name | Type |
|------|------|
| `type` | `Literal['tasks']` |
| `ns` | `list[str]` |
| `data` | `TaskPayload \| TaskResultPayload` |

## Properties

- `type`
- `ns`
- `data`

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/d5f4b2aa960940effc8430165ab3604038e817af/libs/sdk-py/langgraph_sdk/schema.py#L823)
