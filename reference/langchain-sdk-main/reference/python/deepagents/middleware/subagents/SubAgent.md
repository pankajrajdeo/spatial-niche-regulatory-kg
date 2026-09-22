---
title: "SubAgent"
description: "Specification for a declarative subagent."
source: "https://reference.langchain.com/python/deepagents/middleware/subagents/SubAgent"
category: "reference"
tags: [reference, deepagents, middleware, subagents, subagent]
---

# SubAgent

> **Class** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/subagents/SubAgent)

Specification for a declarative subagent.

By default the subagent is isolated: it receives only the delegated task
description. Setting `mode="fork"` makes it continue the parent's
conversation instead.

!!! warning "Experimental"

    `mode="fork"` is experimental and may change in a future release.

When using `create_deep_agent`, subagents automatically receive
a default middleware stack before any custom `middleware` specified in
this spec.

## Signature

```python
SubAgent()
```

## Description

**Required fields:**

name: Unique identifier for the subagent.

    The main agent uses this name when calling the `task()` tool.
description: What this subagent does.

    Be specific and action-oriented. The main agent uses this
    to decide when to delegate.

Optional fields:
system_prompt: Instructions for the subagent.

    Appended to the inherited prompt under `mode="fork"`.
mode: `isolated` (default) for a subagent that only sees the
    delegated task, or `fork` to continue the parent's conversation.
tools: Tools the subagent can use.

    If not specified, inherits tools from the main agent
    via `default_tools`.
model: Override the main agent's model.

    Use the format `'provider:model-name'` (e.g., `'openai:gpt-5.5'`).
middleware: Additional middleware for custom behavior, logging,
    or rate limiting. To restrict filesystem tools, include a
    `FilesystemMiddleware(tools=...)` instance here — it
    will be used as the subagent's filesystem middleware instead of
    the default one.
interrupt_on: Configure human-in-the-loop for specific tools.

    Requires a checkpointer.
skills: Skill source paths for `SkillsMiddleware`.

    List of paths to skill directories
    (e.g., `["/skills/user/", "/skills/project/"]`).
permissions: Filesystem permission rules for this subagent.

    If omitted, inherits the parent agent's permissions. If provided,
    replaces the parent agent's rules entirely for this subagent.

    Rules are evaluated in declaration order; the first match wins.

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    name: str,
    description: str,
    tools: NotRequired[Sequence[BaseTool | Callable | dict[str, Any]]],
    model: NotRequired[str | BaseChatModel],
    middleware: NotRequired[list[AgentMiddleware]],
    interrupt_on: NotRequired[dict[str, bool | InterruptOnConfig]],
    skills: NotRequired[list[str]],
    permissions: NotRequired[list[FilesystemPermission]],
    response_format: NotRequired[ResponseFormat[Any] | type | dict[str, Any]],
    system_prompt: NotRequired[str],
    mode: NotRequired[Literal['isolated', 'fork']],
)
```

| Name | Type |
|------|------|
| `name` | `str` |
| `description` | `str` |
| `tools` | `NotRequired[Sequence[BaseTool \| Callable \| dict[str, Any]]]` |
| `model` | `NotRequired[str \| BaseChatModel]` |
| `middleware` | `NotRequired[list[AgentMiddleware]]` |
| `interrupt_on` | `NotRequired[dict[str, bool \| InterruptOnConfig]]` |
| `skills` | `NotRequired[list[str]]` |
| `permissions` | `NotRequired[list[FilesystemPermission]]` |
| `response_format` | `NotRequired[ResponseFormat[Any] \| type \| dict[str, Any]]` |
| `system_prompt` | `NotRequired[str]` |
| `mode` | `NotRequired[Literal['isolated', 'fork']]` |

## Properties

- `name`
- `description`
- `tools`
- `model`
- `middleware`
- `interrupt_on`
- `skills`
- `permissions`
- `response_format`
- `system_prompt`
- `mode`

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/middleware/subagents.py#L66)
