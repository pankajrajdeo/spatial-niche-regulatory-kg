---
title: "messages"
description: "A property or attribute that returns a list of messages."
source: "https://reference.langchain.com/python/langchain-core/chat_history/BaseChatMessageHistory/messages"
category: "reference"
tags: [reference, langchain-core, chat_history, basechatmessagehistory, messages]
---

# messages

> **Attribute** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/chat_history/BaseChatMessageHistory/messages)

A property or attribute that returns a list of messages.

In general, getting the messages may involve IO to the underlying persistence
layer, so this operation is expected to incur some latency.

## Signature

```python
messages: list[BaseMessage]
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/chat_history.py#L92)
