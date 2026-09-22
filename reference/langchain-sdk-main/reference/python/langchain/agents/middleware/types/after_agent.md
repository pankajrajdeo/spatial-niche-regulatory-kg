---
title: "after_agent"
description: "Decorator used to dynamically create a middleware with the after_agent hook."
source: "https://reference.langchain.com/python/langchain/agents/middleware/types/after_agent"
category: "reference"
tags: [reference, langchain, agents, middleware, types, after_agent]
---

# after_agent

> **Function** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/types/after_agent)

Decorator used to dynamically create a middleware with the `after_agent` hook.

Async version is `aafter_agent`.

## Signature

```python
after_agent(
    func: _CallableWithStateAndRuntime[StateT, ContextT] | None = None,
    *,
    state_schema: type[StateT] | None = None,
    tools: list[BaseTool] | None = None,
    can_jump_to: list[JumpTo] | None = None,
    name: str | None = None,
) -> Callable[[_CallableWithStateAndRuntime[StateT, ContextT]], AgentMiddleware[StateT, ContextT]] | AgentMiddleware[StateT, ContextT]
```

## Description

The decorated function should return:

- `dict[str, Any]` - State updates to merge into the agent state
- `Command` - A command to control flow (e.g., jump to different node)
- `None` - No state updates or flow control

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `func` | `_CallableWithStateAndRuntime[StateT, ContextT] \| None` | No | The function to be decorated.  Must accept: `state: StateT, runtime: Runtime[ContextT]` - State and runtime context (default: `None`) |
| `state_schema` | `type[StateT] \| None` | No | Optional custom state schema type.  If not provided, uses the default `AgentState` schema. (default: `None`) |
| `tools` | `list[BaseTool] \| None` | No | Optional list of additional tools to register with this middleware. (default: `None`) |
| `can_jump_to` | `list[JumpTo] \| None` | No | Optional list of valid jump destinations for conditional edges.  Valid values are: `'tools'`, `'model'`, `'end'` (default: `None`) |
| `name` | `str \| None` | No | Optional name for the generated middleware class.  If not provided, uses the decorated function's name. (default: `None`) |

## Returns

`Callable[[_CallableWithStateAndRuntime[StateT, ContextT]], AgentMiddleware[StateT, ContextT]] | AgentMiddleware[StateT, ContextT]`

Either an `AgentMiddleware` instance (if func is provided) or a decorator
function that can be applied to a function.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a18de590e7ccf5c647fbf3d689e5f1a15f78e9f5/libs/langchain_v1/langchain/agents/middleware/types.py#L1530)
