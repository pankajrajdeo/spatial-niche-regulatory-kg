---
title: "OnFailure"
description: "Type Alias in langchain"
source: "https://reference.langchain.com/python/langchain/agents/middleware/_retry/OnFailure"
category: "reference"
tags: [reference, langchain, agents, middleware, retry, onfailure]
---

# OnFailure

> **Type Alias** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/_retry/OnFailure)

Type for specifying failure handling behavior.

Can be either:
- A literal action string (`'error'` or `'continue'`)
    - `'error'`: Re-raise the exception, stopping agent execution.
    - `'continue'`: Inject a message with the error details, allowing the agent to continue.

        For tool retries, a `ToolMessage` with the error details will be injected.

        For model retries, an `AIMessage` with the error details will be returned.
- A callable that takes an exception and returns a string for error message content

## Signature

```python
OnFailure = Literal['error', 'continue'] | Callable[[Exception], str]
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a18de590e7ccf5c647fbf3d689e5f1a15f78e9f5/libs/langchain_v1/langchain/agents/middleware/_retry.py#L24)
