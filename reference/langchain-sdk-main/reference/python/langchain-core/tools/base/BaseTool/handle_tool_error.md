---
title: "handle_tool_error"
description: "Handle ToolException raised by tool execution."
source: "https://reference.langchain.com/python/langchain-core/tools/base/BaseTool/handle_tool_error"
category: "reference"
tags: [reference, langchain-core, tools, base, basetool, handle_tool_error]
---

# handle_tool_error

> **Attribute** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/tools/base/BaseTool/handle_tool_error)

Handle `ToolException` raised by tool execution.

If `False`, the exception is re-raised. If `True`, the exception message is
returned as tool output. If a string is passed, that string is returned
as tool output. If a callable is passed, it receives the exception and
its return value is used as the tool output.

Callable handlers may return either a string or a list of message
content blocks. If the tool was invoked with a `tool_call_id`, the handled
content is wrapped in a `ToolMessage` with `status="error"`.

## Signature

```python
handle_tool_error: bool | str | Callable[[ToolException], ToolExceptionHandlerOutput] | None = False
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/tools/base.py#L527)
