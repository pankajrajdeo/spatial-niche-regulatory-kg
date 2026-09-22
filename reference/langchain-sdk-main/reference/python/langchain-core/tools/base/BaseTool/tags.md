---
title: "tags"
description: "Optional list of tags associated with the tool."
source: "https://reference.langchain.com/python/langchain-core/tools/base/BaseTool/tags"
category: "reference"
tags: [reference, langchain-core, tools, base, basetool, tags]
---

# tags

> **Attribute** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/tools/base/BaseTool/tags)

Optional list of tags associated with the tool.

These tags will be associated with each call to this tool,
and passed as arguments to the handlers defined in `callbacks`.

You can use these to, e.g., identify a specific instance of a tool with its use
case.

## Signature

```python
tags: list[str] | None = None
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/tools/base.py#L508)
