---
title: "context_before"
description: "Context lines before the match."
source: "https://reference.langchain.com/python/deepagents/backends/protocol/GrepMatch/context_before"
category: "reference"
tags: [reference, deepagents, backends, protocol, grepmatch, context_before]
---

# context_before

> **Attribute** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/protocol/GrepMatch/context_before)

Context lines before the match.

Present (alongside `context_after`) only when a backend was asked for
`context_lines > 0` (via a backend-specific argument, e.g.
`FilesystemBackend.grep`); both keys are set together on every match or on
none. An empty list means no context lines were available on that side: the
match sits at the file boundary, the adjacent line was itself a match
(matches are never repeated as context), or the file could not be re-read
(in which case the failure is reported in `GrepResult.error`).

## Signature

```python
context_before: NotRequired[list[ContextLine]]
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/backends/protocol.py#L171)
