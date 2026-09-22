---
title: "glob_search"
description: "Fast file pattern matching tool that works with any codebase size."
source: "https://reference.langchain.com/python/langchain/agents/middleware/file_search/FilesystemFileSearchMiddleware/__init__/glob_search"
category: "reference"
tags: [reference, langchain, agents, middleware, file_search, filesystemfilesearchmiddleware, init, glob_search]
---

# glob_search

> **Function** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/file_search/FilesystemFileSearchMiddleware/__init__/glob_search)

Fast file pattern matching tool that works with any codebase size.

Supports glob patterns like `**/*.js` or `src/**/*.ts`.

Returns matching file paths sorted by modification time.

Use this tool when you need to find files by name patterns.

## Signature

```python
glob_search(
    pattern: str,
    path: str = '/',
) -> str
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `pattern` | `str` | Yes | The glob pattern to match files against. |
| `path` | `str` | No | The directory to search in. If not specified, searches from root. (default: `'/'`) |

## Returns

`str`

Newline-separated list of matching file paths, sorted by modification

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a18de590e7ccf5c647fbf3d689e5f1a15f78e9f5/libs/langchain_v1/langchain/agents/middleware/file_search.py#L154)
