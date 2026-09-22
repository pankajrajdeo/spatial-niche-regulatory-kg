---
title: "patch_config"
description: "Patch a config with new values."
source: "https://reference.langchain.com/python/langchain-core/runnables/retry/patch_config"
category: "reference"
tags: [reference, langchain-core, runnables, retry, patch_config]
---

# patch_config

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/config/patch_config)

Patch a config with new values.

## Signature

```python
patch_config(
    config: RunnableConfig | None,
    *,
    callbacks: BaseCallbackManager | None = None,
    recursion_limit: int | None = None,
    max_concurrency: int | None = None,
    run_name: str | None = None,
    configurable: dict[str, Any] | None = None,
) -> RunnableConfig
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `config` | `RunnableConfig \| None` | Yes | The config to patch. |
| `callbacks` | `BaseCallbackManager \| None` | No | The callbacks to set. (default: `None`) |
| `recursion_limit` | `int \| None` | No | The recursion limit to set. (default: `None`) |
| `max_concurrency` | `int \| None` | No | The max concurrency to set. (default: `None`) |
| `run_name` | `str \| None` | No | The run name to set. (default: `None`) |
| `configurable` | `dict[str, Any] \| None` | No | The configurable to set. (default: `None`) |

## Returns

`RunnableConfig`

The patched config.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/runnables/config.py#L357)
