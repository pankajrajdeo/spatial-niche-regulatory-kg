---
title: "on_text"
description: "Handle text output."
source: "https://reference.langchain.com/python/langchain-core/callbacks/file/FileCallbackHandler/on_text"
category: "reference"
tags: [reference, langchain-core, callbacks, file, filecallbackhandler, on_text]
---

# on_text

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/callbacks/file/FileCallbackHandler/on_text)

Handle text output.

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
| `text` | `str` | Yes | The text to write. |
| `color` | `str \| None` | No | Color override for this specific output.  If `None`, uses `self.color`. (default: `None`) |
| `end` | `str` | No | String appended after the text. (default: `''`) |
| `**kwargs` | `Any` | No | Additional keyword arguments. (default: `{}`) |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/callbacks/file.py#L235)
