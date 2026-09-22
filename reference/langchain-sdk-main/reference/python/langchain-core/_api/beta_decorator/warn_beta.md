---
title: "warn_beta"
description: "Display a standardized beta annotation."
source: "https://reference.langchain.com/python/langchain-core/_api/beta_decorator/warn_beta"
category: "reference"
tags: [reference, langchain-core, api, beta_decorator, warn_beta]
---

# warn_beta

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/_api/beta_decorator/warn_beta)

Display a standardized beta annotation.

## Signature

```python
warn_beta(
    *,
    message: str = '',
    name: str = '',
    obj_type: str = '',
    addendum: str = '',
) -> None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `message` | `str` | No | Override the default beta message.  The %(name)s, %(obj_type)s, %(addendum)s format specifiers will be replaced by the values of the respective arguments passed to this function. (default: `''`) |
| `name` | `str` | No | The name of the annotated object. (default: `''`) |
| `obj_type` | `str` | No | The object type being annotated. (default: `''`) |
| `addendum` | `str` | No | Additional text appended directly to the final message. (default: `''`) |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/_api/beta_decorator.py#L226)
