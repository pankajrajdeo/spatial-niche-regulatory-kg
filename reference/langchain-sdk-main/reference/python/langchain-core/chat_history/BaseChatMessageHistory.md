---
title: "BaseChatMessageHistory"
description: "Abstract base class for storing chat message history."
source: "https://reference.langchain.com/python/langchain-core/chat_history/BaseChatMessageHistory"
category: "reference"
tags: [reference, langchain-core, chat_history, basechatmessagehistory]
---

# BaseChatMessageHistory

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/chat_history/BaseChatMessageHistory)

Abstract base class for storing chat message history.

Implementations guidelines:

Implementations are expected to over-ride all or some of the following methods:

* `add_messages`: sync variant for bulk addition of messages
* `aadd_messages`: async variant for bulk addition of messages
* `messages`: sync variant for getting messages
* `aget_messages`: async variant for getting messages
* `clear`: sync variant for clearing messages
* `aclear`: async variant for clearing messages

`add_messages` contains a default implementation that calls `add_message`
for each message in the sequence. This is provided for backwards compatibility
with existing implementations which only had `add_message`.

Async variants all have default implementations that call the sync variants.
Implementers can choose to override the async implementations to provide
truly async implementations.

Usage guidelines:

When used for updating history, users should favor usage of `add_messages`
over `add_message` or other variants like `add_user_message` and `add_ai_message`
to avoid unnecessary round-trips to the underlying persistence layer.

## Signature

```python
BaseChatMessageHistory()
```

## Description

**Example:**

```python
import json
import os
from langchain_core.messages import messages_from_dict, message_to_dict

class FileChatMessageHistory(BaseChatMessageHistory):
    storage_path: str
    session_id: str

    @property
    def messages(self) -> list[BaseMessage]:
        try:
            with open(
                os.path.join(self.storage_path, self.session_id),
                "r",
                encoding="utf-8",
            ) as f:
                messages_data = json.load(f)
            return messages_from_dict(messages_data)
        except FileNotFoundError:
            return []

    def add_messages(self, messages: Sequence[BaseMessage]) -> None:
        all_messages = list(self.messages)  # Existing messages
        all_messages.extend(messages)  # Add new messages

        serialized = [message_to_dict(message) for message in all_messages]
        file_path = os.path.join(self.storage_path, self.session_id)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(serialized, f)

    def clear(self) -> None:
        file_path = os.path.join(self.storage_path, self.session_id)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump([], f)
```

## Extends

- `ABC`

## Properties

- `messages`

## Methods

- [`aget_messages()`](https://reference.langchain.com/python/langchain-core/chat_history/BaseChatMessageHistory/aget_messages)
- [`add_user_message()`](https://reference.langchain.com/python/langchain-core/chat_history/BaseChatMessageHistory/add_user_message)
- [`add_ai_message()`](https://reference.langchain.com/python/langchain-core/chat_history/BaseChatMessageHistory/add_ai_message)
- [`add_message()`](https://reference.langchain.com/python/langchain-core/chat_history/BaseChatMessageHistory/add_message)
- [`add_messages()`](https://reference.langchain.com/python/langchain-core/chat_history/BaseChatMessageHistory/add_messages)
- [`aadd_messages()`](https://reference.langchain.com/python/langchain-core/chat_history/BaseChatMessageHistory/aadd_messages)
- [`clear()`](https://reference.langchain.com/python/langchain-core/chat_history/BaseChatMessageHistory/clear)
- [`aclear()`](https://reference.langchain.com/python/langchain-core/chat_history/BaseChatMessageHistory/aclear)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/chat_history.py#L22)
