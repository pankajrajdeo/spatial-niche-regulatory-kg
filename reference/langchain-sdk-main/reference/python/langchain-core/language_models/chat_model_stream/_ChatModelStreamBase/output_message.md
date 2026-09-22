---
title: "output_message"
description: "The assembled message if the stream has finished, else None."
source: "https://reference.langchain.com/python/langchain-core/language_models/chat_model_stream/_ChatModelStreamBase/output_message"
category: "reference"
tags: [reference, langchain-core, language_models, chat_model_stream, chatmodelstreambase, output_message]
---

# output_message

> **Attribute** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/language_models/chat_model_stream/_ChatModelStreamBase/output_message)

The assembled message if the stream has finished, else `None`.

Unlike `ChatModelStream.output` (which blocks until the stream
finishes), this never pumps, blocks, or raises. Intended for the
stream driver (`stream_events(version="v3")` and its async
equivalent) to check whether the stream produced a message before
firing `on_llm_end` callbacks.

## Signature

```python
output_message: AIMessage | None
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/language_models/chat_model_stream.py#L650)
