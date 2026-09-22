---
title: "abefore_agent"
description: "Async logic to run before the agent execution starts."
source: "https://reference.langchain.com/python/langchain/agents/middleware/types/AgentMiddleware/abefore_agent"
category: "reference"
tags: [reference, langchain, agents, middleware, types, agentmiddleware, abefore_agent]
---

# abefore_agent

> **Method** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/types/AgentMiddleware/abefore_agent)

Async logic to run before the agent execution starts.

## Signature

```python
abefore_agent(
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

Agent state updates to apply before agent execution.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a18de590e7ccf5c647fbf3d689e5f1a15f78e9f5/libs/langchain_v1/langchain/agents/middleware/types.py#L442)
