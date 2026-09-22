---
title: "FakeEmbeddings"
description: "Fake embedding model for unit testing purposes."
source: "https://reference.langchain.com/python/langchain-core/embeddings/fake/FakeEmbeddings"
category: "reference"
tags: [reference, langchain-core, embeddings, fake, fakeembeddings]
---

# FakeEmbeddings

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/embeddings/fake/FakeEmbeddings)

Fake embedding model for unit testing purposes.

This embedding model creates embeddings by sampling from a normal distribution.

!!! danger "Toy model"
    Do not use this outside of testing, as it is not a real embedding model.

## Signature

```python
FakeEmbeddings()
```

## Description

**Instantiate:**

```python
from langchain_core.embeddings import FakeEmbeddings

embed = FakeEmbeddings(size=100)
```

**Embed single text:**

```python
input_text = "The meaning of life is 42"
vector = embed.embed_query(input_text)
print(vector[:3])
```
```python
[-0.700234640213188, -0.581266257710429, -1.1328482266445354]
```

**Embed multiple texts:**

```python
input_texts = ["Document 1...", "Document 2..."]
vectors = embed.embed_documents(input_texts)
print(len(vectors))
# The first 3 coordinates for the first vector
print(vectors[0][:3])
```
```python
2
[-0.5670477847544458, -0.31403828652395727, -0.5840547508955257]
```

## Extends

- `Embeddings`
- `BaseModel`

## Properties

- `size`

## Methods

- [`embed_documents()`](https://reference.langchain.com/python/langchain-core/embeddings/fake/FakeEmbeddings/embed_documents)
- [`embed_query()`](https://reference.langchain.com/python/langchain-core/embeddings/fake/FakeEmbeddings/embed_query)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/embeddings/fake.py#L16)
