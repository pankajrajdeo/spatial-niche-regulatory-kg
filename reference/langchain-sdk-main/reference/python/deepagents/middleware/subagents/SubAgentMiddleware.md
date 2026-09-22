---
title: "SubAgentMiddleware"
description: "Middleware for providing subagents to an agent via a task tool."
source: "https://reference.langchain.com/python/deepagents/middleware/subagents/SubAgentMiddleware"
category: "reference"
tags: [reference, deepagents, middleware, subagents, subagentmiddleware]
---

# SubAgentMiddleware

> **Class** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/subagents/SubAgentMiddleware)

Middleware for providing subagents to an agent via a `task` tool.

This middleware adds a `task` tool to the agent that can be used
to invoke subagents.

Subagents are useful for handling complex tasks that require multiple steps,
or tasks that require a lot of context to resolve.

A chief benefit of subagents is that they can handle multi-step tasks,
and then return a clean, concise response to the main agent.

Subagents are also great for different domains of expertise that require
a narrower subset of tools and focus.

## Signature

```python
SubAgentMiddleware(
    self,
    *,
    backend: BackendProtocol,
    subagents: Sequence[SubAgent | CompiledSubAgent],
    system_prompt: str | None = None,
    task_description: str | None = None,
    private_state_keys: frozenset[str] | None = None,
    state_schema: type | None = None,
)
```

## Description

**Example:**

```python
from deepagents.middleware import SubAgentMiddleware
from langchain.agents import create_agent

agent = create_agent(
    "openai:gpt-5.5",
    middleware=[
        SubAgentMiddleware(
            backend=my_backend,
            subagents=[
                {
                    "name": "researcher",
                    "description": "Research agent",
                    "system_prompt": "You are a researcher.",
                    "model": "openai:gpt-5.5",
                    "tools": [search_tool],
                }
            ],
        )
    ],
)
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `backend` | `BackendProtocol` | Yes | Backend for file operations and execution. |
| `subagents` | `Sequence[SubAgent \| CompiledSubAgent]` | Yes | List of fully-specified subagent configs.  Each SubAgent must specify `model` and `tools`.  Optional `interrupt_on` on individual subagents is respected. |
| `system_prompt` | `str \| None` | No | Instructions appended to main agent's system prompt about how to use the task tool. (default: `None`) |
| `task_description` | `str \| None` | No | Custom description for the task tool. (default: `None`) |
| `state_schema` | `type \| None` | No | Base graph state schema forwarded to raw `SubAgent` specs when their runnables are compiled.  Leave unset to use `create_agent`'s default. `CompiledSubAgent` entries are unaffected — callers own those runnables' schemas. (default: `None`) |

## Extends

- `AgentMiddleware[Any, ContextT, ResponseT]`

## Constructors

```python
__init__(
    self,
    *,
    backend: BackendProtocol,
    subagents: Sequence[SubAgent | CompiledSubAgent],
    system_prompt: str | None = None,
    task_description: str | None = None,
    private_state_keys: frozenset[str] | None = None,
    state_schema: type | None = None,
) -> None
```

| Name | Type |
|------|------|
| `backend` | `BackendProtocol` |
| `subagents` | `Sequence[SubAgent \| CompiledSubAgent]` |
| `system_prompt` | `str \| None` |
| `task_description` | `str \| None` |
| `private_state_keys` | `frozenset[str] \| None` |
| `state_schema` | `type \| None` |

## Properties

- `trace_policy`
- `subagent_names`
- `system_prompt`
- `tools`
- `private_state_keys`

## Methods

- [`wrap_model_call()`](https://reference.langchain.com/python/deepagents/middleware/subagents/SubAgentMiddleware/wrap_model_call)
- [`awrap_model_call()`](https://reference.langchain.com/python/deepagents/middleware/subagents/SubAgentMiddleware/awrap_model_call)

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/middleware/subagents.py#L842)
