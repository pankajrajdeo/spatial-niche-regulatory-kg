---
title: "InterruptOnConfig"
description: "Configuration for an action requiring human in the loop."
source: "https://reference.langchain.com/python/langchain/agents/middleware/human_in_the_loop/InterruptOnConfig"
category: "reference"
tags: [reference, langchain, agents, middleware, human_in_the_loop, interruptonconfig]
---

# InterruptOnConfig

> **Class** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/human_in_the_loop/InterruptOnConfig)

Configuration for an action requiring human in the loop.

This is the configuration format used in the `HumanInTheLoopMiddleware.__init__`
method.

## Signature

```python
InterruptOnConfig()
```

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    allowed_decisions: list[DecisionType],
    description: NotRequired[str | _DescriptionFactory],
    args_schema: NotRequired[dict[str, Any]],
    when: NotRequired[Callable[[ToolCallRequest], bool]],
)
```

| Name | Type |
|------|------|
| `allowed_decisions` | `list[DecisionType]` |
| `description` | `NotRequired[str \| _DescriptionFactory]` |
| `args_schema` | `NotRequired[dict[str, Any]]` |
| `when` | `NotRequired[Callable[[ToolCallRequest], bool]]` |

## Properties

- `allowed_decisions`
- `description`
- `args_schema`
- `when`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a18de590e7ccf5c647fbf3d689e5f1a15f78e9f5/libs/langchain_v1/langchain/agents/middleware/human_in_the_loop.py#L161)
