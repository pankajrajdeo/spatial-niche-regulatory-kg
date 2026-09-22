---
title: "SSRFPolicy"
description: "Immutable policy controlling which URLs/IPs are considered safe."
source: "https://reference.langchain.com/python/langchain-core/_security/_policy/SSRFPolicy"
category: "reference"
tags: [reference, langchain-core, security, policy, ssrfpolicy]
---

# SSRFPolicy

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/_security/_policy/SSRFPolicy)

Immutable policy controlling which URLs/IPs are considered safe.

## Signature

```python
SSRFPolicy(
    self,
    allowed_schemes: frozenset[str] = frozenset({'http', 'https'}),
    block_private_ips: bool = True,
    block_localhost: bool = True,
    block_cloud_metadata: bool = True,
    block_k8s_internal: bool = True,
    allowed_hosts: frozenset[str] = frozenset(),
    additional_blocked_cidrs: tuple[ipaddress.IPv4Network | ipaddress.IPv6Network, ...] = (),
)
```

## Constructors

```python
__init__(
    self,
    allowed_schemes: frozenset[str] = frozenset({'http', 'https'}),
    block_private_ips: bool = True,
    block_localhost: bool = True,
    block_cloud_metadata: bool = True,
    block_k8s_internal: bool = True,
    allowed_hosts: frozenset[str] = frozenset(),
    additional_blocked_cidrs: tuple[ipaddress.IPv4Network | ipaddress.IPv6Network, ...] = (),
) -> None
```

| Name | Type |
|------|------|
| `allowed_schemes` | `frozenset[str]` |
| `block_private_ips` | `bool` |
| `block_localhost` | `bool` |
| `block_cloud_metadata` | `bool` |
| `block_k8s_internal` | `bool` |
| `allowed_hosts` | `frozenset[str]` |
| `additional_blocked_cidrs` | `tuple[ipaddress.IPv4Network \| ipaddress.IPv6Network, ...]` |

## Properties

- `allowed_schemes`
- `block_private_ips`
- `block_localhost`
- `block_cloud_metadata`
- `block_k8s_internal`
- `allowed_hosts`
- `additional_blocked_cidrs`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/_security/_policy.py#L102)
