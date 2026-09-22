---
title: "utils"
description: "Module contains utility functions for working with messages."
source: "https://reference.langchain.com/python/langchain-core/messages/utils"
category: "reference"
tags: [reference, langchain-core, messages, utils]
---

# utils

> **Module** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/messages/utils)

Module contains utility functions for working with messages.

Some examples of what you can do with these functions include:

* Convert messages to strings (serialization)
* Convert messages from dicts to Message objects (deserialization)
* Filter messages from a list of messages based on name, type or id etc.

## Properties

- `logger`
- `AnyMessage`

## Methods

- [`create_message()`](https://reference.langchain.com/python/langchain-core/messages/utils/create_message)
- [`convert_to_openai_data_block()`](https://reference.langchain.com/python/langchain-core/messages/utils/convert_to_openai_data_block)
- [`is_data_content_block()`](https://reference.langchain.com/python/langchain-core/messages/utils/is_data_content_block)
- [`get_model_json_schema()`](https://reference.langchain.com/python/langchain-core/messages/utils/get_model_json_schema)
- [`get_buffer_string()`](https://reference.langchain.com/python/langchain-core/messages/utils/get_buffer_string)
- [`messages_from_dict()`](https://reference.langchain.com/python/langchain-core/messages/utils/messages_from_dict)
- [`message_chunk_to_message()`](https://reference.langchain.com/python/langchain-core/messages/utils/message_chunk_to_message)
- [`convert_to_messages()`](https://reference.langchain.com/python/langchain-core/messages/utils/convert_to_messages)
- [`filter_messages()`](https://reference.langchain.com/python/langchain-core/messages/utils/filter_messages)
- [`merge_message_runs()`](https://reference.langchain.com/python/langchain-core/messages/utils/merge_message_runs)
- [`trim_messages()`](https://reference.langchain.com/python/langchain-core/messages/utils/trim_messages)
- [`convert_to_openai_messages()`](https://reference.langchain.com/python/langchain-core/messages/utils/convert_to_openai_messages)
- [`count_tokens_approximately()`](https://reference.langchain.com/python/langchain-core/messages/utils/count_tokens_approximately)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/messages/utils.py)
