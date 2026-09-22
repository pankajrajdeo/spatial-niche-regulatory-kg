---
title: "DELETE_TOOL_DESCRIPTION"
description: "View source on GitHub"
source: "https://reference.langchain.com/python/deepagents/middleware/filesystem/DELETE_TOOL_DESCRIPTION"
category: "reference"
tags: [reference, deepagents, middleware, filesystem, delete_tool_description]
---

# DELETE_TOOL_DESCRIPTION

> **Attribute** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/filesystem/DELETE_TOOL_DESCRIPTION)

## Signature

```python
DELETE_TOOL_DESCRIPTION = 'Deletes a file or directory from the filesystem.\n\nUsage:\n- Permanently removes the file or directory at the given absolute path.\n- Deleting a directory removes it and everything inside it, recursively. Prefer\n  deleting a directory in one call over deleting each file individually.\n- This cannot be undone, so only delete paths you are sure are no longer needed.\n'
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/middleware/filesystem.py#L1403)
