---
title: "get_from_env"
description: "Get a value from a dictionary or an environment variable."
source: "https://reference.langchain.com/python/langchain-core/utils/env/get_from_env"
category: "reference"
tags: [reference, langchain-core, utils, env, get_from_env]
---

# get_from_env

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/utils/env/get_from_env)

Get a value from a dictionary or an environment variable.

## Signature

```python
get_from_env(
    key: str,
    env_key: str,
    default: str | None = None,
) -> str
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `key` | `str` | Yes | The key to look up in the dictionary. |
| `env_key` | `str` | Yes | The environment variable to look up if the key is not in the dictionary. |
| `default` | `str \| None` | No | The default value to return if the key is not in the dictionary or the environment. (default: `None`) |

## Returns

`str`

The value of the key.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/utils/env.py#L60)
