---
title: "on_tool_start"
description: "Run when tool starts running."
source: "https://reference.langchain.com/python/langchain-core/callbacks/manager/CallbackManager/on_tool_start"
category: "reference"
tags: [reference, langchain-core, callbacks, manager, callbackmanager, on_tool_start]
---

# on_tool_start

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/callbacks/manager/CallbackManager/on_tool_start)

Run when tool starts running.

## Signature

```python
on_tool_start(
    self,
    serialized: dict[str, Any] | None,
    input_str: str,
    run_id: UUID | None = None,
    parent_run_id: UUID | None = None,
    inputs: dict[str, Any] | None = None,
    **kwargs: Any = {},
) -> CallbackManagerForToolRun
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `serialized` | `dict[str, Any] \| None` | Yes | Serialized representation of the tool. |
| `input_str` | `str` | Yes | The  input to the tool as a string.  Non-string inputs are cast to strings. |
| `run_id` | `UUID \| None` | No | ID for the run. (default: `None`) |
| `parent_run_id` | `UUID \| None` | No | The ID of the parent run. (default: `None`) |
| `inputs` | `dict[str, Any] \| None` | No | The original input to the tool if provided.  Recommended for usage instead of input_str when the original input is needed.  If provided, the inputs are expected to be formatted as a dict. The keys will correspond to the named-arguments in the tool. (default: `None`) |
| `**kwargs` | `Any` | No | The keyword arguments to pass to the event handler (default: `{}`) |

## Returns

`CallbackManagerForToolRun`

The callback manager for the tool run.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/callbacks/manager.py#L1530)
