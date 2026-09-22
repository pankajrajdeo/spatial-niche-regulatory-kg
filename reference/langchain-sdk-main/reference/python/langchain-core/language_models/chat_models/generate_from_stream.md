---
title: "generate_from_stream"
description: "Generate from a stream."
source: "https://reference.langchain.com/python/langchain-core/language_models/chat_models/generate_from_stream"
category: "reference"
tags: [reference, langchain-core, language_models, chat_models, generate_from_stream]
---

# generate_from_stream

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/language_models/chat_models/generate_from_stream)

Generate from a stream.

## Signature

```python
generate_from_stream(
    stream: Iterator[ChatGenerationChunk],
) -> ChatResult
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `stream` | `Iterator[ChatGenerationChunk]` | Yes | Iterator of `ChatGenerationChunk`. |

## Returns

`ChatResult`

Chat result.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/language_models/chat_models.py#L218)
