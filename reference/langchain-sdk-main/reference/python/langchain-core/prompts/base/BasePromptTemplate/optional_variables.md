---
title: "optional_variables"
description: "A list of the names of the variables for placeholder or MessagePlaceholder that are optional."
source: "https://reference.langchain.com/python/langchain-core/prompts/base/BasePromptTemplate/optional_variables"
category: "reference"
tags: [reference, langchain-core, prompts, base, baseprompttemplate, optional_variables]
---

# optional_variables

> **Attribute** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/prompts/base/BasePromptTemplate/optional_variables)

A list of the names of the variables for placeholder or `MessagePlaceholder` that
are optional.

These variables are auto inferred from the prompt and user need not provide them.

## Signature

```python
optional_variables: list[str] = Field(default=[])
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/prompts/base.py#L48)
