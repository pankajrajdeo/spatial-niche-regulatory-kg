---
title: "from_data"
description: "Initialize the Blob from in-memory data."
source: "https://reference.langchain.com/python/langchain-core/documents/base/Blob/from_data"
category: "reference"
tags: [reference, langchain-core, documents, base, blob, from_data]
---

# from_data

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/documents/base/Blob/from_data)

Initialize the `Blob` from in-memory data.

## Signature

```python
from_data(
    cls,
    data: str | bytes,
    *,
    encoding: str = 'utf-8',
    mime_type: str | None = None,
    path: str | None = None,
    metadata: dict[Any, Any] | None = None,
) -> Blob
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `data` | `str \| bytes` | Yes | The in-memory data associated with the `Blob` |
| `encoding` | `str` | No | Encoding to use if decoding the bytes into a string (default: `'utf-8'`) |
| `mime_type` | `str \| None` | No | If provided, will be set as the MIME type of the data (default: `None`) |
| `path` | `str \| None` | No | If provided, will be set as the source from which the data came (default: `None`) |
| `metadata` | `dict[Any, Any] \| None` | No | Metadata to associate with the `Blob` (default: `None`) |

## Returns

`Blob`

`Blob` instance

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/documents/base.py#L250)
