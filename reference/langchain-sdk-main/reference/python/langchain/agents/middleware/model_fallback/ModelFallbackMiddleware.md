---
title: "ModelFallbackMiddleware"
description: "Automatic fallback to alternative models on errors."
source: "https://reference.langchain.com/python/langchain/agents/middleware/model_fallback/ModelFallbackMiddleware"
category: "reference"
tags: [reference, langchain, agents, middleware, model_fallback, modelfallbackmiddleware]
---

# ModelFallbackMiddleware

> **Class** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/model_fallback/ModelFallbackMiddleware)

Automatic fallback to alternative models on errors.

Retries failed model calls with alternative models in sequence until
success or all models exhausted. Primary model specified in `create_agent`.

## Signature

```python
ModelFallbackMiddleware(
    self,
    first_model: str | BaseChatModel,
    *additional_models: str | BaseChatModel = (),
)
```

## Description

**Example:**

```python
from langchain.agents.middleware import ModelFallbackMiddleware
from langchain.agents import create_agent

fallback = ModelFallbackMiddleware(
    "openai:gpt-5.5",  # Try first on error
    "anthropic:claude-sonnet-4-5-20250929",  # Then this
)

agent = create_agent(
    model="openai:gpt-5.5",  # Primary model
    middleware=[fallback],
)

# If primary fails: tries gpt-5.5, then claude-sonnet-4-5-20250929
result = await agent.invoke({"messages": [HumanMessage("Hello")]})
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `first_model` | `str \| BaseChatModel` | Yes | First fallback model (string name or instance). |
| `*additional_models` | `str \| BaseChatModel` | No | Additional fallbacks in order. (default: `()`) |

## Extends

- `AgentMiddleware[AgentState[ResponseT], ContextT, ResponseT]`

## Constructors

```python
__init__(
    self,
    first_model: str | BaseChatModel,
    *additional_models: str | BaseChatModel = (),
) -> None
```

| Name | Type |
|------|------|
| `first_model` | `str \| BaseChatModel` |

## Properties

- `models`

## Methods

- [`wrap_model_call()`](https://reference.langchain.com/python/langchain/agents/middleware/model_fallback/ModelFallbackMiddleware/wrap_model_call)
- [`awrap_model_call()`](https://reference.langchain.com/python/langchain/agents/middleware/model_fallback/ModelFallbackMiddleware/awrap_model_call)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a18de590e7ccf5c647fbf3d689e5f1a15f78e9f5/libs/langchain_v1/langchain/agents/middleware/model_fallback.py#L279)
