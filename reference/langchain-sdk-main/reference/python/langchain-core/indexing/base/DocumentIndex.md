---
title: "DocumentIndex"
description: "A document retriever that supports indexing operations."
source: "https://reference.langchain.com/python/langchain-core/indexing/base/DocumentIndex"
category: "reference"
tags: [reference, langchain-core, indexing, base, documentindex]
---

# DocumentIndex

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/indexing/base/DocumentIndex)

A document retriever that supports indexing operations.

This indexing interface is designed to be a generic abstraction for storing and
querying documents that has an ID and metadata associated with it.

The interface is designed to be agnostic to the underlying implementation of the
indexing system.

The interface is designed to support the following operations:

1. Storing document in the index.
2. Fetching document by ID.
3. Searching for document using a query.

## Signature

```python
DocumentIndex(
    self,
    *args: Any = (),
    **kwargs: Any = {},
)
```

## Extends

- `BaseRetriever`

## Methods

- [`upsert()`](https://reference.langchain.com/python/langchain-core/indexing/base/DocumentIndex/upsert)
- [`aupsert()`](https://reference.langchain.com/python/langchain-core/indexing/base/DocumentIndex/aupsert)
- [`delete()`](https://reference.langchain.com/python/langchain-core/indexing/base/DocumentIndex/delete)
- [`adelete()`](https://reference.langchain.com/python/langchain-core/indexing/base/DocumentIndex/adelete)
- [`get()`](https://reference.langchain.com/python/langchain-core/indexing/base/DocumentIndex/get)
- [`aget()`](https://reference.langchain.com/python/langchain-core/indexing/base/DocumentIndex/aget)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/indexing/base.py#L496)
