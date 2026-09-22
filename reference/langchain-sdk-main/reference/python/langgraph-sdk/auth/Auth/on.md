---
title: "on"
description: "Entry point for authorization handlers that control access to specific resources."
source: "https://reference.langchain.com/python/langgraph-sdk/auth/Auth/on"
category: "reference"
tags: [reference, langgraph-sdk, auth, on]
---

# on

> **Attribute** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/auth/Auth/on)

Entry point for authorization handlers that control access to specific resources.

The on class provides a flexible way to define authorization rules for different
resources and actions in your application. It supports three main usage patterns:

1. Global handlers that run for all resources and actions
2. Resource-specific handlers that run for all actions on a resource
3. Resource and action specific handlers for fine-grained control

## Signature

```python
on = _On(self)
```

## Description

**Each handler must be an async function that accepts two parameters:**

- ctx (AuthContext): Contains request context and authenticated user info
- value: The data being authorized (type varies by endpoint)

The handler should return one of:

    - None or True: Accept the request
    - False: Reject with 403 error
    - FilterType: Apply filtering rules to the response

???+ example "Examples"

    Start by denying all requests by default, then add specific handlers
    to allow access:

```python
    # Default deny: reject all unhandled requests
    @auth.on
    async def deny_all(ctx: AuthContext, value: Any) -> False:
        return False
```

    Resource-specific handler. This takes precedence over the global handler
    for all actions on the `threads` resource:

```python
    @auth.on.threads
    async def allow_thread_access(ctx: AuthContext, value: Any) -> Auth.types.FilterType:
        # Only allow access to threads owned by the user
        return {"owner": ctx.user.identity}
```

    Resource and action specific handler:

```python
    @auth.on.threads.delete
    async def allow_admin_thread_deletion(ctx: AuthContext, value: Any) -> bool:
        # Only admins can delete threads
        return "admin" in ctx.user.permissions
```

    Multiple resources or actions:

```python
    @auth.on(resources=["threads", "assistants"], actions=["read", "search"])
    async def allow_reads(ctx: AuthContext, value: Any) -> Auth.types.FilterType:
        # Allow read/search access to resources owned by the user
        return {"owner": ctx.user.identity}
```

    Auth for the `store` resource is a bit different since its structure is developer defined.
    You typically want to scope store operations by rewriting the namespace to include the user's identity.
    The `value` dict is mutable — changes to `value["namespace"]` are used by the server for the actual operation.

```python
    @auth.on.store
    async def scope_store(ctx: AuthContext, value: Auth.types.on.store.value):
        # Allow store access but scope to user's namespace
        namespace = tuple(value["namespace"]) if value.get("namespace") else ()
        if not namespace or namespace[0] != ctx.user.identity:
            namespace = (ctx.user.identity, *namespace)
        value["namespace"] = namespace
```

    You can also register handlers for specific store actions:

```python
    @auth.on.store.put
    async def allow_put(ctx: AuthContext, value: Auth.types.on.store.put.value):
        # Allow puts, scoped to user's namespace
        value["namespace"] = (ctx.user.identity, *value["namespace"])

    @auth.on.store.get
    async def allow_get(ctx: AuthContext, value: Auth.types.on.store.get.value):
        # Allow gets, scoped to user's namespace
        value["namespace"] = (ctx.user.identity, *value["namespace"])
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/d5f4b2aa960940effc8430165ab3604038e817af/libs/sdk-py/langgraph_sdk/auth/__init__.py#L130)
