---
title: "BaseRetriever"
description: "Abstract base class for a document retrieval system."
source: "https://reference.langchain.com/python/langchain-core/retrievers/BaseRetriever"
category: "reference"
tags: [reference, langchain-core, retrievers, baseretriever]
---

# BaseRetriever

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/retrievers/BaseRetriever)

Abstract base class for a document retrieval system.

A retrieval system is defined as something that can take string queries and return
the most 'relevant' documents from some source.

Usage:

A retriever follows the standard `Runnable` interface, and should be used via the
standard `Runnable` methods of `invoke`, `ainvoke`, `batch`, `abatch`.

Implementation:

When implementing a custom retriever, the class should implement the
`_get_relevant_documents` method to define the logic for retrieving documents.

Optionally, an async native implementations can be provided by overriding the
`_aget_relevant_documents` method.

!!! example "Retriever that returns the first 5 documents from a list of documents"

```python
    from langchain_core.documents import Document
    from langchain_core.retrievers import BaseRetriever

    class SimpleRetriever(BaseRetriever):
        docs: list[Document]
        k: int = 5

        def _get_relevant_documents(self, query: str) -> list[Document]:
            """Return the first k documents from the list of documents"""
            return self.docs[:self.k]

        async def _aget_relevant_documents(self, query: str) -> list[Document]:
            """(Optional) async native implementation."""
            return self.docs[:self.k]
```

!!! example "Simple retriever based on a scikit-learn vectorizer"

```python
    from sklearn.metrics.pairwise import cosine_similarity

    class TFIDFRetriever(BaseRetriever, BaseModel):
        vectorizer: Any
        docs: list[Document]
        tfidf_array: Any
        k: int = 4

        class Config:
            arbitrary_types_allowed = True

        def _get_relevant_documents(self, query: str) -> list[Document]:
            # Ip -- (n_docs,x), Op -- (n_docs,n_Feats)
            query_vec = self.vectorizer.transform([query])
            # Op -- (n_docs,1) -- Cosine Sim with each doc
            results = cosine_similarity(self.tfidf_array, query_vec).reshape((-1,))
            return [self.docs[i] for i in results.argsort()[-self.k :][::-1]]
```

## Signature

```python
BaseRetriever(
    self,
    *args: Any = (),
    **kwargs: Any = {},
)
```

## Extends

- `RunnableSerializable[RetrieverInput, RetrieverOutput]`
- `ABC`

## Properties

- `model_config`
- `tags`
- `metadata`

## Methods

- [`invoke()`](https://reference.langchain.com/python/langchain-core/retrievers/BaseRetriever/invoke)
- [`ainvoke()`](https://reference.langchain.com/python/langchain-core/retrievers/BaseRetriever/ainvoke)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/retrievers.py#L55)
