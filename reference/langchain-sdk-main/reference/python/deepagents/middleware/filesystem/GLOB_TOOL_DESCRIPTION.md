---
title: "GLOB_TOOL_DESCRIPTION"
description: "View source on GitHub"
source: "https://reference.langchain.com/python/deepagents/middleware/filesystem/GLOB_TOOL_DESCRIPTION"
category: "reference"
tags: [reference, deepagents, middleware, filesystem, glob_tool_description]
---

# GLOB_TOOL_DESCRIPTION

> **Attribute** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/filesystem/GLOB_TOOL_DESCRIPTION)

## Signature

```python
GLOB_TOOL_DESCRIPTION = 'Find files matching a glob pattern, returning absolute paths.\n\nSupports `*` (any characters within a path segment), `**` (any directories), `?` (single character), `[abc]` (one character from a set), and `{a,b}` (alternatives), e.g. `*.py`, `src/**/*.py`, `*.{yml,yaml}`.\n\nA pattern without `/` matches the file name at any depth under the search root (`*.py` matches `src/app/main.py`). A pattern containing `/` matches the search-root-relative path (`src/**/*.py`). A leading `/` anchors to the search root (`/*.py` matches only top-level Python files).\n\nLeading-dot names are only matched when the pattern segment itself starts with `.` (use `.env`, or `.github/**/*.yml`). Because `**` will not descend into dot-directories, the bare form `*.yml` is *broader* than `**/*.yml` and is usually what you want.'
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/middleware/filesystem.py#L1412)
