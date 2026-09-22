---
title: "sanitize_tool_call_id"
description: "Sanitize tool_call_id to prevent path traversal and separator issues."
source: "https://reference.langchain.com/python/deepagents/backends/utils/sanitize_tool_call_id"
category: "reference"
tags: [reference, deepagents, backends, utils, sanitize_tool_call_id]
---

# sanitize_tool_call_id

> **Function** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/utils/sanitize_tool_call_id)

Sanitize tool_call_id to prevent path traversal and separator issues.

Replaces dangerous characters (., /, \) with underscores.

## Signature

```python
sanitize_tool_call_id(
    tool_call_id: str,
) -> str
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/backends/utils.py#L201)
