---
title: "SyncProjection"
description: "Sync iterable of deltas with pull-based backpressure."
source: "https://reference.langchain.com/python/langchain-core/language_models/chat_model_stream/SyncProjection"
category: "reference"
tags: [reference, langchain-core, language_models, chat_model_stream, syncprojection]
---

# SyncProjection

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/language_models/chat_model_stream/SyncProjection)

Sync iterable of deltas with pull-based backpressure.

Follows the same `_request_more` convention as langgraph's
`EventLog`: when the cursor catches up to the buffer and the
projection is not done, it calls `_request_more()` to pull more
events from the producer.

Each call to `__iter__` creates a new cursor at position 0.
Multiple iterators replay all deltas from the start.

## Signature

```python
SyncProjection(
    self,
)
```

## Extends

- `_ProjectionBase`

## Constructors

```python
__init__(
    self,
) -> None
```

## Methods

- [`set_start()`](https://reference.langchain.com/python/langchain-core/language_models/chat_model_stream/SyncProjection/set_start)
- [`set_request_more()`](https://reference.langchain.com/python/langchain-core/language_models/chat_model_stream/SyncProjection/set_request_more)
- [`get()`](https://reference.langchain.com/python/langchain-core/language_models/chat_model_stream/SyncProjection/get)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/language_models/chat_model_stream.py#L218)
