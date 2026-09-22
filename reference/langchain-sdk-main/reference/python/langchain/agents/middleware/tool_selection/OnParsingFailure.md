---
title: "OnParsingFailure"
description: "Type Alias in langchain"
source: "https://reference.langchain.com/python/langchain/agents/middleware/tool_selection/OnParsingFailure"
category: "reference"
tags: [reference, langchain, agents, middleware, tool_selection, onparsingfailure]
---

# OnParsingFailure

> **Type Alias** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/tool_selection/OnParsingFailure)

Behavior when the selection model keeps returning a malformed response.

Can be either:
- `'error'`: Raise a `ValueError` (the default).
- `'none'`: Select no tools.
- `'all'`: Select every available tool.
- A `list[str]` of tool names to fall back to.
- A callable that takes the last (malformed) response and returns tool names to use.

## Signature

```python
OnParsingFailure = Literal['error', 'none', 'all'] | list[str] | Callable[[Any], list[str]]
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a18de590e7ccf5c647fbf3d689e5f1a15f78e9f5/libs/langchain_v1/langchain/agents/middleware/tool_selection.py#L42)
