---
title: "agenerate"
description: "Asynchronously pass a sequence of prompts to a model and return generations."
source: "https://reference.langchain.com/python/langchain-core/language_models/llms/BaseLLM/agenerate"
category: "reference"
tags: [reference, langchain-core, language_models, llms, basellm, agenerate]
---

# agenerate

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/language_models/llms/BaseLLM/agenerate)

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
    prompts: list[str],
    stop: list[str] | None = None,
    callbacks: Callbacks | list[Callbacks] | None = None,
    *,
    tags: list[str] | list[list[str]] | None = None,
    metadata: builtins.dict[str, Any] | list[builtins.dict[str, Any]] | None = None,
    run_name: str | list[str] | None = None,
    run_id: uuid.UUID | list[uuid.UUID | None] | None = None,
    **kwargs: Any = {},
) -> LLMResult
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `prompts` | `list[str]` | Yes | List of string prompts. |
| `stop` | `list[str] \| None` | No | Stop words to use when generating.  Model output is cut off at the first occurrence of any of these substrings. (default: `None`) |
| `callbacks` | `Callbacks \| list[Callbacks] \| None` | No | `Callbacks` to pass through.  Used for executing additional functionality, such as logging or streaming, throughout generation. (default: `None`) |
| `tags` | `list[str] \| list[list[str]] \| None` | No | List of tags to associate with each prompt. If provided, the length of the list must match the length of the prompts list. (default: `None`) |
| `metadata` | `builtins.dict[str, Any] \| list[builtins.dict[str, Any]] \| None` | No | List of metadata dictionaries to associate with each prompt. If provided, the length of the list must match the length of the prompts list. (default: `None`) |
| `run_name` | `str \| list[str] \| None` | No | List of run names to associate with each prompt. If provided, the length of the list must match the length of the prompts list. (default: `None`) |
| `run_id` | `uuid.UUID \| list[uuid.UUID \| None] \| None` | No | List of run IDs to associate with each prompt. If provided, the length of the list must match the length of the prompts list. (default: `None`) |
| `**kwargs` | `Any` | No | Arbitrary additional keyword arguments.  These are usually passed to the model provider API call. (default: `{}`) |

## Returns

`LLMResult`

An `LLMResult`, which contains a list of candidate `Generations` for each
input prompt and additional model provider-specific output.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/language_models/llms.py#L1135)
