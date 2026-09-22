---
title: "optional"
description: "Whether format_messages must be provided."
source: "https://reference.langchain.com/python/langchain-core/prompts/chat/MessagesPlaceholder/optional"
category: "reference"
tags: [reference, langchain-core, prompts, chat, messagesplaceholder, optional]
---

# optional

> **Attribute** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/prompts/chat/MessagesPlaceholder/optional)

Whether `format_messages` must be provided.

If `True` `format_messages` can be called with no arguments and will return an empty
list.

If `False` then a named argument with name `variable_name` must be passed in, even
if the value is an empty list.

## Signature

```python
optional: bool = False
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/prompts/chat.py#L129)
