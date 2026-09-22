---
title: "batch"
description: "View source on GitHub"
source: "https://reference.langchain.com/python/langchain-core/language_models/llms/BaseLLM/batch"
category: "reference"
tags: [reference, langchain-core, language_models, llms, basellm, batch]
---

# batch

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/language_models/llms/BaseLLM/batch)

## Signature

```python
batch(
    self,
    inputs: list[LanguageModelInput],
    config: RunnableConfig | list[RunnableConfig] | None = None,
    *,
    return_exceptions: bool = False,
    **kwargs: Any = {},
) -> list[str]
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/language_models/llms.py#L420)
