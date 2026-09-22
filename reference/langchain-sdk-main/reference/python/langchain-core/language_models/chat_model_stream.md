---
title: "chat_model_stream"
description: "Per-message streaming objects for content-block protocol events."
source: "https://reference.langchain.com/python/langchain-core/language_models/chat_model_stream"
category: "reference"
tags: [reference, langchain-core, language_models, chat_model_stream]
---

# chat_model_stream

> **Module** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/language_models/chat_model_stream)

Per-message streaming objects for content-block protocol events.

`ChatModelStream` is the synchronous variant returned by
`BaseChatModel.stream_events(version="v3")`.  `AsyncChatModelStream` is the
asynchronous variant returned by `BaseChatModel.astream_events(version="v3")`.

Both expose typed projection properties (`.text`, `.reasoning`,
`.tool_calls`, `.usage`, `.output`) that accumulate protocol
events as they arrive.  Projections can be iterated for deltas or
drained for the final accumulated value.

Raw protocol events are also available via direct iteration on the
stream object (replay-buffer semantics — multiple independent
consumers supported).

## Methods

- [`finalize_tool_call_chunk()`](https://reference.langchain.com/python/langchain-core/language_models/chat_model_stream/finalize_tool_call_chunk)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/language_models/chat_model_stream.py)
