---
title: "awrap_model_call"
description: "Inject a compact-tool usage nudge into the system prompt (async)."
source: "https://reference.langchain.com/python/deepagents/middleware/summarization/SummarizationToolMiddleware/awrap_model_call"
category: "reference"
tags: [reference, deepagents, middleware, summarization, summarizationtoolmiddleware, awrap_model_call]
---

# awrap_model_call

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/summarization/SummarizationToolMiddleware/awrap_model_call)

Inject a compact-tool usage nudge into the system prompt (async).

This only updates prompt text so the model can decide whether to call
`compact_conversation` earlier in long sessions. It does not execute the
tool automatically.

## Signature

```python
awrap_model_call(
    self,
    request: ModelRequest,
    handler: Callable[[ModelRequest], Awaitable[ModelResponse]],
) -> ModelResponse
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `request` | `ModelRequest` | Yes | The model request to process. |
| `handler` | `Callable[[ModelRequest], Awaitable[ModelResponse]]` | Yes | The handler to call with the modified request. |

## Returns

`ModelResponse`

The model response from the handler.

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/middleware/summarization.py#L2267)
