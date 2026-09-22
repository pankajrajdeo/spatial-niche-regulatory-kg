---
title: "FilesystemFileSearchMiddleware"
description: "Provides Glob and Grep search over filesystem files."
source: "https://reference.langchain.com/python/langchain/agents/middleware/file_search/FilesystemFileSearchMiddleware"
category: "reference"
tags: [reference, langchain, agents, middleware, file_search, filesystemfilesearchmiddleware]
---

# FilesystemFileSearchMiddleware

> **Class** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/file_search/FilesystemFileSearchMiddleware)

Provides Glob and Grep search over filesystem files.

This middleware adds two tools that search through local filesystem:

- Glob: Fast file pattern matching by file path
- Grep: Fast content search using ripgrep or Python fallback

## Signature

```python
FilesystemFileSearchMiddleware(
    self,
    *,
    root_path: str,
    use_ripgrep: bool = True,
    max_file_size_mb: int = 10,
)
```

## Description

**Example:**

```python
from langchain.agents import create_agent
from langchain.agents.middleware import (
    FilesystemFileSearchMiddleware,
)

agent = create_agent(
    model=model,
    tools=[],  # Add tools as needed
    middleware=[
        FilesystemFileSearchMiddleware(root_path="/workspace"),
    ],
)
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `root_path` | `str` | Yes | Root directory to search. |
| `use_ripgrep` | `bool` | No | Whether to use `ripgrep` for search.  Falls back to Python if `ripgrep` unavailable. (default: `True`) |
| `max_file_size_mb` | `int` | No | Maximum file size to search in MB. (default: `10`) |

## Extends

- `AgentMiddleware[AgentState[ResponseT], ContextT, ResponseT]`

## Constructors

```python
__init__(
    self,
    *,
    root_path: str,
    use_ripgrep: bool = True,
    max_file_size_mb: int = 10,
) -> None
```

| Name | Type |
|------|------|
| `root_path` | `str` |
| `use_ripgrep` | `bool` |
| `max_file_size_mb` | `int` |

## Properties

- `root_path`
- `use_ripgrep`
- `max_file_size_bytes`
- `glob_search`
- `grep_search`
- `tools`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a18de590e7ccf5c647fbf3d689e5f1a15f78e9f5/libs/langchain_v1/langchain/agents/middleware/file_search.py#L108)
