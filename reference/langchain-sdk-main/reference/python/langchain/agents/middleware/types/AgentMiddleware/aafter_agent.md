---
title: "aafter_agent"
description: "Async logic to run after the agent execution completes."
source: "https://reference.langchain.com/python/langchain/agents/middleware/types/AgentMiddleware/aafter_agent"
category: "reference"
tags: [reference, langchain, agents, middleware, types, agentmiddleware, aafter_agent]
---

# aafter_agent

> **Method** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/types/AgentMiddleware/aafter_agent)

Async logic to run after the agent execution completes.

## Signature

```python
aafter_agent(
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

Agent state updates to apply after agent execution.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a18de590e7ccf5c647fbf3d689e5f1a15f78e9f5/libs/langchain_v1/langchain/agents/middleware/types.py#L661)
