---
title: "BaseRateLimiter"
description: "Base class for rate limiters."
source: "https://reference.langchain.com/python/langchain-core/rate_limiters/BaseRateLimiter"
category: "reference"
tags: [reference, langchain-core, rate_limiters, baseratelimiter]
---

# BaseRateLimiter

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/rate_limiters/BaseRateLimiter)

Base class for rate limiters.

Usage of the base limiter is through the acquire and aacquire methods depending
on whether running in a sync or async context.

Implementations are free to add a timeout parameter to their initialize method
to allow users to specify a timeout for acquiring the necessary tokens when
using a blocking call.

Current limitations:

- Rate limiting information is not surfaced in tracing or callbacks. This means
    that the total time it takes to invoke a chat model will encompass both
    the time spent waiting for tokens and the time spent making the request.

## Signature

```python
BaseRateLimiter()
```

## Extends

- `abc.ABC`

## Methods

- [`acquire()`](https://reference.langchain.com/python/langchain-core/rate_limiters/BaseRateLimiter/acquire)
- [`aacquire()`](https://reference.langchain.com/python/langchain-core/rate_limiters/BaseRateLimiter/aacquire)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/rate_limiters.py#L11)
