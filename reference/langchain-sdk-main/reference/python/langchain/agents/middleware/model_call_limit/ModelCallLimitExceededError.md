---
title: "ModelCallLimitExceededError"
description: "Exception raised when model call limits are exceeded."
source: "https://reference.langchain.com/python/langchain/agents/middleware/model_call_limit/ModelCallLimitExceededError"
category: "reference"
tags: [reference, langchain, agents, middleware, model_call_limit, modelcalllimitexceedederror]
---

# ModelCallLimitExceededError

> **Class** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/model_call_limit/ModelCallLimitExceededError)

Exception raised when model call limits are exceeded.

This exception is raised when the configured exit behavior is `'error'` and either
the thread or run model call limit has been exceeded.

## Signature

```python
ModelCallLimitExceededError(
    self,
    thread_count: int,
    run_count: int,
    thread_limit: int | None,
    run_limit: int | None,
)
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `thread_count` | `int` | Yes | Current thread model call count. |
| `run_count` | `int` | Yes | Current run model call count. |
| `thread_limit` | `int \| None` | Yes | Thread model call limit (if set). |
| `run_limit` | `int \| None` | Yes | Run model call limit (if set). |

## Extends

- `Exception`

## Constructors

```python
__init__(
    self,
    thread_count: int,
    run_count: int,
    thread_limit: int | None,
    run_limit: int | None,
) -> None
```

| Name | Type |
|------|------|
| `thread_count` | `int` |
| `run_count` | `int` |
| `thread_limit` | `int \| None` |
| `run_limit` | `int \| None` |

## Properties

- `thread_count`
- `run_count`
- `thread_limit`
- `run_limit`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a18de590e7ccf5c647fbf3d689e5f1a15f78e9f5/libs/langchain_v1/langchain/agents/middleware/model_call_limit.py#L63)
