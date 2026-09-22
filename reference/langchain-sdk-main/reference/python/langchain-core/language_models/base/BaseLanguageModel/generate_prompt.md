---
title: "generate_prompt"
description: "Pass a sequence of prompts to the model and return model generations."
source: "https://reference.langchain.com/python/langchain-core/language_models/base/BaseLanguageModel/generate_prompt"
category: "reference"
tags: [reference, langchain-core, language_models, base, baselanguagemodel, generate_prompt]
---

# generate_prompt

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/language_models/base/BaseLanguageModel/generate_prompt)

Pass a sequence of prompts to the model and return model generations.

This method should make use of batched calls for models that expose a batched
API.

Use this method when you want to:

1. Take advantage of batched calls,
2. Need more output from the model than just the top generated value,
3. Are building chains that are agnostic to the underlying language model
    type (e.g., pure text completion models vs chat models).

## Signature

```python
generate_prompt(
    self,
    prompts: list[PromptValue],
    stop: list[str] | None = None,
    callbacks: Callbacks = None,
    **kwargs: Any = {},
) -> LLMResult
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `prompts` | `list[PromptValue]` | Yes | List of `PromptValue` objects.  A `PromptValue` is an object that can be converted to match the format of any language model (string for pure text generation models and `BaseMessage` objects for chat models). |
| `stop` | `list[str] \| None` | No | Stop words to use when generating.  Model output is cut off at the first occurrence of any of these substrings. (default: `None`) |
| `callbacks` | `Callbacks` | No | `Callbacks` to pass through.  Used for executing additional functionality, such as logging or streaming, throughout generation. (default: `None`) |
| `**kwargs` | `Any` | No | Arbitrary additional keyword arguments.  These are usually passed to the model provider API call. (default: `{}`) |

## Returns

`LLMResult`

An `LLMResult`, which contains a list of candidate `Generation` objects for
each input prompt and additional model provider-specific output.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/language_models/base.py#L317)
