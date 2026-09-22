---
title: "InvalidToolCall"
description: "Allowance for errors made by LLM."
source: "https://reference.langchain.com/python/langchain-core/messages/content/InvalidToolCall"
category: "reference"
tags: [reference, langchain-core, messages, content, invalidtoolcall]
---

# InvalidToolCall

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/messages/content/InvalidToolCall)

Allowance for errors made by LLM.

Here we add an `error` key to surface errors made during generation
(e.g., invalid JSON arguments.)

## Signature

```python
InvalidToolCall()
```

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    type: Literal['invalid_tool_call'],
    id: str | None,
    name: str | None,
    args: str | None,
    error: str | None,
    index: NotRequired[int | str],
    extras: NotRequired[dict[str, Any]],
)
```

| Name | Type |
|------|------|
| `type` | `Literal['invalid_tool_call']` |
| `id` | `str \| None` |
| `name` | `str \| None` |
| `args` | `str \| None` |
| `error` | `str \| None` |
| `index` | `NotRequired[int \| str]` |
| `extras` | `NotRequired[dict[str, Any]]` |

## Properties

- `type`
- `id`
- `name`
- `args`
- `error`
- `index`
- `extras`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/messages/content.py#L336)
