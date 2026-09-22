---
title: "aformat_messages"
description: "Async format the chat template into a list of finalized messages."
source: "https://reference.langchain.com/python/langchain-core/prompts/chat/ChatPromptTemplate/aformat_messages"
category: "reference"
tags: [reference, langchain-core, prompts, chat, chatprompttemplate, aformat_messages]
---

# aformat_messages

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/prompts/chat/ChatPromptTemplate/aformat_messages)

Async format the chat template into a list of finalized messages.

## Signature

```python
aformat_messages(
    self,
    **kwargs: Any = {},
) -> list[BaseMessage]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `**kwargs` | `Any` | No | Keyword arguments to use for filling in template variables in all the template messages in this chat template. (default: `{}`) |

## Returns

`list[BaseMessage]`

List of formatted messages.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/prompts/chat.py#L1202)
