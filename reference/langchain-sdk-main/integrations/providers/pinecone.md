---
title: "Pinecone integrations"
description: "Integrate with Pinecone using LangChain Python."
source: "https://docs.langchain.com/oss/python/integrations/providers/pinecone"
category: "docs"
tags: [docs, integrations, providers, pinecone]
---

# Pinecone integrations

> Integrate with Pinecone using LangChain Python.

> [Pinecone](https://docs.pinecone.io/docs/overview) is a vector database with broad functionality.

## Installation and setup

Install the Python SDK:

**pip**

```bash
pip install langchain-pinecone
```

**uv**

```bash
uv add langchain-pinecone
```

## Vector store

There exists a wrapper around Pinecone indexes, allowing you to use it as a vectorstore,
whether for semantic search or example selection.

```python
from langchain_pinecone import PineconeVectorStore
```

For a more detailed walkthrough of the Pinecone vectorstore, see [this notebook](../vectorstores/pinecone.md)

### Sparse vector store

LangChain's `PineconeSparseVectorStore` enables sparse retrieval using Pinecone's sparse English model. It maps text to sparse vectors and supports adding documents and similarity search.

```python
from langchain_pinecone import PineconeSparseVectorStore

# Initialize sparse vector store
vector_store = PineconeSparseVectorStore(
    index=my_index,
    embedding_model="pinecone-sparse-english-v0"
)
# Add documents
vector_store.add_documents(documents)
# Query
results = vector_store.similarity_search("your query", k=3)
```

For a more detailed walkthrough, see the [Pinecone Sparse Vector Store notebook](../vectorstores/pinecone_sparse.md).

### Sparse embedding

LangChain's `PineconeSparseEmbeddings` provides sparse embedding generation using Pinecone's `pinecone-sparse-english-v0` model.

```python
from langchain_pinecone.embeddings import PineconeSparseEmbeddings

# Initialize sparse embeddings
sparse_embeddings = PineconeSparseEmbeddings(
    model="pinecone-sparse-english-v0"
)
# Embed a single query (returns SparseValues)
query_embedding = sparse_embeddings.embed_query("sample text")

# Embed multiple documents (returns list of SparseValues)
docs = ["Document 1 content", "Document 2 content"]
doc_embeddings = sparse_embeddings.embed_documents(docs)
```

For more detailed usage, see the [Pinecone Sparse Embeddings notebook](../vectorstores/pinecone_sparse.md).

## Retrievers

### Self query retriever

Pinecone vector store can be used as a retriever for self-querying.

***

> [!NOTE]
> [Connect these docs](../../use-these-docs.md) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/providers/pinecone.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
