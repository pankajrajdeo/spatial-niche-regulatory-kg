---
title: "wrap_model_call"
description: "Try fallback models in sequence on errors."
source: "https://reference.langchain.com/python/langchain/agents/middleware/model_fallback/ModelFallbackMiddleware/wrap_model_call"
category: "reference"
tags: [reference, langchain, agents, middleware, model_fallback, modelfallbackmiddleware, wrap_model_call]
---

# wrap_model_call

> **Method** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/model_fallback/ModelFallbackMiddleware/wrap_model_call)

Try fallback models in sequence on errors.

## Signature

```python
wrap_model_call(
    self,
    request: ModelRequest[ContextT],
    handler: Callable[[ModelRequest[ContextT]], ModelResponse[ResponseT]],
) -> ModelResponse[ResponseT] | AIMessage
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `request` | `ModelRequest[ContextT]` | Yes | Initial model request. |
| `handler` | `Callable[[ModelRequest[ContextT]], ModelResponse[ResponseT]]` | Yes | Callback to execute the model. |

## Returns

`ModelResponse[ResponseT] | AIMessage`

AIMessage from successful model call.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a18de590e7ccf5c647fbf3d689e5f1a15f78e9f5/libs/langchain_v1/langchain/agents/middleware/model_fallback.py#L327)
