---
title: "should_retry_exception"
description: "Check if an exception should trigger a retry."
source: "https://reference.langchain.com/python/langchain/agents/middleware/tool_retry/should_retry_exception"
category: "reference"
tags: [reference, langchain, agents, middleware, tool_retry, should_retry_exception]
---

# should_retry_exception

> **Function** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/_retry/should_retry_exception)

Check if an exception should trigger a retry.

## Signature

```python
should_retry_exception(
    exc: Exception,
    retry_on: RetryOn,
) -> bool
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `exc` | `Exception` | Yes | The exception that occurred. |
| `retry_on` | `RetryOn` | Yes | Either a tuple of exception types to retry on, or a callable that takes an exception and returns `True` if it should be retried. |

## Returns

`bool`

`True` if the exception should be retried, `False` otherwise.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a18de590e7ccf5c647fbf3d689e5f1a15f78e9f5/libs/langchain_v1/langchain/agents/middleware/_retry.py#L77)
