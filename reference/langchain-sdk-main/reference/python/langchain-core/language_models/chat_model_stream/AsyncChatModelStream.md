---
title: "AsyncChatModelStream"
description: "Asynchronous per-message streaming object for a single LLM response."
source: "https://reference.langchain.com/python/langchain-core/language_models/chat_model_stream/AsyncChatModelStream"
category: "reference"
tags: [reference, langchain-core, language_models, chat_model_stream, asyncchatmodelstream]
---

# AsyncChatModelStream

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/language_models/chat_model_stream/AsyncChatModelStream)

Asynchronous per-message streaming object for a single LLM response.

Returned by `BaseChatModel.astream_events(version="v3")`.  Content-block events
are fed into this object by a background producer task.

Projections:

- `.text` — async iterable of text deltas; awaitable for full text
- `.reasoning` — async iterable of reasoning deltas; awaitable
- `.tool_calls` — async iterable of `ToolCallChunk` deltas;
  awaitable for `list[ToolCall]`
- `.output` — awaitable for assembled `AIMessage`

Usage info is available on `.output.usage_metadata` once the stream
has finished.

!!! note "Output shape is always v1 content blocks"

    The assembled message's content is always a list of v1
    protocol blocks, regardless of the model's `output_version`
    setting — see `ChatModelStream` for the full rationale.

The stream itself is awaitable (`msg = await stream`) and
async-iterable (`async for event in stream`).

## Signature

```python
AsyncChatModelStream(
    self,
    *,
    namespace: list[str] | None = None,
    node: str | None = None,
    message_id: str | None = None,
)
```

## Extends

- `_ChatModelStreamBase`

## Constructors

```python
__init__(
    self,
    *,
    namespace: list[str] | None = None,
    node: str | None = None,
    message_id: str | None = None,
) -> None
```

| Name | Type |
|------|------|
| `namespace` | `list[str] \| None` |
| `node` | `str \| None` |
| `message_id` | `str \| None` |

## Properties

- `text`
- `reasoning`
- `tool_calls`
- `output`

## Methods

- [`set_arequest_more()`](https://reference.langchain.com/python/langchain-core/language_models/chat_model_stream/AsyncChatModelStream/set_arequest_more)
- [`set_start()`](https://reference.langchain.com/python/langchain-core/language_models/chat_model_stream/AsyncChatModelStream/set_start)
- [`aclose()`](https://reference.langchain.com/python/langchain-core/language_models/chat_model_stream/AsyncChatModelStream/aclose)
- [`fail()`](https://reference.langchain.com/python/langchain-core/language_models/chat_model_stream/AsyncChatModelStream/fail)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/language_models/chat_model_stream.py#L1281)
