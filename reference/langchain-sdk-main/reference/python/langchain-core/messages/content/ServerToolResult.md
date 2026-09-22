---
title: "ServerToolResult"
description: "Result of a server-side tool call."
source: "https://reference.langchain.com/python/langchain-core/messages/content/ServerToolResult"
category: "reference"
tags: [reference, langchain-core, messages, content, servertoolresult]
---

# ServerToolResult

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/messages/content/ServerToolResult)

Result of a server-side tool call.

## Signature

```python
ServerToolResult()
```

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    type: Literal['server_tool_result'],
    id: NotRequired[str],
    tool_call_id: str,
    status: Literal['success', 'error'],
    output: NotRequired[Any],
    index: NotRequired[int | str],
    extras: NotRequired[dict[str, Any]],
)
```

| Name | Type |
|------|------|
| `type` | `Literal['server_tool_result']` |
| `id` | `NotRequired[str]` |
| `tool_call_id` | `str` |
| `status` | `Literal['success', 'error']` |
| `output` | `NotRequired[Any]` |
| `index` | `NotRequired[int \| str]` |
| `extras` | `NotRequired[dict[str, Any]]` |

## Properties

- `type`
- `id`
- `tool_call_id`
- `status`
- `output`
- `index`
- `extras`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/messages/content.py#L425)
