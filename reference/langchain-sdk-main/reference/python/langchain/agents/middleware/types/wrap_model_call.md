---
title: "wrap_model_call"
description: "Create middleware with wrap_model_call hook from a function."
source: "https://reference.langchain.com/python/langchain/agents/middleware/types/wrap_model_call"
category: "reference"
tags: [reference, langchain, agents, middleware, types, wrap_model_call]
---

# wrap_model_call

> **Function** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/types/wrap_model_call)

Create middleware with `wrap_model_call` hook from a function.

Converts a function with handler callback into middleware that can intercept model
calls, implement retry logic, handle errors, and rewrite responses.

## Signature

```python
wrap_model_call(
    func: _CallableReturningModelResponse[ContextT, ResponseT] | None = None,
    *,
    state_schema: type[StateT] | None = None,
    tools: list[BaseTool] | None = None,
    name: str | None = None,
) -> Callable[[_CallableReturningModelResponse[ContextT, ResponseT]], AgentMiddleware[StateT, ContextT]] | AgentMiddleware[StateT, ContextT]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `func` | `_CallableReturningModelResponse[ContextT, ResponseT] \| None` | No | Function accepting (request, handler) that calls handler(request) to execute the model and returns `ModelResponse` or `AIMessage`.  Request contains state and runtime. (default: `None`) |
| `state_schema` | `type[StateT] \| None` | No | Custom state schema.  Defaults to `AgentState`. (default: `None`) |
| `tools` | `list[BaseTool] \| None` | No | Additional tools to register with this middleware. (default: `None`) |
| `name` | `str \| None` | No | Middleware class name.  Defaults to function name. (default: `None`) |

## Returns

`Callable[[_CallableReturningModelResponse[ContextT, ResponseT]], AgentMiddleware[StateT, ContextT]] | AgentMiddleware[StateT, ContextT]`

`AgentMiddleware` instance if func provided, otherwise a decorator.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a18de590e7ccf5c647fbf3d689e5f1a15f78e9f5/libs/langchain_v1/langchain/agents/middleware/types.py#L1864)
