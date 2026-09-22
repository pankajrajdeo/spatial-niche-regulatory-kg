---
title: "AIMessage"
description: "Message from an AI."
source: "https://reference.langchain.com/python/langchain-core/messages/ai/AIMessage"
category: "reference"
tags: [reference, langchain-core, messages, ai, aimessage]
---

# AIMessage

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/messages/ai/AIMessage)

Message from an AI.

An `AIMessage` is returned from a chat model as a response to a prompt.

This message represents the output of the model and consists of both
the raw output as returned by the model and standardized fields
(e.g., tool calls, usage metadata) added by the LangChain framework.

## Signature

```python
AIMessage(
    self,
    content: str | list[str | dict[Any, Any]] | None = None,
    content_blocks: list[types.ContentBlock] | None = None,
    **kwargs: Any = {},
)
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `content` | `str \| list[str \| dict[Any, Any]] \| None` | No | The content of the message. (default: `None`) |
| `content_blocks` | `list[types.ContentBlock] \| None` | No | Typed standard content. (default: `None`) |
| `**kwargs` | `Any` | No | Additional arguments to pass to the parent class. (default: `{}`) |

## Extends

- `BaseMessage`

## Constructors

```python
__init__(
    self,
    content: str | list[str | dict[Any, Any]] | None = None,
    content_blocks: list[types.ContentBlock] | None = None,
    **kwargs: Any = {},
) -> None
```

| Name | Type |
|------|------|
| `content` | `str \| list[str \| dict[Any, Any]] \| None` |
| `content_blocks` | `list[types.ContentBlock] \| None` |

## Properties

- `tool_calls`
- `invalid_tool_calls`
- `usage_metadata`
- `type`
- `lc_attributes`
- `content_blocks`

## Methods

- [`pretty_repr()`](https://reference.langchain.com/python/langchain-core/messages/ai/AIMessage/pretty_repr)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/messages/ai.py#L160)
