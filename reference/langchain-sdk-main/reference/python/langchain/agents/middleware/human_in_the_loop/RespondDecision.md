---
title: "RespondDecision"
description: "Response when a human answers on behalf of the tool, skipping execution."
source: "https://reference.langchain.com/python/langchain/agents/middleware/human_in_the_loop/RespondDecision"
category: "reference"
tags: [reference, langchain, agents, middleware, human_in_the_loop, responddecision]
---

# RespondDecision

> **Class** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/human_in_the_loop/RespondDecision)

Response when a human answers on behalf of the tool, skipping execution.

Used for "ask user" style tools whose real implementation is the human's
response. The tool is not executed; instead, a synthetic `ToolMessage` with
`status="success"` and the provided `message` is returned to the model.

## Signature

```python
RespondDecision()
```

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    type: Literal['respond'],
    message: str,
)
```

| Name | Type |
|------|------|
| `type` | `Literal['respond']` |
| `message` | `str` |

## Properties

- `type`
- `message`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a18de590e7ccf5c647fbf3d689e5f1a15f78e9f5/libs/langchain_v1/langchain/agents/middleware/human_in_the_loop.py#L126)
