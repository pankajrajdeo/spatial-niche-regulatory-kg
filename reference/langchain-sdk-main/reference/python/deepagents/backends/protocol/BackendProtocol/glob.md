---
title: "glob"
description: "Find files matching a glob pattern."
source: "https://reference.langchain.com/python/deepagents/backends/protocol/BackendProtocol/glob"
category: "reference"
tags: [reference, deepagents, backends, protocol, backendprotocol, glob]
---

# glob

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/protocol/BackendProtocol/glob)

Find files matching a glob pattern.

Pattern matching follows the shared backend contract (aligned with
grep include-glob, not classic non-recursive shell globbing):

- Patterns without `/` match the basename at any depth under `path`.

    Example: `*.py` matches `src/app/main.py`.
- Patterns containing `/` match paths relative to the search root, with
  `**` support.

    Example: `src/**/*.py` matches `src/app/main.py`.
- A leading `/` anchors the pattern to the search root; it narrows the
  match rather than widening it.

    Example: `/*.py` matches `top.py` but not `src/app/main.py`.
- Leading-dot names match only when the pattern segment itself starts
  with `.`. Since `**` will not descend into dot-directories, a bare
  pattern is *broader* than its `**/` form.

    Example: `*.yml` matches `.github/workflows/ci.yml`; `**/*.yml`
    does not. `.env` matches `.env`; `*` does not.

Only regular files are returned; directories are never matched.

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
| `pattern` | `str` | Yes | Glob pattern with wildcards to match file paths.  Supports:  - `*` matches any characters within a path segment - `**` matches any directories recursively - `?` matches a single character - `[abc]` matches one character from a set, `[!abc]` negates - `{a,b}` brace expansion, including nested groups |
| `path` | `str \| None` | No | Optional base directory to search from.  If omitted, the backend chooses its default search root.  The pattern is applied relative to this path. (default: `None`) |

## Returns

`GlobResult`

`GlobResult` with matching files or error. Patterns the matcher

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/backends/protocol.py#L598)
