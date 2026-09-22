---
title: "outputs"
description: "Output classes."
source: "https://reference.langchain.com/python/langchain-core/outputs"
category: "reference"
tags: [reference, langchain-core, outputs]
---

# outputs

> **Module** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/outputs)

Output classes.

Used to represent the output of a language model call and the output of a chat.

The top container for information is the `LLMResult` object. `LLMResult` is used by both
chat models and LLMs. This object contains the output of the language model and any
additional information that the model provider wants to return.

When invoking models via the standard runnable methods (e.g. invoke, batch, etc.):

- Chat models will return `AIMessage` objects.
- LLMs will return regular text strings.

In addition, users can access the raw output of either LLMs or chat models via
callbacks. The `on_chat_model_end` and `on_llm_end` callbacks will return an `LLMResult`
object containing the generated outputs and any additional information returned by the
model provider.

In general, if information is already available in the AIMessage object, it is
recommended to access it from there rather than from the `LLMResult` object.

## Methods

- [`import_attr()`](https://reference.langchain.com/python/langchain-core/outputs/import_attr)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/outputs/__init__.py)
