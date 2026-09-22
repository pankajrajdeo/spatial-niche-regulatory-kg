---
title: "add_user_message"
description: "Convenience method for adding a human message string to the store."
source: "https://reference.langchain.com/python/langchain-core/chat_history/BaseChatMessageHistory/add_user_message"
category: "reference"
tags: [reference, langchain-core, chat_history, basechatmessagehistory, add_user_message]
---

# add_user_message

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/chat_history/BaseChatMessageHistory/add_user_message)

Convenience method for adding a human message string to the store.

!!! note

    This is a convenience method. Code should favor the bulk `add_messages`
    interface instead to save on round-trips to the persistence layer.

This method may be deprecated in a future release.

## Signature

```python
add_user_message(
    self,
    message: HumanMessage | str,
) -> None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `message` | `HumanMessage \| str` | Yes | The `HumanMessage` to add to the store. |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/chat_history.py#L112)
