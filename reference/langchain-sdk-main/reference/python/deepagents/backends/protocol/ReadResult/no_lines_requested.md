---
title: "no_lines_requested"
description: "The read asked for zero lines and the file was never inspected."
source: "https://reference.langchain.com/python/deepagents/backends/protocol/ReadResult/no_lines_requested"
category: "reference"
tags: [reference, deepagents, backends, protocol, readresult, no_lines_requested]
---

# no_lines_requested

> **Attribute** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/protocol/ReadResult/no_lines_requested)

The read asked for zero lines and the file was never inspected.

Set by backends when a non-positive `limit` short-circuits the read, so
the middleware can tell a never-inspected window apart from a file that
was inspected and is genuinely empty — both otherwise arrive as empty
content with no pagination metadata.

## Signature

```python
no_lines_requested: bool = False
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/backends/protocol.py#L225)
