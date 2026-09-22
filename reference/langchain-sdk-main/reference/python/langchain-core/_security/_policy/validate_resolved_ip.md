---
title: "validate_resolved_ip"
description: "Validate a resolved IP address against the SSRF policy."
source: "https://reference.langchain.com/python/langchain-core/_security/_policy/validate_resolved_ip"
category: "reference"
tags: [reference, langchain-core, security, policy, validate_resolved_ip]
---

# validate_resolved_ip

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/_security/_policy/validate_resolved_ip)

Validate a resolved IP address against the SSRF policy.

Raises SSRFBlockedError if the IP is blocked.

## Signature

```python
validate_resolved_ip(
    ip_str: str,
    policy: SSRFPolicy,
) -> None
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/_security/_policy.py#L194)
