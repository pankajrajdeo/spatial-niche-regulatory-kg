---
title: "after_model"
description: "Check AI messages for PII after model invocation."
source: "https://reference.langchain.com/python/langchain/agents/middleware/pii/PIIMiddleware/after_model"
category: "reference"
tags: [reference, langchain, agents, middleware, pii, piimiddleware, after_model]
---

# after_model

> **Method** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/pii/PIIMiddleware/after_model)

Check AI messages for PII after model invocation.

## Signature

```python
after_model(
    self,
    state: AgentState[Any],
    runtime: Runtime[ContextT],
) -> dict[str, Any] | None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `state` | `AgentState[Any]` | Yes | The current agent state. |
| `runtime` | `Runtime[ContextT]` | Yes | The langgraph runtime. |

## Returns

`dict[str, Any] | None`

Updated state with PII handled according to strategy, or None if no PII
detected.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a18de590e7ccf5c647fbf3d689e5f1a15f78e9f5/libs/langchain_v1/langchain/agents/middleware/pii.py#L799)
