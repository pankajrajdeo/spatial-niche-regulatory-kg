---
title: "get_num_tokens_from_messages"
description: "Get the number of tokens in the messages."
source: "https://reference.langchain.com/python/langchain-core/language_models/base/BaseLanguageModel/get_num_tokens_from_messages"
category: "reference"
tags: [reference, langchain-core, language_models, base, baselanguagemodel, get_num_tokens_from_messages]
---

# get_num_tokens_from_messages

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/language_models/base/BaseLanguageModel/get_num_tokens_from_messages)

Get the number of tokens in the messages.

Useful for checking if an input fits in a model's context window.

This should be overridden by model-specific implementations to provide accurate
token counts via model-specific tokenizers.

!!! note

    * The base implementation of `get_num_tokens_from_messages` ignores tool
        schemas.
    * The base implementation of `get_num_tokens_from_messages` adds additional
        prefixes to messages in represent user roles, which will add to the
        overall token count. Model-specific implementations may choose to
        handle this differently.

## Signature

```python
get_num_tokens_from_messages(
    self,
    messages: list[BaseMessage],
    tools: Sequence[Any] | None = None,
) -> int
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `messages` | `list[BaseMessage]` | Yes | The message inputs to tokenize. |
| `tools` | `Sequence[Any] \| None` | No | If provided, sequence of dict, `BaseModel`, function, or `BaseTool` objects to be converted to tool schemas. (default: `None`) |

## Returns

`int`

The sum of the number of tokens across the messages.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/language_models/base.py#L465)
