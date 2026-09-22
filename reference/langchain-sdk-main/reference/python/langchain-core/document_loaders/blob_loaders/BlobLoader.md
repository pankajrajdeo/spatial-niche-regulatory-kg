---
title: "BlobLoader"
description: "Abstract interface for blob loaders implementation."
source: "https://reference.langchain.com/python/langchain-core/document_loaders/blob_loaders/BlobLoader"
category: "reference"
tags: [reference, langchain-core, document_loaders, blob_loaders, blobloader]
---

# BlobLoader

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/document_loaders/blob_loaders/BlobLoader)

Abstract interface for blob loaders implementation.

Implementer should be able to load raw content from a storage system according to
some criteria and return the raw content lazily as a stream of blobs.

## Signature

```python
BlobLoader()
```

## Extends

- `ABC`

## Methods

- [`yield_blobs()`](https://reference.langchain.com/python/langchain-core/document_loaders/blob_loaders/BlobLoader/yield_blobs)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/document_loaders/blob_loaders.py#L19)
