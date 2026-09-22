---
title: "flatten"
description: "Flatten generations into a single list."
source: "https://reference.langchain.com/python/langchain-core/outputs/llm_result/LLMResult/flatten"
category: "reference"
tags: [reference, langchain-core, outputs, llm_result, llmresult, flatten]
---

# flatten

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/outputs/llm_result/LLMResult/flatten)

Flatten generations into a single list.

Unpack `list[list[Generation]] -> list[LLMResult]` where each returned
`LLMResult` contains only a single `Generation`. If token usage information is
available, it is kept only for the `LLMResult` corresponding to the top-choice
`Generation`, to avoid over-counting of token usage downstream.

## Signature

```python
flatten(
    self,
) -> list[LLMResult]
```

## Returns

`list[LLMResult]`

List of `LLMResult` objects where each returned `LLMResult` contains a
single `Generation`.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/outputs/llm_result.py#L60)
