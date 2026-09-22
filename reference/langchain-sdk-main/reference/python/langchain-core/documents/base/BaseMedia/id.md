---
title: "id"
description: "An optional identifier for the document."
source: "https://reference.langchain.com/python/langchain-core/documents/base/BaseMedia/id"
category: "reference"
tags: [reference, langchain-core, documents, base, basemedia, id]
---

# id

> **Attribute** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/documents/base/BaseMedia/id)

An optional identifier for the document.

Ideally this should be unique across the document collection and formatted
as a UUID, but this will not be enforced.

## Signature

```python
id: str | None = Field(default=None, coerce_numbers_to_str=True)
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/documents/base.py#L48)
