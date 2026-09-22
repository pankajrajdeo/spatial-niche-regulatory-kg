---
title: "on_tool_start"
description: "Run when the tool starts running."
source: "https://reference.langchain.com/python/langchain-core/callbacks/streaming_stdout/StreamingStdOutCallbackHandler/on_tool_start"
category: "reference"
tags: [reference, langchain-core, callbacks, streaming_stdout, streamingstdoutcallbackhandler, on_tool_start]
---

# on_tool_start

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/callbacks/streaming_stdout/StreamingStdOutCallbackHandler/on_tool_start)

Run when the tool starts running.

## Signature

```python
on_tool_start(
    self,
    serialized: dict[str, Any],
    input_str: str,
    **kwargs: Any = {},
) -> None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `serialized` | `dict[str, Any]` | Yes | The serialized tool. |
| `input_str` | `str` | Yes | The input string. |
| `**kwargs` | `Any` | No | Additional keyword arguments. (default: `{}`) |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/callbacks/streaming_stdout.py#L105)
