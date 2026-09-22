---
title: "validate_url"
description: "Validate a URL against the SSRF policy, including DNS resolution."
source: "https://reference.langchain.com/python/langchain-core/_security/_policy/validate_url"
category: "reference"
tags: [reference, langchain-core, security, policy, validate_url]
---

# validate_url

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/_security/_policy/validate_url)

Validate a URL against the SSRF policy, including DNS resolution.

This is the primary entry-point for async code paths. It delegates
scheme/hostname/allowed-hosts checks to `validate_url_sync`, then
resolves DNS and validates every resolved IP.

## Signature

```python
validate_url(
    url: str,
    policy: SSRFPolicy = DEFAULT_SSRF_POLICY,
) -> None
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/_security/_policy.py#L245)
