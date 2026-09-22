---
title: "FewShotChatMessagePromptTemplate"
description: "Chat prompt template that supports few-shot examples."
source: "https://reference.langchain.com/python/langchain-core/prompts/few_shot/FewShotChatMessagePromptTemplate"
category: "reference"
tags: [reference, langchain-core, prompts, few_shot, fewshotchatmessageprompttemplate]
---

# FewShotChatMessagePromptTemplate

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/prompts/few_shot/FewShotChatMessagePromptTemplate)

Chat prompt template that supports few-shot examples.

The high level structure of produced by this prompt template is a list of messages
consisting of prefix message(s), example message(s), and suffix message(s).

This structure enables creating a conversation with intermediate examples like:

```txt
System: You are a helpful AI Assistant

Human: What is 2+2?

AI: 4

Human: What is 2+3?

AI: 5

Human: What is 4+4?
```

This prompt template can be used to generate a fixed list of examples or else to
dynamically select examples based on the input.

## Signature

```python
FewShotChatMessagePromptTemplate(
    self,
    *args: Any = (),
    **kwargs: Any = {},
)
```

## Extends

- `BaseChatPromptTemplate`
- `_FewShotPromptTemplateMixin`

## Properties

- `input_variables`
- `example_prompt`
- `model_config`

## Methods

- [`is_lc_serializable()`](https://reference.langchain.com/python/langchain-core/prompts/few_shot/FewShotChatMessagePromptTemplate/is_lc_serializable)
- [`format_messages()`](https://reference.langchain.com/python/langchain-core/prompts/few_shot/FewShotChatMessagePromptTemplate/format_messages)
- [`aformat_messages()`](https://reference.langchain.com/python/langchain-core/prompts/few_shot/FewShotChatMessagePromptTemplate/aformat_messages)
- [`format()`](https://reference.langchain.com/python/langchain-core/prompts/few_shot/FewShotChatMessagePromptTemplate/format)
- [`aformat()`](https://reference.langchain.com/python/langchain-core/prompts/few_shot/FewShotChatMessagePromptTemplate/aformat)
- [`pretty_repr()`](https://reference.langchain.com/python/langchain-core/prompts/few_shot/FewShotChatMessagePromptTemplate/pretty_repr)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/prompts/few_shot.py#L262)
