---
title: "set_start"
description: "Install a lazy-start callback invoked on first consumption."
source: "https://reference.langchain.com/python/langchain-core/language_models/chat_model_stream/AsyncProjection/set_start"
category: "reference"
tags: [reference, langchain-core, language_models, chat_model_stream, asyncprojection, set_start]
---

# set_start

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/language_models/chat_model_stream/AsyncProjection/set_start)

Install a lazy-start callback invoked on first consumption.

## Signature

```python
set_start(
    self,
    cb: Callable[[], Awaitable[None]] | None,
) -> None
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/language_models/chat_model_stream.py#L367)
