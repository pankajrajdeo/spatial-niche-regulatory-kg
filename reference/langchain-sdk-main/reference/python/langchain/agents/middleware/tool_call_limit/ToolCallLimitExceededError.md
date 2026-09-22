---
title: "ToolCallLimitExceededError"
description: "Exception raised when tool call limits are exceeded."
source: "https://reference.langchain.com/python/langchain/agents/middleware/tool_call_limit/ToolCallLimitExceededError"
category: "reference"
tags: [reference, langchain, agents, middleware, tool_call_limit, toolcalllimitexceedederror]
---

# ToolCallLimitExceededError

> **Class** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/tool_call_limit/ToolCallLimitExceededError)

Exception raised when tool call limits are exceeded.

This exception is raised when the configured exit behavior is `'error'` and either
the thread or run tool call limit has been exceeded.

## Signature

```python
ToolCallLimitExceededError(
    self,
    thread_count: int,
    run_count: int,
    thread_limit: int | None,
    run_limit: int | None,
    tool_name: str | None = None,
)
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `thread_count` | `int` | Yes | Current thread tool call count. |
| `run_count` | `int` | Yes | Current run tool call count. |
| `thread_limit` | `int \| None` | Yes | Thread tool call limit (if set). |
| `run_limit` | `int \| None` | Yes | Run tool call limit (if set). |
| `tool_name` | `str \| None` | No | Tool name being limited (if specific tool), or None for all tools. (default: `None`) |

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
    tool_name: str | None = None,
) -> None
```

| Name | Type |
|------|------|
| `thread_count` | `int` |
| `run_count` | `int` |
| `thread_limit` | `int \| None` |
| `run_limit` | `int \| None` |
| `tool_name` | `str \| None` |

## Properties

- `thread_count`
- `run_count`
- `thread_limit`
- `run_limit`
- `tool_name`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a18de590e7ccf5c647fbf3d689e5f1a15f78e9f5/libs/langchain_v1/langchain/agents/middleware/tool_call_limit.py#L105)
