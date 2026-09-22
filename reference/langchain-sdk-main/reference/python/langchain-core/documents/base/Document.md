---
title: "Document"
description: "Class for storing a piece of text and associated metadata."
source: "https://reference.langchain.com/python/langchain-core/documents/base/Document"
category: "reference"
tags: [reference, langchain-core, documents, base, document]
---

# Document

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/documents/base/Document)

Class for storing a piece of text and associated metadata.

!!! note

    `Document` is for **retrieval workflows**, not chat I/O. For sending text
    to an LLM in a conversation, use message types from `langchain.messages`.

## Signature

```python
Document(
    self,
    page_content: str,
    **kwargs: Any = {},
)
```

## Description

**Example:**

```python
from langchain_core.documents import Document

document = Document(
    page_content="Hello, world!", metadata={"source": "https://example.com"}
)
```

## Extends

- `BaseMedia`

## Constructors

```python
__init__(
    self,
    page_content: str,
    **kwargs: Any = {},
) -> None
```

| Name | Type |
|------|------|
| `page_content` | `str` |

## Properties

- `page_content`
- `type`

## Methods

- [`is_lc_serializable()`](https://reference.langchain.com/python/langchain-core/documents/base/Document/is_lc_serializable)
- [`get_lc_namespace()`](https://reference.langchain.com/python/langchain-core/documents/base/Document/get_lc_namespace)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/documents/base.py#L288)
