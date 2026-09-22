---
title: "register_configure_hook"
description: "Register a configure hook."
source: "https://reference.langchain.com/python/langchain-core/tracers/context/register_configure_hook"
category: "reference"
tags: [reference, langchain-core, tracers, context, register_configure_hook]
---

# register_configure_hook

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/tracers/context/register_configure_hook)

Register a configure hook.

## Signature

```python
register_configure_hook(
    context_var: ContextVar[Any | None],
    inheritable: bool,
    handle_class: type[BaseCallbackHandler] | None = None,
    env_var: str | None = None,
) -> None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `context_var` | `ContextVar[Any \| None]` | Yes | The context variable. |
| `inheritable` | `bool` | Yes | Whether the context variable is inheritable. |
| `handle_class` | `type[BaseCallbackHandler] \| None` | No | The callback handler class. (default: `None`) |
| `env_var` | `str \| None` | No | The environment variable. (default: `None`) |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/tracers/context.py#L171)
