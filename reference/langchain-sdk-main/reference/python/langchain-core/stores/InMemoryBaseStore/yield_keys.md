---
title: "yield_keys"
description: "Get an iterator over keys that match the given prefix."
source: "https://reference.langchain.com/python/langchain-core/stores/InMemoryBaseStore/yield_keys"
category: "reference"
tags: [reference, langchain-core, stores, inmemorybasestore, yield_keys]
---

# yield_keys

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/stores/InMemoryBaseStore/yield_keys)

Get an iterator over keys that match the given prefix.

## Signature

```python
yield_keys(
    self,
    *,
    prefix: str | None = None,
) -> Iterator[str]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `prefix` | `str \| None` | No | The prefix to match. (default: `None`) |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/stores.py#L210)
