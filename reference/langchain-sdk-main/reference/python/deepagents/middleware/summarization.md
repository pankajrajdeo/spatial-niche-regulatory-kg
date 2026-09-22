---
title: "summarization"
description: "Summarization middleware for automatic and tool-based conversation compaction."
source: "https://reference.langchain.com/python/deepagents/middleware/summarization"
category: "reference"
tags: [reference, deepagents, middleware, summarization]
---

# summarization

> **Module** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/summarization)

Summarization middleware for automatic and tool-based conversation compaction.

This module provides two middleware classes and a convenience factory:

- `SummarizationMiddleware` — automatically compacts the conversation when token
    usage exceeds a configurable threshold.

    Older messages are summarized via an LLM call and the full history is
    offloaded to a backend for later retrieval.
- `SummarizationToolMiddleware` — exposes a `compact_conversation` tool that
    lets the agent (or a human-in-the-loop approval flow) trigger compaction on
    demand.

    Composes with a `SummarizationMiddleware` instance and reuses its
    summarization engine.
- `create_summarization_tool_middleware` — convenience factory that creates both
    middleware layers with model-aware defaults.

## Usage

```python
from deepagents import create_deep_agent
from deepagents.middleware.summarization import (
    SummarizationMiddleware,
    SummarizationToolMiddleware,
)
from deepagents.backends import FilesystemBackend

backend = FilesystemBackend(root_dir="/data")

summ = SummarizationMiddleware(
    model="gpt-5.5",
    backend=backend,
    trigger=("fraction", 0.85),
    keep=("fraction", 0.10),
)
tool_mw = SummarizationToolMiddleware(summ)

agent = create_deep_agent(middleware=[summ, tool_mw])
```

## Storage

Offloaded messages are stored as markdown at `/conversation_history/{session_id}.md`,
where `session_id` is an internally generated per-invocation id.

Each summarization event appends a new section to this file, creating a running
log of all evicted messages. Base64 media in evicted messages is written
separately under `<artifacts_root>/conversation_history/media/` and referenced
by path from the markdown, so the history file stays text-only (see
`_offload_inline_media` for the exact path).

## Summary prompt

`DEEPAGENTS_DEFAULT_SUMMARY_PROMPT` augments LangChain's `DEFAULT_SUMMARY_PROMPT`
with a deepagents-specific addendum explaining the media reference tags that the
offloading behavior introduces, so the summarizing model knows to preserve them.
It is the default `summary_prompt` for `SummarizationMiddleware` and both
factories.

## Properties

- `DEEPAGENTS_DEFAULT_SUMMARY_PROMPT`
- `logger`
- `SUMMARIZATION_EVENT_KEY`
- `SUMMARIZATION_SESSION_ID_KEY`
- `SummarizationMiddleware`

## Methods

- [`append_to_system_message()`](https://reference.langchain.com/python/deepagents/middleware/summarization/append_to_system_message)
- [`compute_summarization_defaults()`](https://reference.langchain.com/python/deepagents/middleware/summarization/compute_summarization_defaults)
- [`create_summarization_middleware()`](https://reference.langchain.com/python/deepagents/middleware/summarization/create_summarization_middleware)
- [`create_summarization_tool_middleware()`](https://reference.langchain.com/python/deepagents/middleware/summarization/create_summarization_tool_middleware)

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/middleware/summarization.py)
