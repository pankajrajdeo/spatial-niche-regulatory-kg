---
title: "AgentMiddleware"
description: "Base middleware class for an agent."
source: "https://reference.langchain.com/python/langchain/agents/middleware/types/AgentMiddleware"
category: "reference"
tags: [reference, langchain, agents, middleware, types, agentmiddleware]
---

# AgentMiddleware

> **Class** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/types/AgentMiddleware)

Base middleware class for an agent.

Subclass this and implement any of the defined methods to customize agent behavior
between steps in the main agent loop.

## Signature

```python
AgentMiddleware()
```

## Extends

- `Generic[StateT, ContextT, ResponseT]`

## Properties

- `state_schema`
- `tools`
- `trace_policy`
- `transformers`
- `name`

## Methods

- [`before_agent()`](https://reference.langchain.com/python/langchain/agents/middleware/types/AgentMiddleware/before_agent)
- [`abefore_agent()`](https://reference.langchain.com/python/langchain/agents/middleware/types/AgentMiddleware/abefore_agent)
- [`before_model()`](https://reference.langchain.com/python/langchain/agents/middleware/types/AgentMiddleware/before_model)
- [`abefore_model()`](https://reference.langchain.com/python/langchain/agents/middleware/types/AgentMiddleware/abefore_model)
- [`after_model()`](https://reference.langchain.com/python/langchain/agents/middleware/types/AgentMiddleware/after_model)
- [`aafter_model()`](https://reference.langchain.com/python/langchain/agents/middleware/types/AgentMiddleware/aafter_model)
- [`wrap_model_call()`](https://reference.langchain.com/python/langchain/agents/middleware/types/AgentMiddleware/wrap_model_call)
- [`awrap_model_call()`](https://reference.langchain.com/python/langchain/agents/middleware/types/AgentMiddleware/awrap_model_call)
- [`after_agent()`](https://reference.langchain.com/python/langchain/agents/middleware/types/AgentMiddleware/after_agent)
- [`aafter_agent()`](https://reference.langchain.com/python/langchain/agents/middleware/types/AgentMiddleware/aafter_agent)
- [`wrap_tool_call()`](https://reference.langchain.com/python/langchain/agents/middleware/types/AgentMiddleware/wrap_tool_call)
- [`awrap_tool_call()`](https://reference.langchain.com/python/langchain/agents/middleware/types/AgentMiddleware/awrap_tool_call)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a18de590e7ccf5c647fbf3d689e5f1a15f78e9f5/libs/langchain_v1/langchain/agents/middleware/types.py#L385)
