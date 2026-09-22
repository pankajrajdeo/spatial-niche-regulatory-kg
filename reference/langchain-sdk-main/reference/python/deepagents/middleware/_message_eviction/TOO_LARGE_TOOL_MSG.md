---
title: "TOO_LARGE_TOOL_MSG"
description: "View source on GitHub"
source: "https://reference.langchain.com/python/deepagents/middleware/_message_eviction/TOO_LARGE_TOOL_MSG"
category: "reference"
tags: [reference, deepagents, middleware, message_eviction, too_large_tool_msg]
---

# TOO_LARGE_TOOL_MSG

> **Attribute** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/_message_eviction/TOO_LARGE_TOOL_MSG)

## Signature

```python
TOO_LARGE_TOOL_MSG = 'Tool result too large, the result of this tool call {tool_call_id} was saved in the filesystem at this path: {file_path}\n\nYou can read the result from the filesystem by using the read_file tool, but make sure to only read part of the result at a time.\n\nYou can do this by specifying an offset and limit in the read_file tool call. For example, to read the first 100 lines, you can use the read_file tool with offset=0 and limit=100.\n\nHere is a preview showing the head and tail of the result (lines of the form `... [N lines truncated] ...` indicate omitted lines in the middle of the content):\n\n{content_sample}\n'
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/middleware/_message_eviction.py#L26)
