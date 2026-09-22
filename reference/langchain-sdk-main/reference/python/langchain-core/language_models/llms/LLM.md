---
title: "LLM"
description: "Simple interface for implementing a custom LLM."
source: "https://reference.langchain.com/python/langchain-core/language_models/llms/LLM"
category: "reference"
tags: [reference, langchain-core, language_models, llms, llm]
---

# LLM

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/language_models/llms/LLM)

Simple interface for implementing a custom LLM.

You should subclass this class and implement the following:

- `_call` method: Run the LLM on the given prompt and input (used by `invoke`).
- `_identifying_params` property: Return a dictionary of the identifying parameters
    This is critical for caching and tracing purposes. Identifying parameters
    is a dict that identifies the LLM.
    It should mostly include a `model_name`.

Optional: Override the following methods to provide more optimizations:

- `_acall`: Provide a native async version of the `_call` method.
    If not provided, will delegate to the synchronous version using
    `run_in_executor`. (Used by `ainvoke`).
- `_stream`: Stream the LLM on the given prompt and input.
    `stream` will use `_stream` if provided, otherwise it
    use `_call` and output will arrive in one chunk.
- `_astream`: Override to provide a native async version of the `_stream` method.
    `astream` will use `_astream` if provided, otherwise it will implement
    a fallback behavior that will use `_stream` if `_stream` is implemented,
    and use `_acall` if `_stream` is not implemented.

## Signature

```python
LLM(
    self,
    *args: Any = (),
    **kwargs: Any = {},
)
```

## Extends

- `BaseLLM`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/language_models/llms.py#L1442)
