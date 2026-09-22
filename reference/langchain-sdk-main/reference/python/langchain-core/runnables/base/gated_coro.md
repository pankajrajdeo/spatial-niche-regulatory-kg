---
title: "gated_coro"
description: "Run a coroutine with a semaphore."
source: "https://reference.langchain.com/python/langchain-core/runnables/base/gated_coro"
category: "reference"
tags: [reference, langchain-core, runnables, base, gated_coro]
---

# gated_coro

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/utils/gated_coro)

Run a coroutine with a semaphore.

## Signature

```python
gated_coro(
    semaphore: asyncio.Semaphore,
    coro: Coroutine[Any, Any, Any],
) -> Any
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `semaphore` | `asyncio.Semaphore` | Yes | The semaphore to use. |
| `coro` | `Coroutine[Any, Any, Any]` | Yes | The coroutine to run. |

## Returns

`Any`

The result of the coroutine.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/runnables/utils.py#L49)
