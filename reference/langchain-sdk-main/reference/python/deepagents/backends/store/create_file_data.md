---
title: "create_file_data"
description: "Create a FileData object with timestamps."
source: "https://reference.langchain.com/python/deepagents/backends/store/create_file_data"
category: "reference"
tags: [reference, deepagents, backends, store, create_file_data]
---

# create_file_data

> **Function** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/utils/create_file_data)

Create a `FileData` object with timestamps.

## Signature

```python
create_file_data(
    content: str,
    created_at: str | None = None,
    encoding: str = 'utf-8',
) -> FileData
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `content` | `str` | Yes | File content as string (plain text or base64-encoded binary). |
| `created_at` | `str \| None` | No | Optional creation timestamp (ISO format). (default: `None`) |
| `encoding` | `str` | No | Content encoding — `"utf-8"` for text, `"base64"` for binary. (default: `'utf-8'`) |

## Returns

`FileData`

FileD`ata dict with content, encoding, and timestamps.

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/backends/utils.py#L359)
