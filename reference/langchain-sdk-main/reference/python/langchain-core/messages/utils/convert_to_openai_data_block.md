---
title: "convert_to_openai_data_block"
description: "Format standard data content block to format expected by OpenAI."
source: "https://reference.langchain.com/python/langchain-core/messages/utils/convert_to_openai_data_block"
category: "reference"
tags: [reference, langchain-core, messages, utils, convert_to_openai_data_block]
---

# convert_to_openai_data_block

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/messages/block_translators/openai/convert_to_openai_data_block)

Format standard data content block to format expected by OpenAI.

"Standard data content block" can include old-style LangChain v0 blocks
(URLContentBlock, Base64ContentBlock, IDContentBlock) or new ones.

## Signature

```python
convert_to_openai_data_block(
    block: dict[str, Any],
    api: Literal['chat/completions', 'responses'] = 'chat/completions',
) -> dict[str, Any]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `block` | `dict[str, Any]` | Yes | The content block to convert. |
| `api` | `Literal['chat/completions', 'responses']` | No | The OpenAI API being targeted. Either "chat/completions" or "responses". (default: `'chat/completions'`) |

## Returns

`dict[str, Any]`

The formatted content block.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/messages/block_translators/openai.py#L58)
