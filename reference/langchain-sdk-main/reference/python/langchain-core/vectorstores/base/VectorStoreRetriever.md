---
title: "VectorStoreRetriever"
description: "Base Retriever class for VectorStore."
source: "https://reference.langchain.com/python/langchain-core/vectorstores/base/VectorStoreRetriever"
category: "reference"
tags: [reference, langchain-core, vectorstores, base, vectorstoreretriever]
---

# VectorStoreRetriever

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/vectorstores/base/VectorStoreRetriever)

Base Retriever class for VectorStore.

## Signature

```python
VectorStoreRetriever(
    self,
    *args: Any = (),
    **kwargs: Any = {},
)
```

## Extends

- `BaseRetriever`

## Properties

- `vectorstore`
- `search_type`
- `search_kwargs`
- `allowed_search_types`
- `model_config`

## Methods

- [`validate_search_type()`](https://reference.langchain.com/python/langchain-core/vectorstores/base/VectorStoreRetriever/validate_search_type)
- [`add_documents()`](https://reference.langchain.com/python/langchain-core/vectorstores/base/VectorStoreRetriever/add_documents)
- [`aadd_documents()`](https://reference.langchain.com/python/langchain-core/vectorstores/base/VectorStoreRetriever/aadd_documents)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/vectorstores/base.py#L964)
