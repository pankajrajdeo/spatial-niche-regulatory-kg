---
title: "grep"
description: "Search for a literal text pattern in files."
source: "https://reference.langchain.com/python/deepagents/backends/filesystem/FilesystemBackend/grep"
category: "reference"
tags: [reference, deepagents, backends, filesystem, filesystembackend, grep]
---

# grep

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/filesystem/FilesystemBackend/grep)

Search for a literal text pattern in files.

Uses ripgrep if available, falling back to Python search.

## Signature

```python
grep(
    self,
    pattern: str,
    path: str | None = None,
    glob: str | None = None,
    *,
    max_count: int | None = None,
    context_lines: int = 0,
) -> GrepResult
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `pattern` | `str` | Yes | Literal string to search for (NOT regex). |
| `path` | `str \| None` | No | Directory or file path to search in. Defaults to current directory. (default: `None`) |
| `glob` | `str \| None` | No | Optional glob pattern to filter which files to search. (default: `None`) |
| `max_count` | `int \| None` | No | Optional total cap on returned matches across all files. `None` returns every match; an int stops the search once the cap is reached and flags the result with `truncated=True`. (default: `None`) |
| `context_lines` | `int` | No | Number of lines to include before and after each match.  This is a backend-level API. It is deliberately not exposed through the agent-facing `grep` tool (`GrepSchema`), so matches returned via that tool never carry context. (default: `0`) |

## Returns

`GrepResult`

`GrepResult` with matches or error. When `context_lines > 0` and some

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/backends/filesystem.py#L617)
