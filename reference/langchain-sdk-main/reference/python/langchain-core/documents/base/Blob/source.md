---
title: "source"
description: "The source location of the blob as string if known otherwise none."
source: "https://reference.langchain.com/python/langchain-core/documents/base/Blob/source"
category: "reference"
tags: [reference, langchain-core, documents, base, blob, source]
---

# source

> **Attribute** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/documents/base/Blob/source)

The source location of the blob as string if known otherwise none.

If a path is associated with the `Blob`, it will default to the path location.

Unless explicitly set via a metadata field called `'source'`, in which
case that value will be used instead.

## Signature

```python
source: str | None
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/documents/base.py#L137)
