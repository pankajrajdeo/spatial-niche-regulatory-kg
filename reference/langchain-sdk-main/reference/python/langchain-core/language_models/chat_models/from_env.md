---
title: "from_env"
description: "Create a factory method that gets a value from an environment variable."
source: "https://reference.langchain.com/python/langchain-core/language_models/chat_models/from_env"
category: "reference"
tags: [reference, langchain-core, language_models, chat_models, from_env]
---

# from_env

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/utils/utils/from_env)

Create a factory method that gets a value from an environment variable.

## Signature

```python
from_env(
    key: str | Sequence[str],
    /,
    *,
    default: str | _NoDefaultType | None = _NoDefault,
    error_message: str | None = None,
) -> Callable[[], str] | Callable[[], str | None]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `key` | `str \| Sequence[str]` | Yes | The environment variable to look up.  If a list of keys is provided, the first key found in the environment will be used. If no key is found, the default value will be used if set, otherwise an error will be raised. |
| `default` | `str \| _NoDefaultType \| None` | No | The default value to return if the environment variable is not set. (default: `_NoDefault`) |
| `error_message` | `str \| None` | No | The error message which will be raised if the key is not found and no default value is provided.  This will be raised as a ValueError. (default: `None`) |

## Returns

`Callable[[], str] | Callable[[], str | None]`

Factory method that will look up the value from the environment.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/utils/utils.py#L368)
