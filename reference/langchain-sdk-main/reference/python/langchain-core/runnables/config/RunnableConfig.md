---
title: "RunnableConfig"
description: "Configuration for a Runnable."
source: "https://reference.langchain.com/python/langchain-core/runnables/config/RunnableConfig"
category: "reference"
tags: [reference, langchain-core, runnables, config, runnableconfig]
---

# RunnableConfig

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/config/RunnableConfig)

Configuration for a `Runnable`.

!!! note Custom values

    The `TypedDict` has `total=False` set intentionally to:

    - Allow partial configs to be created and merged together via `merge_configs`
    - Support config propagation from parent to child runnables via
        `var_child_runnable_config` (a `ContextVar` that automatically passes
        config down the call stack without explicit parameter passing), where
        configs are merged rather than replaced

    !!! example

```python
        # Parent sets tags
        chain.invoke(input, config={"tags": ["parent"]})
        # Child automatically inherits and can add:
        # ensure_config({"tags": ["child"]}) -> {"tags": ["parent", "child"]}
```

## Signature

```python
RunnableConfig()
```

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    tags: list[str],
    metadata: dict[str, Any],
    callbacks: Callbacks,
    run_name: str,
    max_concurrency: int | None,
    recursion_limit: int,
    configurable: dict[str, Any],
    run_id: uuid.UUID | None,
)
```

| Name | Type |
|------|------|
| `tags` | `list[str]` |
| `metadata` | `dict[str, Any]` |
| `callbacks` | `Callbacks` |
| `run_name` | `str` |
| `max_concurrency` | `int \| None` |
| `recursion_limit` | `int` |
| `configurable` | `dict[str, Any]` |
| `run_id` | `uuid.UUID \| None` |

## Properties

- `tags`
- `metadata`
- `callbacks`
- `run_name`
- `max_concurrency`
- `recursion_limit`
- `configurable`
- `run_id`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/runnables/config.py#L57)
