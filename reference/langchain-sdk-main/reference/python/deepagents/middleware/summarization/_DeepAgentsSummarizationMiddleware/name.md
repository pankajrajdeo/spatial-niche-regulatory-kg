---
title: "name"
description: "Report the public SummarizationMiddleware alias for string-form exclusion."
source: "https://reference.langchain.com/python/deepagents/middleware/summarization/_DeepAgentsSummarizationMiddleware/name"
category: "reference"
tags: [reference, deepagents, middleware, summarization, deepagentssummarizationmiddleware, name]
---

# name

> **Attribute** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/summarization/_DeepAgentsSummarizationMiddleware/name)

Report the public `SummarizationMiddleware` alias for string-form exclusion.

The impl class is private (`_DeepAgentsSummarizationMiddleware`) but
ships under the public `SummarizationMiddleware` name, so
`excluded_middleware={"SummarizationMiddleware"}` targets this class.
Subclasses fall back to `type(self).__name__` so user-authored
extensions don't silently inherit the alias.

## Signature

```python
name: str
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/middleware/summarization.py#L534)
