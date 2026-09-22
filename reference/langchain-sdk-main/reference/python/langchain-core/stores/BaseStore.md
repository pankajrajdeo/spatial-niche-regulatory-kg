---
title: "BaseStore"
description: "Abstract interface for a key-value store."
source: "https://reference.langchain.com/python/langchain-core/stores/BaseStore"
category: "reference"
tags: [reference, langchain-core, stores, basestore]
---

# BaseStore

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/stores/BaseStore)

Abstract interface for a key-value store.

This is an interface that's meant to abstract away the details of different
key-value stores. It provides a simple interface for getting, setting, and deleting
key-value pairs.

The basic methods are `mget`, `mset`, and `mdelete` for getting, setting, and
deleting multiple key-value pairs at once. The `yield_keys` method is used to
iterate over keys that match a given prefix.

The async versions of these methods are also provided, which are meant to be used in
async contexts. The async methods are named with an `a` prefix, e.g., `amget`,
`amset`, `amdelete`, and `ayield_keys`.

By default, the `amget`, `amset`, `amdelete`, and `ayield_keys` methods are
implemented using the synchronous methods. If the store can natively support async
operations, it should override these methods.

By design the methods only accept batches of keys and values, and not single keys or
values. This is done to force user code to work with batches which will usually be
more efficient by saving on round trips to the store.

## Signature

```python
BaseStore()
```

## Extends

- `ABC`
- `Generic[K, V]`

## Methods

- [`mget()`](https://reference.langchain.com/python/langchain-core/stores/BaseStore/mget)
- [`amget()`](https://reference.langchain.com/python/langchain-core/stores/BaseStore/amget)
- [`mset()`](https://reference.langchain.com/python/langchain-core/stores/BaseStore/mset)
- [`amset()`](https://reference.langchain.com/python/langchain-core/stores/BaseStore/amset)
- [`mdelete()`](https://reference.langchain.com/python/langchain-core/stores/BaseStore/mdelete)
- [`amdelete()`](https://reference.langchain.com/python/langchain-core/stores/BaseStore/amdelete)
- [`yield_keys()`](https://reference.langchain.com/python/langchain-core/stores/BaseStore/yield_keys)
- [`ayield_keys()`](https://reference.langchain.com/python/langchain-core/stores/BaseStore/ayield_keys)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/stores.py#L26)
