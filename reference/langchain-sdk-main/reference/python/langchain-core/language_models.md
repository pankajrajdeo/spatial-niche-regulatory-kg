---
title: "language_models"
description: "Core language model abstractions."
source: "https://reference.langchain.com/python/langchain-core/language_models"
category: "reference"
tags: [reference, langchain-core, language_models]
---

# language_models

> **Module** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/language_models)

Core language model abstractions.

LangChain has two main classes to work with language models: chat models and
"old-fashioned" LLMs (string-in, string-out).

**Chat models**

Language models that use a sequence of messages as inputs and return chat messages
as outputs (as opposed to using plain text).

Chat models support the assignment of distinct roles to conversation messages, helping
to distinguish messages from the AI, users, and instructions such as system messages.

The key abstraction for chat models is
[`BaseChatModel`][langchain_core.language_models.BaseChatModel]. Implementations should
inherit from this class.

See existing [chat model integrations](../../../integrations/chat.md).

**LLMs (legacy)**

Language models that takes a string as input and returns a string.

These are traditionally older models (newer models generally are chat models).

Although the underlying models are string in, string out, the LangChain wrappers also
allow these models to take messages as input. This gives them the same interface as
chat models. When messages are passed in as input, they will be formatted into a string
under the hood before being passed to the underlying model.

## Properties

- `LanguageModelLike`
- `ModelProfileRegistry`

## Methods

- [`import_attr()`](https://reference.langchain.com/python/langchain-core/language_models/import_attr)
- [`is_openai_data_block()`](https://reference.langchain.com/python/langchain-core/language_models/is_openai_data_block)
- [`get_tokenizer()`](https://reference.langchain.com/python/langchain-core/language_models/get_tokenizer)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/language_models/__init__.py)
