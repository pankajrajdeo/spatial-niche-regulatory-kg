---
title: "APIStatusError"
description: "- APIError"
source: "https://reference.langchain.com/python/langgraph-sdk/errors/APIStatusError"
category: "reference"
tags: [reference, langgraph-sdk, errors, apistatuserror]
---

# APIStatusError

> **Class** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/errors/APIStatusError)

## Signature

```python
APIStatusError(
    self,
    message: str,
    *,
    response: httpx.Response,
    body: object | None,
)
```

## Extends

- `APIError`

## Constructors

```python
__init__(
    self,
    message: str,
    *,
    response: httpx.Response,
    body: object | None,
) -> None
```

| Name | Type |
|------|------|
| `message` | `str` |
| `response` | `httpx.Response` |
| `body` | `object \| None` |

## Properties

- `response`
- `status_code`
- `request_id`

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/d5f4b2aa960940effc8430165ab3604038e817af/libs/sdk-py/langgraph_sdk/errors.py#L82)
