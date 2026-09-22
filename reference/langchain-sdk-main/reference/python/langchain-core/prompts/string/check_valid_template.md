---
title: "check_valid_template"
description: "Check that template string is valid."
source: "https://reference.langchain.com/python/langchain-core/prompts/string/check_valid_template"
category: "reference"
tags: [reference, langchain-core, prompts, string, check_valid_template]
---

# check_valid_template

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/prompts/string/check_valid_template)

Check that template string is valid.

## Signature

```python
check_valid_template(
    template: str,
    template_format: str,
    input_variables: list[str],
) -> None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `template` | `str` | Yes | The template string. |
| `template_format` | `str` | Yes | The template format.  Should be one of `'f-string'` or `'jinja2'`. |
| `input_variables` | `list[str]` | Yes | The input variables. |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/prompts/string.py#L262)
