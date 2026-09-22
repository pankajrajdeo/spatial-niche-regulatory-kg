---
title: "on_text"
description: "Run when the agent ends."
source: "https://reference.langchain.com/python/langchain-core/callbacks/stdout/StdOutCallbackHandler/on_text"
category: "reference"
tags: [reference, langchain-core, callbacks, stdout, stdoutcallbackhandler, on_text]
---

# on_text

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/callbacks/stdout/StdOutCallbackHandler/on_text)

Run when the agent ends.

## Signature

```python
on_text(
    self,
    text: str,
    color: str | None = None,
    end: str = '',
    **kwargs: Any = {},
) -> None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `text` | `str` | Yes | The text to print. |
| `color` | `str \| None` | No | The color to use for the text. (default: `None`) |
| `end` | `str` | No | The end character to use. (default: `''`) |
| `**kwargs` | `Any` | No | Additional keyword arguments. (default: `{}`) |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/callbacks/stdout.py#L94)
