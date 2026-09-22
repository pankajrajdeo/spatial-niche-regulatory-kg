---
title: "get_template_variables"
description: "Get the variables from the template."
source: "https://reference.langchain.com/python/langchain-core/prompts/image/get_template_variables"
category: "reference"
tags: [reference, langchain-core, prompts, image, get_template_variables]
---

# get_template_variables

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/prompts/string/get_template_variables)

Get the variables from the template.

## Signature

```python
get_template_variables(
    template: str,
    template_format: str,
) -> list[str]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `template` | `str` | Yes | The template string. |
| `template_format` | `str` | Yes | The template format.  Should be one of `'f-string'`, `'mustache'` or `'jinja2'`. |

## Returns

`list[str]`

The variables from the template.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/prompts/string.py#L298)
