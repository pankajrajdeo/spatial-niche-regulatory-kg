---
title: "StudioUser"
description: "A user object that's populated from authenticated requests from the LangGraph studio."
source: "https://reference.langchain.com/python/langgraph-sdk/auth/types/StudioUser"
category: "reference"
tags: [reference, langgraph-sdk, auth, types, studiouser]
---

# StudioUser

> **Class** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/auth/types/StudioUser)

A user object that's populated from authenticated requests from the LangGraph studio.

Note: Studio auth can be disabled in your `langgraph.json` config.

```json
{
  "auth": {
    "disable_studio_auth": true
  }
}
```

You can use `isinstance` checks in your authorization handlers (`@auth.on`) to control access specifically
for developers accessing the instance from the LangGraph Studio UI.

???+ example "Examples"

    Use `@auth.on` to deny by default, but allow Studio users through:

```python
    @auth.on
    async def deny_all_except_studio(ctx: Auth.types.AuthContext, value: Any) -> bool:
        # Allow Studio users, deny everyone else by default
        if isinstance(ctx.user, Auth.types.StudioUser):
            return True
        return False

    # Then add specific handlers to allow access for non-Studio users
    @auth.on.threads
    async def allow_thread_access(ctx: Auth.types.AuthContext, value: Any) -> Auth.types.FilterType:
        return {"owner": ctx.user.identity}
```

## Signature

```python
StudioUser(
    self,
    username: str,
    is_authenticated: bool = False,
)
```

## Constructors

```python
__init__(
    self,
    username: str,
    is_authenticated: bool = False,
) -> None
```

| Name | Type |
|------|------|
| `username` | `str` |
| `is_authenticated` | `bool` |

## Properties

- `username`
- `is_authenticated`
- `display_name`
- `identity`
- `permissions`

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/d5f4b2aa960940effc8430165ab3604038e817af/libs/sdk-py/langgraph_sdk/auth/types.py#L218)
