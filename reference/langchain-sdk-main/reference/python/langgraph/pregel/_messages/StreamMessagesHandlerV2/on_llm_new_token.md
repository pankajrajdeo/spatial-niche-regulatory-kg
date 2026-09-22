---
title: "on_llm_new_token"
description: "Intentional no-op — v1 chunks are not used on v2-flagged runs."
source: "https://reference.langchain.com/python/langgraph/pregel/_messages/StreamMessagesHandlerV2/on_llm_new_token"
category: "reference"
tags: [reference, langgraph, pregel, messages, streammessageshandlerv2, on_llm_new_token]
---

# on_llm_new_token

> **Method** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/pregel/_messages/StreamMessagesHandlerV2/on_llm_new_token)

Intentional no-op — v1 chunks are not used on v2-flagged runs.

The v2 marker already steers `invoke` to the event generator, so
`on_llm_new_token` should not fire under normal routing. This
override stays a pass-through (no call to `super()`) to make
the intent explicit and to guard against any caller (e.g. a
node that calls `model.stream()` directly, which still fires
the v1 callback) leaking AIMessageChunks onto a v2-flagged
messages stream.

## Signature

```python
on_llm_new_token(
    self,
    token: str,
    *,
    chunk: ChatGenerationChunk | None = None,
    run_id: UUID,
    parent_run_id: UUID | None = None,
    tags: list[str] | None = None,
    **kwargs: Any = {},
) -> Any
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/644815f9e5bc52ad8f7a5227a456227e9c3e639b/libs/langgraph/langgraph/pregel/_messages.py#L275)
