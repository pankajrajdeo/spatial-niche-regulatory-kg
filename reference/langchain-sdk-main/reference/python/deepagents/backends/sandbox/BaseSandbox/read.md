---
title: "read"
description: "Read file content with server-side line-based pagination."
source: "https://reference.langchain.com/python/deepagents/backends/sandbox/BaseSandbox/read"
category: "reference"
tags: [reference, deepagents, backends, sandbox, basesandbox, read]
---

# read

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/sandbox/BaseSandbox/read)

Read file content with server-side line-based pagination.

Runs a Python script on the sandbox via `execute()` that reads the
file, detects encoding, and applies offset/limit pagination for text
files. Only the requested page is returned over the wire, and text
output is capped to about 500 KiB to avoid backend stdout/log transport
failures. When that cap is exceeded, the returned content is truncated
with guidance to continue pagination using a different `offset` or
smaller `limit`.

Binary files (non-UTF-8) are returned base64-encoded without
pagination.

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
| `file_path` | `str` | Yes | Absolute path to the file to read. |
| `offset` | `int` | No | Starting line number (0-indexed).  Only applied to text files, and clamped to the start of the file when negative. (default: `0`) |
| `limit` | `int` | No | Maximum number of lines to return.  Only applied to text files with content: a non-positive value returns empty content with no pagination metadata. Empty files return the empty-file reminder regardless of `limit`. (default: `2000`) |

## Returns

`ReadResult`

`ReadResult` with `file_data` on success or `error` on failure.

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/backends/sandbox.py#L1525)
