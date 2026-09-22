---
title: "DEFAULT_TOOL_DESCRIPTION"
description: "View source on GitHub"
source: "https://reference.langchain.com/python/langchain/agents/middleware/shell_tool/DEFAULT_TOOL_DESCRIPTION"
category: "reference"
tags: [reference, langchain, agents, middleware, shell_tool, default_tool_description]
---

# DEFAULT_TOOL_DESCRIPTION

> **Attribute** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/shell_tool/DEFAULT_TOOL_DESCRIPTION)

## Signature

```python
DEFAULT_TOOL_DESCRIPTION = 'Execute a shell command inside a persistent session. Before running a command, confirm the working directory is correct (e.g., inspect with `ls` or `pwd`) and ensure any parent directories exist. Prefer absolute paths and quote paths containing spaces, such as `cd "/path/with spaces"`. Chain multiple commands with `&&` or `;` instead of embedding newlines. Avoid unnecessary `cd` usage unless explicitly required so the session remains stable. Outputs may be truncated when they become very large, and long running commands will be terminated once their configured timeout elapses.'
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a18de590e7ccf5c647fbf3d689e5f1a15f78e9f5/libs/langchain_v1/langchain/agents/middleware/shell_tool.py#L59)
