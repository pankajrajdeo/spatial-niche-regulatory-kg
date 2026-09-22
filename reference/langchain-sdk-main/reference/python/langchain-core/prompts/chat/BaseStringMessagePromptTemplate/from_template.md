---
title: "from_template"
description: "Create a class from a string template."
source: "https://reference.langchain.com/python/langchain-core/prompts/chat/BaseStringMessagePromptTemplate/from_template"
category: "reference"
tags: [reference, langchain-core, prompts, chat, basestringmessageprompttemplate, from_template]
---

# from_template

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/prompts/chat/BaseStringMessagePromptTemplate/from_template)

Create a class from a string template.

## Signature

```python
from_template(
    cls,
    template: str,
    template_format: PromptTemplateFormat = 'f-string',
    partial_variables: dict[str, Any] | None = None,
    **kwargs: Any = {},
) -> Self
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `template` | `str` | Yes | a template. |
| `template_format` | `PromptTemplateFormat` | No | format of the template. (default: `'f-string'`) |
| `partial_variables` | `dict[str, Any] \| None` | No | A dictionary of variables that can be used to partially fill in the template.  For example, if the template is `"{variable1} {variable2}"`, and `partial_variables` is `{"variable1": "foo"}`, then the final prompt will be `"foo {variable2}"`. (default: `None`) |
| `**kwargs` | `Any` | No | Keyword arguments to pass to the constructor. (default: `{}`) |

## Returns

`Self`

A new instance of this class.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/prompts/chat.py#L235)
