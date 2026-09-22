---
title: "EncryptionContext"
description: "Context passed to encryption/decryption handlers."
source: "https://reference.langchain.com/python/langgraph-sdk/encryption/types/EncryptionContext"
category: "reference"
tags: [reference, langgraph-sdk, encryption, types, encryptioncontext]
---

# EncryptionContext

> **Class** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/encryption/types/EncryptionContext)

Context passed to encryption/decryption handlers.

Contains arbitrary non-secret key-values that will be stored on encrypt.
These key-values are intended to be sent to an external service that
manages keys and handles the actual encryption and decryption of data.

## Signature

```python
EncryptionContext(
    self,
    model: str | None = None,
    metadata: dict[str, typing.Any] | None = None,
    field: str | None = None,
)
```

## Constructors

```python
__init__(
    self,
    model: str | None = None,
    metadata: dict[str, typing.Any] | None = None,
    field: str | None = None,
)
```

| Name | Type |
|------|------|
| `model` | `str \| None` |
| `metadata` | `dict[str, typing.Any] \| None` |
| `field` | `str \| None` |

## Properties

- `model`
- `field`
- `metadata`

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/d5f4b2aa960940effc8430165ab3604038e817af/libs/sdk-py/langgraph_sdk/encryption/types.py#L37)
