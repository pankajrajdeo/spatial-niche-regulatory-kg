---
title: "grep_search"
description: "Fast content search tool that works with any codebase size."
source: "https://reference.langchain.com/python/langchain/agents/middleware/file_search/FilesystemFileSearchMiddleware/__init__/grep_search"
category: "reference"
tags: [reference, langchain, agents, middleware, file_search, filesystemfilesearchmiddleware, init, grep_search]
---

# grep_search

> **Function** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/file_search/FilesystemFileSearchMiddleware/__init__/grep_search)

Fast content search tool that works with any codebase size.

Searches file contents using regular expressions. Supports full regex
syntax and filters files by pattern with the include parameter.

## Signature

```python
grep_search(
    pattern: str,
    path: str = '/',
    include: str | None = None,
    output_mode: Literal['files_with_matches', 'content', 'count'] = 'files_with_matches',
) -> str
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `pattern` | `str` | Yes | The regular expression pattern to search for in file contents. |
| `path` | `str` | No | The directory to search in. If not specified, searches from root. (default: `'/'`) |
| `include` | `str \| None` | No | File pattern to filter (e.g., `'*.js'`, `'*.{ts,tsx}'`). (default: `None`) |
| `output_mode` | `Literal['files_with_matches', 'content', 'count']` | No | Output format:  - `'files_with_matches'`: Only file paths containing matches - `'content'`: Matching lines with `file:line:content` format - `'count'`: Count of matches per file (default: `'files_with_matches'`) |

## Returns

`str`

Search results formatted according to `output_mode`.
Returns `'No matches found'` if no results.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a18de590e7ccf5c647fbf3d689e5f1a15f78e9f5/libs/langchain_v1/langchain/agents/middleware/file_search.py#L209)
