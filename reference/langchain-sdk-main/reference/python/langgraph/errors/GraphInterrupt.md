---
title: "GraphInterrupt"
description: "Raised when a subgraph is interrupted, suppressed by the root graph. Never raised directly, or surfaced to the user."
source: "https://reference.langchain.com/python/langgraph/errors/GraphInterrupt"
category: "reference"
tags: [reference, langgraph, errors, graphinterrupt]
---

# GraphInterrupt

> **Class** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/errors/GraphInterrupt)

Raised when a subgraph is interrupted, suppressed by the root graph.
Never raised directly, or surfaced to the user.

## Signature

```python
GraphInterrupt(
    self,
    interrupts: Sequence[Interrupt] = (),
)
```

## Extends

- `GraphBubbleUp`

## Constructors

```python
__init__(
    self,
    interrupts: Sequence[Interrupt] = (),
) -> None
```

| Name | Type |
|------|------|
| `interrupts` | `Sequence[Interrupt]` |

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/644815f9e5bc52ad8f7a5227a456227e9c3e639b/libs/langgraph/langgraph/errors.py#L102)
