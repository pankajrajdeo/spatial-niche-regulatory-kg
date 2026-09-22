---
title: "grep_matches_from_files"
description: "Return structured grep matches from an in-memory files mapping."
source: "https://reference.langchain.com/python/deepagents/backends/state/grep_matches_from_files"
category: "reference"
tags: [reference, deepagents, backends, state, grep_matches_from_files]
---

# grep_matches_from_files

> **Function** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/utils/grep_matches_from_files)

Return structured grep matches from an in-memory files mapping.

Performs literal text search (not regex).

Returns a `GrepResult` with matches on success. When `max_count` is set, at
most that many matches are returned; if more exist the scan stops and the
result is flagged `truncated=True`. Exactly `max_count` matches with none
dropped is reported complete (`truncated=False`).

We deliberately do not raise here to keep backends non-throwing in tool
contexts and preserve user-facing error messages: a refused `glob` filter
is returned as `GrepResult(error=...)`, not raised.

## Signature

```python
grep_matches_from_files(
    files: dict[str, Any],
    pattern: str,
    path: str | None = None,
    glob: str | None = None,
    *,
    max_count: int | None = None,
) -> GrepResult
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/backends/utils.py#L937)
