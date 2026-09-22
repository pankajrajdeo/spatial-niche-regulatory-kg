---
title: "delete"
description: "Delete a file or directory from state."
source: "https://reference.langchain.com/python/deepagents/backends/state/StateBackend/delete"
category: "reference"
tags: [reference, deepagents, backends, state, statebackend, delete]
---

# delete

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/state/StateBackend/delete)

Delete a file or directory from state.

Deleting a path removes the exact file at `file_path` plus every nested
key under it (the prefix `file_path` + "/"), so a directory is removed
recursively. Each removal is queued via `CONFIG_KEY_SEND` as a ``None``
value, which the `files` channel reducer interprets as a deletion marker.

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

`DeleteResult` with `file_path` on success, or an error if nothing is
stored at or under it.

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/backends/state.py#L250)
