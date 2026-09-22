---
title: "format"
description: "Format the prompt with the inputs."
source: "https://reference.langchain.com/python/langchain-core/prompts/base/BasePromptTemplate/format"
category: "reference"
tags: [reference, langchain-core, prompts, base, baseprompttemplate, format]
---

# format

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/prompts/base/BasePromptTemplate/format)

Format the prompt with the inputs.

## Signature

```python
format(
    self,
    **kwargs: Any = {},
) -> FormatOutputType
```

## Description

**Example:**

```python
prompt.format(variable1="foo")
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `**kwargs` | `Any` | No | Any arguments to be passed to the prompt template. (default: `{}`) |

## Returns

`FormatOutputType`

A formatted string.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/prompts/base.py#L316)
