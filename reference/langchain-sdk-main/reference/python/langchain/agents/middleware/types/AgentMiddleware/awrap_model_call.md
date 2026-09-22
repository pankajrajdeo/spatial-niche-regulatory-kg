---
title: "awrap_model_call"
description: "Intercept and control async model execution via handler callback."
source: "https://reference.langchain.com/python/langchain/agents/middleware/types/AgentMiddleware/awrap_model_call"
category: "reference"
tags: [reference, langchain, agents, middleware, types, agentmiddleware, awrap_model_call]
---

# awrap_model_call

> **Method** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/types/AgentMiddleware/awrap_model_call)

Intercept and control async model execution via handler callback.

The handler callback executes the model request and returns a `ModelResponse`.

Middleware can call the handler multiple times for retry logic, skip calling
it to short-circuit, or modify the request/response. Multiple middleware
compose with first in list as outermost layer.

## Signature

```python
awrap_model_call(
    self,
    request: ModelRequest[ContextT],
    handler: Callable[[ModelRequest[ContextT]], Awaitable[ModelResponse[ResponseT]]],
) -> ModelResponse[ResponseT] | AIMessage | ExtendedModelResponse[ResponseT]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `request` | `ModelRequest[ContextT]` | Yes | Model request to execute (includes state and runtime). |
| `handler` | `Callable[[ModelRequest[ContextT]], Awaitable[ModelResponse[ResponseT]]]` | Yes | Async callback that executes the model request and returns `ModelResponse`.  Call this to execute the model.  Can be called multiple times for retry logic.  Can skip calling it to short-circuit. |

## Returns

`ModelResponse[ResponseT] | AIMessage | ExtendedModelResponse[ResponseT]`

The model call result.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a18de590e7ccf5c647fbf3d689e5f1a15f78e9f5/libs/langchain_v1/langchain/agents/middleware/types.py#L598)
