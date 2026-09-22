---
title: "CachePolicy"
description: "Configuration for caching nodes."
source: "https://reference.langchain.com/python/langgraph/types/CachePolicy"
category: "reference"
tags: [reference, langgraph, types, cachepolicy]
---

# CachePolicy

> **Class** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/types/CachePolicy)

Configuration for caching nodes.

## Signature

```python
CachePolicy(
    self,
    *,
    key_func: KeyFuncT = default_cache_key,
    ttl: int | None = None,
)
```

## Extends

- `Generic[KeyFuncT]`

## Constructors

```python
__init__(
    self,
    *,
    key_func: KeyFuncT = default_cache_key,
    ttl: int | None = None,
) -> None
```

| Name | Type |
|------|------|
| `key_func` | `KeyFuncT` |
| `ttl` | `int \| None` |

## Properties

- `key_func`
- `ttl`

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/644815f9e5bc52ad8f7a5227a456227e9c3e639b/libs/langgraph/langgraph/types.py#L520)
