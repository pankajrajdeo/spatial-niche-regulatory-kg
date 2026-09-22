---
title: "aupdate"
description: "Async update cache based on prompt and llm_string."
source: "https://reference.langchain.com/python/langchain-core/caches/InMemoryCache/aupdate"
category: "reference"
tags: [reference, langchain-core, caches, inmemorycache, aupdate]
---

# aupdate

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/caches/InMemoryCache/aupdate)

Async update cache based on `prompt` and `llm_string`.

## Signature

```python
aupdate(
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
| `llm_string` | `str` | Yes | A string representation of the LLM configuration. |
| `return_val` | `RETURN_VAL_TYPE` | Yes | The value to be cached. The value is a list of `Generation` (or subclasses). |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/caches.py#L253)
