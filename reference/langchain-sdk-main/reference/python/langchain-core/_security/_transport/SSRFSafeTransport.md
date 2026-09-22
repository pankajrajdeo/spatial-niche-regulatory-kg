---
title: "SSRFSafeTransport"
description: "httpx async transport that validates DNS results against an SSRF policy."
source: "https://reference.langchain.com/python/langchain-core/_security/_transport/SSRFSafeTransport"
category: "reference"
tags: [reference, langchain-core, security, transport, ssrfsafetransport]
---

# SSRFSafeTransport

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/_security/_transport/SSRFSafeTransport)

httpx async transport that validates DNS results against an SSRF policy.

For every outgoing request the transport:
1. Checks the URL scheme against `policy.allowed_schemes`.
2. Validates the hostname against blocked patterns.
3. Resolves DNS and validates **all** returned IPs.
4. Rewrites the request to connect to the first valid IP while
   preserving the original `Host` header and TLS SNI hostname.

Redirects are re-validated on each hop because `follow_redirects`
is set on the *client*, causing `handle_async_request` to be called
again for each redirect target.

## Signature

```python
SSRFSafeTransport(
    self,
    policy: SSRFPolicy = DEFAULT_SSRF_POLICY,
    **transport_kwargs: object = {},
)
```

## Extends

- `httpx.AsyncBaseTransport`

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

- [`handle_async_request()`](https://reference.langchain.com/python/langchain-core/_security/_transport/SSRFSafeTransport/handle_async_request)
- [`aclose()`](https://reference.langchain.com/python/langchain-core/_security/_transport/SSRFSafeTransport/aclose)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/_security/_transport.py#L31)
