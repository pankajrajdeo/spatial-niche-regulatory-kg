---
title: "ToolCall"
description: "Represents an AI's request to call a tool."
source: "https://reference.langchain.com/python/langchain-core/messages/content/ToolCall"
category: "reference"
tags: [reference, langchain-core, messages, content, toolcall]
---

# ToolCall

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/messages/content/ToolCall)

Represents an AI's request to call a tool.

## Signature

```python
ToolCall()
```

## Description

**Example:**

```python
{"name": "foo", "args": {"a": 1}, "id": "123"}
```

This represents a request to call the tool named "foo" with arguments {"a": 1}
and an identifier of "123".

!!! note "Factory function"

`create_tool_call` may also be used as a factory to create a
`ToolCall`. Benefits include:

* Automatic ID generation (when not provided)
* Required arguments strictly validated at creation time

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    type: Literal['tool_call'],
    id: str | None,
    name: str,
    args: dict[str, Any],
    index: NotRequired[int | str],
    extras: NotRequired[dict[str, Any]],
)
```

| Name | Type |
|------|------|
| `type` | `Literal['tool_call']` |
| `id` | `str \| None` |
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

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/messages/content.py#L247)
