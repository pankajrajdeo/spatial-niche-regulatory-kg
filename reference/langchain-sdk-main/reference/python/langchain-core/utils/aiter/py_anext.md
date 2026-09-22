---
title: "py_anext"
description: "Pure-Python implementation of anext() for testing purposes."
source: "https://reference.langchain.com/python/langchain-core/utils/aiter/py_anext"
category: "reference"
tags: [reference, langchain-core, utils, aiter, py_anext]
---

# py_anext

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/utils/aiter/py_anext)

Pure-Python implementation of `anext()` for testing purposes.

Closely matches the builtin `anext()` C implementation.

Can be used to compare the built-in implementation of the inner coroutines machinery
to C-implementation of `__anext__()` and `send()` or `throw()` on the returned
generator.

## Signature

```python
py_anext(
    iterator: AsyncIterator[T],
    default: T | Any = _no_default,
) -> Awaitable[T | Any | None]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `iterator` | `AsyncIterator[T]` | Yes | The async iterator to advance. |
| `default` | `T \| Any` | No | The value to return if the iterator is exhausted.  If not provided, a `StopAsyncIteration` exception is raised. (default: `_no_default`) |

## Returns

`Awaitable[T | Any | None]`

The next value from the iterator, or the default value if the iterator is
exhausted.

## ⚠️ Deprecated

Deprecated since version 1.1.2. Will be removed in version 2.0.0.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/utils/aiter.py#L37)
