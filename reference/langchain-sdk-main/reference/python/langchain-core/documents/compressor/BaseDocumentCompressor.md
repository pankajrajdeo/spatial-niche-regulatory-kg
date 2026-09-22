---
title: "BaseDocumentCompressor"
description: "Base class for document compressors."
source: "https://reference.langchain.com/python/langchain-core/documents/compressor/BaseDocumentCompressor"
category: "reference"
tags: [reference, langchain-core, documents, compressor, basedocumentcompressor]
---

# BaseDocumentCompressor

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/documents/compressor/BaseDocumentCompressor)

Base class for document compressors.

This abstraction is primarily used for post-processing of retrieved documents.

`Document` objects matching a given query are first retrieved.

Then the list of documents can be further processed.

For example, one could re-rank the retrieved documents using an LLM.

!!! note
    Users should favor using a `RunnableLambda` instead of sub-classing from this
    interface.

## Signature

```python
BaseDocumentCompressor()
```

## Extends

- `BaseModel`
- `ABC`

## Methods

- [`compress_documents()`](https://reference.langchain.com/python/langchain-core/documents/compressor/BaseDocumentCompressor/compress_documents)
- [`acompress_documents()`](https://reference.langchain.com/python/langchain-core/documents/compressor/BaseDocumentCompressor/acompress_documents)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/documents/compressor.py#L19)
