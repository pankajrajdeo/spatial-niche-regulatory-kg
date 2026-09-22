---
title: "TriggerClause"
description: "Dictionary-based trigger specification for AND conditions."
source: "https://reference.langchain.com/python/langchain/agents/middleware/summarization/TriggerClause"
category: "reference"
tags: [reference, langchain, agents, middleware, summarization, triggerclause]
---

# TriggerClause

> **Class** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/summarization/TriggerClause)

Dictionary-based trigger specification for AND conditions.

All specified thresholds in a single `TriggerClause` must be met for the clause to
trigger summarization (AND semantics). When multiple clauses are provided in a list,
summarization triggers if any clause is met (OR semantics).

## Signature

```python
TriggerClause()
```

## Description

**Example:**

```python
# AND: Trigger when tokens >= 4000 AND messages >= 10
trigger_clause: TriggerClause = {"tokens": 4000, "messages": 10}

# Use in a list for OR semantics:
trigger_list: list[TriggerClause] = [
    {"tokens": 5000, "messages": 3},
    {"tokens": 3000, "messages": 6},
]
```

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    tokens: int,
    messages: int,
    fraction: float,
)
```

| Name | Type |
|------|------|
| `tokens` | `int` |
| `messages` | `int` |
| `fraction` | `float` |

## Properties

- `tokens`
- `messages`
- `fraction`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a18de590e7ccf5c647fbf3d689e5f1a15f78e9f5/libs/langchain_v1/langchain/agents/middleware/summarization.py#L187)
