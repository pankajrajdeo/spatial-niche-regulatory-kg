---
title: "achunks_to_events"
description: "Async variant of chunks_to_events."
source: "https://reference.langchain.com/python/langchain-core/language_models/_compat_bridge/achunks_to_events"
category: "reference"
tags: [reference, langchain-core, language_models, compat_bridge, achunks_to_events]
---

# achunks_to_events

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/language_models/_compat_bridge/achunks_to_events)

Async variant of `chunks_to_events`.

## Signature

```python
achunks_to_events(
    chunks: AsyncIterator[ChatGenerationChunk],
    *,
    message_id: str | None = None,
) -> AsyncIterator[MessagesData]
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/language_models/_compat_bridge.py#L696)
