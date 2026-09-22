---
title: "EditDecision"
description: "Response when a human edits the action."
source: "https://reference.langchain.com/python/langchain/agents/middleware/human_in_the_loop/EditDecision"
category: "reference"
tags: [reference, langchain, agents, middleware, human_in_the_loop, editdecision]
---

# EditDecision

> **Class** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/human_in_the_loop/EditDecision)

Response when a human edits the action.

## Signature

```python
EditDecision()
```

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    type: Literal['edit'],
    edited_action: Action,
)
```

| Name | Type |
|------|------|
| `type` | `Literal['edit']` |
| `edited_action` | `Action` |

## Properties

- `type`
- `edited_action`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a18de590e7ccf5c647fbf3d689e5f1a15f78e9f5/libs/langchain_v1/langchain/agents/middleware/human_in_the_loop.py#L98)
