---
title: "env_var_is_set"
description: "Check if an environment variable is set."
source: "https://reference.langchain.com/python/langchain-core/callbacks/manager/env_var_is_set"
category: "reference"
tags: [reference, langchain-core, callbacks, manager, env_var_is_set]
---

# env_var_is_set

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/utils/env/env_var_is_set)

Check if an environment variable is set.

## Signature

```python
env_var_is_set(
    env_var: str,
) -> bool
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `env_var` | `str` | Yes | The name of the environment variable. |

## Returns

`bool`

`True` if the environment variable is set, `False` otherwise.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/utils/env.py#L9)
