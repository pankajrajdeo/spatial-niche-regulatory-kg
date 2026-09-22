---
title: "from_template_file"
description: "Create a class from a template file."
source: "https://reference.langchain.com/python/langchain-core/prompts/chat/BaseStringMessagePromptTemplate/from_template_file"
category: "reference"
tags: [reference, langchain-core, prompts, chat, basestringmessageprompttemplate, from_template_file]
---

# from_template_file

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/prompts/chat/BaseStringMessagePromptTemplate/from_template_file)

Create a class from a template file.

## Signature

```python
from_template_file(
    cls,
    template_file: str | Path,
    **kwargs: Any = {},
) -> Self
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `template_file` | `str \| Path` | Yes | path to a template file. |
| `**kwargs` | `Any` | No | Keyword arguments to pass to the constructor. (default: `{}`) |

## Returns

`Self`

A new instance of this class.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/prompts/chat.py#L267)
