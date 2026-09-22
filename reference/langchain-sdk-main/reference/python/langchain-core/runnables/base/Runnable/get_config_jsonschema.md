---
title: "get_config_jsonschema"
description: "Get a JSON schema that represents the config of the Runnable."
source: "https://reference.langchain.com/python/langchain-core/runnables/base/Runnable/get_config_jsonschema"
category: "reference"
tags: [reference, langchain-core, runnables, base, runnable, get_config_jsonschema]
---

# get_config_jsonschema

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/base/Runnable/get_config_jsonschema)

Get a JSON schema that represents the config of the `Runnable`.

## Signature

```python
get_config_jsonschema(
    self,
    *,
    include: Sequence[str] | None = None,
) -> dict[str, Any]
```

## Description

!!! version-added "Added in `langchain-core` 0.3.0"

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `include` | `Sequence[str] \| None` | No | A list of fields to include in the config schema. (default: `None`) |

## Returns

`dict[str, Any]`

A JSON schema that represents the config of the `Runnable`.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/runnables/base.py#L577)
