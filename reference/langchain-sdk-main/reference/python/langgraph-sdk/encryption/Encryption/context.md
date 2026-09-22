---
title: "context"
description: "Register a context handler to derive encryption context from auth."
source: "https://reference.langchain.com/python/langgraph-sdk/encryption/Encryption/context"
category: "reference"
tags: [reference, langgraph-sdk, encryption, context]
---

# context

> **Method** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/encryption/Encryption/context)

Register a context handler to derive encryption context from auth.

The handler receives the authenticated user and current EncryptionContext,
and returns a dict that becomes ctx.metadata for encrypt/decrypt handlers.

This allows encryption context to be derived from JWT claims or other
auth-derived data instead of requiring a separate X-Encryption-Context header.

Note: The context handler is called once per request in middleware,
so ctx.model and ctx.field will be None in the handler.

## Signature

```python
context(
    self,
    fn: types.ContextHandler,
) -> types.ContextHandler
```

## Description

**Example:**

```python
from langgraph_sdk import Encryption, EncryptionContext
from starlette.authentication import BaseUser

encryption = Encryption()

@encryption.context
async def get_context(user: BaseUser, ctx: EncryptionContext) -> dict:
    # Derive encryption context from authenticated user
    return {
        **ctx.metadata,  # preserve X-Encryption-Context header if present
        "tenant_id": user.tenant_id,
    }
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `fn` | `types.ContextHandler` | Yes | The context handler function |

## Returns

`types.ContextHandler`

The registered handler function

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/d5f4b2aa960940effc8430165ab3604038e817af/libs/sdk-py/langgraph_sdk/encryption/__init__.py#L394)
