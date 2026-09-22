---
title: "droplastn"
description: "Drop the last n elements of an iterator."
source: "https://reference.langchain.com/python/langchain-core/output_parsers/list/droplastn"
category: "reference"
tags: [reference, langchain-core, output_parsers, list, droplastn]
---

# droplastn

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/output_parsers/list/droplastn)

Drop the last `n` elements of an iterator.

## Signature

```python
droplastn(
    iter: Iterator[T],
    n: int,
) -> Iterator[T]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `iter` | `Iterator[T]` | Yes | The iterator to drop elements from. |
| `n` | `int` | Yes | The number of elements to drop. |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/output_parsers/list.py#L23)
