---
title: "upload_files"
description: "Upload multiple files to the filesystem."
source: "https://reference.langchain.com/python/deepagents/backends/filesystem/FilesystemBackend/upload_files"
category: "reference"
tags: [reference, deepagents, backends, filesystem, filesystembackend, upload_files]
---

# upload_files

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/filesystem/FilesystemBackend/upload_files)

Upload multiple files to the filesystem.

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

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/backends/filesystem.py#L1442)
