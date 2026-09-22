---
title: "InMemoryDocumentIndex"
description: "In memory document index."
source: "https://reference.langchain.com/python/langchain-core/indexing/in_memory/InMemoryDocumentIndex"
category: "reference"
tags: [reference, langchain-core, indexing, in_memory, inmemorydocumentindex]
---

# InMemoryDocumentIndex

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/indexing/in_memory/InMemoryDocumentIndex)

In memory document index.

This is an in-memory document index that stores documents in a dictionary.

It provides a simple search API that returns documents by the number of
counts the given query appears in the document.

## Signature

```python
InMemoryDocumentIndex(
    self,
    *args: Any = (),
    **kwargs: Any = {},
)
```

## Extends

- `DocumentIndex`

## Properties

- `store`
- `top_k`

## Methods

- [`upsert()`](https://reference.langchain.com/python/langchain-core/indexing/in_memory/InMemoryDocumentIndex/upsert)
- [`delete()`](https://reference.langchain.com/python/langchain-core/indexing/in_memory/InMemoryDocumentIndex/delete)
- [`get()`](https://reference.langchain.com/python/langchain-core/indexing/in_memory/InMemoryDocumentIndex/get)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/indexing/in_memory.py#L18)
