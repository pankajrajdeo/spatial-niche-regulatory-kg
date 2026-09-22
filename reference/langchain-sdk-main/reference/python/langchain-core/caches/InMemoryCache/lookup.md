---
title: "lookup"
description: "Look up based on prompt and llm_string."
source: "https://reference.langchain.com/python/langchain-core/caches/InMemoryCache/lookup"
category: "reference"
tags: [reference, langchain-core, caches, inmemorycache, lookup]
---

# lookup

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/caches/InMemoryCache/lookup)

Look up based on `prompt` and `llm_string`.

## Signature

```python
lookup(
    self,
    prompt: str,
    llm_string: str,
) -> RETURN_VAL_TYPE | None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `prompt` | `str` | Yes | A string representation of the prompt.  In the case of a chat model, the prompt is a non-trivial serialization of the prompt into the language model. |
| `llm_string` | `str` | Yes | A string representation of the LLM configuration. |

## Returns

`RETURN_VAL_TYPE | None`

On a cache miss, return `None`. On a cache hit, return the cached value.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/caches.py#L201)
