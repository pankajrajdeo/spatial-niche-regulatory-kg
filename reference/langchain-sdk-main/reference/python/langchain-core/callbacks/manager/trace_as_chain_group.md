---
title: "trace_as_chain_group"
description: "Get a callback manager for a chain group in a context manager."
source: "https://reference.langchain.com/python/langchain-core/callbacks/manager/trace_as_chain_group"
category: "reference"
tags: [reference, langchain-core, callbacks, manager, trace_as_chain_group]
---

# trace_as_chain_group

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/callbacks/manager/trace_as_chain_group)

Get a callback manager for a chain group in a context manager.

Useful for grouping different calls together as a single run even if they aren't
composed in a single chain.

## Signature

```python
trace_as_chain_group(
    group_name: str,
    callback_manager: CallbackManager | None = None,
    *,
    inputs: dict[str, Any] | None = None,
    project_name: str | None = None,
    example_id: str | UUID | None = None,
    run_id: UUID | None = None,
    tags: list[str] | None = None,
    metadata: dict[str, Any] | None = None,
) -> Generator[CallbackManagerForChainGroup, None, None]
```

## Description

!!! note

Must have `LANGCHAIN_TRACING_V2` env var set to true to see the trace in
LangSmith.

**Example:**

```python
llm_input = "Foo"
with trace_as_chain_group("group_name", inputs={"input": llm_input}) as manager:
    # Use the callback manager for the chain group
    res = llm.invoke(llm_input, {"callbacks": manager})
    manager.on_chain_end({"output": res})
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `group_name` | `str` | Yes | The name of the chain group. |
| `callback_manager` | `CallbackManager \| None` | No | The callback manager to use. (default: `None`) |
| `inputs` | `dict[str, Any] \| None` | No | The inputs to the chain group. (default: `None`) |
| `project_name` | `str \| None` | No | The name of the project. (default: `None`) |
| `example_id` | `str \| UUID \| None` | No | The ID of the example. (default: `None`) |
| `run_id` | `UUID \| None` | No | The ID of the run. (default: `None`) |
| `tags` | `list[str] \| None` | No | The inheritable tags to apply to all runs. (default: `None`) |
| `metadata` | `dict[str, Any] \| None` | No | The metadata to apply to all runs. (default: `None`) |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/callbacks/manager.py#L55)
