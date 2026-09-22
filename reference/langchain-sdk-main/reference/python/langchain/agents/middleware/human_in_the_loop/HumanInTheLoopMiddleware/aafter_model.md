---
title: "aafter_model"
description: "Async trigger interrupt flows for relevant tool calls after an AIMessage."
source: "https://reference.langchain.com/python/langchain/agents/middleware/human_in_the_loop/HumanInTheLoopMiddleware/aafter_model"
category: "reference"
tags: [reference, langchain, agents, middleware, human_in_the_loop, humanintheloopmiddleware, aafter_model]
---

# aafter_model

> **Method** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/human_in_the_loop/HumanInTheLoopMiddleware/aafter_model)

Async trigger interrupt flows for relevant tool calls after an `AIMessage`.

## Signature

```python
aafter_model(
    self,
    state: AgentState[Any],
    runtime: Runtime[ContextT],
) -> dict[str, Any] | None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `state` | `AgentState[Any]` | Yes | The current agent state. |
| `runtime` | `Runtime[ContextT]` | Yes | The runtime context. |

## Returns

`dict[str, Any] | None`

Updated message with the revised tool calls.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a18de590e7ccf5c647fbf3d689e5f1a15f78e9f5/libs/langchain_v1/langchain/agents/middleware/human_in_the_loop.py#L527)
