---
title: "chunks_to_events"
description: "Convert a stream of ChatGenerationChunk to protocol events."
source: "https://reference.langchain.com/python/langchain-core/language_models/_compat_bridge/chunks_to_events"
category: "reference"
tags: [reference, langchain-core, language_models, compat_bridge, chunks_to_events]
---

# chunks_to_events

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/language_models/_compat_bridge/chunks_to_events)

Convert a stream of `ChatGenerationChunk` to protocol events.

Blocks are tracked independently by source-side identifier. Providers
such as Anthropic can interleave parallel tool-call chunks by index, so
each first-seen block gets a `content-block-start`, deltas keep their
stable wire index, and all open blocks are finalized at message end.
Source-side identifiers (from the block's `index` field, which may be
int or string) are translated to sequential `uint` wire indices.

## Signature

```python
chunks_to_events(
    chunks: Iterator[ChatGenerationChunk],
    *,
    message_id: str | None = None,
) -> Iterator[MessagesData]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `chunks` | `Iterator[ChatGenerationChunk]` | Yes | Iterator of `ChatGenerationChunk` from `_stream()`. |
| `message_id` | `str \| None` | No | Optional stable message ID. (default: `None`) |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/language_models/_compat_bridge.py#L590)
