---
title: "delete"
description: "Delete a file or directory from the filesystem."
source: "https://reference.langchain.com/python/deepagents/backends/filesystem/FilesystemBackend/delete"
category: "reference"
tags: [reference, deepagents, backends, filesystem, filesystembackend, delete]
---

# delete

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/filesystem/FilesystemBackend/delete)

Delete a file or directory from the filesystem.

Files are unlinked. Directories are removed recursively along with all
of their contents. Symlinks are removed as links and never followed into
their target (so deleting a symlink to a directory removes only the link).

## Signature

```python
delete(
    self,
    file_path: str,
) -> DeleteResult
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `file_path` | `str` | Yes | Path to the file or directory to delete. |

## Returns

`DeleteResult`

`DeleteResult` with the deleted path on success, or an error if the
path does not exist or removal fails. A recursive directory
removal may delete some entries before failing partway (for
example when a nested entry is not writable).

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/backends/filesystem.py#L583)
