---
title: "ModelCallLimitMiddleware"
description: "Tracks model call counts and enforces limits."
source: "https://reference.langchain.com/python/langchain/agents/middleware/model_call_limit/ModelCallLimitMiddleware"
category: "reference"
tags: [reference, langchain, agents, middleware, model_call_limit, modelcalllimitmiddleware]
---

# ModelCallLimitMiddleware

> **Class** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/model_call_limit/ModelCallLimitMiddleware)

Tracks model call counts and enforces limits.

This middleware monitors the number of model calls made during agent execution
and can terminate the agent when specified limits are reached. It supports
both thread-level and run-level call counting with configurable exit behaviors.

Thread-level: The middleware tracks the number of model calls and persists
call count across multiple runs (invocations) of the agent.

Run-level: The middleware tracks the number of model calls made during a single
run (invocation) of the agent.

## Signature

```python
ModelCallLimitMiddleware(
    self,
    *,
    thread_limit: int | None = None,
    run_limit: int | None = None,
    exit_behavior: Literal['end', 'error'] = 'end',
)
```

## Description

**Example:**

```python
from langchain.agents.middleware import ModelCallLimitMiddleware
from langchain.agents import create_agent

# Create middleware with limits
call_tracker = ModelCallLimitMiddleware(thread_limit=10, run_limit=5, exit_behavior="end")

agent = create_agent("openai:gpt-5.5", middleware=[call_tracker])

# Agent will automatically jump to end when limits are exceeded
result = await agent.invoke({"messages": [HumanMessage("Help me with a task")]})
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `thread_limit` | `int \| None` | No | Maximum number of model calls allowed per thread.  `None` means no limit. (default: `None`) |
| `run_limit` | `int \| None` | No | Maximum number of model calls allowed per run.  `None` means no limit. (default: `None`) |
| `exit_behavior` | `Literal['end', 'error']` | No | What to do when limits are exceeded.  - `'end'`: Jump to the end of the agent execution and     inject an artificial AI message indicating that the limit was     exceeded. - `'error'`: Raise a `ModelCallLimitExceededError` (default: `'end'`) |

## Extends

- `AgentMiddleware[ModelCallLimitState[ResponseT], ContextT, ResponseT]`

## Constructors

```python
__init__(
    self,
    *,
    thread_limit: int | None = None,
    run_limit: int | None = None,
    exit_behavior: Literal['end', 'error'] = 'end',
) -> None
```

| Name | Type |
|------|------|
| `thread_limit` | `int \| None` |
| `run_limit` | `int \| None` |
| `exit_behavior` | `Literal['end', 'error']` |

## Properties

- `state_schema`
- `thread_limit`
- `run_limit`
- `exit_behavior`

## Methods

- [`before_model()`](https://reference.langchain.com/python/langchain/agents/middleware/model_call_limit/ModelCallLimitMiddleware/before_model)
- [`abefore_model()`](https://reference.langchain.com/python/langchain/agents/middleware/model_call_limit/ModelCallLimitMiddleware/abefore_model)
- [`after_model()`](https://reference.langchain.com/python/langchain/agents/middleware/model_call_limit/ModelCallLimitMiddleware/after_model)
- [`aafter_model()`](https://reference.langchain.com/python/langchain/agents/middleware/model_call_limit/ModelCallLimitMiddleware/aafter_model)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a18de590e7ccf5c647fbf3d689e5f1a15f78e9f5/libs/langchain_v1/langchain/agents/middleware/model_call_limit.py#L94)
