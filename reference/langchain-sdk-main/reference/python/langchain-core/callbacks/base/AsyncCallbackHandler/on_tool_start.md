---
title: "on_tool_start"
description: "Run when the tool starts running."
source: "https://reference.langchain.com/python/langchain-core/callbacks/base/AsyncCallbackHandler/on_tool_start"
category: "reference"
tags: [reference, langchain-core, callbacks, base, asynccallbackhandler, on_tool_start]
---

# on_tool_start

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/callbacks/base/AsyncCallbackHandler/on_tool_start)

Run when the tool starts running.

## Signature

```python
on_tool_start(
    self,
    serialized: dict[str, Any],
    input_str: str,
    *,
    run_id: UUID,
    parent_run_id: UUID | None = None,
    tags: list[str] | None = None,
    metadata: dict[str, Any] | None = None,
    inputs: dict[str, Any] | None = None,
    **kwargs: Any = {},
) -> None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `serialized` | `dict[str, Any]` | Yes | The serialized tool. |
| `input_str` | `str` | Yes | The input string. |
| `run_id` | `UUID` | Yes | The ID of the current run. |
| `parent_run_id` | `UUID \| None` | No | The ID of the parent run. (default: `None`) |
| `tags` | `list[str] \| None` | No | The tags. (default: `None`) |
| `metadata` | `dict[str, Any] \| None` | No | The metadata. (default: `None`) |
| `inputs` | `dict[str, Any] \| None` | No | The inputs. (default: `None`) |
| `**kwargs` | `Any` | No | Additional keyword arguments. (default: `{}`) |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/callbacks/base.py#L782)
