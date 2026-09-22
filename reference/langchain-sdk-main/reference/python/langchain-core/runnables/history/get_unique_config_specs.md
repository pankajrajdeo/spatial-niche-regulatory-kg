---
title: "get_unique_config_specs"
description: "Get the unique config specs from a sequence of config specs."
source: "https://reference.langchain.com/python/langchain-core/runnables/history/get_unique_config_specs"
category: "reference"
tags: [reference, langchain-core, runnables, history, get_unique_config_specs]
---

# get_unique_config_specs

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/utils/get_unique_config_specs)

Get the unique config specs from a sequence of config specs.

## Signature

```python
get_unique_config_specs(
    specs: Iterable[ConfigurableFieldSpec],
) -> list[ConfigurableFieldSpec]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `specs` | `Iterable[ConfigurableFieldSpec]` | Yes | The config specs. |

## Returns

`list[ConfigurableFieldSpec]`

The unique config specs.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/runnables/utils.py#L680)
