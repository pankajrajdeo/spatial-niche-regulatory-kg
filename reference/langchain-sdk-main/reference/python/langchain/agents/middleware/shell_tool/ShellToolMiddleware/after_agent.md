---
title: "after_agent"
description: "Run shutdown commands and release resources when an agent completes."
source: "https://reference.langchain.com/python/langchain/agents/middleware/shell_tool/ShellToolMiddleware/after_agent"
category: "reference"
tags: [reference, langchain, agents, middleware, shell_tool, shelltoolmiddleware, after_agent]
---

# after_agent

> **Method** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/shell_tool/ShellToolMiddleware/after_agent)

Run shutdown commands and release resources when an agent completes.

## Signature

```python
after_agent(
    self,
    state: ShellToolState[ResponseT],
    runtime: Runtime[ContextT],
) -> None
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a18de590e7ccf5c647fbf3d689e5f1a15f78e9f5/libs/langchain_v1/langchain/agents/middleware/shell_tool.py#L686)
