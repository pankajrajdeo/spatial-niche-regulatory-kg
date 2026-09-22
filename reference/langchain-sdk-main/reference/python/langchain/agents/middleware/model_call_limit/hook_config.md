---
title: "hook_config"
description: "Decorator to configure hook behavior in middleware methods."
source: "https://reference.langchain.com/python/langchain/agents/middleware/model_call_limit/hook_config"
category: "reference"
tags: [reference, langchain, agents, middleware, model_call_limit, hook_config]
---

# hook_config

> **Function** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/types/hook_config)

Decorator to configure hook behavior in middleware methods.

Use this decorator on `before_model` or `after_model` methods in middleware classes
to configure their behavior. Currently supports specifying which destinations they
can jump to, which establishes conditional edges in the agent graph.

## Signature

```python
hook_config(
    *,
    can_jump_to: list[JumpTo] | None = None,
) -> Callable[[CallableT], CallableT]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `can_jump_to` | `list[JumpTo] \| None` | No | Optional list of valid jump destinations.  Can be:  - `'tools'`: Jump to the tools node - `'model'`: Jump back to the model node - `'end'`: Jump to the end of the graph (default: `None`) |

## Returns

`Callable[[CallableT], CallableT]`

Decorator function that marks the method with configuration metadata.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a18de590e7ccf5c647fbf3d689e5f1a15f78e9f5/libs/langchain_v1/langchain/agents/middleware/types.py#L879)
