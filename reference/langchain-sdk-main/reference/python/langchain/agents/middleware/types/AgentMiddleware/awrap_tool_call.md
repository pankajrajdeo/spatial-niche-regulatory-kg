---
title: "awrap_tool_call"
description: "Intercept and control async tool execution via handler callback."
source: "https://reference.langchain.com/python/langchain/agents/middleware/types/AgentMiddleware/awrap_tool_call"
category: "reference"
tags: [reference, langchain, agents, middleware, types, agentmiddleware, awrap_tool_call]
---

# awrap_tool_call

> **Method** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/types/AgentMiddleware/awrap_tool_call)

Intercept and control async tool execution via handler callback.

The handler callback executes the tool call and returns a `ToolMessage` or
`Command`. Middleware can call the handler multiple times for retry logic, skip
calling it to short-circuit, or modify the request/response. Multiple middleware
compose with first in list as outermost layer.

## Signature

```python
awrap_tool_call(
    self,
    request: ToolCallRequest,
    handler: Callable[[ToolCallRequest], Awaitable[ToolMessage | Command[Any]]],
) -> ToolMessage | Command[Any]
```

## Description

The handler `Callable` can be invoked multiple times for retry logic.

Each call to handler is independent and stateless.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `request` | `ToolCallRequest` | Yes | Tool call request with call `dict`, `BaseTool`, state, and runtime.  Access state via `request.state` and runtime via `request.runtime`. |
| `handler` | `Callable[[ToolCallRequest], Awaitable[ToolMessage \| Command[Any]]]` | Yes | Async callable to execute the tool and returns `ToolMessage` or `Command`.  Call this to execute the tool.  Can be called multiple times for retry logic.  Can skip calling it to short-circuit. |

## Returns

`ToolMessage | Command[Any]`

`ToolMessage` or `Command` (the final result).

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a18de590e7ccf5c647fbf3d689e5f1a15f78e9f5/libs/langchain_v1/langchain/agents/middleware/types.py#L756)
