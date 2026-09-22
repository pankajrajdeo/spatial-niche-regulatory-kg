---
title: "messages"
description: "Get an iterator over messages."
source: "https://reference.langchain.com/python/langchain-core/language_models/fake_chat_models/GenericFakeChatModel/messages"
category: "reference"
tags: [reference, langchain-core, language_models, fake_chat_models, genericfakechatmodel, messages]
---

# messages

> **Attribute** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/language_models/fake_chat_models/GenericFakeChatModel/messages)

Get an iterator over messages.

This can be expanded to accept other types like Callables / dicts / strings
to make the interface more generic if needed.

!!! note
    if you want to pass a list, you can use `iter` to convert it to an iterator.

!!! warning
    Streaming is not implemented yet. We should try to implement it in the future by
    delegating to invoke and then breaking the resulting output into message chunks.

## Signature

```python
messages: Iterator[AIMessage | str]
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/language_models/fake_chat_models.py#L238)
