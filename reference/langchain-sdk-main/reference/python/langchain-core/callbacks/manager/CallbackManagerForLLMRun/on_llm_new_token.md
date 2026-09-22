---
title: "on_llm_new_token"
description: "Run when LLM generates a new token."
source: "https://reference.langchain.com/python/langchain-core/callbacks/manager/CallbackManagerForLLMRun/on_llm_new_token"
category: "reference"
tags: [reference, langchain-core, callbacks, manager, callbackmanagerforllmrun, on_llm_new_token]
---

# on_llm_new_token

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/callbacks/manager/CallbackManagerForLLMRun/on_llm_new_token)

Run when LLM generates a new token.

## Signature

```python
on_llm_new_token(
    self,
    token: str | list[str | dict[str, Any]],
    *,
    chunk: GenerationChunk | ChatGenerationChunk | None = None,
    **kwargs: Any = {},
) -> None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `token` | `str \| list[str \| dict[str, Any]]` | Yes | The new token, or a list of content blocks. |
| `chunk` | `GenerationChunk \| ChatGenerationChunk \| None` | No | The chunk. (default: `None`) |
| `**kwargs` | `Any` | No | Additional keyword arguments. (default: `{}`) |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/callbacks/manager.py#L708)
