---
title: "ActionRequest"
description: "Represents an action request with a name, args, and description."
source: "https://reference.langchain.com/python/langchain/agents/middleware/human_in_the_loop/ActionRequest"
category: "reference"
tags: [reference, langchain, agents, middleware, human_in_the_loop, actionrequest]
---

# ActionRequest

> **Class** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/human_in_the_loop/ActionRequest)

Represents an action request with a name, args, and description.

## Signature

```python
ActionRequest()
```

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    name: str,
    args: dict[str, Any],
    description: NotRequired[str],
)
```

| Name | Type |
|------|------|
| `name` | `str` |
| `args` | `dict[str, Any]` |
| `description` | `NotRequired[str]` |

## Properties

- `name`
- `args`
- `description`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a18de590e7ccf5c647fbf3d689e5f1a15f78e9f5/libs/langchain_v1/langchain/agents/middleware/human_in_the_loop.py#L52)
