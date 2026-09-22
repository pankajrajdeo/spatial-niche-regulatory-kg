---
title: "read"
description: "Read file content for the requested line range."
source: "https://reference.langchain.com/python/deepagents/backends/protocol/BackendProtocol/read"
category: "reference"
tags: [reference, deepagents, backends, protocol, backendprotocol, read]
---

# read

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/protocol/BackendProtocol/read)

Read file content for the requested line range.

Implementations must tolerate degenerate windows rather than raising:
a negative `offset` reads from the first line, and a non-positive
`limit` returns empty content with every pagination field unset.
`deepagents.backends.utils.normalize_read_bounds` clamps both bounds for
implementations that slice in Python.

Implementations must also set `start_line` whenever they return
line-numberable text. The middleware falls back to deriving the gutter
from `offset` when `start_line` is unset, which only yields a valid
1-indexed gutter for windows the backend actually sliced.

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
| `file_path` | `str` | Yes | Absolute path to the file to read. Must start with `'/'`. |
| `offset` | `int` | No | Line number to start reading from (0-indexed). (default: `0`) |
| `limit` | `int` | No | Maximum number of lines to read. (default: `2000`) |

## Returns

`ReadResult`

`ReadResult` with raw (unformatted) content for the requested window,
or an error if the file doesn't exist or can't be read.

Line-number formatting is applied downstream by the filesystem
middleware (`format_content_with_line_numbers`), not by backends:
it adds the gutter, starts numbering at `offset + 1`, and splits
lines longer than 5000 characters into continuation rows
(e.g., `5.1`, `5.2`).

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/backends/protocol.py#L454)
