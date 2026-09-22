---
title: "ServerToolCall"
description: "Tool call that is executed server-side."
source: "https://reference.langchain.com/python/langchain-core/messages/content/ServerToolCall"
category: "reference"
tags: [reference, langchain-core, messages, content, servertoolcall]
---

# ServerToolCall

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/messages/content/ServerToolCall)

Tool call that is executed server-side.

For example: code execution, web search, etc.

## Signature

```python
ServerToolCall()
```

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    type: Literal['server_tool_call'],
    id: str,
    name: str,
    args: dict[str, Any],
    index: NotRequired[int | str],
    extras: NotRequired[dict[str, Any]],
)
```

| Name | Type |
|------|------|
| `type` | `Literal['server_tool_call']` |
| `id` | `str` |
| `name` | `str` |
| `args` | `dict[str, Any]` |
| `index` | `NotRequired[int \| str]` |
| `extras` | `NotRequired[dict[str, Any]]` |

## Properties

- `type`
- `id`
- `name`
- `args`
- `index`
- `extras`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/messages/content.py#L372)
