---
title: "on_tool_start"
description: "Run when the tool starts running."
source: "https://reference.langchain.com/python/langchain-core/callbacks/manager/AsyncCallbackManager/on_tool_start"
category: "reference"
tags: [reference, langchain-core, callbacks, manager, asynccallbackmanager, on_tool_start]
---

# on_tool_start

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/callbacks/manager/AsyncCallbackManager/on_tool_start)

Run when the tool starts running.

## Signature

```python
on_tool_start(
    self,
    serialized: dict[str, Any] | None,
    input_str: str,
    run_id: UUID | None = None,
    parent_run_id: UUID | None = None,
    **kwargs: Any = {},
) -> AsyncCallbackManagerForToolRun
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `serialized` | `dict[str, Any] \| None` | Yes | The serialized tool. |
| `input_str` | `str` | Yes | The input to the tool. |
| `run_id` | `UUID \| None` | No | The ID of the run. (default: `None`) |
| `parent_run_id` | `UUID \| None` | No | The ID of the parent run. (default: `None`) |
| `**kwargs` | `Any` | No | Additional keyword arguments. (default: `{}`) |

## Returns

`AsyncCallbackManagerForToolRun`

The async callback manager for the tool run.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/callbacks/manager.py#L2071)
