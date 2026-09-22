---
title: "before_agent"
description: "Detect a new grading run and reset iteration bookkeeping."
source: "https://reference.langchain.com/python/deepagents/middleware/rubric/RubricMiddleware/before_agent"
category: "reference"
tags: [reference, deepagents, middleware, rubric, rubricmiddleware, before_agent]
---

# before_agent

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/rubric/RubricMiddleware/before_agent)

Detect a new grading run and reset iteration bookkeeping.

A "new grading run" is either a different `rubric` string than
`_active_rubric`, or the same `rubric` after the previous run
reached a terminal status (`satisfied`, `max_iterations_reached`,
or `failed`). In that case we mint a fresh `_current_grading_run_id`,
reset `_rubric_iterations` to 0, and clear `_rubric_status` so a
new run starts fresh.

If `rubric` is unset the middleware is a no-op for this run.

## Signature

```python
before_agent(
    self,
    state: RubricState,
    runtime: Runtime[ContextT],
) -> dict[str, Any] | None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `state` | `RubricState` | Yes | Agent state. |
| `runtime` | `Runtime[ContextT]` | Yes | Agent runtime (unused). |

## Returns

`dict[str, Any] | None`

State update dict or None if no change.

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/middleware/rubric.py#L606)
