---
title: "on_llm_new_token"
description: "Run on new LLM token. Only available when streaming is enabled."
source: "https://reference.langchain.com/python/langchain-core/callbacks/streaming_stdout/StreamingStdOutCallbackHandler/on_llm_new_token"
category: "reference"
tags: [reference, langchain-core, callbacks, streaming_stdout, streamingstdoutcallbackhandler, on_llm_new_token]
---

# on_llm_new_token

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/callbacks/streaming_stdout/StreamingStdOutCallbackHandler/on_llm_new_token)

Run on new LLM token. Only available when streaming is enabled.

## Signature

```python
on_llm_new_token(
    self,
    token: str | list[str | dict[str, Any]],
    **kwargs: Any = {},
) -> None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `token` | `str \| list[str \| dict[str, Any]]` | Yes | The new token, or a list of content blocks. |
| `**kwargs` | `Any` | No | Additional keyword arguments. (default: `{}`) |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/callbacks/streaming_stdout.py#L49)
