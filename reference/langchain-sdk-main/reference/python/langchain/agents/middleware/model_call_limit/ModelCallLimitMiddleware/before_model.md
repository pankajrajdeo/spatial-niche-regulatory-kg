---
title: "before_model"
description: "Check model call limits before making a model call."
source: "https://reference.langchain.com/python/langchain/agents/middleware/model_call_limit/ModelCallLimitMiddleware/before_model"
category: "reference"
tags: [reference, langchain, agents, middleware, model_call_limit, modelcalllimitmiddleware, before_model]
---

# before_model

> **Method** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/model_call_limit/ModelCallLimitMiddleware/before_model)

Check model call limits before making a model call.

## Signature

```python
before_model(
    self,
    state: ModelCallLimitState[ResponseT],
    runtime: Runtime[ContextT],
) -> dict[str, Any] | None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `state` | `ModelCallLimitState[ResponseT]` | Yes | The current agent state containing call counts. |
| `runtime` | `Runtime[ContextT]` | Yes | The langgraph runtime. |

## Returns

`dict[str, Any] | None`

If limits are exceeded and exit_behavior is `'end'`, returns
a `Command` to jump to the end with a limit exceeded message. Otherwise
returns `None`.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a18de590e7ccf5c647fbf3d689e5f1a15f78e9f5/libs/langchain_v1/langchain/agents/middleware/model_call_limit.py#L166)
