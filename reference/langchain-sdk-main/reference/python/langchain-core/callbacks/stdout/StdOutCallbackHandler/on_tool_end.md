---
title: "on_tool_end"
description: "If not the final action, print out observation."
source: "https://reference.langchain.com/python/langchain-core/callbacks/stdout/StdOutCallbackHandler/on_tool_end"
category: "reference"
tags: [reference, langchain-core, callbacks, stdout, stdoutcallbackhandler, on_tool_end]
---

# on_tool_end

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/callbacks/stdout/StdOutCallbackHandler/on_tool_end)

If not the final action, print out observation.

## Signature

```python
on_tool_end(
    self,
    output: Any,
    color: str | None = None,
    observation_prefix: str | None = None,
    llm_prefix: str | None = None,
    **kwargs: Any = {},
) -> None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `output` | `Any` | Yes | The output to print. |
| `color` | `str \| None` | No | The color to use for the text. (default: `None`) |
| `observation_prefix` | `str \| None` | No | The observation prefix. (default: `None`) |
| `llm_prefix` | `str \| None` | No | The LLM prefix. (default: `None`) |
| `**kwargs` | `Any` | No | Additional keyword arguments. (default: `{}`) |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/callbacks/stdout.py#L69)
