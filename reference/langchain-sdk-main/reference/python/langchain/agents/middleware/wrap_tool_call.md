---
title: "wrap_tool_call"
description: "Intercept tool execution for retries, monitoring, or modification."
source: "https://reference.langchain.com/python/langchain/agents/middleware/wrap_tool_call"
category: "reference"
tags: [reference, langchain, agents, middleware, wrap_tool_call]
---

# wrap_tool_call

> **Method** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/types/AgentMiddleware/wrap_tool_call)

Intercept tool execution for retries, monitoring, or modification.

Async version is `awrap_tool_call`

Multiple middleware compose automatically (first defined = outermost).

Exceptions propagate unless `handle_tool_errors` is configured on `ToolNode`.

## Signature

```python
wrap_tool_call(
    self,
    request: ToolCallRequest,
    handler: Callable[[ToolCallRequest], ToolMessage | Command[Any]],
) -> ToolMessage | Command[Any]
```

## Description

The handler `Callable` can be invoked multiple times for retry logic.

Each call to handler is independent and stateless.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `request` | `ToolCallRequest` | Yes | Tool call request with call `dict`, `BaseTool`, state, and runtime.  Access state via `request.state` and runtime via `request.runtime`. |
| `handler` | `Callable[[ToolCallRequest], ToolMessage \| Command[Any]]` | Yes | `Callable` to execute the tool (can be called multiple times). |

## Returns

`ToolMessage | Command[Any]`

`ToolMessage` or `Command` (the final result).

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a18de590e7ccf5c647fbf3d689e5f1a15f78e9f5/libs/langchain_v1/langchain/agents/middleware/types.py#L674)
