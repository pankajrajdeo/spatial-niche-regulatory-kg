---
title: "BaseLLM"
description: "Base LLM abstract interface."
source: "https://reference.langchain.com/python/langchain-core/language_models/llms/BaseLLM"
category: "reference"
tags: [reference, langchain-core, language_models, llms, basellm]
---

# BaseLLM

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/language_models/llms/BaseLLM)

Base LLM abstract interface.

It should take in a prompt and return a string.

## Signature

```python
BaseLLM(
    self,
    *args: Any = (),
    **kwargs: Any = {},
)
```

## Extends

- `BaseLanguageModel[str]`
- `ABC`

## Properties

- `model_config`
- `OutputType`

## Methods

- [`invoke()`](https://reference.langchain.com/python/langchain-core/language_models/llms/BaseLLM/invoke)
- [`ainvoke()`](https://reference.langchain.com/python/langchain-core/language_models/llms/BaseLLM/ainvoke)
- [`batch()`](https://reference.langchain.com/python/langchain-core/language_models/llms/BaseLLM/batch)
- [`abatch()`](https://reference.langchain.com/python/langchain-core/language_models/llms/BaseLLM/abatch)
- [`stream()`](https://reference.langchain.com/python/langchain-core/language_models/llms/BaseLLM/stream)
- [`astream()`](https://reference.langchain.com/python/langchain-core/language_models/llms/BaseLLM/astream)
- [`generate_prompt()`](https://reference.langchain.com/python/langchain-core/language_models/llms/BaseLLM/generate_prompt)
- [`agenerate_prompt()`](https://reference.langchain.com/python/langchain-core/language_models/llms/BaseLLM/agenerate_prompt)
- [`generate()`](https://reference.langchain.com/python/langchain-core/language_models/llms/BaseLLM/generate)
- [`agenerate()`](https://reference.langchain.com/python/langchain-core/language_models/llms/BaseLLM/agenerate)
- [`dict()`](https://reference.langchain.com/python/langchain-core/language_models/llms/BaseLLM/dict)
- [`asdict()`](https://reference.langchain.com/python/langchain-core/language_models/llms/BaseLLM/asdict)
- [`save()`](https://reference.langchain.com/python/langchain-core/language_models/llms/BaseLLM/save)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/language_models/llms.py#L296)
