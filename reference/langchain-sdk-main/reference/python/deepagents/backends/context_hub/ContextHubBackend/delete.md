---
title: "delete"
description: "Delete a file or directory by committing its removal from the hub repo."
source: "https://reference.langchain.com/python/deepagents/backends/context_hub/ContextHubBackend/delete"
category: "reference"
tags: [reference, deepagents, backends, context_hub, contexthubbackend, delete]
---

# delete

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/context_hub/ContextHubBackend/delete)

Delete a file or directory by committing its removal from the hub repo.

Deleting a path removes the exact file plus every nested entry under it
(the prefix `file_path` + "/"), so a directory is removed recursively.

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
stored at or under it (or the hub is unavailable).

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/backends/context_hub.py#L529)
