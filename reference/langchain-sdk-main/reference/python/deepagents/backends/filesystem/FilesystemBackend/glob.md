---
title: "glob"
description: "Find files matching a glob pattern."
source: "https://reference.langchain.com/python/deepagents/backends/filesystem/FilesystemBackend/glob"
category: "reference"
tags: [reference, deepagents, backends, filesystem, filesystembackend, glob]
---

# glob

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/filesystem/FilesystemBackend/glob)

Find files matching a glob pattern.

Pattern matching uses the shared backend contract (same as grep
include-glob):

- Patterns without `/` match the basename at any depth under `path`
  (e.g. `'*.py'` matches nested files).
- Patterns containing `/` match paths relative to `path`, with `**`
  support. A leading `/` anchors to the search root.
- Leading-dot names need an explicit leading `.` in the pattern segment.
  `**` does not descend into dot-directories, so `'*.yml'` matches
  `.github/workflows/ci.yml` while `'**/*.yml'` does not.

## Signature

```python
glob(
    self,
    pattern: str,
    path: str | None = None,
) -> GlobResult
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `pattern` | `str` | Yes | Glob pattern to match files against (e.g., `'*.py'`, `'**/*.txt'`, `'src/**/*.py'`). |
| `path` | `str \| None` | No | Base directory to search from.  Defaults to `root_dir` / `cwd`. (default: `None`) |

## Returns

`GlobResult`

`GlobResult` with matching files. `truncated` is `True` (and

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/backends/filesystem.py#L1301)
