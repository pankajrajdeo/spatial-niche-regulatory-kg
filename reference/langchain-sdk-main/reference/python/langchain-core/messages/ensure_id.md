---
title: "ensure_id"
description: "Ensure the ID is a valid string, generating a new UUID if not provided."
source: "https://reference.langchain.com/python/langchain-core/messages/ensure_id"
category: "reference"
tags: [reference, langchain-core, messages, ensure_id]
---

# ensure_id

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/utils/utils/ensure_id)

Ensure the ID is a valid string, generating a new UUID if not provided.

Auto-generated UUIDs are prefixed by `'lc_'` to indicate they are
LangChain-generated IDs.

## Signature

```python
ensure_id(
    id_val: str | None,
) -> str
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `id_val` | `str \| None` | Yes | Optional string ID value to validate. |

## Returns

`str`

A string ID, either the validated provided value or a newly generated UUID4.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/utils/utils.py#L509)
