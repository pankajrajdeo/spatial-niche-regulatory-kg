---
title: "translate_content_chunk"
description: "Derive standard content blocks from a message chunk with groq content."
source: "https://reference.langchain.com/python/langchain-core/messages/block_translators/groq/translate_content_chunk"
category: "reference"
tags: [reference, langchain-core, messages, block_translators, groq, translate_content_chunk]
---

# translate_content_chunk

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/messages/block_translators/groq/translate_content_chunk)

Derive standard content blocks from a message chunk with groq content.

## Signature

```python
translate_content_chunk(
    message: AIMessageChunk,
) -> list[types.ContentBlock]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `message` | `AIMessageChunk` | Yes | The message chunk to translate. |

## Returns

`list[types.ContentBlock]`

The derived content blocks.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/messages/block_translators/groq.py#L133)
