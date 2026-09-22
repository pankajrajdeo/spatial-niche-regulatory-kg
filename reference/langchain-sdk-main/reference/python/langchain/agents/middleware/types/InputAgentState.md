---
title: "InputAgentState"
description: "Input state schema for the agent."
source: "https://reference.langchain.com/python/langchain/agents/middleware/types/InputAgentState"
category: "reference"
tags: [reference, langchain, agents, middleware, types, inputagentstate]
---

# InputAgentState

> **Class** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/types/InputAgentState)

Input state schema for the agent.

## Signature

```python
InputAgentState()
```

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    messages: Required[Annotated[list[AnyMessage | dict[str, Any]], add_messages]],
)
```

| Name | Type |
|------|------|
| `messages` | `Required[Annotated[list[AnyMessage \| dict[str, Any]], add_messages]]` |

## Properties

- `messages`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a18de590e7ccf5c647fbf3d689e5f1a15f78e9f5/libs/langchain_v1/langchain/agents/middleware/types.py#L357)
