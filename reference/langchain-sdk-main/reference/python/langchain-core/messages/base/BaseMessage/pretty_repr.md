---
title: "pretty_repr"
description: "Get a pretty representation of the message."
source: "https://reference.langchain.com/python/langchain-core/messages/base/BaseMessage/pretty_repr"
category: "reference"
tags: [reference, langchain-core, messages, base, basemessage, pretty_repr]
---

# pretty_repr

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/messages/base/BaseMessage/pretty_repr)

Get a pretty representation of the message.

## Signature

```python
pretty_repr(
    self,
    html: bool = False,
) -> str
```

## Description

**Example:**

```python
from langchain_core.messages import HumanMessage

msg = HumanMessage(content="What is the capital of France?")
print(msg.pretty_repr())
```

Results in:

```txt
================================ Human Message =================================

What is the capital of France?
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `html` | `bool` | No | Whether to format the message as HTML. If `True`, the message will be formatted with HTML tags. (default: `False`) |

## Returns

`str`

A pretty representation of the message.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/messages/base.py#L309)
