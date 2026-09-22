---
title: "bind"
description: "Bind kwargs to this chat model, returning a typed _ChatModelBinding."
source: "https://reference.langchain.com/python/langchain-core/language_models/chat_models/BaseChatModel/bind"
category: "reference"
tags: [reference, langchain-core, language_models, chat_models, basechatmodel, bind]
---

# bind

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/language_models/chat_models/BaseChatModel/bind)

Bind kwargs to this chat model, returning a typed `_ChatModelBinding`.

Overrides `Runnable.bind` so the result preserves chat-model-specific
`stream_events` / `astream_events` overloads. Without this override,
`model.bind(...).stream_events(version="v3")` would type as
`Iterator[Any]` and `await model.bind(...).astream_events(version="v3")`
as `Any`, forcing callers to `cast`.

## Signature

```python
bind(
    self,
    **kwargs: Any = {},
) -> _ChatModelBinding
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/language_models/chat_models.py#L2354)
