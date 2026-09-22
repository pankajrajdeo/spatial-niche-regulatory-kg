---
title: "TodoListMiddleware"
description: "Middleware that provides todo list management capabilities to agents."
source: "https://reference.langchain.com/python/langchain/agents/middleware/todo/TodoListMiddleware"
category: "reference"
tags: [reference, langchain, agents, middleware, todo, todolistmiddleware]
---

# TodoListMiddleware

> **Class** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/todo/TodoListMiddleware)

Middleware that provides todo list management capabilities to agents.

This middleware adds a `write_todos` tool that allows agents to create and manage
structured task lists for complex multi-step operations. It's designed to help
agents track progress, organize complex tasks, and provide users with visibility
into task completion status.

The middleware automatically injects system prompts that guide the agent on when
and how to use the todo functionality effectively. It also enforces that the
`write_todos` tool is called at most once per model turn, since the tool replaces
the entire todo list and parallel calls would create ambiguity about precedence.

## Signature

```python
TodoListMiddleware(
    self,
    *,
    system_prompt: str = WRITE_TODOS_SYSTEM_PROMPT,
    tool_description: str = WRITE_TODOS_TOOL_DESCRIPTION,
)
```

## Description

**Example:**

```python
from langchain.agents.middleware import TodoListMiddleware
from langchain.agents import create_agent

agent = create_agent("openai:gpt-5.5", middleware=[TodoListMiddleware()])

# Agent now has access to write_todos tool and todo state tracking
result = await agent.invoke({"messages": [HumanMessage("Help me refactor my codebase")]})

print(result["todos"])  # Array of todo items with status tracking
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `system_prompt` | `str` | No | Custom system prompt to guide the agent on using the todo tool. (default: `WRITE_TODOS_SYSTEM_PROMPT`) |
| `tool_description` | `str` | No | Custom description for the `write_todos` tool. (default: `WRITE_TODOS_TOOL_DESCRIPTION`) |

## Extends

- `AgentMiddleware[PlanningState[ResponseT], ContextT, ResponseT]`

## Constructors

```python
__init__(
    self,
    *,
    system_prompt: str = WRITE_TODOS_SYSTEM_PROMPT,
    tool_description: str = WRITE_TODOS_TOOL_DESCRIPTION,
) -> None
```

| Name | Type |
|------|------|
| `system_prompt` | `str` |
| `tool_description` | `str` |

## Properties

- `state_schema`
- `system_prompt`
- `tool_description`
- `tools`

## Methods

- [`wrap_model_call()`](https://reference.langchain.com/python/langchain/agents/middleware/todo/TodoListMiddleware/wrap_model_call)
- [`awrap_model_call()`](https://reference.langchain.com/python/langchain/agents/middleware/todo/TodoListMiddleware/awrap_model_call)
- [`after_model()`](https://reference.langchain.com/python/langchain/agents/middleware/todo/TodoListMiddleware/after_model)
- [`aafter_model()`](https://reference.langchain.com/python/langchain/agents/middleware/todo/TodoListMiddleware/aafter_model)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a18de590e7ccf5c647fbf3d689e5f1a15f78e9f5/libs/langchain_v1/langchain/agents/middleware/todo.py#L174)
