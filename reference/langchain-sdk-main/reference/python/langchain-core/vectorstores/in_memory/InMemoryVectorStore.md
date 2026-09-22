---
title: "InMemoryVectorStore"
description: "In-memory vector store implementation."
source: "https://reference.langchain.com/python/langchain-core/vectorstores/in_memory/InMemoryVectorStore"
category: "reference"
tags: [reference, langchain-core, vectorstores, in_memory, inmemoryvectorstore]
---

# InMemoryVectorStore

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/vectorstores/in_memory/InMemoryVectorStore)

In-memory vector store implementation.

Uses a dictionary, and computes cosine similarity for search using numpy.

## Signature

```python
InMemoryVectorStore(
    self,
    embedding: Embeddings,
)
```

## Description

**Setup:**

Install `langchain-core`.

```bash
pip install -U langchain-core
```

Key init args — indexing params:

* embedding_function: Embeddings
    Embedding function to use.

**Instantiate:**

```python
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_openai import OpenAIEmbeddings

vector_store = InMemoryVectorStore(OpenAIEmbeddings())
```

**Add Documents:**

```python
from langchain_core.documents import Document

document_1 = Document(id="1", page_content="foo", metadata={"baz": "bar"})
document_2 = Document(id="2", page_content="thud", metadata={"bar": "baz"})
document_3 = Document(id="3", page_content="i will be deleted :(")

documents = [document_1, document_2, document_3]
vector_store.add_documents(documents=documents)
```

**Inspect documents:**

```python
top_n = 10
for index, (id, doc) in enumerate(vector_store.store.items()):
    if index < top_n:
        # docs have keys 'id', 'vector', 'text', 'metadata'
        print(f"{id}: {doc['text']}")
    else:
        break
```

**Delete Documents:**

```python
vector_store.delete(ids=["3"])
```

**Search:**

```python
results = vector_store.similarity_search(query="thud", k=1)
for doc in results:
    print(f"* {doc.page_content} [{doc.metadata}]")
```

```txt
* thud [{'bar': 'baz'}]
```

**Search with filter:**

```python
def _filter_function(doc: Document) -> bool:
    return doc.metadata.get("bar") == "baz"

results = vector_store.similarity_search(
    query="thud", k=1, filter=_filter_function
)
for doc in results:
    print(f"* {doc.page_content} [{doc.metadata}]")
```

```txt
* thud [{'bar': 'baz'}]
```

**Search with score:**

```python
results = vector_store.similarity_search_with_score(query="qux", k=1)
for doc, score in results:
    print(f"* [SIM={score:3f}] {doc.page_content} [{doc.metadata}]")
```

```txt
* [SIM=0.832268] foo [{'baz': 'bar'}]
```

**Async:**

```python
# add documents
# await vector_store.aadd_documents(documents=documents)

# delete documents
# await vector_store.adelete(ids=["3"])

# search
# results = vector_store.asimilarity_search(query="thud", k=1)

# search with score
results = await vector_store.asimilarity_search_with_score(query="qux", k=1)
for doc, score in results:
    print(f"* [SIM={score:3f}] {doc.page_content} [{doc.metadata}]")
```

```txt
* [SIM=0.832268] foo [{'baz': 'bar'}]
```

**Use as Retriever:**

```python
retriever = vector_store.as_retriever(
    search_type="mmr",
    search_kwargs={"k": 1, "fetch_k": 2, "lambda_mult": 0.5},
)
retriever.invoke("thud")
```

```txt
[Document(id='2', metadata={'bar': 'baz'}, page_content='thud')]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `embedding` | `Embeddings` | Yes | embedding function to use. |

## Extends

- `VectorStore`

## Constructors

```python
__init__(
    self,
    embedding: Embeddings,
) -> None
```

| Name | Type |
|------|------|
| `embedding` | `Embeddings` |

## Properties

- `store`
- `embedding`
- `embeddings`

## Methods

- [`delete()`](https://reference.langchain.com/python/langchain-core/vectorstores/in_memory/InMemoryVectorStore/delete)
- [`adelete()`](https://reference.langchain.com/python/langchain-core/vectorstores/in_memory/InMemoryVectorStore/adelete)
- [`add_documents()`](https://reference.langchain.com/python/langchain-core/vectorstores/in_memory/InMemoryVectorStore/add_documents)
- [`aadd_documents()`](https://reference.langchain.com/python/langchain-core/vectorstores/in_memory/InMemoryVectorStore/aadd_documents)
- [`get_by_ids()`](https://reference.langchain.com/python/langchain-core/vectorstores/in_memory/InMemoryVectorStore/get_by_ids)
- [`aget_by_ids()`](https://reference.langchain.com/python/langchain-core/vectorstores/in_memory/InMemoryVectorStore/aget_by_ids)
- [`similarity_search_with_score_by_vector()`](https://reference.langchain.com/python/langchain-core/vectorstores/in_memory/InMemoryVectorStore/similarity_search_with_score_by_vector)
- [`similarity_search_with_score()`](https://reference.langchain.com/python/langchain-core/vectorstores/in_memory/InMemoryVectorStore/similarity_search_with_score)
- [`asimilarity_search_with_score()`](https://reference.langchain.com/python/langchain-core/vectorstores/in_memory/InMemoryVectorStore/asimilarity_search_with_score)
- [`similarity_search_by_vector()`](https://reference.langchain.com/python/langchain-core/vectorstores/in_memory/InMemoryVectorStore/similarity_search_by_vector)
- [`asimilarity_search_by_vector()`](https://reference.langchain.com/python/langchain-core/vectorstores/in_memory/InMemoryVectorStore/asimilarity_search_by_vector)
- [`similarity_search()`](https://reference.langchain.com/python/langchain-core/vectorstores/in_memory/InMemoryVectorStore/similarity_search)
- [`asimilarity_search()`](https://reference.langchain.com/python/langchain-core/vectorstores/in_memory/InMemoryVectorStore/asimilarity_search)
- [`max_marginal_relevance_search_by_vector()`](https://reference.langchain.com/python/langchain-core/vectorstores/in_memory/InMemoryVectorStore/max_marginal_relevance_search_by_vector)
- [`max_marginal_relevance_search()`](https://reference.langchain.com/python/langchain-core/vectorstores/in_memory/InMemoryVectorStore/max_marginal_relevance_search)
- [`amax_marginal_relevance_search()`](https://reference.langchain.com/python/langchain-core/vectorstores/in_memory/InMemoryVectorStore/amax_marginal_relevance_search)
- [`from_texts()`](https://reference.langchain.com/python/langchain-core/vectorstores/in_memory/InMemoryVectorStore/from_texts)
- [`afrom_texts()`](https://reference.langchain.com/python/langchain-core/vectorstores/in_memory/InMemoryVectorStore/afrom_texts)
- [`load()`](https://reference.langchain.com/python/langchain-core/vectorstores/in_memory/InMemoryVectorStore/load)
- [`dump()`](https://reference.langchain.com/python/langchain-core/vectorstores/in_memory/InMemoryVectorStore/dump)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/vectorstores/in_memory.py#L34)
