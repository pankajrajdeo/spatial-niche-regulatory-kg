---
title: "append_to_system_message"
description: "Append text to a system message."
source: "https://reference.langchain.com/python/deepagents/graph/append_to_system_message"
category: "reference"
tags: [reference, deepagents, graph, append_to_system_message]
---

# append_to_system_message

> **Function** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/_utils/append_to_system_message)

Append text to a system message.

## Signature

```python
append_to_system_message(
    system_message: SystemMessage | None,
    text: str,
) -> SystemMessage
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `system_message` | `SystemMessage \| None` | Yes | Existing system message or None. |
| `text` | `str` | Yes | Text to add to the system message. |

## Returns

`SystemMessage`

New SystemMessage with the text appended.

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/middleware/_utils.py#L6)
