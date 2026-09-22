---
title: "ToolRetryMiddleware"
description: "Middleware that automatically retries failed tool calls with configurable backoff."
source: "https://reference.langchain.com/python/langchain/agents/middleware/tool_retry/ToolRetryMiddleware"
category: "reference"
tags: [reference, langchain, agents, middleware, tool_retry, toolretrymiddleware]
---

# ToolRetryMiddleware

> **Class** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/tool_retry/ToolRetryMiddleware)

Middleware that automatically retries failed tool calls with configurable backoff.

Supports retrying on specific exceptions and exponential backoff.

## Signature

```python
ToolRetryMiddleware(
    self,
    *,
    max_retries: int = 2,
    tools: list[BaseTool | str] | None = None,
    retry_on: RetryOn = default_retry_on,
    on_failure: OnFailure = 'continue',
    backoff_factor: float = 2.0,
    initial_delay: float = 1.0,
    max_delay: float = 60.0,
    jitter: bool = True,
)
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `max_retries` | `int` | No | Maximum number of retry attempts after the initial call.  Must be `>= 0`. (default: `2`) |
| `tools` | `list[BaseTool \| str] \| None` | No | Optional list of tools or tool names to apply retry logic to.  Can be a list of `BaseTool` instances or tool name strings.  If `None`, applies to all tools. (default: `None`) |
| `retry_on` | `RetryOn` | No | Either a tuple of exception types to retry on, or a callable that takes an exception and returns `True` if it should be retried.  By default, retryable model errors and all unclassified exceptions are retried. Exceptions that do not match propagate immediately and are not handled by `on_failure`. (default: `default_retry_on`) |
| `on_failure` | `OnFailure` | No | Behavior when all retries are exhausted.  Options:  - `'continue'`: Return a `ToolMessage` with error details,     allowing the LLM to handle the failure and potentially recover. - `'error'`: Re-raise the exception, stopping agent execution. - **Custom callable:** Function that takes the exception and returns a     string for the `ToolMessage` content, allowing custom error     formatting.  **Deprecated values** (for backwards compatibility):  - `'return_message'`: Use `'continue'` instead. - `'raise'`: Use `'error'` instead. (default: `'continue'`) |
| `backoff_factor` | `float` | No | Multiplier for exponential backoff.  Each retry waits `initial_delay * (backoff_factor ** retry_number)` seconds.  Set to `0.0` for constant delay. (default: `2.0`) |
| `initial_delay` | `float` | No | Initial delay in seconds before first retry. (default: `1.0`) |
| `max_delay` | `float` | No | Maximum delay in seconds between retries.  Caps exponential backoff growth. (default: `60.0`) |
| `jitter` | `bool` | No | Whether to add random jitter (`±25%`) to delay to avoid thundering herd. (default: `True`) |

## Extends

- `AgentMiddleware[AgentState[ResponseT], ContextT, ResponseT]`

## Constructors

```python
__init__(
    self,
    *,
    max_retries: int = 2,
    tools: list[BaseTool | str] | None = None,
    retry_on: RetryOn = default_retry_on,
    on_failure: OnFailure = 'continue',
    backoff_factor: float = 2.0,
    initial_delay: float = 1.0,
    max_delay: float = 60.0,
    jitter: bool = True,
) -> None
```

| Name | Type |
|------|------|
| `max_retries` | `int` |
| `tools` | `list[BaseTool \| str] \| None` |
| `retry_on` | `RetryOn` |
| `on_failure` | `OnFailure` |
| `backoff_factor` | `float` |
| `initial_delay` | `float` |
| `max_delay` | `float` |
| `jitter` | `bool` |

## Properties

- `max_retries`
- `tools`
- `retry_on`
- `on_failure`
- `backoff_factor`
- `initial_delay`
- `max_delay`
- `jitter`

## Methods

- [`wrap_tool_call()`](https://reference.langchain.com/python/langchain/agents/middleware/tool_retry/ToolRetryMiddleware/wrap_tool_call)
- [`awrap_tool_call()`](https://reference.langchain.com/python/langchain/agents/middleware/tool_retry/ToolRetryMiddleware/awrap_tool_call)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a18de590e7ccf5c647fbf3d689e5f1a15f78e9f5/libs/langchain_v1/langchain/agents/middleware/tool_retry.py#L32)
