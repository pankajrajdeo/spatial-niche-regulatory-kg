---
title: "Command"
description: "Represents one or more commands to control graph execution flow and state."
source: "https://reference.langchain.com/python/langgraph-sdk/schema/Command"
category: "reference"
tags: [reference, langgraph-sdk, schema, command]
---

# Command

> **Class** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/schema/Command)

Represents one or more commands to control graph execution flow and state.

This type defines the control commands that can be returned by nodes to influence
graph execution. It lets you navigate to other nodes, update graph state,
and resume from interruptions.

## Signature

```python
Command()
```

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    goto: Send | str | Sequence[Send | str],
    update: dict[str, Any] | Sequence[tuple[str, Any]],
    resume: Any,
)
```

| Name | Type |
|------|------|
| `goto` | `Send \| str \| Sequence[Send \| str]` |
| `update` | `dict[str, Any] \| Sequence[tuple[str, Any]]` |
| `resume` | `Any` |

## Properties

- `goto`
- `update`
- `resume`

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/d5f4b2aa960940effc8430165ab3604038e817af/libs/sdk-py/langgraph_sdk/schema.py#L890)
