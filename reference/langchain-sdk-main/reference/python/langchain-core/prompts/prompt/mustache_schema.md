---
title: "mustache_schema"
description: "Get the variables from a mustache template."
source: "https://reference.langchain.com/python/langchain-core/prompts/prompt/mustache_schema"
category: "reference"
tags: [reference, langchain-core, prompts, prompt, mustache_schema]
---

# mustache_schema

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/prompts/string/mustache_schema)

Get the variables from a mustache template.

## Signature

```python
mustache_schema(
    template: str,
) -> type[BaseModel]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `template` | `str` | Yes | The template string. |

## Returns

`type[BaseModel]`

The variables from the template as a Pydantic model.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/prompts/string.py#L158)
