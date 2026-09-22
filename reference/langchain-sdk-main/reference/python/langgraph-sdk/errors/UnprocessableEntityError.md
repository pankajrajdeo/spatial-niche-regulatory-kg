---
title: "UnprocessableEntityError"
description: "- APIStatusError"
source: "https://reference.langchain.com/python/langgraph-sdk/errors/UnprocessableEntityError"
category: "reference"
tags: [reference, langgraph-sdk, errors, unprocessableentityerror]
---

# UnprocessableEntityError

> **Class** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/errors/UnprocessableEntityError)

## Signature

```python
UnprocessableEntityError(
    self,
    message: str,
    *,
    response: httpx.Response,
    body: object | None,
)
```

## Extends

- `APIStatusError`

## Properties

- `status_code`

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/d5f4b2aa960940effc8430165ab3604038e817af/libs/sdk-py/langgraph_sdk/errors.py#L128)
