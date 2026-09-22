---
title: "from_documents"
description: "Return VectorStore initialized from documents and embeddings."
source: "https://reference.langchain.com/python/langchain-core/vectorstores/base/VectorStore/from_documents"
category: "reference"
tags: [reference, langchain-core, vectorstores, base, vectorstore, from_documents]
---

# from_documents

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/vectorstores/base/VectorStore/from_documents)

Return `VectorStore` initialized from documents and embeddings.

## Signature

```python
from_documents(
    cls,
    documents: list[Document],
    embedding: Embeddings,
    **kwargs: Any = {},
) -> Self
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `documents` | `list[Document]` | Yes | List of `Document` objects to add to the `VectorStore`. |
| `embedding` | `Embeddings` | Yes | Embedding function to use. |
| `**kwargs` | `Any` | No | Additional keyword arguments. (default: `{}`) |

## Returns

`Self`

`VectorStore` initialized from documents and embeddings.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/vectorstores/base.py#L786)
