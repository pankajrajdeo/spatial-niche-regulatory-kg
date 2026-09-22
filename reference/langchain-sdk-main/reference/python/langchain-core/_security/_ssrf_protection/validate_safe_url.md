---
title: "validate_safe_url"
description: "Validate a URL for SSRF protection."
source: "https://reference.langchain.com/python/langchain-core/_security/_ssrf_protection/validate_safe_url"
category: "reference"
tags: [reference, langchain-core, security, ssrf_protection, validate_safe_url]
---

# validate_safe_url

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/_security/_ssrf_protection/validate_safe_url)

Validate a URL for SSRF protection.

This function validates URLs to prevent Server-Side Request Forgery (SSRF) attacks
by blocking requests to private networks and cloud metadata endpoints.

## Signature

```python
validate_safe_url(
    url: str | AnyHttpUrl,
    *,
    allow_private: bool = False,
    allow_http: bool = True,
) -> str
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `url` | `str \| AnyHttpUrl` | Yes | The URL to validate (string or Pydantic HttpUrl). |
| `allow_private` | `bool` | No | If `True`, allows private IPs and localhost (for development).           Cloud metadata endpoints are ALWAYS blocked. (default: `False`) |
| `allow_http` | `bool` | No | If `True`, allows both HTTP and HTTPS.  If `False`, only HTTPS. (default: `True`) |

## Returns

`str`

The validated URL as a string.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/_security/_ssrf_protection.py#L41)
