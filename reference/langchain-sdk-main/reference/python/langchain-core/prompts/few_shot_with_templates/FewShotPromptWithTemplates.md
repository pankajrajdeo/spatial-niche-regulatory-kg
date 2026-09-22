---
title: "FewShotPromptWithTemplates"
description: "Prompt template that contains few shot examples."
source: "https://reference.langchain.com/python/langchain-core/prompts/few_shot_with_templates/FewShotPromptWithTemplates"
category: "reference"
tags: [reference, langchain-core, prompts, few_shot_with_templates, fewshotpromptwithtemplates]
---

# FewShotPromptWithTemplates

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/prompts/few_shot_with_templates/FewShotPromptWithTemplates)

Prompt template that contains few shot examples.

## Signature

```python
FewShotPromptWithTemplates(
    self,
    *args: Any = (),
    **kwargs: Any = {},
)
```

## Extends

- `StringPromptTemplate`

## Properties

- `examples`
- `example_selector`
- `example_prompt`
- `suffix`
- `example_separator`
- `prefix`
- `template_format`
- `validate_template`
- `model_config`

## Methods

- [`get_lc_namespace()`](https://reference.langchain.com/python/langchain-core/prompts/few_shot_with_templates/FewShotPromptWithTemplates/get_lc_namespace)
- [`check_examples_and_selector()`](https://reference.langchain.com/python/langchain-core/prompts/few_shot_with_templates/FewShotPromptWithTemplates/check_examples_and_selector)
- [`template_is_valid()`](https://reference.langchain.com/python/langchain-core/prompts/few_shot_with_templates/FewShotPromptWithTemplates/template_is_valid)
- [`format()`](https://reference.langchain.com/python/langchain-core/prompts/few_shot_with_templates/FewShotPromptWithTemplates/format)
- [`aformat()`](https://reference.langchain.com/python/langchain-core/prompts/few_shot_with_templates/FewShotPromptWithTemplates/aformat)
- [`save()`](https://reference.langchain.com/python/langchain-core/prompts/few_shot_with_templates/FewShotPromptWithTemplates/save)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/prompts/few_shot_with_templates.py#L19)
