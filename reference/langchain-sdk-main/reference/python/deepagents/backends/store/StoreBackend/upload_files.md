---
title: "upload_files"
description: "Upload multiple files to the store."
source: "https://reference.langchain.com/python/deepagents/backends/store/StoreBackend/upload_files"
category: "reference"
tags: [reference, deepagents, backends, store, storebackend, upload_files]
---

# upload_files

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/store/StoreBackend/upload_files)

Upload multiple files to the store.

Binary files (images, PDFs, etc.) are stored as base64-encoded strings.
Text files are stored as utf-8 strings.

## Signature

```python
upload_files(
    self,
    files: list[tuple[str, bytes]],
) -> list[FileUploadResponse]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `files` | `list[tuple[str, bytes]]` | Yes | List of `(path, content)` tuples where content is bytes. |

## Returns

`list[FileUploadResponse]`

List of `FileUploadResponse` objects, one per input file.

Response order matches input order.

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/backends/store.py#L655)
