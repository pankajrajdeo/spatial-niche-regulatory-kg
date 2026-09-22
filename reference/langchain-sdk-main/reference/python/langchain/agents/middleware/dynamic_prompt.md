---
title: "dynamic_prompt"
description: "Decorator used to dynamically generate system prompts for the model."
source: "https://reference.langchain.com/python/langchain/agents/middleware/dynamic_prompt"
category: "reference"
tags: [reference, langchain, agents, middleware, dynamic_prompt]
---

# dynamic_prompt

> **Function** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/types/dynamic_prompt)

Decorator used to dynamically generate system prompts for the model.

This is a convenience decorator that creates middleware using `wrap_model_call`
specifically for dynamic prompt generation. The decorated function should return
a string that will be set as the system prompt for the model request.

## Signature

```python
dynamic_prompt(
    func: _CallableReturningSystemMessage[ContextT] | None = None,
) -> Callable[[_CallableReturningSystemMessage[ContextT]], AgentMiddleware[StateT, ContextT]] | AgentMiddleware[StateT, ContextT]
```

## Description

**The decorated function should return:**

- `str` – The system prompt string to use for the model request
- `SystemMessage` – A complete system message to use for the model request

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `func` | `_CallableReturningSystemMessage[ContextT] \| None` | No | The function to be decorated.  Must accept: `request: ModelRequest` - Model request (contains state and runtime) (default: `None`) |

## Returns

`Callable[[_CallableReturningSystemMessage[ContextT]], AgentMiddleware[StateT, ContextT]] | AgentMiddleware[StateT, ContextT]`

Either an `AgentMiddleware` instance (if func is provided) or a decorator
function that can be applied to a function.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a18de590e7ccf5c647fbf3d689e5f1a15f78e9f5/libs/langchain_v1/langchain/agents/middleware/types.py#L1704)
