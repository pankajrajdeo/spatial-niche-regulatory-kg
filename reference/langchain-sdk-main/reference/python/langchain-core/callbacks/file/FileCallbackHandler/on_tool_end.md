---
title: "on_tool_end"
description: "Handle tool end by writing the output with optional prefixes."
source: "https://reference.langchain.com/python/langchain-core/callbacks/file/FileCallbackHandler/on_tool_end"
category: "reference"
tags: [reference, langchain-core, callbacks, file, filecallbackhandler, on_tool_end]
---

# on_tool_end

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/callbacks/file/FileCallbackHandler/on_tool_end)

Handle tool end by writing the output with optional prefixes.

## Signature

```python
on_tool_end(
    self,
    output: str,
    color: str | None = None,
    observation_prefix: str | None = None,
    llm_prefix: str | None = None,
    **kwargs: Any = {},
) -> None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `output` | `str` | Yes | The tool output to write. |
| `color` | `str \| None` | No | Color override for this specific output.  If `None`, uses `self.color`. (default: `None`) |
| `observation_prefix` | `str \| None` | No | Optional prefix to write before the output. (default: `None`) |
| `llm_prefix` | `str \| None` | No | Optional prefix to write after the output. (default: `None`) |
| `**kwargs` | `Any` | No | Additional keyword arguments. (default: `{}`) |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/callbacks/file.py#L208)
