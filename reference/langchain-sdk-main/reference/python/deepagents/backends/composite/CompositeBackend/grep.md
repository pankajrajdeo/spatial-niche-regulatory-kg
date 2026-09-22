---
title: "grep"
description: "Search files for literal text pattern."
source: "https://reference.langchain.com/python/deepagents/backends/composite/CompositeBackend/grep"
category: "reference"
tags: [reference, deepagents, backends, composite, compositebackend, grep]
---

# grep

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/composite/CompositeBackend/grep)

Search files for literal text pattern.

Routes to backends based on path: specific route searches one backend,
`"/"` or `None` searches all backends, otherwise searches
default backend.

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
| `pattern` | `str` | Yes | Literal text to search for (NOT regex). |
| `path` | `str \| None` | No | Directory to search. None searches all backends. (default: `None`) |
| `glob` | `str \| None` | No | Glob pattern to filter files (e.g., `"*.py"`, `"**/*.txt"`).  Filters by filename, not content. (default: `None`) |
| `max_count` | `int \| None` | No | Optional total cap on returned matches across all routed backends. `None` returns every match; an int enforces the cap globally (not per backend), short-circuits remaining routes once the cap is reached, and flags the result `truncated=True`.  Unlike a single backend, composite does not guarantee the "exactly `max_count` matches means complete" boundary: when an earlier route fills the budget exactly, the remaining routes are short-circuited and the result is flagged `truncated=True` even if those routes would have contributed nothing. The flag is thus conservative — it may over-report truncation, never under-report. (default: `None`) |

## Returns

`GrepResult`

`GrepResult` with matches or error.

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/backends/composite.py#L459)
