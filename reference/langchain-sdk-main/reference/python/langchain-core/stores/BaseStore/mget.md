---
title: "mget"
description: "Get the values associated with the given keys."
source: "https://reference.langchain.com/python/langchain-core/stores/BaseStore/mget"
category: "reference"
tags: [reference, langchain-core, stores, basestore, mget]
---

# mget

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/stores/BaseStore/mget)

Get the values associated with the given keys.

## Signature

```python
mget(
    self,
    keys: Sequence[K],
) -> list[V | None]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `keys` | `Sequence[K]` | Yes | A sequence of keys. |

## Returns

`list[V | None]`

A sequence of optional values associated with the keys.
If a key is not found, the corresponding value will be `None`.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/stores.py#L80)
