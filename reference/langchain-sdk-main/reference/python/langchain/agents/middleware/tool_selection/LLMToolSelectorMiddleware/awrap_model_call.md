---
title: "awrap_model_call"
description: "Filter tools based on LLM selection before invoking the model via handler."
source: "https://reference.langchain.com/python/langchain/agents/middleware/tool_selection/LLMToolSelectorMiddleware/awrap_model_call"
category: "reference"
tags: [reference, langchain, agents, middleware, tool_selection, llmtoolselectormiddleware, awrap_model_call]
---

# awrap_model_call

> **Method** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/tool_selection/LLMToolSelectorMiddleware/awrap_model_call)

Filter tools based on LLM selection before invoking the model via handler.

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

The model call result.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a18de590e7ccf5c647fbf3d689e5f1a15f78e9f5/libs/langchain_v1/langchain/agents/middleware/tool_selection.py#L450)
