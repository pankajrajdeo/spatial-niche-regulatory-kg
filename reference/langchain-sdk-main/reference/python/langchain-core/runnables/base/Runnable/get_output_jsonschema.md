---
title: "get_output_jsonschema"
description: "Get a JSON schema that represents the output of the Runnable."
source: "https://reference.langchain.com/python/langchain-core/runnables/base/Runnable/get_output_jsonschema"
category: "reference"
tags: [reference, langchain-core, runnables, base, runnable, get_output_jsonschema]
---

# get_output_jsonschema

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/base/Runnable/get_output_jsonschema)

Get a JSON schema that represents the output of the `Runnable`.

## Signature

```python
get_output_jsonschema(
    self,
    config: RunnableConfig | None = None,
) -> dict[str, Any]
```

## Description

**Example:**

```python
from langchain_core.runnables import RunnableLambda

def add_one(x: int) -> int:
    return x + 1

runnable = RunnableLambda(add_one)

print(runnable.get_output_jsonschema())
```

!!! version-added "Added in `langchain-core` 0.3.0"

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `config` | `RunnableConfig \| None` | No | A config to use when generating the schema. (default: `None`) |

## Returns

`dict[str, Any]`

A JSON schema that represents the output of the `Runnable`.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/runnables/base.py#L499)
