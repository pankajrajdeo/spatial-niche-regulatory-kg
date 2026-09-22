---
title: "mset"
description: "Set the values for the given keys."
source: "https://reference.langchain.com/python/langchain-core/stores/BaseStore/mset"
category: "reference"
tags: [reference, langchain-core, stores, basestore, mset]
---

# mset

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/stores/BaseStore/mset)

Set the values for the given keys.

## Signature

```python
mset(
    self,
    key_value_pairs: Sequence[tuple[K, V]],
) -> None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `key_value_pairs` | `Sequence[tuple[K, V]]` | Yes | A sequence of key-value pairs. |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/stores.py#L104)
