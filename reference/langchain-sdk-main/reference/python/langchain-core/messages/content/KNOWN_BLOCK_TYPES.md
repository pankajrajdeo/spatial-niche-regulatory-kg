---
title: "KNOWN_BLOCK_TYPES"
description: "These are block types known to langchain-core >= 1.0.0."
source: "https://reference.langchain.com/python/langchain-core/messages/content/KNOWN_BLOCK_TYPES"
category: "reference"
tags: [reference, langchain-core, messages, content, known_block_types]
---

# KNOWN_BLOCK_TYPES

> **Attribute** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/messages/content/KNOWN_BLOCK_TYPES)

These are block types known to `langchain-core >= 1.0.0`.

If a block has a type not in this set, it is considered to be provider-specific.

## Signature

```python
KNOWN_BLOCK_TYPES = {'text', 'reasoning', 'tool_call', 'invalid_tool_call', 'tool_call_chunk', 'image', 'audio', 'file', 'text-plain', 'video', 'server_tool_call', 'server_tool_call_chunk', 'server_tool_result', 'non_standard'}
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/messages/content.py#L856)
