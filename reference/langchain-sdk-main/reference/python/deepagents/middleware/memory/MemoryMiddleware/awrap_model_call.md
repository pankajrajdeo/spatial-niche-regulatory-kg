---
title: "awrap_model_call"
description: "Async wrap model call to inject memory into system prompt."
source: "https://reference.langchain.com/python/deepagents/middleware/memory/MemoryMiddleware/awrap_model_call"
category: "reference"
tags: [reference, deepagents, middleware, memory, memorymiddleware, awrap_model_call]
---

# awrap_model_call

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/memory/MemoryMiddleware/awrap_model_call)

Async wrap model call to inject memory into system prompt.

## Signature

```python
awrap_model_call(
    self,
    request: ModelRequest[ContextT],
    handler: Callable[[ModelRequest[ContextT]], Awaitable[ModelResponse[ResponseT]]],
) -> ModelResponse[ResponseT]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `request` | `ModelRequest[ContextT]` | Yes | Model request being processed. |
| `handler` | `Callable[[ModelRequest[ContextT]], Awaitable[ModelResponse[ResponseT]]]` | Yes | Async handler function to call with modified request. |

## Returns

`ModelResponse[ResponseT]`

Model response from handler.

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/middleware/memory.py#L402)
