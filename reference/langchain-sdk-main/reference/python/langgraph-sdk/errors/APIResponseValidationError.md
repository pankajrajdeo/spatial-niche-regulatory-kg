---
title: "APIResponseValidationError"
description: "- APIError"
source: "https://reference.langchain.com/python/langgraph-sdk/errors/APIResponseValidationError"
category: "reference"
tags: [reference, langgraph-sdk, errors, apiresponsevalidationerror]
---

# APIResponseValidationError

> **Class** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/errors/APIResponseValidationError)

## Signature

```python
APIResponseValidationError(
    self,
    response: httpx.Response,
    body: object | None,
    *,
    message: str | None = None,
)
```

## Extends

- `APIError`

## Constructors

```python
__init__(
    self,
    response: httpx.Response,
    body: object | None,
    *,
    message: str | None = None,
) -> None
```

| Name | Type |
|------|------|
| `response` | `httpx.Response` |
| `body` | `object \| None` |
| `message` | `str \| None` |

## Properties

- `response`
- `status_code`

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/d5f4b2aa960940effc8430165ab3604038e817af/libs/sdk-py/langgraph_sdk/errors.py#L62)
