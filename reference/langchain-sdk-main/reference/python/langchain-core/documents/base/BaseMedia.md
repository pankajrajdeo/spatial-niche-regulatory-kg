---
title: "BaseMedia"
description: "Base class for content used in retrieval and data processing workflows."
source: "https://reference.langchain.com/python/langchain-core/documents/base/BaseMedia"
category: "reference"
tags: [reference, langchain-core, documents, base, basemedia]
---

# BaseMedia

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/documents/base/BaseMedia)

Base class for content used in retrieval and data processing workflows.

Provides common fields for content that needs to be stored, indexed, or searched.

!!! note

    For multimodal content in **chat messages** (images, audio sent to/from LLMs),
    use `langchain.messages` content blocks instead.

## Signature

```python
BaseMedia(
    self,
    *args: Any = (),
    **kwargs: Any = {},
)
```

## Extends

- `Serializable`

## Properties

- `id`
- `metadata`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/documents/base.py#L34)
