---
title: "grep"
description: "Search for a literal text pattern in files."
source: "https://reference.langchain.com/python/deepagents/backends/protocol/BackendProtocol/grep"
category: "reference"
tags: [reference, deepagents, backends, protocol, backendprotocol, grep]
---

# grep

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/protocol/BackendProtocol/grep)

Search for a literal text pattern in files.

## Signature

```python
grep(
    self,
    pattern: str,
    path: str | None = None,
    glob: str | None = None,
    *,
    max_count: int | None = None,
) -> GrepResult
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `pattern` | `str` | Yes | Literal string to search for (NOT regex).  Performs exact substring matching within file content.  Example: `"TODO"` matches any line containing `"TODO"` |
| `path` | `str \| None` | No | Optional directory path to search in.  If `None`, searches in current working directory.  Example: `'/workspace/src'` (default: `None`) |
| `glob` | `str \| None` | No | Optional glob pattern to filter which FILES to search.  Filters by filename/path, not content.  Supports standard glob wildcards:  - `*` matches any characters in filename - `**` matches any directories recursively - `?` matches single character - `[abc]` matches one character from set (default: `None`) |
| `max_count` | `int \| None` | No | Optional total cap on the number of matches returned across all files.  `None` (the default) preserves existing backend behavior and returns every match. When set to an int, at most that many matches are returned; if more exist the search stops and the result is flagged with `GrepResult.truncated=True`. Exactly `max_count` matches with none dropped is reported complete (`truncated=False`). Interpreted as a total cap, not a per-file cap. (default: `None`) |

## Returns

`GrepResult`

`GrepResult` with matches or error.

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/backends/protocol.py#L499)
