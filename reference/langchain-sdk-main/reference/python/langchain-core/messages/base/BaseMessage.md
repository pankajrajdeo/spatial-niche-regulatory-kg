---
title: "BaseMessage"
description: "Base abstract message class."
source: "https://reference.langchain.com/python/langchain-core/messages/base/BaseMessage"
category: "reference"
tags: [reference, langchain-core, messages, base, basemessage]
---

# BaseMessage

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/messages/base/BaseMessage)

Base abstract message class.

Messages are the inputs and outputs of a chat model.

Examples include [`HumanMessage`][langchain.messages.HumanMessage],
[`AIMessage`][langchain.messages.AIMessage], and
[`SystemMessage`][langchain.messages.SystemMessage].

## Signature

```python
BaseMessage(
    self,
    content: str | list[str | dict[Any, Any]] | None = None,
    content_blocks: list[types.ContentBlock] | None = None,
    **kwargs: Any = {},
)
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `content` | `str \| list[str \| dict[Any, Any]] \| None` | No | The contents of the message. (default: `None`) |
| `content_blocks` | `list[types.ContentBlock] \| None` | No | Typed standard content. (default: `None`) |
| `**kwargs` | `Any` | No | Additional arguments to pass to the parent class. (default: `{}`) |

## Extends

- `Serializable`

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

- `content`
- `additional_kwargs`
- `response_metadata`
- `type`
- `name`
- `id`
- `model_config`
- `content_blocks`
- `text`

## Methods

- [`is_lc_serializable()`](https://reference.langchain.com/python/langchain-core/messages/base/BaseMessage/is_lc_serializable)
- [`get_lc_namespace()`](https://reference.langchain.com/python/langchain-core/messages/base/BaseMessage/get_lc_namespace)
- [`pretty_repr()`](https://reference.langchain.com/python/langchain-core/messages/base/BaseMessage/pretty_repr)
- [`pretty_print()`](https://reference.langchain.com/python/langchain-core/messages/base/BaseMessage/pretty_print)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/messages/base.py#L93)
