---
title: "set_arequest_more"
description: "Wire the async pull callback iterators use to drive the source."
source: "https://reference.langchain.com/python/langchain-core/language_models/chat_model_stream/AsyncProjection/set_arequest_more"
category: "reference"
tags: [reference, langchain-core, language_models, chat_model_stream, asyncprojection, set_arequest_more]
---

# set_arequest_more

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/language_models/chat_model_stream/AsyncProjection/set_arequest_more)

Wire the async pull callback iterators use to drive the source.

Mirrors `SyncProjection.set_request_more`. Under caller-driven
streaming, consumers call this callback when their buffer is
empty so that the owning graph advances one step.

## Signature

```python
set_arequest_more(
    self,
    cb: Callable[[], Awaitable[bool]] | None,
) -> None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `cb` | `Callable[[], Awaitable[bool]] \| None` | Yes | Async no-arg callable returning `True` when a new event was produced, `False` when the source is exhausted. Pass `None` to unwire. |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/language_models/chat_model_stream.py#L371)
