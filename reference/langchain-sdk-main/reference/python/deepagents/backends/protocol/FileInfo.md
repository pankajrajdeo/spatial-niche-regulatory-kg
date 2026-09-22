---
title: "FileInfo"
description: "Structured file listing info."
source: "https://reference.langchain.com/python/deepagents/backends/protocol/FileInfo"
category: "reference"
tags: [reference, deepagents, backends, protocol, fileinfo]
---

# FileInfo

> **Class** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/protocol/FileInfo)

Structured file listing info.

Minimal contract used across backends. Only `path` is required.
Other fields are best-effort and may be absent depending on backend.

## Signature

```python
FileInfo()
```

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    path: str,
    is_dir: NotRequired[bool],
    size: NotRequired[int],
    modified_at: NotRequired[str],
)
```

| Name | Type |
|------|------|
| `path` | `str` |
| `is_dir` | `NotRequired[bool]` |
| `size` | `NotRequired[int]` |
| `modified_at` | `NotRequired[str]` |

## Properties

- `path`
- `is_dir`
- `size`
- `modified_at`

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/backends/protocol.py#L129)
