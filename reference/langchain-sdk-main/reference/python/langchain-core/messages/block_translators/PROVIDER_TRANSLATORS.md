---
title: "PROVIDER_TRANSLATORS"
description: "Map model provider names to translator functions."
source: "https://reference.langchain.com/python/langchain-core/messages/block_translators/PROVIDER_TRANSLATORS"
category: "reference"
tags: [reference, langchain-core, messages, block_translators, provider_translators]
---

# PROVIDER_TRANSLATORS

> **Attribute** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/messages/block_translators/PROVIDER_TRANSLATORS)

Map model provider names to translator functions.

The dictionary maps provider names (e.g. `'openai'`, `'anthropic'`) to another
dictionary with two keys:
- `'translate_content'`: Function to translate `AIMessage` content.
- `'translate_content_chunk'`: Function to translate `AIMessageChunk` content.

When calling `content_blocks` on an `AIMessage` or `AIMessageChunk`, if
`model_provider` is set in `response_metadata`, the corresponding translator
functions will be used to parse the content into blocks. Otherwise, best-effort parsing
in `BaseMessage` will be used.

## Signature

```python
PROVIDER_TRANSLATORS: dict[str, dict[str, Callable[..., list[types.ContentBlock]]]] = {}
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/messages/block_translators/__init__.py#L24)
