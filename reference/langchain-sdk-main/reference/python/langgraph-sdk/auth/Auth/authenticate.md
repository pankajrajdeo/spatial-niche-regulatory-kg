---
title: "authenticate"
description: "Register an authentication handler function."
source: "https://reference.langchain.com/python/langgraph-sdk/auth/Auth/authenticate"
category: "reference"
tags: [reference, langgraph-sdk, auth, authenticate]
---

# authenticate

> **Method** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/auth/Auth/authenticate)

Register an authentication handler function.

The authentication handler is responsible for verifying credentials
and returning user scopes. It can accept any of the following parameters
by name:

    - request (Request): The raw ASGI request object
    - path (str): The request path, e.g., "/threads/abcd-1234-abcd-1234/runs/abcd-1234-abcd-1234/stream"
    - method (str): The HTTP method, e.g., "GET"
    - path_params (dict[str, str]): URL path parameters, e.g., {"thread_id": "abcd-1234-abcd-1234", "run_id": "abcd-1234-abcd-1234"}
    - query_params (dict[str, str]): URL query parameters, e.g., {"stream": "true"}
    - headers (dict[bytes, bytes]): Request headers
    - authorization (str | None): The Authorization header value (e.g., "Bearer <token>")

## Signature

```python
authenticate(
    self,
    fn: AH,
) -> AH
```

## Description

???+ example "Examples"

Basic token authentication:

```python
@auth.authenticate
async def authenticate(authorization: str) -> str:
    user_id = verify_token(authorization)
    return user_id
```

Accept the full request context:

```python
@auth.authenticate
async def authenticate(
    method: str,
    path: str,
    headers: dict[str, bytes]
) -> str:
    user = await verify_request(method, path, headers)
    return user
```

Return user name and permissions:

```python
@auth.authenticate
async def authenticate(
    method: str,
    path: str,
    headers: dict[str, bytes]
) -> Auth.types.MinimalUserDict:
    permissions, user = await verify_request(method, path, headers)
    # Permissions could be things like ["runs:read", "runs:write", "threads:read", "threads:write"]
    return {
        "identity": user["id"],
        "permissions": permissions,
        "display_name": user["name"],
    }
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `fn` | `AH` | Yes | The authentication handler function to register. Must return a representation of the user. This could be a:     - string (the user id)     - dict containing {"identity": str, "permissions": list[str]}     - or an object with identity and permissions properties Permissions can be optionally used by your handlers downstream. |

## Returns

`AH`

The registered handler function.

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/d5f4b2aa960940effc8430165ab3604038e817af/libs/sdk-py/langgraph_sdk/auth/__init__.py#L225)
