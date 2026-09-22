---
title: "after_agent"
description: "Grade the transcript and decide whether to loop back to the model."
source: "https://reference.langchain.com/python/deepagents/middleware/rubric/RubricMiddleware/after_agent"
category: "reference"
tags: [reference, deepagents, middleware, rubric, rubricmiddleware, after_agent]
---

# after_agent

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/rubric/RubricMiddleware/after_agent)

Grade the transcript and decide whether to loop back to the model.

## Signature

```python
after_agent(
    self,
    state: RubricState,
    runtime: Runtime[ContextT],
) -> dict[str, Any] | None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `state` | `RubricState` | Yes | Agent state at natural stop (no further tool calls). |
| `runtime` | `Runtime[ContextT]` | Yes | Agent runtime; used for streaming and to forward its static context to the nested grader. |

## Returns

`dict[str, Any] | None`

State update dict. May include `jump_to='model'` (with an

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/middleware/rubric.py#L657)
