---
title: "validate_input_variables"
description: "Validate that input variables match the placeholders in a format string."
source: "https://reference.langchain.com/python/langchain-core/utils/formatting/StrictFormatter/validate_input_variables"
category: "reference"
tags: [reference, langchain-core, utils, formatting, strictformatter, validate_input_variables]
---

# validate_input_variables

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/utils/formatting/StrictFormatter/validate_input_variables)

Validate that input variables match the placeholders in a format string.

Checks that the provided input variables can be used to format the given string
without missing or extra keys. This is useful for validating prompt templates
before runtime.

## Signature

```python
validate_input_variables(
    self,
    format_string: str,
    input_variables: list[str],
) -> None
```

## Description

**Example:**

>>> fmt = StrictFormatter()
>>> fmt.validate_input_variables("Hello, {name}!", ["name"])  # OK
>>> fmt.validate_input_variables("Hello, {name}!", ["other"])  # Raises

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `format_string` | `str` | Yes | A string containing replacement fields to validate against (e.g., `'Hello, {name}!'`). |
| `input_variables` | `list[str]` | Yes | List of variable names expected to fill the replacement fields. |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/utils/formatting.py#L50)
