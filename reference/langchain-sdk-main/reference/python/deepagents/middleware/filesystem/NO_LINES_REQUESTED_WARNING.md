---
title: "NO_LINES_REQUESTED_WARNING"
description: "Reported when a read requested zero lines."
source: "https://reference.langchain.com/python/deepagents/middleware/filesystem/NO_LINES_REQUESTED_WARNING"
category: "reference"
tags: [reference, deepagents, middleware, filesystem, no_lines_requested_warning]
---

# NO_LINES_REQUESTED_WARNING

> **Attribute** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/filesystem/NO_LINES_REQUESTED_WARNING)

Reported when a read requested zero lines.

Distinct from `EMPTY_CONTENT_WARNING` on purpose: the `read_file` description
teaches the model that the empty-contents reminder means the file itself is
empty, so reusing it for a zero-line window would state something false about
the filesystem that a following `write_file` could act on destructively.

Backends declare the zero-line window with `ReadResult.no_lines_requested`,
so an inspected-but-empty file (which otherwise arrives identically: empty
content, no pagination metadata) keeps the empty-file reminder instead.

## Signature

```python
NO_LINES_REQUESTED_WARNING = 'System reminder: no lines were read because `limit` was {limit}. The file was not inspected and may have contents; retry with `limit` >= 1 to read it.'
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/middleware/filesystem.py#L916)
