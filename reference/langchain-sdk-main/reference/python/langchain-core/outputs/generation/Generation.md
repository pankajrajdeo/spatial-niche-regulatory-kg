---
title: "Generation"
description: "A single text generation output."
source: "https://reference.langchain.com/python/langchain-core/outputs/generation/Generation"
category: "reference"
tags: [reference, langchain-core, outputs, generation]
---

# Generation

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/outputs/generation/Generation)

A single text generation output.

Generation represents the response from an "old-fashioned" LLM (string-in,
string-out) that generates regular text (not chat messages).

This model is used internally by chat model and will eventually be mapped to a more
general `LLMResult` object, and then projected into an `AIMessage` object.

LangChain users working with chat models will usually access information via
`AIMessage` (returned from runnable interfaces) or `LLMResult` (available via
callbacks). Please refer to `AIMessage` and `LLMResult` for more information.

## Signature

```python
Generation(
    self,
    *args: Any = (),
    **kwargs: Any = {},
)
```

## Extends

- `Serializable`

## Properties

- `text`
- `generation_info`
- `type`

## Methods

- [`is_lc_serializable()`](https://reference.langchain.com/python/langchain-core/outputs/generation/Generation/is_lc_serializable)
- [`get_lc_namespace()`](https://reference.langchain.com/python/langchain-core/outputs/generation/Generation/get_lc_namespace)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/outputs/generation.py#L11)
