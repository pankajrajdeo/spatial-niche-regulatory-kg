---
title: "validate_jinja2"
description: "Validate that the input variables are valid for the template."
source: "https://reference.langchain.com/python/langchain-core/prompts/string/validate_jinja2"
category: "reference"
tags: [reference, langchain-core, prompts, string, validate_jinja2]
---

# validate_jinja2

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/prompts/string/validate_jinja2)

Validate that the input variables are valid for the template.

Issues a warning if missing or extra variables are found.

## Signature

```python
validate_jinja2(
    template: str,
    input_variables: list[str],
) -> None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `template` | `str` | Yes | The template string. |
| `input_variables` | `list[str]` | Yes | The input variables. |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/prompts/string.py#L75)
