---
title: "set_request_more"
description: "Set the pull callback on this stream and all its projections."
source: "https://reference.langchain.com/python/langchain-core/language_models/chat_model_stream/ChatModelStream/set_request_more"
category: "reference"
tags: [reference, langchain-core, language_models, chat_model_stream, chatmodelstream, set_request_more]
---

# set_request_more

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/language_models/chat_model_stream/ChatModelStream/set_request_more)

Set the pull callback on this stream and all its projections.

Used by langgraph's `GraphRunStream._wire_request_more` to
connect the shared graph pump.

## Signature

```python
set_request_more(
    self,
    cb: Callable[[], bool],
) -> None
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/language_models/chat_model_stream.py#L1194)
