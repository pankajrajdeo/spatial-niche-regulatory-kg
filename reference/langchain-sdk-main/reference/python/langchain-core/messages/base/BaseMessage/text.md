---
title: "text"
description: "Get the text content of the message as a string."
source: "https://reference.langchain.com/python/langchain-core/messages/base/BaseMessage/text"
category: "reference"
tags: [reference, langchain-core, messages, base, basemessage, text]
---

# text

> **Attribute** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/messages/base/BaseMessage/text)

Get the text content of the message as a string.

Can be used as both property (`message.text`) and method (`message.text()`).

Handles both string and list content types (e.g. for content blocks). Only
extracts blocks with `type: 'text'`; other block types are ignored.

!!! deprecated
    As of `langchain-core` 1.0.0, calling `.text()` as a method is deprecated.
    Use `.text` as a property instead. This method will be removed in 2.0.0.

## Signature

```python
text: TextAccessor
```

## Returns

`TextAccessor`

The text content of the message.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/messages/base.py#L263)
