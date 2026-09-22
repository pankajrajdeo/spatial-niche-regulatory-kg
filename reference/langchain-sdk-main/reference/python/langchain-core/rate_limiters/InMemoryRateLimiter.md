---
title: "InMemoryRateLimiter"
description: "An in memory rate limiter based on a token bucket algorithm."
source: "https://reference.langchain.com/python/langchain-core/rate_limiters/InMemoryRateLimiter"
category: "reference"
tags: [reference, langchain-core, rate_limiters, inmemoryratelimiter]
---

# InMemoryRateLimiter

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/rate_limiters/InMemoryRateLimiter)

An in memory rate limiter based on a token bucket algorithm.

This is an in memory rate limiter, so it cannot rate limit across
different processes.

The rate limiter only allows time-based rate limiting and does not
take into account any information about the input or the output, so it
cannot be used to rate limit based on the size of the request.

It is thread safe and can be used in either a sync or async context.

The in memory rate limiter is based on a token bucket. The bucket is filled
with tokens at a given rate. Each request consumes a token. If there are
not enough tokens in the bucket, the request is blocked until there are
enough tokens.

These tokens have nothing to do with LLM tokens. They are just
a way to keep track of how many requests can be made at a given time.

Current limitations:

- The rate limiter is not designed to work across different processes. It is
    an in-memory rate limiter, but it is thread safe.
- The rate limiter only supports time-based rate limiting. It does not take
    into account the size of the request or any other factors.

## Signature

```python
InMemoryRateLimiter(
    self,
    *,
    requests_per_second: float = 1,
    check_every_n_seconds: float = 0.1,
    max_bucket_size: float = 1,
)
```

## Description

**Example:**

```python
import time

from langchain_core.rate_limiters import InMemoryRateLimiter

rate_limiter = InMemoryRateLimiter(
    requests_per_second=0.1,  # <-- Can only make a request once every 10 seconds!!
    check_every_n_seconds=0.1,  # Wake up every 100 ms to check whether allowed to make a request,
    max_bucket_size=10,  # Controls the maximum burst size.
)

from langchain_anthropic import ChatAnthropic

model = ChatAnthropic(
    model_name="claude-sonnet-4-5-20250929", rate_limiter=rate_limiter
)

for _ in range(5):
    tic = time.time()
    model.invoke("hello")
    toc = time.time()
    print(toc - tic)
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `requests_per_second` | `float` | No | The number of tokens to add per second to the bucket. The tokens represent "credit" that can be used to make requests. (default: `1`) |
| `check_every_n_seconds` | `float` | No | Check whether the tokens are available every this many seconds. Can be a float to represent fractions of a second. (default: `0.1`) |
| `max_bucket_size` | `float` | No | The maximum number of tokens that can be in the bucket. Must be at least `1`. Used to prevent bursts of requests. (default: `1`) |

## Extends

- `BaseRateLimiter`

## Constructors

```python
__init__(
    self,
    *,
    requests_per_second: float = 1,
    check_every_n_seconds: float = 0.1,
    max_bucket_size: float = 1,
) -> None
```

| Name | Type |
|------|------|
| `requests_per_second` | `float` |
| `check_every_n_seconds` | `float` |
| `max_bucket_size` | `float` |

## Properties

- `requests_per_second`
- `available_tokens`
- `max_bucket_size`
- `last`
- `check_every_n_seconds`

## Methods

- [`acquire()`](https://reference.langchain.com/python/langchain-core/rate_limiters/InMemoryRateLimiter/acquire)
- [`aacquire()`](https://reference.langchain.com/python/langchain-core/rate_limiters/InMemoryRateLimiter/aacquire)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/rate_limiters.py#L67)
