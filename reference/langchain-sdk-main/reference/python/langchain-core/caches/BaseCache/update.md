---
title: "update"
description: "Update cache based on prompt and llm_string."
source: "https://reference.langchain.com/python/langchain-core/caches/BaseCache/update"
category: "reference"
tags: [reference, langchain-core, caches, basecache, update]
---

# update

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/caches/BaseCache/update)

Update cache based on `prompt` and `llm_string`.

The `prompt` and `llm_string` are used to generate a key for the cache. The key
should match that of the lookup method.

## Signature

```python
update(
    self,
    prompt: str,
    llm_string: str,
    return_val: RETURN_VAL_TYPE,
) -> None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `prompt` | `str` | Yes | A string representation of the prompt.  In the case of a chat model, the prompt is a non-trivial serialization of the prompt into the language model. |
| `llm_string` | `str` | Yes | A string representation of the LLM configuration.  This is used to capture the invocation parameters of the LLM (e.g., model name, temperature, stop tokens, max tokens, etc.).  These invocation parameters are serialized into a string representation. |
| `return_val` | `RETURN_VAL_TYPE` | Yes | The value to be cached.  The value is a list of `Generation` (or subclasses). |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/caches.py#L72)
