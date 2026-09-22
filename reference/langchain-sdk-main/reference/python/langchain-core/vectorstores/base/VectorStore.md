---
title: "VectorStore"
description: "Interface for vector store."
source: "https://reference.langchain.com/python/langchain-core/vectorstores/base/VectorStore"
category: "reference"
tags: [reference, langchain-core, vectorstores, base, vectorstore]
---

# VectorStore

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/vectorstores/base/VectorStore)

Interface for vector store.

## Signature

```python
VectorStore()
```

## Extends

- `ABC`

## Properties

- `embeddings`

## Methods

- [`add_texts()`](https://reference.langchain.com/python/langchain-core/vectorstores/base/VectorStore/add_texts)
- [`delete()`](https://reference.langchain.com/python/langchain-core/vectorstores/base/VectorStore/delete)
- [`get_by_ids()`](https://reference.langchain.com/python/langchain-core/vectorstores/base/VectorStore/get_by_ids)
- [`aget_by_ids()`](https://reference.langchain.com/python/langchain-core/vectorstores/base/VectorStore/aget_by_ids)
- [`adelete()`](https://reference.langchain.com/python/langchain-core/vectorstores/base/VectorStore/adelete)
- [`aadd_texts()`](https://reference.langchain.com/python/langchain-core/vectorstores/base/VectorStore/aadd_texts)
- [`add_documents()`](https://reference.langchain.com/python/langchain-core/vectorstores/base/VectorStore/add_documents)
- [`aadd_documents()`](https://reference.langchain.com/python/langchain-core/vectorstores/base/VectorStore/aadd_documents)
- [`search()`](https://reference.langchain.com/python/langchain-core/vectorstores/base/VectorStore/search)
- [`asearch()`](https://reference.langchain.com/python/langchain-core/vectorstores/base/VectorStore/asearch)
- [`similarity_search()`](https://reference.langchain.com/python/langchain-core/vectorstores/base/VectorStore/similarity_search)
- [`similarity_search_with_score()`](https://reference.langchain.com/python/langchain-core/vectorstores/base/VectorStore/similarity_search_with_score)
- [`asimilarity_search_with_score()`](https://reference.langchain.com/python/langchain-core/vectorstores/base/VectorStore/asimilarity_search_with_score)
- [`similarity_search_with_relevance_scores()`](https://reference.langchain.com/python/langchain-core/vectorstores/base/VectorStore/similarity_search_with_relevance_scores)
- [`asimilarity_search_with_relevance_scores()`](https://reference.langchain.com/python/langchain-core/vectorstores/base/VectorStore/asimilarity_search_with_relevance_scores)
- [`asimilarity_search()`](https://reference.langchain.com/python/langchain-core/vectorstores/base/VectorStore/asimilarity_search)
- [`similarity_search_by_vector()`](https://reference.langchain.com/python/langchain-core/vectorstores/base/VectorStore/similarity_search_by_vector)
- [`asimilarity_search_by_vector()`](https://reference.langchain.com/python/langchain-core/vectorstores/base/VectorStore/asimilarity_search_by_vector)
- [`max_marginal_relevance_search()`](https://reference.langchain.com/python/langchain-core/vectorstores/base/VectorStore/max_marginal_relevance_search)
- [`amax_marginal_relevance_search()`](https://reference.langchain.com/python/langchain-core/vectorstores/base/VectorStore/amax_marginal_relevance_search)
- [`max_marginal_relevance_search_by_vector()`](https://reference.langchain.com/python/langchain-core/vectorstores/base/VectorStore/max_marginal_relevance_search_by_vector)
- [`amax_marginal_relevance_search_by_vector()`](https://reference.langchain.com/python/langchain-core/vectorstores/base/VectorStore/amax_marginal_relevance_search_by_vector)
- [`from_documents()`](https://reference.langchain.com/python/langchain-core/vectorstores/base/VectorStore/from_documents)
- [`afrom_documents()`](https://reference.langchain.com/python/langchain-core/vectorstores/base/VectorStore/afrom_documents)
- [`from_texts()`](https://reference.langchain.com/python/langchain-core/vectorstores/base/VectorStore/from_texts)
- [`afrom_texts()`](https://reference.langchain.com/python/langchain-core/vectorstores/base/VectorStore/afrom_texts)
- [`as_retriever()`](https://reference.langchain.com/python/langchain-core/vectorstores/base/VectorStore/as_retriever)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/vectorstores/base.py#L43)
