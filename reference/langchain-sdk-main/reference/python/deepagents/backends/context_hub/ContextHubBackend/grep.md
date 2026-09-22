---
title: "grep"
description: "Search contents for pattern (optional path / glob filters)."
source: "https://reference.langchain.com/python/deepagents/backends/context_hub/ContextHubBackend/grep"
category: "reference"
tags: [reference, deepagents, backends, context_hub, contexthubbackend, grep]
---

# grep

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/context_hub/ContextHubBackend/grep)

Search contents for `pattern` (optional `path` / `glob` filters).

The `glob` filter uses `fnmatch` semantics and does *not* follow the
shared include-glob contract that `glob()` on this class uses: `*`
crosses `/`, and matching is case-normalized. Do not assume the two
agree on a given pattern.

When `max_count` is set, at most that many matches are returned; if more
exist the search stops and the result is flagged `truncated=True`.
Exactly `max_count` matches with none dropped is reported complete
(`truncated=False`).

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

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/backends/context_hub.py#L593)
