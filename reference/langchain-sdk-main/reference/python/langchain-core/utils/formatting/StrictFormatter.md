---
title: "StrictFormatter"
description: "A string formatter that enforces keyword-only argument substitution."
source: "https://reference.langchain.com/python/langchain-core/utils/formatting/StrictFormatter"
category: "reference"
tags: [reference, langchain-core, utils, formatting, strictformatter]
---

# StrictFormatter

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/utils/formatting/StrictFormatter)

A string formatter that enforces keyword-only argument substitution.

This formatter extends Python's built-in `string.Formatter` to provide stricter
validation for prompt template formatting. It ensures that all variable
substitutions use keyword arguments rather than positional arguments, which improves
clarity and reduces errors when formatting prompt templates.

## Signature

```python
StrictFormatter()
```

## Description

**Example:**

>>> fmt = StrictFormatter()
>>> fmt.format("Hello, {name}!", name="World")
'Hello, World!'
>>> fmt.format("Hello, {}!", "World")  # Raises ValueError

## Extends

- `Formatter`

## Methods

- [`vformat()`](https://reference.langchain.com/python/langchain-core/utils/formatting/StrictFormatter/vformat)
- [`validate_input_variables()`](https://reference.langchain.com/python/langchain-core/utils/formatting/StrictFormatter/validate_input_variables)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/utils/formatting.py#L8)
