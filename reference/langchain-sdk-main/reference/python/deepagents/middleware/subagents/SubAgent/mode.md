---
title: "mode"
description: "Context mode. Defaults to isolated, where the subagent only sees the delegated task."
source: "https://reference.langchain.com/python/deepagents/middleware/subagents/SubAgent/mode"
category: "reference"
tags: [reference, deepagents, middleware, subagents, subagent, mode]
---

# mode

> **Attribute** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/subagents/SubAgent/mode)

Context mode. Defaults to `isolated`, where the subagent only sees the delegated task.

Under `fork`, the subagent receives the parent's effective conversation
history and state, and mirrors the parent's prompt-producing middleware so
it rebuilds the same system prompt. It cannot define `skills`, which would
diverge from the parent's. `tools` isn't restricted the same way -- a fork's
own tools work normally; the tradeoff is cache misses.

## Signature

```python
mode: NotRequired[Literal['isolated', 'fork']]
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/middleware/subagents.py#L209)
