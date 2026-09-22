---
title: "update_cache"
description: "Update the cache and get the LLM output."
source: "https://reference.langchain.com/python/langchain-core/language_models/llms/update_cache"
category: "reference"
tags: [reference, langchain-core, language_models, llms, update_cache]
---

# update_cache

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/language_models/llms/update_cache)

Update the cache and get the LLM output.

## Signature

```python
update_cache(
    cache: BaseCache | bool | None,
    existing_prompts: dict[int, list[Generation]],
    llm_string: str,
    missing_prompt_idxs: list[int],
    new_results: LLMResult,
    prompts: list[str],
) -> dict[str, Any] | None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `cache` | `BaseCache \| bool \| None` | Yes | Cache object. |
| `existing_prompts` | `dict[int, list[Generation]]` | Yes | Dictionary of existing prompts. |
| `llm_string` | `str` | Yes | LLM string. |
| `missing_prompt_idxs` | `list[int]` | Yes | List of missing prompt indexes. |
| `new_results` | `LLMResult` | Yes | LLMResult object. |
| `prompts` | `list[str]` | Yes | List of prompts. |

## Returns

`dict[str, Any] | None`

LLM output.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/language_models/llms.py#L230)
