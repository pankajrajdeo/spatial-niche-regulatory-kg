---
title: "BaseAuthContext"
description: "Base class for authentication context."
source: "https://reference.langchain.com/python/langgraph-sdk/auth/types/BaseAuthContext"
category: "reference"
tags: [reference, langgraph-sdk, auth, types, baseauthcontext]
---

# BaseAuthContext

> **Class** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/auth/types/BaseAuthContext)

Base class for authentication context.

Provides the fundamental authentication information needed for
authorization decisions.

## Signature

```python
BaseAuthContext(
    self,
    permissions: Sequence[str],
    user: BaseUser,
)
```

## Constructors

```python
__init__(
    self,
    permissions: Sequence[str],
    user: BaseUser,
) -> None
```

| Name | Type |
|------|------|
| `permissions` | `Sequence[str]` |
| `user` | `BaseUser` |

## Properties

- `permissions`
- `user`

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/d5f4b2aa960940effc8430165ab3604038e817af/libs/sdk-py/langgraph_sdk/auth/types.py#L373)
