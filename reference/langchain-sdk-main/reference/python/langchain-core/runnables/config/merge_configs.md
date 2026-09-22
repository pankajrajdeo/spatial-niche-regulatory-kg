---
title: "merge_configs"
description: "Merge multiple configs into one."
source: "https://reference.langchain.com/python/langchain-core/runnables/config/merge_configs"
category: "reference"
tags: [reference, langchain-core, runnables, config, merge_configs]
---

# merge_configs

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/config/merge_configs)

Merge multiple configs into one.

## Signature

```python
merge_configs(
    *configs: RunnableConfig | None = (),
) -> RunnableConfig
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `*configs` | `RunnableConfig \| None` | No | The configs to merge. (default: `()`) |

## Returns

`RunnableConfig`

The merged config.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/runnables/config.py#L431)
