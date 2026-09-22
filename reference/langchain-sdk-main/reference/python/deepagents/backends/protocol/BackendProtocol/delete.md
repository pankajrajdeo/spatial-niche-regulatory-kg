---
title: "delete"
description: "Delete a path, recursively removing anything nested under it."
source: "https://reference.langchain.com/python/deepagents/backends/protocol/BackendProtocol/delete"
category: "reference"
tags: [reference, deepagents, backends, protocol, backendprotocol, delete]
---

# delete

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/protocol/BackendProtocol/delete)

Delete a path, recursively removing anything nested under it.

This method is optional. Backends that do not implement it inherit this
default, which raises `NotImplementedError`. Callers that need to support
a mix of backends should guard with
[`supports_delete`][deepagents.backends.protocol.supports_delete] before
calling, or catch `NotImplementedError`.

Deletion is recursive: it removes `file_path` plus everything nested
under it. On hierarchical backends (e.g.
[`FilesystemBackend`][deepagents.backends.filesystem.FilesystemBackend])
that means a directory and its contents; on key-value backends it means
the exact key plus every key sharing the `file_path` + "/" prefix.

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
| `file_path` | `str` | Yes | Absolute path to delete (a file, or a directory/prefix to remove recursively). Must start with '/'. |

## Returns

`DeleteResult`

`DeleteResult` with the deleted path on success, or an error if
nothing exists at or under the path or removal fails.

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/backends/protocol.py#L722)
