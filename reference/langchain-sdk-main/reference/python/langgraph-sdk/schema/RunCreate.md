---
title: "RunCreate"
description: "Defines the parameters for initiating a background run."
source: "https://reference.langchain.com/python/langgraph-sdk/schema/RunCreate"
category: "reference"
tags: [reference, langgraph-sdk, schema, runcreate]
---

# RunCreate

> **Class** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/schema/RunCreate)

Defines the parameters for initiating a background run.

## Signature

```python
RunCreate()
```

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    thread_id: str | None,
    assistant_id: str,
    input: dict | None,
    metadata: dict | None,
    config: Config | None,
    context: Context | None,
    checkpoint_id: str | None,
    interrupt_before: list[str] | None,
    interrupt_after: list[str] | None,
    webhook: str | None,
    multitask_strategy: MultitaskStrategy | None,
)
```

| Name | Type |
|------|------|
| `thread_id` | `str \| None` |
| `assistant_id` | `str` |
| `input` | `dict \| None` |
| `metadata` | `dict \| None` |
| `config` | `Config \| None` |
| `context` | `Context \| None` |
| `checkpoint_id` | `str \| None` |
| `interrupt_before` | `list[str] \| None` |
| `interrupt_after` | `list[str] \| None` |
| `webhook` | `str \| None` |
| `multitask_strategy` | `MultitaskStrategy \| None` |

## Properties

- `thread_id`
- `assistant_id`
- `input`
- `metadata`
- `config`
- `context`
- `checkpoint_id`
- `interrupt_before`
- `interrupt_after`
- `webhook`
- `multitask_strategy`

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/d5f4b2aa960940effc8430165ab3604038e817af/libs/sdk-py/langgraph_sdk/schema.py#L522)
