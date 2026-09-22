---
title: "invoke"
description: "Invoke the prompt."
source: "https://reference.langchain.com/python/langchain-core/prompts/base/BasePromptTemplate/invoke"
category: "reference"
tags: [reference, langchain-core, prompts, base, baseprompttemplate, invoke]
---

# invoke

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/prompts/base/BasePromptTemplate/invoke)

Invoke the prompt.

## Signature

```python
invoke(
    self,
    input: builtins.dict[str, Any],
    config: RunnableConfig | None = None,
    **kwargs: Any = {},
) -> PromptValue
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `input` | `builtins.dict[str, Any]` | Yes | Input to the prompt. |
| `config` | `RunnableConfig \| None` | No | Configuration for the prompt. (default: `None`) |

## Returns

`PromptValue`

The output of the prompt.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/prompts/base.py#L209)
