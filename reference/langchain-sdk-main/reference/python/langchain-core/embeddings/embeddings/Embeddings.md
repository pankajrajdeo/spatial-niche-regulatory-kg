---
title: "Embeddings"
description: "Interface for embedding models."
source: "https://reference.langchain.com/python/langchain-core/embeddings/embeddings/Embeddings"
category: "reference"
tags: [reference, langchain-core, embeddings]
---

# Embeddings

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/embeddings/embeddings/Embeddings)

Interface for embedding models.

This is an interface meant for implementing text embedding models.

Text embedding models are used to map text to a vector (a point in n-dimensional
space).

Texts that are similar will usually be mapped to points that are close to each
other in this space. The exact details of what's considered "similar" and how
"distance" is measured in this space are dependent on the specific embedding model.

This abstraction contains a method for embedding a list of documents and a method
for embedding a query text. The embedding of a query text is expected to be a single
vector, while the embedding of a list of documents is expected to be a list of
vectors.

Usually the query embedding is identical to the document embedding, but the
abstraction allows treating them independently.

In addition to the synchronous methods, this interface also provides asynchronous
versions of the methods.

By default, the asynchronous methods are implemented using the synchronous methods;
however, implementations may choose to override the asynchronous methods with
an async native implementation for performance reasons.

## Signature

```python
Embeddings()
```

## Extends

- `ABC`

## Methods

- [`embed_documents()`](https://reference.langchain.com/python/langchain-core/embeddings/embeddings/Embeddings/embed_documents)
- [`embed_query()`](https://reference.langchain.com/python/langchain-core/embeddings/embeddings/Embeddings/embed_query)
- [`aembed_documents()`](https://reference.langchain.com/python/langchain-core/embeddings/embeddings/Embeddings/aembed_documents)
- [`aembed_query()`](https://reference.langchain.com/python/langchain-core/embeddings/embeddings/Embeddings/aembed_query)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/embeddings/embeddings.py#L8)
