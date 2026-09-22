---
title: "BaseLanguageModel"
description: "Abstract base class for interfacing with language models."
source: "https://reference.langchain.com/python/langchain-core/language_models/base/BaseLanguageModel"
category: "reference"
tags: [reference, langchain-core, language_models, base, baselanguagemodel]
---

# BaseLanguageModel

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/language_models/base/BaseLanguageModel)

Abstract base class for interfacing with language models.

All language model wrappers inherited from `BaseLanguageModel`.

## Signature

```python
BaseLanguageModel(
    self,
    *args: Any = (),
    **kwargs: Any = {},
)
```

## Extends

- `RunnableSerializable[LanguageModelInput, LanguageModelOutputVar]`
- `ABC`

## Properties

- `cache`
- `verbose`
- `callbacks`
- `tags`
- `metadata`
- `custom_get_token_ids`
- `model_config`
- `InputType`

## Methods

- [`model_post_init()`](https://reference.langchain.com/python/langchain-core/language_models/base/BaseLanguageModel/model_post_init)
- [`set_verbose()`](https://reference.langchain.com/python/langchain-core/language_models/base/BaseLanguageModel/set_verbose)
- [`generate_prompt()`](https://reference.langchain.com/python/langchain-core/language_models/base/BaseLanguageModel/generate_prompt)
- [`agenerate_prompt()`](https://reference.langchain.com/python/langchain-core/language_models/base/BaseLanguageModel/agenerate_prompt)
- [`with_structured_output()`](https://reference.langchain.com/python/langchain-core/language_models/base/BaseLanguageModel/with_structured_output)
- [`get_token_ids()`](https://reference.langchain.com/python/langchain-core/language_models/base/BaseLanguageModel/get_token_ids)
- [`get_num_tokens()`](https://reference.langchain.com/python/langchain-core/language_models/base/BaseLanguageModel/get_num_tokens)
- [`get_num_tokens_from_messages()`](https://reference.langchain.com/python/langchain-core/language_models/base/BaseLanguageModel/get_num_tokens_from_messages)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/language_models/base.py#L181)
