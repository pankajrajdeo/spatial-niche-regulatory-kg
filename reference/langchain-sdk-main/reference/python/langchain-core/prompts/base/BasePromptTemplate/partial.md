---
title: "partial"
description: "Return a partial of the prompt template."
source: "https://reference.langchain.com/python/langchain-core/prompts/base/BasePromptTemplate/partial"
category: "reference"
tags: [reference, langchain-core, prompts, base, baseprompttemplate, partial]
---

# partial

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/prompts/base/BasePromptTemplate/partial)

Return a partial of the prompt template.

## Signature

```python
partial(
    self,
    **kwargs: str | Callable[[], str] = {},
) -> BasePromptTemplate[FormatOutputType]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `**kwargs` | `str \| Callable[[], str]` | No | Partial variables to set. (default: `{}`) |

## Returns

`BasePromptTemplate[FormatOutputType]`

A partial of the prompt template.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/prompts/base.py#L289)
