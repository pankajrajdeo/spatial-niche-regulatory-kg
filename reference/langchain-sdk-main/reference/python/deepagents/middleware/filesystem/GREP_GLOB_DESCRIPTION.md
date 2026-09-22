---
title: "GREP_GLOB_DESCRIPTION"
description: "View source on GitHub"
source: "https://reference.langchain.com/python/deepagents/middleware/filesystem/GREP_GLOB_DESCRIPTION"
category: "reference"
tags: [reference, deepagents, middleware, filesystem, grep_glob_description]
---

# GREP_GLOB_DESCRIPTION

> **Attribute** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/filesystem/GREP_GLOB_DESCRIPTION)

## Signature

```python
GREP_GLOB_DESCRIPTION = "Glob pattern (NOT regex) limiting which files are searched (e.g. '*.py', '*.ts'). A pattern without '/' matches the file name at any depth; a pattern containing '/' matches the search-root-relative path (e.g. 'src/**/*.py'). This is an in-tool file filter, not a call to the separate glob tool. Brace expansion (e.g. '*.{ts,tsx}') is not supported on all backends; run a separate search per extension for reliable results."
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/middleware/filesystem.py#L1208)
