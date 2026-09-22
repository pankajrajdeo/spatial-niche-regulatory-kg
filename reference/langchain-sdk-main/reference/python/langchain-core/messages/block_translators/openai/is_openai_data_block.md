---
title: "is_openai_data_block"
description: "Check whether a block contains multimodal data in OpenAI Chat Completions format."
source: "https://reference.langchain.com/python/langchain-core/messages/block_translators/openai/is_openai_data_block"
category: "reference"
tags: [reference, langchain-core, messages, block_translators, openai, is_openai_data_block]
---

# is_openai_data_block

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/language_models/_utils/is_openai_data_block)

Check whether a block contains multimodal data in OpenAI Chat Completions format.

Supports both data and ID-style blocks (e.g. `'file_data'` and `'file_id'`)

If additional keys are present, they are ignored / will not affect outcome as long
as the required keys are present and valid.

## Signature

```python
is_openai_data_block(
    block: dict[str, Any],
    filter_: Literal['image', 'audio', 'file'] | None = None,
) -> bool
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `block` | `dict[str, Any]` | Yes | The content block to check. |
| `filter_` | `Literal['image', 'audio', 'file'] \| None` | No | If provided, only return True for blocks matching this specific type. - "image": Only match image_url blocks - "audio": Only match input_audio blocks - "file": Only match file blocks If `None`, match any valid OpenAI data block type. Note that this means that if the block has a valid OpenAI data type but the filter_ is set to a different type, this function will return False. (default: `None`) |

## Returns

`bool`

`True` if the block is a valid OpenAI data block and matches the filter_

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/language_models/_utils.py#L33)
