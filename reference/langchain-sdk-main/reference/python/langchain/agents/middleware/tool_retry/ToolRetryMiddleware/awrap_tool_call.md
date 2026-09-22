---
title: "awrap_tool_call"
description: "Intercept and control async tool execution with retry logic."
source: "https://reference.langchain.com/python/langchain/agents/middleware/tool_retry/ToolRetryMiddleware/awrap_tool_call"
category: "reference"
tags: [reference, langchain, agents, middleware, tool_retry, toolretrymiddleware, awrap_tool_call]
---

# awrap_tool_call

> **Method** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/tool_retry/ToolRetryMiddleware/awrap_tool_call)

Intercept and control async tool execution with retry logic.

## Signature

```python
awrap_tool_call(
    self,
    request: ToolCallRequest,
    handler: Callable[[ToolCallRequest], Awaitable[ToolMessage | Command[Any]]],
) -> ToolMessage | Command[Any]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `request` | `ToolCallRequest` | Yes | Tool call request with call `dict`, `BaseTool`, state, and runtime. |
| `handler` | `Callable[[ToolCallRequest], Awaitable[ToolMessage \| Command[Any]]]` | Yes | Async callable to execute the tool and returns `ToolMessage` or `Command`. |

## Returns

`ToolMessage | Command[Any]`

`ToolMessage` or `Command` (the final result).

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a18de590e7ccf5c647fbf3d689e5f1a15f78e9f5/libs/langchain_v1/langchain/agents/middleware/tool_retry.py#L359)
