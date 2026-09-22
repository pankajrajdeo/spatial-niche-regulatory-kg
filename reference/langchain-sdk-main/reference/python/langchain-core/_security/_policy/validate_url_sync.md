---
title: "validate_url_sync"
description: "Synchronous URL validation (no DNS resolution)."
source: "https://reference.langchain.com/python/langchain-core/_security/_policy/validate_url_sync"
category: "reference"
tags: [reference, langchain-core, security, policy, validate_url_sync]
---

# validate_url_sync

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/_security/_policy/validate_url_sync)

Synchronous URL validation (no DNS resolution).

Suitable for Pydantic validators and other sync contexts. Checks scheme
and hostname patterns only - use `validate_url` for full DNS-aware checking.

## Signature

```python
validate_url_sync(
    url: str,
    policy: SSRFPolicy = DEFAULT_SSRF_POLICY,
) -> None
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/_security/_policy.py#L278)
