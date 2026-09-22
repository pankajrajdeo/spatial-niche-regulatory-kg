---
title: "count_tokens_approximately"
description: "Approximate the total number of tokens in messages."
source: "https://reference.langchain.com/python/langchain-core/messages/utils/count_tokens_approximately"
category: "reference"
tags: [reference, langchain-core, messages, utils, count_tokens_approximately]
---

# count_tokens_approximately

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/messages/utils/count_tokens_approximately)

Approximate the total number of tokens in messages.

The token count includes stringified message content, role, and (optionally) name.

- For AI messages, the token count also includes stringified tool calls.
- For tool messages, the token count also includes the tool call ID.
- For multimodal messages with images, applies a fixed token penalty per image
    instead of counting base64-encoded characters.
- If tools are provided, the token count also includes stringified tool schemas.

## Signature

```python
count_tokens_approximately(
    messages: Iterable[MessageLikeRepresentation],
    *,
    chars_per_token: float = 4.0,
    extra_tokens_per_message: float = 3.0,
    count_name: bool = True,
    tokens_per_image: int = 85,
    use_usage_metadata_scaling: bool = False,
    tools: list[BaseTool | dict[str, Any]] | None = None,
) -> int
```

## Description

**Note:**

This is a simple approximation that may not match the exact token count used by
specific models. For accurate counts, use model-specific tokenizers.

For multimodal messages containing images, a fixed token penalty is applied
per image instead of counting base64-encoded characters, which provides a
more realistic approximation.

!!! version-added "Added in `langchain-core` 0.3.46"

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `messages` | `Iterable[MessageLikeRepresentation]` | Yes | List of messages to count tokens for. |
| `chars_per_token` | `float` | No | Number of characters per token to use for the approximation. One token corresponds to ~4 chars for common English text. You can also specify `float` values for more fine-grained control. [See more here](https://platform.openai.com/tokenizer). (default: `4.0`) |
| `extra_tokens_per_message` | `float` | No | Number of extra tokens to add per message, e.g. special tokens, including beginning/end of message. You can also specify `float` values for more fine-grained control. [See more here](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_count_tokens_with_tiktoken.ipynb). (default: `3.0`) |
| `count_name` | `bool` | No | Whether to include message names in the count. (default: `True`) |
| `tokens_per_image` | `int` | No | Fixed token cost per image (default: 85, aligned with OpenAI's low-resolution image token cost). (default: `85`) |
| `use_usage_metadata_scaling` | `bool` | No | If True, and all AI messages have consistent `response_metadata['model_provider']`, scale the approximate token count using the **most recent** AI message that has `usage_metadata['total_tokens']`. The scaling factor is: `AI_total_tokens / approx_tokens_up_to_that_AI_message` (default: `False`) |
| `tools` | `list[BaseTool \| dict[str, Any]] \| None` | No | List of tools to include in the token count. Each tool can be a `BaseTool` instance, a dict representing a tool schema, or a plain callable. `BaseTool` instances and callables are converted to OpenAI tool format before counting. (default: `None`) |

## Returns

`int`

Approximate number of tokens in the messages (and tools, if provided).

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/messages/utils.py#L2244)
