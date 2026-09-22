---
title: "BaseDocumentTransformer"
description: "Abstract base class for document transformation."
source: "https://reference.langchain.com/python/langchain-core/documents/transformers/BaseDocumentTransformer"
category: "reference"
tags: [reference, langchain-core, documents, transformers, basedocumenttransformer]
---

# BaseDocumentTransformer

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/documents/transformers/BaseDocumentTransformer)

Abstract base class for document transformation.

A document transformation takes a sequence of `Document` objects and returns a
sequence of transformed `Document` objects.

## Signature

```python
BaseDocumentTransformer()
```

## Description

**Example:**

```python
class EmbeddingsRedundantFilter(BaseDocumentTransformer, BaseModel):
    embeddings: Embeddings
    similarity_fn: Callable = cosine_similarity
    similarity_threshold: float = 0.95

    class Config:
        arbitrary_types_allowed = True

    def transform_documents(
        self, documents: Sequence[Document], **kwargs: Any
    ) -> Sequence[Document]:
        stateful_documents = get_stateful_documents(documents)
        embedded_documents = _get_embeddings_from_stateful_docs(
            self.embeddings, stateful_documents
        )
        included_idxs = _filter_similar_embeddings(
            embedded_documents,
            self.similarity_fn,
            self.similarity_threshold,
        )
        return [stateful_documents[i] for i in sorted(included_idxs)]

    async def atransform_documents(
        self, documents: Sequence[Document], **kwargs: Any
    ) -> Sequence[Document]:
        raise NotImplementedError
```

## Extends

- `ABC`

## Methods

- [`transform_documents()`](https://reference.langchain.com/python/langchain-core/documents/transformers/BaseDocumentTransformer/transform_documents)
- [`atransform_documents()`](https://reference.langchain.com/python/langchain-core/documents/transformers/BaseDocumentTransformer/atransform_documents)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/documents/transformers.py#L16)
