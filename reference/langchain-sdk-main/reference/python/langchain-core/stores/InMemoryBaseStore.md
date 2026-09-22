---
title: "InMemoryBaseStore"
description: "In-memory implementation of the BaseStore using a dictionary."
source: "https://reference.langchain.com/python/langchain-core/stores/InMemoryBaseStore"
category: "reference"
tags: [reference, langchain-core, stores, inmemorybasestore]
---

# InMemoryBaseStore

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/stores/InMemoryBaseStore)

In-memory implementation of the `BaseStore` using a dictionary.

## Signature

```python
InMemoryBaseStore(
    self,
)
```

## Extends

- `BaseStore[str, V]`
- `Generic[V]`

## Constructors

```python
__init__(
    self,
) -> None
```

## Properties

- `store`

## Methods

- [`mget()`](https://reference.langchain.com/python/langchain-core/stores/InMemoryBaseStore/mget)
- [`amget()`](https://reference.langchain.com/python/langchain-core/stores/InMemoryBaseStore/amget)
- [`mset()`](https://reference.langchain.com/python/langchain-core/stores/InMemoryBaseStore/mset)
- [`amset()`](https://reference.langchain.com/python/langchain-core/stores/InMemoryBaseStore/amset)
- [`mdelete()`](https://reference.langchain.com/python/langchain-core/stores/InMemoryBaseStore/mdelete)
- [`amdelete()`](https://reference.langchain.com/python/langchain-core/stores/InMemoryBaseStore/amdelete)
- [`yield_keys()`](https://reference.langchain.com/python/langchain-core/stores/InMemoryBaseStore/yield_keys)
- [`ayield_keys()`](https://reference.langchain.com/python/langchain-core/stores/InMemoryBaseStore/ayield_keys)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/stores.py#L176)
