---
title: "detect_ip"
description: "Detect IPv4 or IPv6 addresses in content."
source: "https://reference.langchain.com/python/langchain/agents/middleware/_redaction/detect_ip"
category: "reference"
tags: [reference, langchain, agents, middleware, redaction, detect_ip]
---

# detect_ip

> **Function** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/_redaction/detect_ip)

Detect IPv4 or IPv6 addresses in content.

## Signature

```python
detect_ip(
    content: str,
) -> list[PIIMatch]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `content` | `str` | Yes | The text content to scan for IP addresses. |

## Returns

`list[PIIMatch]`

A list of detected IP address matches.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a18de590e7ccf5c647fbf3d689e5f1a15f78e9f5/libs/langchain_v1/langchain/agents/middleware/_redaction.py#L98)
