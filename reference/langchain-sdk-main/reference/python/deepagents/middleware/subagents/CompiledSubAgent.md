---
title: "CompiledSubAgent"
description: "A pre-compiled agent spec."
source: "https://reference.langchain.com/python/deepagents/middleware/subagents/CompiledSubAgent"
category: "reference"
tags: [reference, deepagents, middleware, subagents, compiledsubagent]
---

# CompiledSubAgent

> **Class** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/subagents/CompiledSubAgent)

A pre-compiled agent spec.

!!! note

    The `runnable`'s state schema must include a 'messages' key.

    This is required for the subagent to communicate results back to
    the main agent.

!!! note

    `CompiledSubAgent` runnables are used as provided. They do not
    inherit `create_deep_agent(state_schema=...)`; if the runnable
    needs custom state fields, compile it with a compatible state
    schema yourself.

When the subagent completes, the parent reads the returned state:
if `structured_response` is non-`None`, it is JSON-serialized and used as
the `ToolMessage` content; otherwise, the last non-empty `AIMessage`
text is used.

## Signature

```python
CompiledSubAgent()
```

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    name: str,
    description: str,
    runnable: Runnable,
    mode: NotRequired[Literal['isolated', 'fork']],
)
```

| Name | Type |
|------|------|
| `name` | `str` |
| `description` | `str` |
| `runnable` | `Runnable` |
| `mode` | `NotRequired[Literal['isolated', 'fork']]` |

## Properties

- `name`
- `description`
- `runnable`
- `mode`

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/middleware/subagents.py#L220)
