---
title: "FewShotPromptTemplate"
description: "Prompt template that contains few shot examples."
source: "https://reference.langchain.com/python/langchain-core/prompts/few_shot/FewShotPromptTemplate"
category: "reference"
tags: [reference, langchain-core, prompts, few_shot, fewshotprompttemplate]
---

# FewShotPromptTemplate

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/prompts/few_shot/FewShotPromptTemplate)

Prompt template that contains few shot examples.

## Signature

```python
FewShotPromptTemplate(
    self,
    **kwargs: Any = {},
)
```

## Extends

- `_FewShotPromptTemplateMixin`
- `StringPromptTemplate`

## Constructors

```python
__init__(
    self,
    **kwargs: Any = {},
) -> None
```

## Properties

- `validate_template`
- `example_prompt`
- `suffix`
- `example_separator`
- `prefix`
- `template_format`
- `model_config`

## Methods

- [`is_lc_serializable()`](https://reference.langchain.com/python/langchain-core/prompts/few_shot/FewShotPromptTemplate/is_lc_serializable)
- [`template_is_valid()`](https://reference.langchain.com/python/langchain-core/prompts/few_shot/FewShotPromptTemplate/template_is_valid)
- [`format()`](https://reference.langchain.com/python/langchain-core/prompts/few_shot/FewShotPromptTemplate/format)
- [`aformat()`](https://reference.langchain.com/python/langchain-core/prompts/few_shot/FewShotPromptTemplate/aformat)
- [`save()`](https://reference.langchain.com/python/langchain-core/prompts/few_shot/FewShotPromptTemplate/save)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/prompts/few_shot.py#L121)
