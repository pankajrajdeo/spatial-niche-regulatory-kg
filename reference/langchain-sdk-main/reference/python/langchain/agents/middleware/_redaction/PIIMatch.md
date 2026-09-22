---
title: "PIIMatch"
description: "Represents an individual match of sensitive data."
source: "https://reference.langchain.com/python/langchain/agents/middleware/_redaction/PIIMatch"
category: "reference"
tags: [reference, langchain, agents, middleware, redaction, piimatch]
---

# PIIMatch

> **Class** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/_redaction/PIIMatch)

Represents an individual match of sensitive data.

## Signature

```python
PIIMatch()
```

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    type: str,
    value: str,
    start: int,
    end: int,
)
```

| Name | Type |
|------|------|
| `type` | `str` |
| `value` | `str` |
| `start` | `int` |
| `end` | `int` |

## Properties

- `type`
- `value`
- `start`
- `end`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a18de590e7ccf5c647fbf3d689e5f1a15f78e9f5/libs/langchain_v1/langchain/agents/middleware/_redaction.py#L20)
