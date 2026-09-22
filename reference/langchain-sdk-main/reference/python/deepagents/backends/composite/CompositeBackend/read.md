---
title: "read"
description: "Read file content, routing to appropriate backend."
source: "https://reference.langchain.com/python/deepagents/backends/composite/CompositeBackend/read"
category: "reference"
tags: [reference, deepagents, backends, composite, compositebackend, read]
---

# read

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/composite/CompositeBackend/read)

Read file content, routing to appropriate backend.

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

`ReadResult`

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/backends/composite.py#L391)
