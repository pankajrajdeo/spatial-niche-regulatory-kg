---
title: "merge_configs"
description: "Merge multiple configs into one."
source: "https://reference.langchain.com/python/langgraph/_internal/_config/merge_configs"
category: "reference"
tags: [reference, langgraph, internal, config, merge_configs]
---

# merge_configs

> **Function** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/_internal/_config/merge_configs)

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

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/644815f9e5bc52ad8f7a5227a456227e9c3e639b/libs/langgraph/langgraph/_internal/_config.py#L147)
