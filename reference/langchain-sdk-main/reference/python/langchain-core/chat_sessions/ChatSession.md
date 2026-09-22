---
title: "ChatSession"
description: "Chat Session."
source: "https://reference.langchain.com/python/langchain-core/chat_sessions/ChatSession"
category: "reference"
tags: [reference, langchain-core, chat_sessions, chatsession]
---

# ChatSession

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/chat_sessions/ChatSession)

Chat Session.

Chat Session represents a single conversation, channel, or other group of messages.

## Signature

```python
ChatSession()
```

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    messages: Sequence[BaseMessage],
    functions: Sequence[dict[str, Any]],
)
```

| Name | Type |
|------|------|
| `messages` | `Sequence[BaseMessage]` |
| `functions` | `Sequence[dict[str, Any]]` |

## Properties

- `messages`
- `functions`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/chat_sessions.py#L9)
