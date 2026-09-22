---
title: "coro_with_context"
description: "Await a coroutine with a context."
source: "https://reference.langchain.com/python/langchain-core/runnables/utils/coro_with_context"
category: "reference"
tags: [reference, langchain-core, runnables, utils, coro_with_context]
---

# coro_with_context

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/utils/coro_with_context)

Await a coroutine with a context.

## Signature

```python
coro_with_context(
    coro: Awaitable[_T],
    context: Context,
    *,
    create_task: bool = False,
) -> Awaitable[_T]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `coro` | `Awaitable[_T]` | Yes | The coroutine to await. |
| `context` | `Context` | Yes | The context to use. |
| `create_task` | `bool` | No | Kept for compatibility; this helper always creates a task. (default: `False`) |

## Returns

`Awaitable[_T]`

The coroutine with the context.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/runnables/utils.py#L142)
