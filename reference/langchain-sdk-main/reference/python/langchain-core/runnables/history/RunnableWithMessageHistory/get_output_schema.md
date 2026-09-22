---
title: "get_output_schema"
description: "Get a Pydantic model that can be used to validate output to the Runnable."
source: "https://reference.langchain.com/python/langchain-core/runnables/history/RunnableWithMessageHistory/get_output_schema"
category: "reference"
tags: [reference, langchain-core, runnables, history, runnablewithmessagehistory, get_output_schema]
---

# get_output_schema

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/history/RunnableWithMessageHistory/get_output_schema)

Get a Pydantic model that can be used to validate output to the `Runnable`.

`Runnable` objects that leverage the `configurable_fields` and
`configurable_alternatives` methods will have a dynamic output schema that
depends on which configuration the `Runnable` is invoked with.

This method allows to get an output schema for a specific configuration.

## Signature

```python
get_output_schema(
    self,
    config: RunnableConfig | None = None,
) -> type[BaseModel]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `config` | `RunnableConfig \| None` | No | A config to use when generating the schema. (default: `None`) |

## Returns

`type[BaseModel]`

A Pydantic model that can be used to validate output.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/runnables/history.py#L419)
