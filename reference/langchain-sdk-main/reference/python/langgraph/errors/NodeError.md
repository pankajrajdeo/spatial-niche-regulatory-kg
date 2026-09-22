---
title: "NodeError"
description: "Failure context passed to a node-level error handler."
source: "https://reference.langchain.com/python/langgraph/errors/NodeError"
category: "reference"
tags: [reference, langgraph, errors, nodeerror]
---

# NodeError

> **Class** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/errors/NodeError)

Failure context passed to a node-level error handler.

Inject by adding a parameter typed `NodeError` to a handler registered via
`StateGraph.add_node(..., error_handler=...)`:

```python
def handler(state: State, error: NodeError) -> Command:
    return Command(update={"status": f"recovered from {error.node}: {error.error}"})
```

## Signature

```python
NodeError(
    self,
    node: str,
    error: BaseException,
)
```

## Constructors

```python
__init__(
    self,
    node: str,
    error: BaseException,
) -> None
```

| Name | Type |
|------|------|
| `node` | `str` |
| `error` | `BaseException` |

## Properties

- `node`
- `error`

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/644815f9e5bc52ad8f7a5227a456227e9c3e639b/libs/langgraph/langgraph/errors.py#L148)
