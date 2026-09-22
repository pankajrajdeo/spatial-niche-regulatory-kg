---
title: "extras"
description: "Optional provider-specific extra fields for the tool."
source: "https://reference.langchain.com/python/langchain-core/tools/base/BaseTool/extras"
category: "reference"
tags: [reference, langchain-core, tools, base, basetool, extras]
---

# extras

> **Attribute** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/tools/base/BaseTool/extras)

Optional provider-specific extra fields for the tool.

This is used to pass provider-specific configuration that doesn't fit into
standard tool fields.

## Signature

```python
extras: dict[str, Any] | None = None
```

## Description

**Example:**

Anthropic-specific fields like [`cache_control`](../../../../../../integrations/chat/anthropic.md#prompt-caching),
[`defer_loading`](../../../../../../integrations/chat/anthropic.md#tool-search),
or `input_examples`.

```python
@tool(extras={"defer_loading": True, "cache_control": {"type": "ephemeral"}})
def my_tool(x: str) -> str:
    return x
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/tools/base.py#L555)
