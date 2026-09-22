---
title: "aget_messages"
description: "Async version of getting messages."
source: "https://reference.langchain.com/python/langchain-core/chat_history/BaseChatMessageHistory/aget_messages"
category: "reference"
tags: [reference, langchain-core, chat_history, basechatmessagehistory, aget_messages]
---

# aget_messages

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/chat_history/BaseChatMessageHistory/aget_messages)

Async version of getting messages.

Can over-ride this method to provide an efficient async implementation.

In general, fetching messages may involve IO to the underlying persistence
layer.

## Signature

```python
aget_messages(
    self,
) -> list[BaseMessage]
```

## Returns

`list[BaseMessage]`

The messages.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/chat_history.py#L99)
