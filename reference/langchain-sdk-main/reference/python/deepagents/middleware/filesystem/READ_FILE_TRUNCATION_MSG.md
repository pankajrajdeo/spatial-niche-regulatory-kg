---
title: "READ_FILE_TRUNCATION_MSG"
description: "View source on GitHub"
source: "https://reference.langchain.com/python/deepagents/middleware/filesystem/READ_FILE_TRUNCATION_MSG"
category: "reference"
tags: [reference, deepagents, middleware, filesystem, read_file_truncation_msg]
---

# READ_FILE_TRUNCATION_MSG

> **Attribute** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/filesystem/READ_FILE_TRUNCATION_MSG)

## Signature

```python
READ_FILE_TRUNCATION_MSG = "\n\n[Output was truncated due to size limits. The file content is very large. Consider reformatting the file to make it easier to navigate. For example, if this is JSON, use execute(command='jq . {file_path}') to pretty-print it with line breaks. For other formats, you can use appropriate formatting tools to split long lines.]"
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/middleware/filesystem.py#L976)
