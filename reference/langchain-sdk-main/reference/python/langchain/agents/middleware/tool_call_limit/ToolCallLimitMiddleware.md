---
title: "ToolCallLimitMiddleware"
description: "Track tool call counts and enforces limits during agent execution."
source: "https://reference.langchain.com/python/langchain/agents/middleware/tool_call_limit/ToolCallLimitMiddleware"
category: "reference"
tags: [reference, langchain, agents, middleware, tool_call_limit, toolcalllimitmiddleware]
---

# ToolCallLimitMiddleware

> **Class** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/tool_call_limit/ToolCallLimitMiddleware)

Track tool call counts and enforces limits during agent execution.

This middleware monitors the number of tool calls made and can terminate or
restrict execution when limits are exceeded. It supports both thread-level
(persistent across runs) and run-level (per invocation) call counting.

## Signature

```python
ToolCallLimitMiddleware(
    self,
    *,
    tool_name: str | None = None,
    thread_limit: int | None = None,
    run_limit: int | None = None,
    exit_behavior: ExitBehavior = 'continue',
)
```

## Description

**Configuration:**

- `exit_behavior`: How to handle when limits are exceeded
- `'continue'`: Block exceeded tools, let execution continue (default)
- `'error'`: Raise an exception
- `'end'`: Stop immediately with a `ToolMessage` for each exceeded tool
    call, a `ToolMessage` explaining any other pending calls were skipped,
    and an AI message explaining why execution stopped

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `tool_name` | `str \| None` | No | Name of the specific tool to limit. If `None`, limits apply to all tools. (default: `None`) |
| `thread_limit` | `int \| None` | No | Maximum number of tool calls allowed per thread. `None` means no limit. (default: `None`) |
| `run_limit` | `int \| None` | No | Maximum number of tool calls allowed per run. `None` means no limit. (default: `None`) |
| `exit_behavior` | `ExitBehavior` | No | How to handle when limits are exceeded.  - `'continue'`: Block exceeded tools with error messages, let other     tools continue. Model decides when to end. - `'error'`: Raise a `ToolCallLimitExceededError` exception - `'end'`: Stop execution immediately with a `ToolMessage` for each     tool call that exceeded the limit and an AI message explaining     why. Any other pending tool call on the same `AIMessage` (e.g.     from parallel tool calling) is given an explanatory     `ToolMessage` instead of being executed. (default: `'continue'`) |

## Extends

- `AgentMiddleware[ToolCallLimitState[ResponseT], ContextT, ResponseT]`

## Constructors

```python
__init__(
    self,
    *,
    tool_name: str | None = None,
    thread_limit: int | None = None,
    run_limit: int | None = None,
    exit_behavior: ExitBehavior = 'continue',
) -> None
```

| Name | Type |
|------|------|
| `tool_name` | `str \| None` |
| `thread_limit` | `int \| None` |
| `run_limit` | `int \| None` |
| `exit_behavior` | `ExitBehavior` |

## Properties

- `state_schema`
- `tool_name`
- `thread_limit`
- `run_limit`
- `exit_behavior`
- `name`

## Methods

- [`after_model()`](https://reference.langchain.com/python/langchain/agents/middleware/tool_call_limit/ToolCallLimitMiddleware/after_model)
- [`aafter_model()`](https://reference.langchain.com/python/langchain/agents/middleware/tool_call_limit/ToolCallLimitMiddleware/aafter_model)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a18de590e7ccf5c647fbf3d689e5f1a15f78e9f5/libs/langchain_v1/langchain/agents/middleware/tool_call_limit.py#L141)
