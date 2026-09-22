---
title: "resolve_model"
description: "Resolve a model string to a BaseChatModel."
source: "https://reference.langchain.com/python/deepagents/_models/resolve_model"
category: "reference"
tags: [reference, deepagents, models, resolve_model]
---

# resolve_model

> **Function** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/_models/resolve_model)

Resolve a model string to a `BaseChatModel`.

If `model` is already a `BaseChatModel`, returns it unchanged.

String models are resolved via `init_chat_model`, composed with any
provider-specific initialization behavior registered in the
`ProviderProfile` registry. Built-in registrations supply NVIDIA NIM and
OpenRouter app attribution headers plus the OpenAI Responses API default;
users can layer additional providers or overrides via
`register_provider_profile`.

## Signature

```python
resolve_model(
    model: str | BaseChatModel,
) -> BaseChatModel
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `model` | `str \| BaseChatModel` | Yes | Model string (e.g. `"openai:gpt-5.4"`) or pre-configured `BaseChatModel` subclass instance. |

## Returns

`BaseChatModel`

Resolved `BaseChatModel` instance.

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/_models.py#L35)
