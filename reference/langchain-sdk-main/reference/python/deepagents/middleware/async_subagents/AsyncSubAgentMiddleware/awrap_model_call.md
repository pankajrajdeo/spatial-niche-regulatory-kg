---
title: "awrap_model_call"
description: "(async) Update the system message to include async subagent instructions."
source: "https://reference.langchain.com/python/deepagents/middleware/async_subagents/AsyncSubAgentMiddleware/awrap_model_call"
category: "reference"
tags: [reference, deepagents, middleware, async_subagents, asyncsubagentmiddleware, awrap_model_call]
---

# awrap_model_call

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/async_subagents/AsyncSubAgentMiddleware/awrap_model_call)

(async) Update the system message to include async subagent instructions.

## Signature

```python
awrap_model_call(
    self,
    request: ModelRequest[ContextT],
    handler: Callable[[ModelRequest[ContextT]], Awaitable[ModelResponse[ResponseT]]],
) -> ModelResponse[ResponseT]
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/middleware/async_subagents.py#L922)
