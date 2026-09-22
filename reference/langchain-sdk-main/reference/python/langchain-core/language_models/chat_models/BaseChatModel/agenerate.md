---
title: "agenerate"
description: "Asynchronously pass a sequence of prompts to a model and return generations."
source: "https://reference.langchain.com/python/langchain-core/language_models/chat_models/BaseChatModel/agenerate"
category: "reference"
tags: [reference, langchain-core, language_models, chat_models, basechatmodel, agenerate]
---

# agenerate

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/language_models/chat_models/BaseChatModel/agenerate)

Asynchronously pass a sequence of prompts to a model and return generations.

This method should make use of batched calls for models that expose a batched
API.

Use this method when you want to:

1. Take advantage of batched calls,
2. Need more output from the model than just the top generated value,
3. Are building chains that are agnostic to the underlying language model
    type (e.g., pure text completion models vs chat models).

## Signature

```python
agenerate(
    self,
    messages: list[list[BaseMessage]],
    stop: list[str] | None = None,
    callbacks: Callbacks = None,
    *,
    tags: list[str] | None = None,
    metadata: builtins.dict[str, Any] | None = None,
    run_name: str | None = None,
    run_id: uuid.UUID | None = None,
    **kwargs: Any = {},
) -> LLMResult
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `messages` | `list[list[BaseMessage]]` | Yes | List of list of messages. |
| `stop` | `list[str] \| None` | No | Stop words to use when generating.  Model output is cut off at the first occurrence of any of these substrings. (default: `None`) |
| `callbacks` | `Callbacks` | No | `Callbacks` to pass through.  Used for executing additional functionality, such as logging or streaming, throughout generation. (default: `None`) |
| `tags` | `list[str] \| None` | No | The tags to apply. (default: `None`) |
| `metadata` | `builtins.dict[str, Any] \| None` | No | The metadata to apply. (default: `None`) |
| `run_name` | `str \| None` | No | The name of the run. (default: `None`) |
| `run_id` | `uuid.UUID \| None` | No | The ID of the run. (default: `None`) |
| `**kwargs` | `Any` | No | Arbitrary additional keyword arguments.  These are usually passed to the model provider API call. (default: `{}`) |

## Returns

`LLMResult`

An `LLMResult`, which contains a list of candidate `Generations` for each
input prompt and additional model provider-specific output.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/language_models/chat_models.py#L1718)
