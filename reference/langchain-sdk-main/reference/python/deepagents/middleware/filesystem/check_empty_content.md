---
title: "check_empty_content"
description: "Check if content is empty and return warning message."
source: "https://reference.langchain.com/python/deepagents/middleware/filesystem/check_empty_content"
category: "reference"
tags: [reference, deepagents, middleware, filesystem, check_empty_content]
---

# check_empty_content

> **Function** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/utils/check_empty_content)

Check if content is empty and return warning message.

## Signature

```python
check_empty_content(
    content: str,
) -> str | None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `content` | `str` | Yes | Content to check |

## Returns

`str | None`

Warning message if empty, `None` otherwise

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/backends/utils.py#L284)
