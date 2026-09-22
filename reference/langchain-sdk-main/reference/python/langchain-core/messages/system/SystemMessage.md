---
title: "SystemMessage"
description: "Message for priming AI behavior."
source: "https://reference.langchain.com/python/langchain-core/messages/system/SystemMessage"
category: "reference"
tags: [reference, langchain-core, messages, system, systemmessage]
---

# SystemMessage

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/messages/system/SystemMessage)

Message for priming AI behavior.

The system message is usually passed in as the first of a sequence
of input messages.

## Signature

```python
SystemMessage(
    self,
    content: str | list[str | dict[Any, Any]] | None = None,
    content_blocks: list[types.ContentBlock] | None = None,
    **kwargs: Any = {},
)
```

## Description

**Example:**

```python
from langchain_core.messages import HumanMessage, SystemMessage

messages = [
    SystemMessage(content="You are a helpful assistant! Your name is Bob."),
    HumanMessage(content="What is your name?"),
]

# Define a chat model and invoke it with the messages
print(model.invoke(messages))
```

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

- `type`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/messages/system.py#L9)
