---
title: "aafter_model"
description: "Async logic to run after the model is called."
source: "https://reference.langchain.com/python/langchain/agents/middleware/types/AgentMiddleware/aafter_model"
category: "reference"
tags: [reference, langchain, agents, middleware, types, agentmiddleware, aafter_model]
---

# aafter_model

> **Method** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/types/AgentMiddleware/aafter_model)

Async logic to run after the model is called.

## Signature

```python
aafter_model(
    self,
    state: StateT,
    runtime: Runtime[ContextT],
) -> dict[str, Any] | None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `state` | `StateT` | Yes | The current agent state. |
| `runtime` | `Runtime[ContextT]` | Yes | The runtime context. |

## Returns

`dict[str, Any] | None`

Agent state updates to apply after model call.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a18de590e7ccf5c647fbf3d689e5f1a15f78e9f5/libs/langchain_v1/langchain/agents/middleware/types.py#L490)
