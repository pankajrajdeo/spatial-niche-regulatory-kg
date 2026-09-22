---
title: "cache_get"
description: "Get a value from the cache."
source: "https://reference.langchain.com/python/langgraph-sdk/cache/cache_get"
category: "reference"
tags: [reference, langgraph-sdk, cache, cache_get]
---

# cache_get

> **Function** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/cache/cache_get)

Get a value from the cache.

Returns the deserialized value, or ``None`` if the key is missing or expired.

Requires Agent Server runtime version 0.7.29 or later.

## Signature

```python
cache_get(
    key: str,
) -> Any | None
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/d5f4b2aa960940effc8430165ab3604038e817af/libs/sdk-py/langgraph_sdk/cache.py#L59)
