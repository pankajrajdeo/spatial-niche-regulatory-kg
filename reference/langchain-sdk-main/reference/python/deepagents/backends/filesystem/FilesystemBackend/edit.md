---
title: "edit"
description: "Edit a file by replacing string occurrences."
source: "https://reference.langchain.com/python/deepagents/backends/filesystem/FilesystemBackend/edit"
category: "reference"
tags: [reference, deepagents, backends, filesystem, filesystembackend, edit]
---

# edit

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/filesystem/FilesystemBackend/edit)

Edit a file by replacing string occurrences.

## Signature

```python
edit(
    self,
    file_path: str,
    old_string: str,
    new_string: str,
    replace_all: bool = False,
) -> EditResult
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `file_path` | `str` | Yes | Path to the file to edit. |
| `old_string` | `str` | Yes | The text to search for and replace. |
| `new_string` | `str` | Yes | The replacement text. |
| `replace_all` | `bool` | No | If `True`, replace all occurrences. If `False` (default), replace only if exactly one occurrence exists. (default: `False`) |

## Returns

`EditResult`

`EditResult` with path and occurrence count on success, or error
message if file not found or replacement fails.

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/backends/filesystem.py#L521)
