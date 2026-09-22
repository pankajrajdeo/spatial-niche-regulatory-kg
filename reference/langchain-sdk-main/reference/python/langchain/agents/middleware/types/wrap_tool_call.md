---
title: "wrap_tool_call"
description: "Create middleware with wrap_tool_call hook from a function."
source: "https://reference.langchain.com/python/langchain/agents/middleware/types/wrap_tool_call"
category: "reference"
tags: [reference, langchain, agents, middleware, types, wrap_tool_call]
---

# wrap_tool_call

> **Function** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/types/wrap_tool_call)

Create middleware with `wrap_tool_call` hook from a function.

Async version is `awrap_tool_call`.

Converts a function with handler callback into middleware that can intercept
tool calls, implement retry logic, monitor execution, and modify responses.

## Signature

```python
wrap_tool_call(
    func: _CallableReturningToolResponse | None = None,
    *,
    state_schema: type[StateT] | None = None,
    tools: list[BaseTool] | None = None,
    name: str | None = None,
) -> Callable[[_CallableReturningToolResponse], AgentMiddleware[StateT, ContextT]] | AgentMiddleware[StateT, ContextT]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `func` | `_CallableReturningToolResponse \| None` | No | Function accepting (request, handler) that calls handler(request) to execute the tool and returns final `ToolMessage` or `Command`.  Can be sync or async. (default: `None`) |
| `state_schema` | `type[StateT] \| None` | No | Optional custom state schema type.  If not provided, uses the default `AgentState` schema. (default: `None`) |
| `tools` | `list[BaseTool] \| None` | No | Additional tools to register with this middleware. (default: `None`) |
| `name` | `str \| None` | No | Middleware class name.  Defaults to function name. (default: `None`) |

## Returns

`Callable[[_CallableReturningToolResponse], AgentMiddleware[StateT, ContextT]] | AgentMiddleware[StateT, ContextT]`

`AgentMiddleware` instance if func provided, otherwise a decorator.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a18de590e7ccf5c647fbf3d689e5f1a15f78e9f5/libs/langchain_v1/langchain/agents/middleware/types.py#L2037)
