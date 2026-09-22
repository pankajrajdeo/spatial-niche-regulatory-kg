---
title: "GraphDrained"
description: "Raised when a graph run exits early due to a drain request."
source: "https://reference.langchain.com/python/langgraph/errors/GraphDrained"
category: "reference"
tags: [reference, langgraph, errors, graphdrained]
---

# GraphDrained

> **Class** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/errors/GraphDrained)

Raised when a graph run exits early due to a drain request.

This indicates the graph stopped cooperatively at a superstep boundary
because `RunControl.request_drain()` was called (e.g., in response to
SIGTERM). The checkpoint is saved and the run can be resumed later.

## Signature

```python
GraphDrained(
    self,
    reason: str = 'shutdown',
)
```

## Extends

- `GraphBubbleUp`

## Constructors

```python
__init__(
    self,
    reason: str = 'shutdown',
) -> None
```

| Name | Type |
|------|------|
| `reason` | `str` |

## Properties

- `reason`

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/644815f9e5bc52ad8f7a5227a456227e9c3e639b/libs/langgraph/langgraph/errors.py#L54)
