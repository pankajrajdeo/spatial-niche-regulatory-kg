---
title: "HumanMessage"
description: "Message from the user."
source: "https://reference.langchain.com/python/langchain-core/messages/human/HumanMessage"
category: "reference"
tags: [reference, langchain-core, messages, human, humanmessage]
---

# HumanMessage

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/messages/human/HumanMessage)

Message from the user.

A `HumanMessage` is a message that is passed in from a user to the model.

## Signature

```python
HumanMessage(
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

# Instantiate a chat model and invoke it with the messages
model = ...
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

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/messages/human.py#L9)
