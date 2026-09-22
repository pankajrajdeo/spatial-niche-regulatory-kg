---
title: "format_messages"
description: "Format messages from kwargs."
source: "https://reference.langchain.com/python/langchain-core/prompts/message/BaseMessagePromptTemplate/format_messages"
category: "reference"
tags: [reference, langchain-core, prompts, message, basemessageprompttemplate, format_messages]
---

# format_messages

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/prompts/message/BaseMessagePromptTemplate/format_messages)

Format messages from kwargs.

Should return a list of `BaseMessage` objects.

## Signature

```python
format_messages(
    self,
    **kwargs: Any = {},
) -> list[BaseMessage]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `**kwargs` | `Any` | No | Keyword arguments to use for formatting. (default: `{}`) |

## Returns

`list[BaseMessage]`

List of `BaseMessage` objects.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/prompts/message.py#L33)
