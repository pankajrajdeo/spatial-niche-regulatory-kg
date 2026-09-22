---
title: "awrap_model_call"
description: "Apply context edits before invoking the model via handler."
source: "https://reference.langchain.com/python/langchain/agents/middleware/context_editing/ContextEditingMiddleware/awrap_model_call"
category: "reference"
tags: [reference, langchain, agents, middleware, context_editing, contexteditingmiddleware, awrap_model_call]
---

# awrap_model_call

> **Method** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/context_editing/ContextEditingMiddleware/awrap_model_call)

Apply context edits before invoking the model via handler.

## Signature

```python
awrap_model_call(
    self,
    request: ModelRequest[ContextT],
    handler: Callable[[ModelRequest[ContextT]], Awaitable[ModelResponse[ResponseT]]],
) -> ModelResponse[ResponseT] | AIMessage
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `request` | `ModelRequest[ContextT]` | Yes | Model request to execute (includes state and runtime). |
| `handler` | `Callable[[ModelRequest[ContextT]], Awaitable[ModelResponse[ResponseT]]]` | Yes | Async callback that executes the model request and returns `ModelResponse`. |

## Returns

`ModelResponse[ResponseT] | AIMessage`

The result of invoking the handler with potentially edited messages.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a18de590e7ccf5c647fbf3d689e5f1a15f78e9f5/libs/langchain_v1/langchain/agents/middleware/context_editing.py#L276)
