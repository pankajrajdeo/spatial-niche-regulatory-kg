---
title: "ChatModelStream"
description: "Synchronous per-message streaming object for a single LLM response."
source: "https://reference.langchain.com/python/langchain-core/language_models/chat_model_stream/ChatModelStream"
category: "reference"
tags: [reference, langchain-core, language_models, chat_model_stream, chatmodelstream]
---

# ChatModelStream

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/language_models/chat_model_stream/ChatModelStream)

Synchronous per-message streaming object for a single LLM response.

Returned by `BaseChatModel.stream_events(version="v3")`.  Content-block protocol
events are fed into this object and accumulated into typed projections.

Projections (always return the same cached object):

- `.text` — iterable of `str` deltas; `str()` for full text
- `.reasoning` — same as `.text` for reasoning content
- `.tool_calls` — iterable of `ToolCallChunk` deltas;
  `.get()` returns `list[ToolCall]`
- `.output` — blocking property, returns assembled `AIMessage`

Usage info is available on `.output.usage_metadata` once the stream
has finished.

!!! note "Output shape is always v1 content blocks"

    `.output.content` is always a list of v1 protocol blocks
    (text, reasoning, tool_call, image, …), regardless of the
    underlying model's `output_version` setting. That attribute
    only controls the legacy `stream()` / `astream()` / `invoke()`
    paths; `ChatModelStream` is built on the content-block
    protocol and emits v1 shapes by construction.

Raw event iteration::

    for event in stream:
        print(event)  # MessagesData dicts

## Signature

```python
ChatModelStream(
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

- [`bind_pump()`](https://reference.langchain.com/python/langchain-core/language_models/chat_model_stream/ChatModelStream/bind_pump)
- [`set_start()`](https://reference.langchain.com/python/langchain-core/language_models/chat_model_stream/ChatModelStream/set_start)
- [`set_request_more()`](https://reference.langchain.com/python/langchain-core/language_models/chat_model_stream/ChatModelStream/set_request_more)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/language_models/chat_model_stream.py#L1125)
