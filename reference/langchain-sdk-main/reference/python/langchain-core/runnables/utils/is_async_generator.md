---
title: "is_async_generator"
description: "Check if a function is an async generator."
source: "https://reference.langchain.com/python/langchain-core/runnables/utils/is_async_generator"
category: "reference"
tags: [reference, langchain-core, runnables, utils, is_async_generator]
---

# is_async_generator

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/utils/is_async_generator)

Check if a function is an async generator.

## Signature

```python
is_async_generator(
    func: Any,
) -> TypeGuard[Callable[..., AsyncIterator[Any]]]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `func` | `Any` | Yes | The function to check. |

## Returns

`TypeGuard[Callable[..., AsyncIterator[Any]]]`

`True` if the function is an async generator, `False` otherwise.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/runnables/utils.py#L767)
