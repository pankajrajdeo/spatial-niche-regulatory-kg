---
title: "Tee"
description: "Create n separate asynchronous iterators over iterable."
source: "https://reference.langchain.com/python/langchain-core/utils/aiter/Tee"
category: "reference"
tags: [reference, langchain-core, utils, aiter, tee]
---

# Tee

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/utils/aiter/Tee)

Create `n` separate asynchronous iterators over `iterable`.

This splits a single `iterable` into multiple iterators, each providing
the same items in the same order.

All child iterators may advance separately but share the same items from `iterable`
-- when the most advanced iterator retrieves an item, it is buffered until the least
advanced iterator has yielded it as well.

A `tee` works lazily and can handle an infinite `iterable`, provided
that all iterators advance.

```python
async def derivative(sensor_data):
    previous, current = a.tee(sensor_data, n=2)
    await a.anext(previous)  # advance one iterator
    return a.map(operator.sub, previous, current)
```

Unlike `itertools.tee`, `.tee` returns a custom type instead of a `tuple`. Like a
tuple, it can be indexed, iterated and unpacked to get the child iterators. In
addition, its `.tee.aclose` method immediately closes all children, and it can be
used in an `async with` context for the same effect.

If `iterable` is an iterator and read elsewhere, `tee` will *not* provide these
items. Also, `tee` must internally buffer each item until the last iterator has
yielded it; if the most and least advanced iterator differ by most data, using a
`list` is more efficient (but not lazy).

If the underlying iterable is concurrency safe (`anext` may be awaited concurrently)
the resulting iterators are concurrency safe as well. Otherwise, the iterators are
safe if there is only ever one single "most advanced" iterator.

To enforce sequential use of `anext`, provide a `lock`

- e.g. an `asyncio.Lock` instance in an `asyncio` application - and access is
    automatically synchronised.

## Signature

```python
Tee(
    self,
    iterable: AsyncIterator[T],
    n: int = 2,
    *,
    lock: AbstractAsyncContextManager[Any] | None = None,
)
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `iterable` | `AsyncIterator[T]` | Yes | The iterable to split. |
| `n` | `int` | No | The number of iterators to create. (default: `2`) |
| `lock` | `AbstractAsyncContextManager[Any] \| None` | No | The lock to synchronise access to the shared buffers. (default: `None`) |

## Extends

- `Generic[T]`

## Constructors

```python
__init__(
    self,
    iterable: AsyncIterator[T],
    n: int = 2,
    *,
    lock: AbstractAsyncContextManager[Any] | None = None,
)
```

| Name | Type |
|------|------|
| `iterable` | `AsyncIterator[T]` |
| `n` | `int` |
| `lock` | `AbstractAsyncContextManager[Any] \| None` |

## Methods

- [`aclose()`](https://reference.langchain.com/python/langchain-core/utils/aiter/Tee/aclose)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/utils/aiter.py#L161)
