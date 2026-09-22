---
title: "slice_read_response"
description: "Slice file data to the requested line range without formatting."
source: "https://reference.langchain.com/python/deepagents/backends/state/slice_read_response"
category: "reference"
tags: [reference, deepagents, backends, state, slice_read_response]
---

# slice_read_response

> **Function** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/utils/slice_read_response)

Slice file data to the requested line range without formatting.

The returned `ReadResult` carries the raw (unformatted) window in
`file_data`; line-number formatting is applied downstream by the
middleware layer.

## Signature

```python
slice_read_response(
    file_data: FileData,
    offset: int,
    limit: int,
) -> ReadResult
```

## Description

Both bounds are clamped through `normalize_read_bounds` before slicing, so
a negative `offset` reads from the first line and a negative `limit` is
treated as `0`.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `file_data` | `FileData` | Yes | `FileData` dict. |
| `offset` | `int` | Yes | Line offset (0-indexed). |
| `limit` | `int` | Yes | Maximum number of lines. |

## Returns

`ReadResult`

`ReadResult` with the sliced raw content and pagination metadata
(`total_lines`, `start_line`, `end_line`, `next_offset`). The
pagination fields are left unset for empty or whitespace-only
content, and when the clamped `limit` is `0`; the zero-`limit`
result additionally sets `no_lines_requested` so the middleware
can tell the never-inspected window apart from a genuinely empty
file. `error` is set instead when the offset exceeds the file
length.

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/backends/utils.py#L469)
