---
title: "translate_content"
description: "Derive standard content blocks from a message with groq content."
source: "https://reference.langchain.com/python/langchain-core/messages/block_translators/groq/translate_content"
category: "reference"
tags: [reference, langchain-core, messages, block_translators, groq, translate_content]
---

# translate_content

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/messages/block_translators/groq/translate_content)

Derive standard content blocks from a message with groq content.

## Signature

```python
translate_content(
    message: AIMessage,
) -> list[types.ContentBlock]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `message` | `AIMessage` | Yes | The message to translate. |

## Returns

`list[types.ContentBlock]`

The derived content blocks.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/messages/block_translators/groq.py#L121)
