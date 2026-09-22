---
title: "get_json_encryptor"
description: "Get the JSON encryptor."
source: "https://reference.langchain.com/python/langgraph-sdk/encryption/Encryption/get_json_encryptor"
category: "reference"
tags: [reference, langgraph-sdk, encryption, get_json_encryptor]
---

# get_json_encryptor

> **Method** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/encryption/Encryption/get_json_encryptor)

Get the JSON encryptor.

## Signature

```python
get_json_encryptor(
    self,
    _model: str | None = None,
) -> types.JsonEncryptor | None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `_model` | `str \| None` | No | Ignored. Kept for backwards compatibility with langgraph-api which passes model_type to this method. (default: `None`) |

## Returns

`types.JsonEncryptor | None`

The JSON encryptor, or None if not registered.

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/d5f4b2aa960940effc8430165ab3604038e817af/libs/sdk-py/langgraph_sdk/encryption/__init__.py#L431)
