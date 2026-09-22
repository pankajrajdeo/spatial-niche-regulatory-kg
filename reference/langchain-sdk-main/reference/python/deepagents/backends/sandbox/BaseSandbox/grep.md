---
title: "grep"
description: "Search file contents for a literal string using grep -F."
source: "https://reference.langchain.com/python/deepagents/backends/sandbox/BaseSandbox/grep"
category: "reference"
tags: [reference, deepagents, backends, sandbox, basesandbox, grep]
---

# grep

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/sandbox/BaseSandbox/grep)

Search file contents for a literal string using `grep -F`.

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
| `pattern` | `str` | Yes | Literal string to search for (not a regex). |
| `path` | `str \| None` | No | Directory or file to search in.  Defaults to `"."`. (default: `None`) |
| `glob` | `str \| None` | No | Optional glob to restrict the search. Patterns without a `/` (e.g. `'*.py'`) match basenames at any depth via `grep --include`; patterns containing a `/` (e.g. `'src/**/*.py'`) match the search-root-relative path via an in-process Python glob. (default: `None`) |
| `max_count` | `int \| None` | No | Optional total cap on returned matches across all files. `None` returns every match; an int stops the search once the cap is reached and flags the result with `truncated=True`. (default: `None`) |

## Returns

`GrepResult`

`GrepResult` with a list of `GrepMatch` dicts, or `error` on failure.

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/backends/sandbox.py#L1875)
