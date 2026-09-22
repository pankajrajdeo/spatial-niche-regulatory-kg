---
title: "AgentState"
description: "State schema for the agent."
source: "https://reference.langchain.com/python/langchain/agents/middleware/types/AgentState"
category: "reference"
tags: [reference, langchain, agents, middleware, types, agentstate]
---

# AgentState

> **Class** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/types/AgentState)

State schema for the agent.

## Signature

```python
AgentState()
```

## Extends

- `TypedDict`
- `Generic[ResponseT]`

## Constructors

```python
__init__(
    messages: Required[Annotated[list[AnyMessage], add_messages]],
    jump_to: NotRequired[Annotated[JumpTo | None, EphemeralValue, PrivateStateAttr]],
    structured_response: NotRequired[Annotated[ResponseT, OmitFromInput]],
)
```

| Name | Type |
|------|------|
| `messages` | `Required[Annotated[list[AnyMessage], add_messages]]` |
| `jump_to` | `NotRequired[Annotated[JumpTo \| None, EphemeralValue, PrivateStateAttr]]` |
| `structured_response` | `NotRequired[Annotated[ResponseT, OmitFromInput]]` |

## Properties

- `messages`
- `jump_to`
- `structured_response`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a18de590e7ccf5c647fbf3d689e5f1a15f78e9f5/libs/langchain_v1/langchain/agents/middleware/types.py#L349)
