---
title: "SSRFProtectedHttpsUrl"
description: "View source on GitHub"
source: "https://reference.langchain.com/python/langchain-core/_security/_ssrf_protection/SSRFProtectedHttpsUrl"
category: "reference"
tags: [reference, langchain-core, security, ssrf_protection, ssrfprotectedhttpsurl]
---

# SSRFProtectedHttpsUrl

> **Attribute** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/_security/_ssrf_protection/SSRFProtectedHttpsUrl)

## Signature

```python
SSRFProtectedHttpsUrl = Annotated[HttpUrl, BeforeValidator(_validate_url_ssrf_https_only)]
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/_security/_ssrf_protection.py#L150)
