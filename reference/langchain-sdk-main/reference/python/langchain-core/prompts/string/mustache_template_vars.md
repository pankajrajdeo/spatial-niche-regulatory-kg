---
title: "mustache_template_vars"
description: "Get the top-level variables from a mustache template."
source: "https://reference.langchain.com/python/langchain-core/prompts/string/mustache_template_vars"
category: "reference"
tags: [reference, langchain-core, prompts, string, mustache_template_vars]
---

# mustache_template_vars

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/prompts/string/mustache_template_vars)

Get the top-level variables from a mustache template.

For nested variables like `{{person.name}}`, only the top-level key (`person`) is
returned.

## Signature

```python
mustache_template_vars(
    template: str,
) -> set[str]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `template` | `str` | Yes | The template string. |

## Returns

`set[str]`

The top-level variables from the template.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/prompts/string.py#L125)
