---
title: "aformat_prompt"
description: "Async create PromptValue."
source: "https://reference.langchain.com/python/langchain-core/prompts/base/BasePromptTemplate/aformat_prompt"
category: "reference"
tags: [reference, langchain-core, prompts, base, baseprompttemplate, aformat_prompt]
---

# aformat_prompt

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/prompts/base/BasePromptTemplate/aformat_prompt)

Async create `PromptValue`.

## Signature

```python
aformat_prompt(
    self,
    **kwargs: Any = {},
) -> PromptValue
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `**kwargs` | `Any` | No | Any arguments to be passed to the prompt template. (default: `{}`) |

## Returns

`PromptValue`

The output of the prompt.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/prompts/base.py#L278)
