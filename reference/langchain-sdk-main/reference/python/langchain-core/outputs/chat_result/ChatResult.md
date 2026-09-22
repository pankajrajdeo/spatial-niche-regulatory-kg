---
title: "ChatResult"
description: "Use to represent the result of a chat model call with a single prompt."
source: "https://reference.langchain.com/python/langchain-core/outputs/chat_result/ChatResult"
category: "reference"
tags: [reference, langchain-core, outputs, chat_result, chatresult]
---

# ChatResult

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/outputs/chat_result/ChatResult)

Use to represent the result of a chat model call with a single prompt.

This container is used internally by some implementations of chat model, it will
eventually be mapped to a more general `LLMResult` object, and  then projected into
an `AIMessage` object.

LangChain users working with chat models will usually access information via
`AIMessage` (returned from runnable interfaces) or `LLMResult` (available via
callbacks). Please refer the `AIMessage` and `LLMResult` schema documentation for
more information.

## Signature

```python
ChatResult()
```

## Extends

- `BaseModel`

## Properties

- `generations`
- `llm_output`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/outputs/chat_result.py#L10)
