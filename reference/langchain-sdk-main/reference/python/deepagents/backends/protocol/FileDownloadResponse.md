---
title: "FileDownloadResponse"
description: "Result of a single file download operation."
source: "https://reference.langchain.com/python/deepagents/backends/protocol/FileDownloadResponse"
category: "reference"
tags: [reference, deepagents, backends, protocol, filedownloadresponse]
---

# FileDownloadResponse

> **Class** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/protocol/FileDownloadResponse)

Result of a single file download operation.

The response is designed to allow partial success in batch operations.

The errors are standardized using `FileOperationError` literals for certain
recoverable conditions for use cases that involve LLMs performing
file operations.

## Signature

```python
FileDownloadResponse(
    self,
    path: str,
    content: bytes | None = None,
    error: FileOperationError | str | None = None,
)
```

## Constructors

```python
__init__(
    self,
    path: str,
    content: bytes | None = None,
    error: FileOperationError | str | None = None,
) -> None
```

| Name | Type |
|------|------|
| `path` | `str` |
| `content` | `bytes \| None` |
| `error` | `FileOperationError \| str \| None` |

## Properties

- `path`
- `content`
- `error`

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/backends/protocol.py#L65)
