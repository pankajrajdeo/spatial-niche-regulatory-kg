---
title: "BaseMessageChunk"
description: "Message chunk, which can be concatenated with other Message chunks."
source: "https://reference.langchain.com/python/langchain-core/messages/base/BaseMessageChunk"
category: "reference"
tags: [reference, langchain-core, messages, base, basemessagechunk]
---

# BaseMessageChunk

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/messages/base/BaseMessageChunk)

Message chunk, which can be concatenated with other Message chunks.

## Signature

```python
BaseMessageChunk(
    self,
    content: str | list[str | dict[Any, Any]] | None = None,
    content_blocks: list[types.ContentBlock] | None = None,
    **kwargs: Any = {},
)
```

## Extends

- `BaseMessage`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/messages/base.py#L409)
