---
title: "metadata"
description: "Optional metadata associated with the tool."
source: "https://reference.langchain.com/python/langchain-core/tools/base/BaseTool/metadata"
category: "reference"
tags: [reference, langchain-core, tools, base, basetool, metadata]
---

# metadata

> **Attribute** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/tools/base/BaseTool/metadata)

Optional metadata associated with the tool.

This metadata will be associated with each call to this tool,
and passed as arguments to the handlers defined in `callbacks`.

You can use these to, e.g., identify a specific instance of a tool with its usecase.

## Signature

```python
metadata: dict[str, Any] | None = None
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/tools/base.py#L518)
