---
title: "messages_to_dict"
description: "Convert a sequence of Messages to a list of dictionaries."
source: "https://reference.langchain.com/python/langchain-core/messages/messages_to_dict"
category: "reference"
tags: [reference, langchain-core, messages, messages_to_dict]
---

# messages_to_dict

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/messages/base/messages_to_dict)

Convert a sequence of Messages to a list of dictionaries.

## Signature

```python
messages_to_dict(
    messages: Sequence[BaseMessage],
) -> list[dict[str, Any]]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `messages` | `Sequence[BaseMessage]` | Yes | Sequence of messages (as `BaseMessage`s) to convert. |

## Returns

`list[dict[str, Any]]`

List of messages as dicts.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/messages/base.py#L488)
