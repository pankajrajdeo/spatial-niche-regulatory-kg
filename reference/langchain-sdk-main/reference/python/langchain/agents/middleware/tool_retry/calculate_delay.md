---
title: "calculate_delay"
description: "Calculate delay for a retry attempt with exponential backoff and optional jitter."
source: "https://reference.langchain.com/python/langchain/agents/middleware/tool_retry/calculate_delay"
category: "reference"
tags: [reference, langchain, agents, middleware, tool_retry, calculate_delay]
---

# calculate_delay

> **Function** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/_retry/calculate_delay)

Calculate delay for a retry attempt with exponential backoff and optional jitter.

## Signature

```python
calculate_delay(
    retry_number: int,
    *,
    backoff_factor: float,
    initial_delay: float,
    max_delay: float,
    jitter: bool,
) -> float
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `retry_number` | `int` | Yes | The retry attempt number (0-indexed). |
| `backoff_factor` | `float` | Yes | Multiplier for exponential backoff.  Set to `0.0` for constant delay. |
| `initial_delay` | `float` | Yes | Initial delay in seconds before first retry. |
| `max_delay` | `float` | Yes | Maximum delay in seconds between retries.  Caps exponential backoff growth. |
| `jitter` | `bool` | Yes | Whether to add random jitter to delay to avoid thundering herd. |

## Returns

`float`

Delay in seconds before next retry.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a18de590e7ccf5c647fbf3d689e5f1a15f78e9f5/libs/langchain_v1/langchain/agents/middleware/_retry.py#L96)
