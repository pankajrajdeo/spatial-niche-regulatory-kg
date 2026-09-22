---
title: "read"
description: "Read file content for the requested line range."
source: "https://reference.langchain.com/python/deepagents/backends/store/StoreBackend/read"
category: "reference"
tags: [reference, deepagents, backends, store, storebackend, read]
---

# read

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/store/StoreBackend/read)

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
| `file_path` | `str` | Yes | Absolute file path. |
| `offset` | `int` | No | Line offset to start reading from (0-indexed). (default: `0`) |
| `limit` | `int` | No | Maximum number of lines to read. (default: `2000`) |

## Returns

`ReadResult`

`ReadResult` with raw (unformatted) content for the requested window.

Line-number formatting is applied by the middleware.

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/backends/store.py#L366)
