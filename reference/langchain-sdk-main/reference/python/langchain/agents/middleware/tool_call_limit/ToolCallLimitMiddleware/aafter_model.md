---
title: "aafter_model"
description: "Async increment tool call counts after a model call and check limits."
source: "https://reference.langchain.com/python/langchain/agents/middleware/tool_call_limit/ToolCallLimitMiddleware/aafter_model"
category: "reference"
tags: [reference, langchain, agents, middleware, tool_call_limit, toolcalllimitmiddleware, aafter_model]
---

# aafter_model

> **Method** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/tool_call_limit/ToolCallLimitMiddleware/aafter_model)

Async increment tool call counts after a model call and check limits.

## Signature

```python
aafter_model(
    self,
    state: ToolCallLimitState[ResponseT],
    runtime: Runtime[ContextT],
) -> dict[str, Any] | None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `state` | `ToolCallLimitState[ResponseT]` | Yes | The current agent state. |
| `runtime` | `Runtime[ContextT]` | Yes | The langgraph runtime. |

## Returns

`dict[str, Any] | None`

State updates with incremented tool call counts. If limits are exceeded
and exit_behavior is `'end'`, also includes a jump to end with a
`ToolMessage` for each exceeded tool call, an explanatory
`ToolMessage` for any other pending tool calls, and an AI message.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a18de590e7ccf5c647fbf3d689e5f1a15f78e9f5/libs/langchain_v1/langchain/agents/middleware/tool_call_limit.py#L473)
