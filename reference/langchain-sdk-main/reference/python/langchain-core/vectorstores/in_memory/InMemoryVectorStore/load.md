---
title: "load"
description: "Load a vector store from a file."
source: "https://reference.langchain.com/python/langchain-core/vectorstores/in_memory/InMemoryVectorStore/load"
category: "reference"
tags: [reference, langchain-core, vectorstores, in_memory, inmemoryvectorstore, load]
---

# load

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/vectorstores/in_memory/InMemoryVectorStore/load)

Load a vector store from a file.

## Signature

```python
load(
    cls,
    path: str,
    embedding: Embeddings,
    **kwargs: Any = {},
) -> InMemoryVectorStore
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `path` | `str` | Yes | The path to load the vector store from. |
| `embedding` | `Embeddings` | Yes | The embedding to use. |
| `**kwargs` | `Any` | No | Additional arguments to pass to the constructor. (default: `{}`) |

## Returns

`InMemoryVectorStore`

A `VectorStore` object.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/vectorstores/in_memory.py#L516)
