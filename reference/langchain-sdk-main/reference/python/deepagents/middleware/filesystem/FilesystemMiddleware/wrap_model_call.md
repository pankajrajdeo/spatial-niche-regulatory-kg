---
title: "wrap_model_call"
description: "Update the system prompt, filter tools, and evict oversized HumanMessages."
source: "https://reference.langchain.com/python/deepagents/middleware/filesystem/FilesystemMiddleware/wrap_model_call"
category: "reference"
tags: [reference, deepagents, middleware, filesystem, filesystemmiddleware, wrap_model_call]
---

# wrap_model_call

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/filesystem/FilesystemMiddleware/wrap_model_call)

Update the system prompt, filter tools, and evict oversized HumanMessages.

In addition to the system-prompt and tool-filtering logic, this method
handles large HumanMessage eviction:

1. Any message already tagged with `lc_evicted_to` in
    `additional_kwargs` is replaced with a truncated preview for the
    model request (content in state is unchanged).
2. If the most recent message is an untagged HumanMessage exceeding the
    eviction threshold, its content is written to the backend and the
    message is tagged in state via `ExtendedModelResponse`.

It also scrubs unsupported multimodal blocks, replacing them with text
placeholders to avoid non-retryable provider errors.

## Signature

```python
wrap_model_call(
    self,
    request: ModelRequest[ContextT],
    handler: Callable[[ModelRequest[ContextT]], ModelResponse[ResponseT]],
) -> ModelResponse[ResponseT] | ExtendedModelResponse
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `request` | `ModelRequest[ContextT]` | Yes | The model request being processed. |
| `handler` | `Callable[[ModelRequest[ContextT]], ModelResponse[ResponseT]]` | Yes | The handler function to call with the modified request. |

## Returns

`ModelResponse[ResponseT] | ExtendedModelResponse`

The model response, or an `ExtendedModelResponse` with a state
update tagging a newly evicted message.

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/middleware/filesystem.py#L3200)
