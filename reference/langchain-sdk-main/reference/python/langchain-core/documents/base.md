---
title: "base"
description: "Base classes for media and documents."
source: "https://reference.langchain.com/python/langchain-core/documents/base"
category: "reference"
tags: [reference, langchain-core, documents, base]
---

# base

> **Module** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/documents/base)

Base classes for media and documents.

This module contains core abstractions for **data retrieval and processing workflows**:

- `BaseMedia`: Base class providing `id` and `metadata` fields
- `Blob`: Raw data loading (files, binary data) - used by document loaders
- `Document`: Text content for retrieval (RAG, vector stores, semantic search)

!!! note "Not for LLM chat messages"

    These classes are for data processing pipelines, not LLM I/O. For multimodal
    content in chat messages (images, audio in conversations), see
    `langchain.messages` content blocks instead.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/documents/base.py)
