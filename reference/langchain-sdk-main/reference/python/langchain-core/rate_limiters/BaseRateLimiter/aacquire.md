---
title: "aacquire"
description: "Attempt to acquire the necessary tokens for the rate limiter."
source: "https://reference.langchain.com/python/langchain-core/rate_limiters/BaseRateLimiter/aacquire"
category: "reference"
tags: [reference, langchain-core, rate_limiters, baseratelimiter, aacquire]
---

# aacquire

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/rate_limiters/BaseRateLimiter/aacquire)

Attempt to acquire the necessary tokens for the rate limiter.

This method blocks until the required tokens are available if `blocking`
is set to `True`.

If `blocking` is set to `False`, the method will immediately return the result
of the attempt to acquire the tokens.

## Signature

```python
aacquire(
    self,
    *,
    blocking: bool = True,
) -> bool
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `blocking` | `bool` | No | If `True`, the method will block until the tokens are available. If `False`, the method will return immediately with the result of the attempt. (default: `True`) |

## Returns

`bool`

`True` if the tokens were successfully acquired, `False` otherwise.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/rate_limiters.py#L47)
