---
title: "BaseCache"
description: "Interface for a caching layer for LLMs and Chat models."
source: "https://reference.langchain.com/python/langchain-core/caches/BaseCache"
category: "reference"
tags: [reference, langchain-core, caches, basecache]
---

# BaseCache

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/caches/BaseCache)

Interface for a caching layer for LLMs and Chat models.

The cache interface consists of the following methods:

- lookup: Look up a value based on a prompt and `llm_string`.
- update: Update the cache based on a prompt and `llm_string`.
- clear: Clear the cache.

In addition, the cache interface provides an async version of each method.

The default implementation of the async methods is to run the synchronous
method in an executor. It's recommended to override the async methods
and provide async implementations to avoid unnecessary overhead.

## Signature

```python
BaseCache()
```

## Extends

- `ABC`

## Methods

- [`lookup()`](https://reference.langchain.com/python/langchain-core/caches/BaseCache/lookup)
- [`update()`](https://reference.langchain.com/python/langchain-core/caches/BaseCache/update)
- [`clear()`](https://reference.langchain.com/python/langchain-core/caches/BaseCache/clear)
- [`alookup()`](https://reference.langchain.com/python/langchain-core/caches/BaseCache/alookup)
- [`aupdate()`](https://reference.langchain.com/python/langchain-core/caches/BaseCache/aupdate)
- [`aclear()`](https://reference.langchain.com/python/langchain-core/caches/BaseCache/aclear)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/caches.py#L32)
