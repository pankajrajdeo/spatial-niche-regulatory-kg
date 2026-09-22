---
title: "PromptValue"
description: "Base abstract class for inputs to any language model."
source: "https://reference.langchain.com/python/langchain-core/prompt_values/PromptValue"
category: "reference"
tags: [reference, langchain-core, prompt_values, promptvalue]
---

# PromptValue

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/prompt_values/PromptValue)

Base abstract class for inputs to any language model.

`PromptValues` can be converted to both LLM (pure text-generation) inputs and
chat model inputs.

## Signature

```python
PromptValue(
    self,
    *args: Any = (),
    **kwargs: Any = {},
)
```

## Extends

- `Serializable`
- `ABC`

## Methods

- [`is_lc_serializable()`](https://reference.langchain.com/python/langchain-core/prompt_values/PromptValue/is_lc_serializable)
- [`get_lc_namespace()`](https://reference.langchain.com/python/langchain-core/prompt_values/PromptValue/get_lc_namespace)
- [`to_string()`](https://reference.langchain.com/python/langchain-core/prompt_values/PromptValue/to_string)
- [`to_messages()`](https://reference.langchain.com/python/langchain-core/prompt_values/PromptValue/to_messages)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/prompt_values.py#L24)
