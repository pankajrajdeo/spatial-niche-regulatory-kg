---
title: "abefore_model"
description: "Async logic to run before the model is called."
source: "https://reference.langchain.com/python/langchain/agents/middleware/types/AgentMiddleware/abefore_model"
category: "reference"
tags: [reference, langchain, agents, middleware, types, agentmiddleware, abefore_model]
---

# abefore_model

> **Method** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/types/AgentMiddleware/abefore_model)

Async logic to run before the model is called.

## Signature

```python
abefore_model(
    self,
    state: StateT,
    runtime: Runtime[ContextT],
) -> dict[str, Any] | None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `state` | `StateT` | Yes | The agent state. |
| `runtime` | `Runtime[ContextT]` | Yes | The runtime context. |

## Returns

`dict[str, Any] | None`

Agent state updates to apply before model call.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a18de590e7ccf5c647fbf3d689e5f1a15f78e9f5/libs/langchain_v1/langchain/agents/middleware/types.py#L466)
