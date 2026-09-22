---
title: "secret_from_env"
description: "Secret from env."
source: "https://reference.langchain.com/python/langchain-core/utils/utils/secret_from_env"
category: "reference"
tags: [reference, langchain-core, utils, secret_from_env]
---

# secret_from_env

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/utils/utils/secret_from_env)

Secret from env.

## Signature

```python
secret_from_env(
    key: str | Sequence[str],
    /,
    *,
    default: str | _NoDefaultType | None = _NoDefault,
    error_message: str | None = None,
) -> Callable[[], SecretStr | None] | Callable[[], SecretStr]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `key` | `str \| Sequence[str]` | Yes | The environment variable to look up. |
| `default` | `str \| _NoDefaultType \| None` | No | The default value to return if the environment variable is not set. (default: `_NoDefault`) |
| `error_message` | `str \| None` | No | The error message which will be raised if the key is not found and no default value is provided.  This will be raised as a `ValueError`. (default: `None`) |

## Returns

`Callable[[], SecretStr | None] | Callable[[], SecretStr]`

Factory method that will look up the secret from the environment.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/utils/utils.py#L442)
