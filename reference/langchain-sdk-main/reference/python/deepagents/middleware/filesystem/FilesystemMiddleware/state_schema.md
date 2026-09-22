---
title: "state_schema"
description: "View source on GitHub"
source: "https://reference.langchain.com/python/deepagents/middleware/filesystem/FilesystemMiddleware/state_schema"
category: "reference"
tags: [reference, deepagents, middleware, filesystem, filesystemmiddleware, state_schema]
---

# state_schema

> **Attribute** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/filesystem/FilesystemMiddleware/state_schema)

## Signature

```python
state_schema: type[FilesystemState] = cast('type[FilesystemState]', FilesystemState if _uses_state_backend(self.backend) else AgentState)
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/middleware/filesystem.py#L1817)
