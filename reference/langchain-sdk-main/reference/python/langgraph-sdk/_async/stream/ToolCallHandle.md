---
title: "ToolCallHandle"
description: "Async handle for one root-scope tool call."
source: "https://reference.langchain.com/python/langgraph-sdk/_async/stream/ToolCallHandle"
category: "reference"
tags: [reference, langgraph-sdk, async, stream, toolcallhandle]
---

# ToolCallHandle

> **Class** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/_async/stream/ToolCallHandle)

Async handle for one root-scope tool call.

## Signature

```python
ToolCallHandle(
    self,
    *,
    tool_call_id: str,
    name: str,
    input: Any = None,
    namespace: list[str] | None = None,
    max_queue_size: int = 1024,
)
```

## Constructors

```python
__init__(
    self,
    *,
    tool_call_id: str,
    name: str,
    input: Any = None,
    namespace: list[str] | None = None,
    max_queue_size: int = 1024,
) -> None
```

| Name | Type |
|------|------|
| `tool_call_id` | `str` |
| `name` | `str` |
| `input` | `Any` |
| `namespace` | `list[str] \| None` |
| `max_queue_size` | `int` |

## Properties

- `tool_call_id`
- `name`
- `input`
- `namespace`
- `done`
- `error`
- `output`
- `deltas`

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/d5f4b2aa960940effc8430165ab3604038e817af/libs/sdk-py/langgraph_sdk/_async/stream.py#L970)
