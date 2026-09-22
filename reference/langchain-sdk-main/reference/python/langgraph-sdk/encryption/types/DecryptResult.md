---
title: "DecryptResult"
description: "Decrypted data and optional replacement ciphertext."
source: "https://reference.langchain.com/python/langgraph-sdk/encryption/types/DecryptResult"
category: "reference"
tags: [reference, langgraph-sdk, encryption, types, decryptresult]
---

# DecryptResult

> **Class** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/encryption/types/DecryptResult)

Decrypted data and optional replacement ciphertext.

Return this from a decrypt handler when encrypted data should be replaced,
such as after rotating its encryption key. Returning plaintext directly
remains supported when no replacement is needed.

## Signature

```python
DecryptResult(
    self,
    plaintext: T,
    replacement: T | None = None,
)
```

## Extends

- `typing.Generic[T]`

## Constructors

```python
__init__(
    self,
    plaintext: T,
    replacement: T | None = None,
) -> None
```

| Name | Type |
|------|------|
| `plaintext` | `T` |
| `replacement` | `T \| None` |

## Properties

- `plaintext`
- `replacement`

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/d5f4b2aa960940effc8430165ab3604038e817af/libs/sdk-py/langgraph_sdk/encryption/types.py#L20)
