---
title: "detect_email"
description: "Detect email addresses in content."
source: "https://reference.langchain.com/python/langchain/agents/middleware/_redaction/detect_email"
category: "reference"
tags: [reference, langchain, agents, middleware, redaction, detect_email]
---

# detect_email

> **Function** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/_redaction/detect_email)

Detect email addresses in content.

## Signature

```python
detect_email(
    content: str,
) -> list[PIIMatch]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `content` | `str` | Yes | The text content to scan for email addresses. |

## Returns

`list[PIIMatch]`

A list of detected email matches.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a18de590e7ccf5c647fbf3d689e5f1a15f78e9f5/libs/langchain_v1/langchain/agents/middleware/_redaction.py#L50)
