---
title: "BasePromptTemplate"
description: "Base class for all prompt templates, returning a prompt."
source: "https://reference.langchain.com/python/langchain-core/prompts/base/BasePromptTemplate"
category: "reference"
tags: [reference, langchain-core, prompts, base, baseprompttemplate]
---

# BasePromptTemplate

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/prompts/base/BasePromptTemplate)

Base class for all prompt templates, returning a prompt.

## Signature

```python
BasePromptTemplate(
    self,
    *args: Any = (),
    **kwargs: Any = {},
)
```

## Extends

- `RunnableSerializable[dict[str, Any], PromptValue]`
- `ABC`
- `Generic[FormatOutputType]`

## Properties

- `input_variables`
- `optional_variables`
- `input_types`
- `output_parser`
- `partial_variables`
- `metadata`
- `tags`
- `model_config`
- `OutputType`

## Methods

- [`validate_variable_names()`](https://reference.langchain.com/python/langchain-core/prompts/base/BasePromptTemplate/validate_variable_names)
- [`get_lc_namespace()`](https://reference.langchain.com/python/langchain-core/prompts/base/BasePromptTemplate/get_lc_namespace)
- [`is_lc_serializable()`](https://reference.langchain.com/python/langchain-core/prompts/base/BasePromptTemplate/is_lc_serializable)
- [`get_input_schema()`](https://reference.langchain.com/python/langchain-core/prompts/base/BasePromptTemplate/get_input_schema)
- [`invoke()`](https://reference.langchain.com/python/langchain-core/prompts/base/BasePromptTemplate/invoke)
- [`ainvoke()`](https://reference.langchain.com/python/langchain-core/prompts/base/BasePromptTemplate/ainvoke)
- [`format_prompt()`](https://reference.langchain.com/python/langchain-core/prompts/base/BasePromptTemplate/format_prompt)
- [`aformat_prompt()`](https://reference.langchain.com/python/langchain-core/prompts/base/BasePromptTemplate/aformat_prompt)
- [`partial()`](https://reference.langchain.com/python/langchain-core/prompts/base/BasePromptTemplate/partial)
- [`format()`](https://reference.langchain.com/python/langchain-core/prompts/base/BasePromptTemplate/format)
- [`aformat()`](https://reference.langchain.com/python/langchain-core/prompts/base/BasePromptTemplate/aformat)
- [`dict()`](https://reference.langchain.com/python/langchain-core/prompts/base/BasePromptTemplate/dict)
- [`asdict()`](https://reference.langchain.com/python/langchain-core/prompts/base/BasePromptTemplate/asdict)
- [`save()`](https://reference.langchain.com/python/langchain-core/prompts/base/BasePromptTemplate/save)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/prompts/base.py#L38)
