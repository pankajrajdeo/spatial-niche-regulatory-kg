---
title: "get_lc_namespace"
description: "Get the namespace of the LangChain object."
source: "https://reference.langchain.com/python/langchain-core/prompts/structured/StructuredPrompt/get_lc_namespace"
category: "reference"
tags: [reference, langchain-core, prompts, structured, structuredprompt, get_lc_namespace]
---

# get_lc_namespace

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/prompts/structured/StructuredPrompt/get_lc_namespace)

Get the namespace of the LangChain object.

For example, if the class is `langchain.llms.openai.OpenAI`, then the namespace
is `["langchain", "llms", "openai"]`

## Signature

```python
get_lc_namespace(
    cls,
) -> list[str]
```

## Returns

`list[str]`

The namespace of the LangChain object.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/prompts/structured.py#L84)
