---
title: "add_documents"
description: "Add documents to the VectorStore."
source: "https://reference.langchain.com/python/langchain-core/vectorstores/base/VectorStoreRetriever/add_documents"
category: "reference"
tags: [reference, langchain-core, vectorstores, base, vectorstoreretriever, add_documents]
---

# add_documents

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/vectorstores/base/VectorStoreRetriever/add_documents)

Add documents to the `VectorStore`.

## Signature

```python
add_documents(
    self,
    documents: list[Document],
    **kwargs: Any = {},
) -> list[str]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `documents` | `list[Document]` | Yes | Documents to add to the `VectorStore`. |
| `**kwargs` | `Any` | No | Other keyword arguments that subclasses might use. (default: `{}`) |

## Returns

`list[str]`

List of IDs of the added texts.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/vectorstores/base.py#L1087)
