---
title: "llm_output"
description: "For arbitrary model provider-specific output."
source: "https://reference.langchain.com/python/langchain-core/outputs/llm_result/LLMResult/llm_output"
category: "reference"
tags: [reference, langchain-core, outputs, llm_result, llmresult, llm_output]
---

# llm_output

> **Attribute** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/outputs/llm_result/LLMResult/llm_output)

For arbitrary model provider-specific output.

This dictionary is a free-form dictionary that can contain any information that the
provider wants to return. It is not standardized and keys may vary by provider and
over time.

Users should generally avoid relying on this field and instead rely on accessing
relevant information from standardized fields present in AIMessage.

## Signature

```python
llm_output: dict[str, Any] | None = None
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/outputs/llm_result.py#L40)
