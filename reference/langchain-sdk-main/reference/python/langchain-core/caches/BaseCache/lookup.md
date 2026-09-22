---
title: "lookup"
description: "Look up based on prompt and llm_string."
source: "https://reference.langchain.com/python/langchain-core/caches/BaseCache/lookup"
category: "reference"
tags: [reference, langchain-core, caches, basecache, lookup]
---

# lookup

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/caches/BaseCache/lookup)

Look up based on `prompt` and `llm_string`.

A cache implementation is expected to generate a key from the 2-tuple
of `prompt` and `llm_string` (e.g., by concatenating them with a delimiter).

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
| `llm_string` | `str` | Yes | A string representation of the LLM configuration.  This is used to capture the invocation parameters of the LLM (e.g., model name, temperature, stop tokens, max tokens, etc.).  These invocation parameters are serialized into a string representation. |

## Returns

`RETURN_VAL_TYPE | None`

On a cache miss, return `None`. On a cache hit, return the cached value.
The cached value is a list of `Generation` (or subclasses).

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/caches.py#L48)
