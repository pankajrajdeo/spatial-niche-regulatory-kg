---
title: "ReadResult"
description: "Result from backend read operations."
source: "https://reference.langchain.com/python/deepagents/backends/protocol/ReadResult"
category: "reference"
tags: [reference, deepagents, backends, protocol, readresult]
---

# ReadResult

> **Class** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/protocol/ReadResult)

Result from backend read operations.

## Signature

```python
ReadResult(
    self,
    error: str | None = None,
    file_data: FileData | None = None,
    total_lines: int | None = None,
    start_line: int | None = None,
    end_line: int | None = None,
    next_offset: int | None = None,
    no_lines_requested: bool = False,
)
```

## Constructors

```python
__init__(
    self,
    error: str | None = None,
    file_data: FileData | None = None,
    total_lines: int | None = None,
    start_line: int | None = None,
    end_line: int | None = None,
    next_offset: int | None = None,
    no_lines_requested: bool = False,
) -> None
```

| Name | Type |
|------|------|
| `error` | `str \| None` |
| `file_data` | `FileData \| None` |
| `total_lines` | `int \| None` |
| `start_line` | `int \| None` |
| `end_line` | `int \| None` |
| `next_offset` | `int \| None` |
| `no_lines_requested` | `bool` |

## Properties

- `error`
- `file_data`
- `total_lines`
- `start_line`
- `end_line`
- `next_offset`
- `no_lines_requested`

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/backends/protocol.py#L203)
