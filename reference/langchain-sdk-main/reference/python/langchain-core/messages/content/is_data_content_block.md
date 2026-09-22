---
title: "is_data_content_block"
description: "Check if the provided content block is a data content block."
source: "https://reference.langchain.com/python/langchain-core/messages/content/is_data_content_block"
category: "reference"
tags: [reference, langchain-core, messages, content, is_data_content_block]
---

# is_data_content_block

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/messages/content/is_data_content_block)

Check if the provided content block is a data content block.

Returns True for both v0 (old-style) and v1 (new-style) multimodal data blocks.

## Signature

```python
is_data_content_block(
    block: dict[str, Any],
) -> bool
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `block` | `dict[str, Any]` | Yes | The content block to check. |

## Returns

`bool`

`True` if the content block is a data content block, `False` otherwise.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/messages/content.py#L908)
