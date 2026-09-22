---
title: "input_types"
description: "A dictionary of the types of the variables the prompt template expects."
source: "https://reference.langchain.com/python/langchain-core/prompts/base/BasePromptTemplate/input_types"
category: "reference"
tags: [reference, langchain-core, prompts, base, baseprompttemplate, input_types]
---

# input_types

> **Attribute** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/prompts/base/BasePromptTemplate/input_types)

A dictionary of the types of the variables the prompt template expects.

If not provided, all variables are assumed to be strings.

## Signature

```python
input_types: builtins.dict[str, Any] = Field(default_factory=dict, exclude=True)
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/prompts/base.py#L55)
