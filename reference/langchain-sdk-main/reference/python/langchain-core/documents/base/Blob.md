---
title: "Blob"
description: "Raw data abstraction for document loading and file processing."
source: "https://reference.langchain.com/python/langchain-core/documents/base/Blob"
category: "reference"
tags: [reference, langchain-core, documents, base, blob]
---

# Blob

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/documents/base/Blob)

Raw data abstraction for document loading and file processing.

Represents raw bytes or text, either in-memory or by file reference. Used
primarily by document loaders to decouple data loading from parsing.

Inspired by [Mozilla's `Blob`](https://developer.mozilla.org/en-US/docs/Web/API/Blob)

???+ example "Initialize a blob from in-memory data"

```python
    from langchain_core.documents import Blob

    blob = Blob.from_data("Hello, world!")

    # Read the blob as a string
    print(blob.as_string())

    # Read the blob as bytes
    print(blob.as_bytes())

    # Read the blob as a byte stream
    with blob.as_bytes_io() as f:
        print(f.read())
```

??? example "Load from memory and specify MIME type and metadata"

```python
    from langchain_core.documents import Blob

    blob = Blob.from_data(
        data="Hello, world!",
        mime_type="text/plain",
        metadata={"source": "https://example.com"},
    )
```

??? example "Load the blob from a file"

```python
    from langchain_core.documents import Blob

    blob = Blob.from_path("path/to/file.txt")

    # Read the blob as a string
    print(blob.as_string())

    # Read the blob as bytes
    print(blob.as_bytes())

    # Read the blob as a byte stream
    with blob.as_bytes_io() as f:
        print(f.read())
```

## Signature

```python
Blob(
    self,
    *args: Any = (),
    **kwargs: Any = {},
)
```

## Extends

- `BaseMedia`

## Properties

- `data`
- `mimetype`
- `encoding`
- `path`
- `model_config`
- `source`

## Methods

- [`check_blob_is_valid()`](https://reference.langchain.com/python/langchain-core/documents/base/Blob/check_blob_is_valid)
- [`as_string()`](https://reference.langchain.com/python/langchain-core/documents/base/Blob/as_string)
- [`as_bytes()`](https://reference.langchain.com/python/langchain-core/documents/base/Blob/as_bytes)
- [`as_bytes_io()`](https://reference.langchain.com/python/langchain-core/documents/base/Blob/as_bytes_io)
- [`from_path()`](https://reference.langchain.com/python/langchain-core/documents/base/Blob/from_path)
- [`from_data()`](https://reference.langchain.com/python/langchain-core/documents/base/Blob/from_data)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/documents/base.py#L59)
