---
title: "run"
description: "Run the tool."
source: "https://reference.langchain.com/python/langchain-core/tools/base/BaseTool/run"
category: "reference"
tags: [reference, langchain-core, tools, base, basetool, run]
---

# run

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/tools/base/BaseTool/run)

Run the tool.

## Signature

```python
run(
    self,
    tool_input: str | dict[str, Any],
    verbose: bool | None = None,
    start_color: str | None = 'green',
    color: str | None = 'green',
    callbacks: Callbacks = None,
    *,
    tags: list[str] | None = None,
    metadata: dict[str, Any] | None = None,
    run_name: str | None = None,
    run_id: uuid.UUID | None = None,
    config: RunnableConfig | None = None,
    tool_call_id: str | None = None,
    **kwargs: Any = {},
) -> Any
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `tool_input` | `str \| dict[str, Any]` | Yes | The input to the tool. |
| `verbose` | `bool \| None` | No | Whether to log the tool's progress. (default: `None`) |
| `start_color` | `str \| None` | No | The color to use when starting the tool. (default: `'green'`) |
| `color` | `str \| None` | No | The color to use when ending the tool. (default: `'green'`) |
| `callbacks` | `Callbacks` | No | Callbacks to be called during tool execution. (default: `None`) |
| `tags` | `list[str] \| None` | No | Optional list of tags associated with the tool. (default: `None`) |
| `metadata` | `dict[str, Any] \| None` | No | Optional metadata associated with the tool. (default: `None`) |
| `run_name` | `str \| None` | No | The name of the run. (default: `None`) |
| `run_id` | `uuid.UUID \| None` | No | The id of the run. (default: `None`) |
| `config` | `RunnableConfig \| None` | No | The configuration for the tool. (default: `None`) |
| `tool_call_id` | `str \| None` | No | The id of the tool call. (default: `None`) |
| `**kwargs` | `Any` | No | Keyword arguments to be passed to tool callbacks (event handler) (default: `{}`) |

## Returns

`Any`

The output of the tool.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/tools/base.py#L1009)
