---
title: "on_llm_new_token"
description: "Run on new output token. Only available when streaming is enabled."
source: "https://reference.langchain.com/python/langchain-core/callbacks/base/AsyncCallbackHandler/on_llm_new_token"
category: "reference"
tags: [reference, langchain-core, callbacks, base, asynccallbackhandler, on_llm_new_token]
---

# on_llm_new_token

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/callbacks/base/AsyncCallbackHandler/on_llm_new_token)

Run on new output token. Only available when streaming is enabled.

For both chat models and non-chat models (legacy text completion LLMs).

## Signature

```python
on_llm_new_token(
    self,
    token: str | list[str | dict[str, Any]],
    *,
    chunk: GenerationChunk | ChatGenerationChunk | None = None,
    run_id: UUID,
    parent_run_id: UUID | None = None,
    tags: list[str] | None = None,
    **kwargs: Any = {},
) -> None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `token` | `str \| list[str \| dict[str, Any]]` | Yes | The new token, or a list of content blocks. |
| `chunk` | `GenerationChunk \| ChatGenerationChunk \| None` | No | The new generated chunk, containing content and other information. (default: `None`) |
| `run_id` | `UUID` | Yes | The ID of the current run. |
| `parent_run_id` | `UUID \| None` | No | The ID of the parent run. (default: `None`) |
| `tags` | `list[str] \| None` | No | The tags. (default: `None`) |
| `**kwargs` | `Any` | No | Additional keyword arguments. (default: `{}`) |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/callbacks/base.py#L632)
