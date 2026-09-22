---
title: "get_num_tokens"
description: "Get the number of tokens present in the text."
source: "https://reference.langchain.com/python/langchain-core/language_models/base/BaseLanguageModel/get_num_tokens"
category: "reference"
tags: [reference, langchain-core, language_models, base, baselanguagemodel, get_num_tokens]
---

# get_num_tokens

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/language_models/base/BaseLanguageModel/get_num_tokens)

Get the number of tokens present in the text.

Useful for checking if an input fits in a model's context window.

This should be overridden by model-specific implementations to provide accurate
token counts via model-specific tokenizers.

## Signature

```python
get_num_tokens(
    self,
    text: str,
) -> int
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `text` | `str` | Yes | The string input to tokenize. |

## Returns

`int`

The integer number of tokens in the text.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/language_models/base.py#L448)
