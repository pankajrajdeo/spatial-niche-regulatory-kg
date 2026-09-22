---
title: "get_model_identifier"
description: "Extract the provider-native model identifier from a chat model."
source: "https://reference.langchain.com/python/deepagents/_models/get_model_identifier"
category: "reference"
tags: [reference, deepagents, models, get_model_identifier]
---

# get_model_identifier

> **Function** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/_models/get_model_identifier)

Extract the provider-native model identifier from a chat model.

Providers do not agree on a single field name for the identifier. Some use
`model_name`, while others use `model`.

## Signature

```python
get_model_identifier(
    model: BaseChatModel,
) -> str | None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `model` | `BaseChatModel` | Yes | Chat model instance to inspect. |

## Returns

`str | None`

The configured model identifier, or `None` if it is unavailable.

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/_models.py#L60)
