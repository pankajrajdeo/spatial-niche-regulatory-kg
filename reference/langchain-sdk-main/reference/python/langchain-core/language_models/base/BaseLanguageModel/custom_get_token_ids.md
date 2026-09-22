---
title: "custom_get_token_ids"
description: "Optional encoder to use for counting tokens."
source: "https://reference.langchain.com/python/langchain-core/language_models/base/BaseLanguageModel/custom_get_token_ids"
category: "reference"
tags: [reference, langchain-core, language_models, base, baselanguagemodel, custom_get_token_ids]
---

# custom_get_token_ids

> **Attribute** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/language_models/base/BaseLanguageModel/custom_get_token_ids)

Optional encoder to use for counting tokens.

## Signature

```python
custom_get_token_ids: Callable[[str], list[int]] | None = Field(default=None, exclude=True)
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/language_models/base.py#L213)
