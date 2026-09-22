---
title: "stream_events"
description: "Stream events from this chat model."
source: "https://reference.langchain.com/python/langchain-core/language_models/chat_models/BaseChatModel/stream_events"
category: "reference"
tags: [reference, langchain-core, language_models, chat_models, basechatmodel, stream_events]
---

# stream_events

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/language_models/chat_models/BaseChatModel/stream_events)

Stream events from this chat model.

For `version="v1"` / `"v2"`, yields `StreamEvent` dicts (see
`Runnable.stream_events`). For `version="v3"`, returns a
`ChatModelStream` exposing typed projections (`.text`,
`.reasoning`, `.tool_calls`, `.output`).

!!! warning "Beta"

    `version="v3"` is in beta. The protocol shape, return type,
    and surface area may change in future releases. Calling it
    emits a `LangChainBetaWarning` at runtime.

!!! note "v3 always produces v1-shaped content"

    `ChatModelStream.output.content` is always a list of v1
    content blocks (text / reasoning / tool_call / image / …),
    regardless of the model's `output_version` attribute. The
    setting only affects the legacy `stream()` / `astream()` /
    `invoke()` paths. If you're mixing
    `stream_events(version="v3")` with those paths in the same
    pipeline and need a consistent output shape across them,
    set `output_version="v1"` on the model.

## Signature

```python
stream_events(
    self,
    input: LanguageModelInput,
    config: RunnableConfig | None = None,
    *,
    version: Literal['v1', 'v2', 'v3'] = 'v2',
    stop: list[str] | None = None,
    **kwargs: Any = {},
) -> Iterator[StreamEvent] | ChatModelStream
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `input` | `LanguageModelInput` | Yes | The model input. |
| `config` | `RunnableConfig \| None` | No | Optional runnable config. (default: `None`) |
| `version` | `Literal['v1', 'v2', 'v3']` | No | Streaming-event schema version. `"v3"` selects the content-block-centric streaming protocol. (default: `'v2'`) |
| `stop` | `list[str] \| None` | No | Optional stop sequences. Only used for `version="v3"`; ignored otherwise. (default: `None`) |
| `**kwargs` | `Any` | No | Additional keyword arguments. For `version="v3"`, forwarded to the model. (default: `{}`) |

## Returns

`Iterator[StreamEvent] | ChatModelStream`

For `version="v3"`, a `ChatModelStream` with typed

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/language_models/chat_models.py#L1307)
