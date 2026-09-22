---
title: "BaseStringMessagePromptTemplate"
description: "Base class for message prompt templates that use a string prompt template."
source: "https://reference.langchain.com/python/langchain-core/prompts/chat/BaseStringMessagePromptTemplate"
category: "reference"
tags: [reference, langchain-core, prompts, chat, basestringmessageprompttemplate]
---

# BaseStringMessagePromptTemplate

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/prompts/chat/BaseStringMessagePromptTemplate)

Base class for message prompt templates that use a string prompt template.

## Signature

```python
BaseStringMessagePromptTemplate(
    self,
    *args: Any = (),
    **kwargs: Any = {},
)
```

## Extends

- `BaseMessagePromptTemplate`
- `ABC`

## Properties

- `prompt`
- `additional_kwargs`
- `input_variables`

## Methods

- [`from_template()`](https://reference.langchain.com/python/langchain-core/prompts/chat/BaseStringMessagePromptTemplate/from_template)
- [`from_template_file()`](https://reference.langchain.com/python/langchain-core/prompts/chat/BaseStringMessagePromptTemplate/from_template_file)
- [`format()`](https://reference.langchain.com/python/langchain-core/prompts/chat/BaseStringMessagePromptTemplate/format)
- [`aformat()`](https://reference.langchain.com/python/langchain-core/prompts/chat/BaseStringMessagePromptTemplate/aformat)
- [`format_messages()`](https://reference.langchain.com/python/langchain-core/prompts/chat/BaseStringMessagePromptTemplate/format_messages)
- [`aformat_messages()`](https://reference.langchain.com/python/langchain-core/prompts/chat/BaseStringMessagePromptTemplate/aformat_messages)
- [`pretty_repr()`](https://reference.langchain.com/python/langchain-core/prompts/chat/BaseStringMessagePromptTemplate/pretty_repr)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/prompts/chat.py#L226)
