---
title: "ToolErrorMiddleware"
description: "Return selected tool-execution exceptions to the model as error ToolMessages."
source: "https://reference.langchain.com/python/langchain/agents/middleware/tool_error/ToolErrorMiddleware"
category: "reference"
tags: [reference, langchain, agents, middleware, tool_error, toolerrormiddleware]
---

# ToolErrorMiddleware

> **Class** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/tool_error/ToolErrorMiddleware)

Return selected tool-execution exceptions to the model as error `ToolMessage`s.

`on_error` is called for each exception raised by tool execution. Return content
(a `str` or a list of content blocks) to convert the exception into a
`ToolMessage(status="error")`; return `None` — or simply don't return — to let the
exception propagate (halting the run). Handling is therefore opt-in — exceptions you
do not return content for propagate unchanged, so arbitrary internal exceptions are
never serialized to the model or end user unless you choose to surface them.

Langgraph control-flow signals (interrupts, parent commands) always propagate and
never reach `on_error`.

Prefer returning content that names the exception type over the raw exception message,
which may carry sensitive or internal detail.

Provide at least one of `on_error` or `aon_error`. `aon_error` handles errors on the
async execution path (falling back to `on_error` when omitted); the sync path only
ever calls `on_error`. For async-only usage, pass `aon_error` alone — running such a
middleware on the sync path raises, since the async handler cannot be awaited there.

This middleware does not retry. For retries, compose with `ToolRetryMiddleware`
placed *inner* and configured with `on_failure="error"` so exceptions reach this
middleware.

This middleware only sees exceptions raised by tool *execution*. Argument-binding
and validation errors are handled upstream by `ToolNode` (converted to an error
`ToolMessage` before the tool runs), so they do not reach `on_error`.

## Signature

```python
ToolErrorMiddleware(
    self,
    on_error: OnError | None = None,
    *,
    aon_error: AOnError | None = None,
    tools: list[BaseTool | str] | None = None,
)
```

## Description

**Example:**

```python
from langchain.agents import create_agent
from langchain.agents.middleware import ToolErrorMiddleware

def on_error(exc: Exception, request: ToolCallRequest) -> str | None:
    if isinstance(exc, ValueError):
        return f"`{request.tool_call['name']}` failed; fix the input and retry."
    return None  # propagate everything else

agent = create_agent(model, tools=[...], middleware=[ToolErrorMiddleware(on_error)])
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `on_error` | `OnError \| None` | No | Handler called for each exception raised by tool execution. Return content (`str` or list of content blocks) to convert the exception into an error `ToolMessage`. Return `None` — or simply don't return — to let the exception propagate. Falling through without a return therefore re-raises, so handle only the exceptions you mean to. Receives the exception and the tool call request (tool name, args, call id). Used on the sync path and, unless `aon_error` is given, on the async path. (default: `None`) |
| `aon_error` | `AOnError \| None` | No | Optional async handler, used on the async execution path. Falls back to `on_error` when not provided. (default: `None`) |
| `tools` | `list[BaseTool \| str] \| None` | No | Optional list of tools or tool names to apply handling to. If `None`, applies to all tools. (default: `None`) |

## Extends

- `AgentMiddleware[AgentState[ResponseT], ContextT, ResponseT]`

## Constructors

```python
__init__(
    self,
    on_error: OnError | None = None,
    *,
    aon_error: AOnError | None = None,
    tools: list[BaseTool | str] | None = None,
) -> None
```

| Name | Type |
|------|------|
| `on_error` | `OnError \| None` |
| `aon_error` | `AOnError \| None` |
| `tools` | `list[BaseTool \| str] \| None` |

## Properties

- `trace_policy`
- `on_error`
- `aon_error`
- `tools`

## Methods

- [`wrap_tool_call()`](https://reference.langchain.com/python/langchain/agents/middleware/tool_error/ToolErrorMiddleware/wrap_tool_call)
- [`awrap_tool_call()`](https://reference.langchain.com/python/langchain/agents/middleware/tool_error/ToolErrorMiddleware/awrap_tool_call)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a18de590e7ccf5c647fbf3d689e5f1a15f78e9f5/libs/langchain_v1/langchain/agents/middleware/tool_error.py#L37)
