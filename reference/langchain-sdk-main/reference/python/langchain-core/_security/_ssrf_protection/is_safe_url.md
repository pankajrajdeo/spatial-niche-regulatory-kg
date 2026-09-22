---
title: "is_safe_url"
description: "Non-throwing version of validate_safe_url."
source: "https://reference.langchain.com/python/langchain-core/_security/_ssrf_protection/is_safe_url"
category: "reference"
tags: [reference, langchain-core, security, ssrf_protection, is_safe_url]
---

# is_safe_url

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/_security/_ssrf_protection/is_safe_url)

Non-throwing version of `validate_safe_url`.

## Signature

```python
is_safe_url(
    url: str | AnyHttpUrl,
    *,
    allow_private: bool = False,
    allow_http: bool = True,
) -> bool
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/_security/_ssrf_protection.py#L110)
