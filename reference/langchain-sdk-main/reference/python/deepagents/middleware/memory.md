---
title: "memory"
description: "Middleware for loading agent memory/context from AGENTS.md files."
source: "https://reference.langchain.com/python/deepagents/middleware/memory"
category: "reference"
tags: [reference, deepagents, middleware, memory]
---

# memory

> **Module** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/memory)

Middleware for loading agent memory/context from AGENTS.md files.

This module implements support for the AGENTS.md specification (https://agents.md/),
loading memory/context from configurable sources and injecting into the system prompt.

## Overview

AGENTS.md files provide project-specific context and instructions to help AI agents
work effectively. Unlike skills (which are on-demand workflows), memory is always
loaded and provides persistent context.

## Usage

```python
from deepagents import MemoryMiddleware
from deepagents.backends.filesystem import FilesystemBackend

# Security: FilesystemBackend allows reading/writing from the entire filesystem.
# Either ensure the agent is running within a sandbox OR add human-in-the-loop (HIL)
# approval to file operations.
backend = FilesystemBackend(root_dir="/")

middleware = MemoryMiddleware(
    backend=backend,
    sources=[
        "~/.deepagents/AGENTS.md",
        "./.deepagents/AGENTS.md",
    ],
)

agent = create_deep_agent(middleware=[middleware])
```

## Memory Sources

Sources are simply paths to AGENTS.md files that are loaded in order and combined.
Multiple sources are concatenated in order, with all content included.
Later sources appear after earlier ones in the combined prompt.

## File Format

AGENTS.md files are standard Markdown with no required structure.
Common sections include:
- Project overview
- Build/test commands
- Code style guidelines
- Architecture notes

HTML comments (`<!-- ... -->`) are stripped before content is injected into the
system prompt. They can be used for authoring notes or machine-managed markers
without exposing them to the model.

## Properties

- `logger`
- `MEMORY_SYSTEM_PROMPT`

## Methods

- [`append_to_system_message()`](https://reference.langchain.com/python/deepagents/middleware/memory/append_to_system_message)

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/middleware/memory.py)
