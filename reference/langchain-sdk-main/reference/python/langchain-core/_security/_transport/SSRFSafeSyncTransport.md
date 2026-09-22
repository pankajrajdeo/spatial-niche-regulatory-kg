---
title: "SSRFSafeSyncTransport"
description: "httpx sync transport that validates DNS results against an SSRF policy."
source: "https://reference.langchain.com/python/langchain-core/_security/_transport/SSRFSafeSyncTransport"
category: "reference"
tags: [reference, langchain-core, security, transport, ssrfsafesynctransport]
---

# SSRFSafeSyncTransport

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/_security/_transport/SSRFSafeSyncTransport)

httpx sync transport that validates DNS results against an SSRF policy.

Sync mirror of `SSRFSafeTransport`. See that class for full documentation.

## Signature

```python
SSRFSafeSyncTransport(
    self,
    policy: SSRFPolicy = DEFAULT_SSRF_POLICY,
    **transport_kwargs: object = {},
)
```

## Extends

- `httpx.BaseTransport`

## Constructors

```python
__init__(
    self,
    policy: SSRFPolicy = DEFAULT_SSRF_POLICY,
    **transport_kwargs: object = {},
) -> None
```

| Name | Type |
|------|------|
| `policy` | `SSRFPolicy` |

## Methods

- [`handle_request()`](https://reference.langchain.com/python/langchain-core/_security/_transport/SSRFSafeSyncTransport/handle_request)
- [`close()`](https://reference.langchain.com/python/langchain-core/_security/_transport/SSRFSafeSyncTransport/close)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/_security/_transport.py#L130)
