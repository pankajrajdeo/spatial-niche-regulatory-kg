---
title: "on_text"
description: "Run when a text is received."
source: "https://reference.langchain.com/python/langchain-core/callbacks/manager/RunManager/on_text"
category: "reference"
tags: [reference, langchain-core, callbacks, manager, runmanager, on_text]
---

# on_text

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/callbacks/manager/RunManager/on_text)

Run when a text is received.

## Signature

```python
on_text(
    self,
    text: str,
    **kwargs: Any = {},
) -> None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `text` | `str` | Yes | The received text. |
| `**kwargs` | `Any` | No | Additional keyword arguments. (default: `{}`) |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/callbacks/manager.py#L549)
