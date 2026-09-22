---
title: "detect_url"
description: "Detect URLs in content using regex and stdlib validation."
source: "https://reference.langchain.com/python/langchain/agents/middleware/pii/detect_url"
category: "reference"
tags: [reference, langchain, agents, middleware, pii, detect_url]
---

# detect_url

> **Function** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/_redaction/detect_url)

Detect URLs in content using regex and stdlib validation.

## Signature

```python
detect_url(
    content: str,
) -> list[PIIMatch]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `content` | `str` | Yes | The text content to scan for URLs. |

## Returns

`list[PIIMatch]`

A list of detected URL matches.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a18de590e7ccf5c647fbf3d689e5f1a15f78e9f5/libs/langchain_v1/langchain/agents/middleware/_redaction.py#L149)
