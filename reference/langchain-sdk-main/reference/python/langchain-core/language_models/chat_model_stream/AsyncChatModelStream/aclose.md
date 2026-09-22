---
title: "aclose"
description: "Cancel the background producer task and release resources."
source: "https://reference.langchain.com/python/langchain-core/language_models/chat_model_stream/AsyncChatModelStream/aclose"
category: "reference"
tags: [reference, langchain-core, language_models, chat_model_stream, asyncchatmodelstream, aclose]
---

# aclose

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/language_models/chat_model_stream/AsyncChatModelStream/aclose)

Cancel the background producer task and release resources.

If a consumer cancels mid-stream or decides to stop iterating
early, the producer task keeps pumping the provider HTTP call to
completion because `asyncio.Task` has no implicit link to its
awaiter. Call this method to cancel the producer explicitly; the
stream transitions to an errored state with `CancelledError`.

If the stream has already produced a message successfully (for
example, after `await stream.output`), the producer may still be
running post-stream work such as `on_llm_end` callbacks. In that
case `aclose()` awaits the task rather than cancelling it —
turning a successful run into a cancelled one would drop the
end callback and corrupt tracing.

Idempotent: safe to call multiple times, including after the
stream has finished normally. Also invoked by the async context
manager protocol on `__aexit__`.

## Signature

```python
aclose(
    self,
) -> None
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/language_models/chat_model_stream.py#L1413)
