---
title: "read"
description: "Read file content for the requested line range."
source: "https://reference.langchain.com/python/deepagents/backends/filesystem/FilesystemBackend/read"
category: "reference"
tags: [reference, deepagents, backends, filesystem, filesystembackend, read]
---

# read

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/filesystem/FilesystemBackend/read)

Read file content for the requested line range.

## Signature

```python
read(
    self,
    file_path: str,
    offset: int = 0,
    limit: int = 2000,
) -> ReadResult
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `file_path` | `str` | Yes | Absolute or relative file path. |
| `offset` | `int` | No | Line offset to start reading from (0-indexed).  Only applied to text files, and clamped to the start of the file when negative. (default: `0`) |
| `limit` | `int` | No | Maximum number of lines to read.  Only applied to text files with content: a non-positive value returns empty content with no pagination metadata. Empty and whitespace-only files return the empty-file reminder regardless of `limit`, and binary files return their full payload. (default: `2000`) |

## Returns

`ReadResult`

`ReadResult` with raw (unformatted) content for the requested window.

Line-number formatting is applied by the middleware.

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/backends/filesystem.py#L414)
