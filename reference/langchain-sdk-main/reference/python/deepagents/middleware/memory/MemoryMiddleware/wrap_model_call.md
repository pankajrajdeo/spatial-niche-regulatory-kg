---
title: "wrap_model_call"
description: "Wrap model call to inject memory into system prompt."
source: "https://reference.langchain.com/python/deepagents/middleware/memory/MemoryMiddleware/wrap_model_call"
category: "reference"
tags: [reference, deepagents, middleware, memory, memorymiddleware, wrap_model_call]
---

# wrap_model_call

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/memory/MemoryMiddleware/wrap_model_call)

Wrap model call to inject memory into system prompt.

## Signature

```python
wrap_model_call(
    self,
    request: ModelRequest[ContextT],
    handler: Callable[[ModelRequest[ContextT]], ModelResponse[ResponseT]],
) -> ModelResponse[ResponseT]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `request` | `ModelRequest[ContextT]` | Yes | Model request being processed. |
| `handler` | `Callable[[ModelRequest[ContextT]], ModelResponse[ResponseT]]` | Yes | Handler function to call with modified request. |

## Returns

`ModelResponse[ResponseT]`

Model response from handler.

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/middleware/memory.py#L385)
