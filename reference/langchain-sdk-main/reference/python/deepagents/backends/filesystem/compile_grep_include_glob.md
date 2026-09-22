---
title: "compile_grep_include_glob"
description: "Compile a grep include-glob into a matcher with ripgrep-like semantics."
source: "https://reference.langchain.com/python/deepagents/backends/filesystem/compile_grep_include_glob"
category: "reference"
tags: [reference, deepagents, backends, filesystem, compile_grep_include_glob]
---

# compile_grep_include_glob

> **Function** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/utils/compile_grep_include_glob)

Compile a grep include-glob into a matcher with ripgrep-like semantics.

Provides one shared include-glob behavior for every backend so the same
`grep(..., glob=...)` call closely mirrors ripgrep for common include
patterns, whether or not ripgrep is installed:

- Patterns without a `/` match the basename at any depth.

    Example: `*.py` matches `src/app/main.py`.
- Patterns containing a `/` match the path relative to the grep search
    root, with `**` support.

    Example: `src/**/*.py` matches `src/app/main.py`.
- A leading `/` anchors the pattern to the search root; it narrows the match
    rather than widening it.

    Example: `/*.py` matches `top.py` but not `src/app/main.py`.

Leading-dot names match only when the pattern segment itself starts with
`.` (no `DOTMATCH`), and `**` will not descend into dot-directories. A bare
pattern is therefore *broader* than its `**/` form: `*.yml` matches
`.github/workflows/ci.yml`, while `**/*.yml` does not.

Exclusion/negation patterns (a leading `!`) are not supported: the `!` is
treated literally rather than inverting the match, so results for such
patterns can diverge from `rg --glob '!...'`.

This is the single source of truth for both `grep(..., glob=...)` and
backend `glob()`.

## Signature

```python
compile_grep_include_glob(
    pattern: str,
) -> Callable[[str], bool]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `pattern` | `str` | Yes | Glob include pattern. |

## Returns

`Callable[[str], bool]`

Predicate accepting a search-root-relative POSIX path; returns True when

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/backends/utils.py#L97)
