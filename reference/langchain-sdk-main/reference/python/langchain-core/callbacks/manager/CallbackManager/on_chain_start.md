---
title: "on_chain_start"
description: "Run when chain starts running."
source: "https://reference.langchain.com/python/langchain-core/callbacks/manager/CallbackManager/on_chain_start"
category: "reference"
tags: [reference, langchain-core, callbacks, manager, callbackmanager, on_chain_start]
---

# on_chain_start

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/callbacks/manager/CallbackManager/on_chain_start)

Run when chain starts running.

## Signature

```python
on_chain_start(
    self,
    serialized: dict[str, Any] | None,
    inputs: dict[str, Any] | Any,
    run_id: UUID | None = None,
    **kwargs: Any = {},
) -> CallbackManagerForChainRun
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `serialized` | `dict[str, Any] \| None` | Yes | The serialized chain. |
| `inputs` | `dict[str, Any] \| Any` | Yes | The inputs to the chain. |
| `run_id` | `UUID \| None` | No | The ID of the run. (default: `None`) |
| `**kwargs` | `Any` | No | Additional keyword arguments. (default: `{}`) |

## Returns

`CallbackManagerForChainRun`

The callback manager for the chain run.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/callbacks/manager.py#L1485)
