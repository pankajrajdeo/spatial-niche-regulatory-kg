---
title: "validate_retry_params"
description: "Validate retry parameters."
source: "https://reference.langchain.com/python/langchain/agents/middleware/model_retry/validate_retry_params"
category: "reference"
tags: [reference, langchain, agents, middleware, model_retry, validate_retry_params]
---

# validate_retry_params

> **Function** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/_retry/validate_retry_params)

Validate retry parameters.

## Signature

```python
validate_retry_params(
    max_retries: int,
    initial_delay: float,
    max_delay: float,
    backoff_factor: float,
) -> None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `max_retries` | `int` | Yes | Maximum number of retry attempts. |
| `initial_delay` | `float` | Yes | Initial delay in seconds before first retry. |
| `max_delay` | `float` | Yes | Maximum delay in seconds between retries. |
| `backoff_factor` | `float` | Yes | Multiplier for exponential backoff. |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a18de590e7ccf5c647fbf3d689e5f1a15f78e9f5/libs/langchain_v1/langchain/agents/middleware/_retry.py#L39)
