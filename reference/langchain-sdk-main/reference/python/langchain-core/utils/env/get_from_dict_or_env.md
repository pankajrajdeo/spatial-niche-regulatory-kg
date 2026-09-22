---
title: "get_from_dict_or_env"
description: "Get a value from a dictionary or an environment variable."
source: "https://reference.langchain.com/python/langchain-core/utils/env/get_from_dict_or_env"
category: "reference"
tags: [reference, langchain-core, utils, env, get_from_dict_or_env]
---

# get_from_dict_or_env

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/utils/env/get_from_dict_or_env)

Get a value from a dictionary or an environment variable.

## Signature

```python
get_from_dict_or_env(
    data: dict[str, Any],
    key: str | list[str],
    env_key: str,
    default: str | None = None,
) -> str
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `data` | `dict[str, Any]` | Yes | The dictionary to look up the key in. |
| `key` | `str \| list[str]` | Yes | The key to look up in the dictionary.  This can be a list of keys to try in order. |
| `env_key` | `str` | Yes | The environment variable to look up if the key is not in the dictionary. |
| `default` | `str \| None` | No | The default value to return if the key is not in the dictionary or the environment. (default: `None`) |

## Returns

`str`

The dict value or the environment variable value.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/utils/env.py#L26)
