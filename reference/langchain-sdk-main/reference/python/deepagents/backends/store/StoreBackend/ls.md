---
title: "ls"
description: "List files and directories in the specified directory (non-recursive)."
source: "https://reference.langchain.com/python/deepagents/backends/store/StoreBackend/ls"
category: "reference"
tags: [reference, deepagents, backends, store, storebackend, ls]
---

# ls

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/store/StoreBackend/ls)

List files and directories in the specified directory (non-recursive).

## Signature

```python
ls(
    self,
    path: str,
) -> LsResult
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `path` | `str` | Yes | Absolute path to directory. |

## Returns

`LsResult`

List of `FileInfo`-like dicts for files and directories directly
in the directory.

Directories have a trailing `/` in their path and `is_dir=True`.

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/backends/store.py#L306)
