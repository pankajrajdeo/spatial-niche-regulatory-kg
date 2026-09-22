---
title: "from_path"
description: "Load the blob from a path like object."
source: "https://reference.langchain.com/python/langchain-core/documents/base/Blob/from_path"
category: "reference"
tags: [reference, langchain-core, documents, base, blob, from_path]
---

# from_path

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/documents/base/Blob/from_path)

Load the blob from a path like object.

## Signature

```python
from_path(
    cls,
    path: PathLike,
    *,
    encoding: str = 'utf-8',
    mime_type: str | None = None,
    guess_type: bool = True,
    metadata: dict[Any, Any] | None = None,
) -> Blob
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `path` | `PathLike` | Yes | Path-like object to file to be read |
| `encoding` | `str` | No | Encoding to use if decoding the bytes into a string (default: `'utf-8'`) |
| `mime_type` | `str \| None` | No | If provided, will be set as the MIME type of the data (default: `None`) |
| `guess_type` | `bool` | No | If `True`, the MIME type will be guessed from the file extension, if a MIME type was not provided (default: `True`) |
| `metadata` | `dict[Any, Any] \| None` | No | Metadata to associate with the `Blob` (default: `None`) |

## Returns

`Blob`

`Blob` instance

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/documents/base.py#L213)
