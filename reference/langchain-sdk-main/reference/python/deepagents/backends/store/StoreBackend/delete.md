---
title: "delete"
description: "Delete a file or directory from the store."
source: "https://reference.langchain.com/python/deepagents/backends/store/StoreBackend/delete"
category: "reference"
tags: [reference, deepagents, backends, store, storebackend, delete]
---

# delete

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/store/StoreBackend/delete)

Delete a file or directory from the store.

Deleting a path removes the exact key `file_path` plus every key nested
under it (the prefix `file_path` + "/"), so a directory is removed
recursively. Wildcards (e.g. `*`) in `file_path` are treated literally.

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
| `file_path` | `str` | Yes | Path of the file or directory to delete. |

## Returns

`DeleteResult`

`DeleteResult` with `file_path` on success, or an error if no key is
stored at or under it.

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/backends/store.py#L548)
