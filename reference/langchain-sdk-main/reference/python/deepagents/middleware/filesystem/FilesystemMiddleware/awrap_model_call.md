---
title: "awrap_model_call"
description: "(async) Update the system prompt and filter tools based on backend capabilities."
source: "https://reference.langchain.com/python/deepagents/middleware/filesystem/FilesystemMiddleware/awrap_model_call"
category: "reference"
tags: [reference, deepagents, middleware, filesystem, filesystemmiddleware, awrap_model_call]
---

# awrap_model_call

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/filesystem/FilesystemMiddleware/awrap_model_call)

(async) Update the system prompt and filter tools based on backend capabilities.

Also evicts oversized HumanMessages to the filesystem. See
`wrap_model_call` for full documentation.

## Signature

```python
awrap_model_call(
    self,
    request: ModelRequest[ContextT],
    handler: Callable[[ModelRequest[ContextT]], Awaitable[ModelResponse[ResponseT]]],
) -> ModelResponse[ResponseT] | ExtendedModelResponse
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `request` | `ModelRequest[ContextT]` | Yes | The model request being processed. |
| `handler` | `Callable[[ModelRequest[ContextT]], Awaitable[ModelResponse[ResponseT]]]` | Yes | The handler function to call with the modified request. |

## Returns

`ModelResponse[ResponseT] | ExtendedModelResponse`

The model response from the handler, or an `ExtendedModelResponse`
with a state update tagging newly evicted messages.

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/middleware/filesystem.py#L3246)
