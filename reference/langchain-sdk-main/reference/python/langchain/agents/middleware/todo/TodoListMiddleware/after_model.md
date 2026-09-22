---
title: "after_model"
description: "Check for parallel write_todos tool calls and return errors if detected."
source: "https://reference.langchain.com/python/langchain/agents/middleware/todo/TodoListMiddleware/after_model"
category: "reference"
tags: [reference, langchain, agents, middleware, todo, todolistmiddleware, after_model]
---

# after_model

> **Method** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/todo/TodoListMiddleware/after_model)

Check for parallel write_todos tool calls and return errors if detected.

The todo list is designed to be updated at most once per model turn. Since
the `write_todos` tool replaces the entire todo list with each call, making
multiple parallel calls would create ambiguity about which update should take
precedence. This method prevents such conflicts by rejecting any response that
contains multiple write_todos tool calls.

## Signature

```python
after_model(
    self,
    state: PlanningState[ResponseT],
    runtime: Runtime[ContextT],
) -> dict[str, Any] | None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `state` | `PlanningState[ResponseT]` | Yes | The current agent state containing messages. |
| `runtime` | `Runtime[ContextT]` | Yes | The LangGraph runtime instance. |

## Returns

`dict[str, Any] | None`

A dict containing error ToolMessages for each write_todos call if multiple

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a18de590e7ccf5c647fbf3d689e5f1a15f78e9f5/libs/langchain_v1/langchain/agents/middleware/todo.py#L285)
