---
title: "InMemoryCache"
description: "Cache that stores things in memory."
source: "https://reference.langchain.com/python/langchain-core/caches/InMemoryCache"
category: "reference"
tags: [reference, langchain-core, caches, inmemorycache]
---

# InMemoryCache

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/caches/InMemoryCache)

Cache that stores things in memory.

## Signature

```python
InMemoryCache(
    self,
    *,
    maxsize: int | None = None,
)
```

## Description

**Example:**

```python
from langchain_core.caches import InMemoryCache
from langchain_core.outputs import Generation

# Initialize cache
cache = InMemoryCache()

# Update cache
cache.update(
    prompt="What is the capital of France?",
    llm_string="model='gpt-5.4-mini',
    return_val=[Generation(text="Paris")],
)

# Lookup cache
result = cache.lookup(
    prompt="What is the capital of France?",
    llm_string="model='gpt-5.4-mini',
)
# result is [Generation(text="Paris")]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `maxsize` | `int \| None` | No | The maximum number of items to store in the cache.  If `None`, the cache has no maximum size.  If the cache exceeds the maximum size, the oldest items are removed. (default: `None`) |

## Extends

- `BaseCache`

## Constructors

```python
__init__(
    self,
    *,
    maxsize: int | None = None,
) -> None
```

| Name | Type |
|------|------|
| `maxsize` | `int \| None` |

## Methods

- [`lookup()`](https://reference.langchain.com/python/langchain-core/caches/InMemoryCache/lookup)
- [`update()`](https://reference.langchain.com/python/langchain-core/caches/InMemoryCache/update)
- [`clear()`](https://reference.langchain.com/python/langchain-core/caches/InMemoryCache/clear)
- [`alookup()`](https://reference.langchain.com/python/langchain-core/caches/InMemoryCache/alookup)
- [`aupdate()`](https://reference.langchain.com/python/langchain-core/caches/InMemoryCache/aupdate)
- [`aclear()`](https://reference.langchain.com/python/langchain-core/caches/InMemoryCache/aclear)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/caches.py#L155)
