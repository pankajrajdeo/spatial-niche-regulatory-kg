---
title: "StreamMessagesHandlerV2"
description: "v2 variant of StreamMessagesHandler."
source: "https://reference.langchain.com/python/langgraph/pregel/_messages/StreamMessagesHandlerV2"
category: "reference"
tags: [reference, langgraph, pregel, messages, streammessageshandlerv2]
---

# StreamMessagesHandlerV2

> **Class** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/pregel/_messages/StreamMessagesHandlerV2)

v2 variant of `StreamMessagesHandler`.

Declaring `_V2StreamingCallbackHandler` as a base flips
`BaseChatModel.invoke` to route through `_stream_chat_model_events`
(firing `on_stream_event`) instead of `_stream` (firing
`on_llm_new_token`). Inherits `on_stream_event` from the parent,
which forwards protocol events onto the messages stream channel.

Pregel attaches this class instead of the v1 handler only when
`StreamingHandler` opts in via the internal
`CONFIG_KEY_STREAM_MESSAGES_V2` config key; direct
`graph.stream(stream_mode="messages")` callers keep the v1
AIMessageChunk shape.

## Signature

```python
StreamMessagesHandlerV2(
    self,
    stream: Callable[[StreamChunk], None],
    subgraphs: bool,
    *,
    parent_ns: tuple[str, ...] | None = None,
)
```

## Extends

- `StreamMessagesHandler`
- `_V2StreamingCallbackHandler`

## Constructors

```python
__init__(
    self,
    stream: Callable[[StreamChunk], None],
    subgraphs: bool,
    *,
    parent_ns: tuple[str, ...] | None = None,
) -> None
```

| Name | Type |
|------|------|
| `stream` | `Callable[[StreamChunk], None]` |
| `subgraphs` | `bool` |
| `parent_ns` | `tuple[str, ...] \| None` |

## Methods

- [`on_llm_new_token()`](https://reference.langchain.com/python/langgraph/pregel/_messages/StreamMessagesHandlerV2/on_llm_new_token)
- [`on_llm_end()`](https://reference.langchain.com/python/langgraph/pregel/_messages/StreamMessagesHandlerV2/on_llm_end)
- [`on_llm_error()`](https://reference.langchain.com/python/langgraph/pregel/_messages/StreamMessagesHandlerV2/on_llm_error)
- [`on_stream_event()`](https://reference.langchain.com/python/langgraph/pregel/_messages/StreamMessagesHandlerV2/on_stream_event)

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/644815f9e5bc52ad8f7a5227a456227e9c3e639b/libs/langgraph/langgraph/pregel/_messages.py#L259)
