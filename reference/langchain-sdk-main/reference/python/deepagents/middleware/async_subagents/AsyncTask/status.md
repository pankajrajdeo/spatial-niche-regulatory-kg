---
title: "status"
description: "Current task status (e.g., 'running', 'success', 'error', 'cancelled')."
source: "https://reference.langchain.com/python/deepagents/middleware/async_subagents/AsyncTask/status"
category: "reference"
tags: [reference, deepagents, middleware, async_subagents, asynctask, status]
---

# status

> **Attribute** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/async_subagents/AsyncTask/status)

Current task status (e.g., `'running'`, `'success'`, `'error'`, `'cancelled'`).

Typed as `str` rather than a `Literal` because the LangGraph SDK's
`Run.status` is `str` — using a `Literal` here would require `cast` at every
SDK boundary.

## Signature

```python
status: str
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/middleware/async_subagents.py#L95)
