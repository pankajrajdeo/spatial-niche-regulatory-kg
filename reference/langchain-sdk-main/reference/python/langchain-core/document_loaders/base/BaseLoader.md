---
title: "BaseLoader"
description: "Interface for document loader."
source: "https://reference.langchain.com/python/langchain-core/document_loaders/base/BaseLoader"
category: "reference"
tags: [reference, langchain-core, document_loaders, base, baseloader]
---

# BaseLoader

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/document_loaders/base/BaseLoader)

Interface for document loader.

Implementations should implement the lazy-loading method using generators to avoid
loading all documents into memory at once.

`load` is provided just for user convenience and should not be overridden.

## Signature

```python
BaseLoader()
```

## Extends

- `ABC`

## Methods

- [`load()`](https://reference.langchain.com/python/langchain-core/document_loaders/base/BaseLoader/load)
- [`aload()`](https://reference.langchain.com/python/langchain-core/document_loaders/base/BaseLoader/aload)
- [`load_and_split()`](https://reference.langchain.com/python/langchain-core/document_loaders/base/BaseLoader/load_and_split)
- [`lazy_load()`](https://reference.langchain.com/python/langchain-core/document_loaders/base/BaseLoader/lazy_load)
- [`alazy_load()`](https://reference.langchain.com/python/langchain-core/document_loaders/base/BaseLoader/alazy_load)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/document_loaders/base.py#L26)
