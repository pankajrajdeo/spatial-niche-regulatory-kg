---
title: "ProviderToolSearchMiddleware"
description: "Defer selected tools behind provider-native tool search."
source: "https://reference.langchain.com/python/langchain/agents/middleware/provider_tool_search/ProviderToolSearchMiddleware"
category: "reference"
tags: [reference, langchain, agents, middleware, provider_tool_search, providertoolsearchmiddleware]
---

# ProviderToolSearchMiddleware

> **Class** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/provider_tool_search/ProviderToolSearchMiddleware)

Defer selected tools behind provider-native tool search.

Instead of sending every tool schema on every turn, this middleware marks
selected tools as deferred (via `extras["defer_loading"]`) and injects the
provider's server-side tool search tool. The provider then retrieves the
full schema of a deferred tool only when the model needs it, which keeps the
request payload small when many tools are bound.

A tool is deferred when its name (or instance) is passed in `searchable_tools`,
or when it already carries `extras["defer_loading"] is True`.

Only providers with server-side tool search are supported (currently
Anthropic and OpenAI). The provider is inferred from the bound model.

!!! warning

    This relies on provider-native tool search and only takes effect for
    supported providers. If a tool is deferred but the model's provider
    cannot be identified or does not support tool search, the model call
    raises `ValueError`. When no tool is deferred, the middleware passes the
    request through unchanged regardless of provider.

## Signature

```python
ProviderToolSearchMiddleware(
    self,
    *,
    searchable_tools: list[ToolIdentifier] | None = None,
)
```

## Description

**Example:**

```python
from langchain.agents import create_agent
from langchain.agents.middleware import ProviderToolSearchMiddleware

agent = create_agent(
    "anthropic:claude-opus-4-8",
    tools=[get_weather, send_email, lookup_order],
    middleware=[ProviderToolSearchMiddleware(searchable_tools=["lookup_order"])],
)
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `searchable_tools` | `list[ToolIdentifier] \| None` | No | Tools or tool names to defer behind provider-native tool search. (default: `None`) |

## Extends

- `AgentMiddleware[AgentState[ResponseT], ContextT, ResponseT]`

## Constructors

```python
__init__(
    self,
    *,
    searchable_tools: list[ToolIdentifier] | None = None,
) -> None
```

| Name | Type |
|------|------|
| `searchable_tools` | `list[ToolIdentifier] \| None` |

## Properties

- `searchable_tool_names`

## Methods

- [`wrap_model_call()`](https://reference.langchain.com/python/langchain/agents/middleware/provider_tool_search/ProviderToolSearchMiddleware/wrap_model_call)
- [`awrap_model_call()`](https://reference.langchain.com/python/langchain/agents/middleware/provider_tool_search/ProviderToolSearchMiddleware/awrap_model_call)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a18de590e7ccf5c647fbf3d689e5f1a15f78e9f5/libs/langchain_v1/langchain/agents/middleware/provider_tool_search.py#L57)
