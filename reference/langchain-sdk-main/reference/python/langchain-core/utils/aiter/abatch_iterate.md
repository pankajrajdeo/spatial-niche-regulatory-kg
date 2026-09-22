---
title: "abatch_iterate"
description: "Utility batching function for async iterables."
source: "https://reference.langchain.com/python/langchain-core/utils/aiter/abatch_iterate"
category: "reference"
tags: [reference, langchain-core, utils, aiter, abatch_iterate]
---

# abatch_iterate

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/utils/aiter/abatch_iterate)

Utility batching function for async iterables.

## Signature

```python
abatch_iterate(
    size: int | None,
    iterable: AsyncIterable[T],
) -> AsyncIterator[list[T]]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `size` | `int \| None` | Yes | The size of the batch.  If `None`, returns a single batch. |
| `iterable` | `AsyncIterable[T]` | Yes | The async iterable to batch. |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/utils/aiter.py#L325)
