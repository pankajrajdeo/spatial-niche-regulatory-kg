---
title: "InjectedToolCallId"
description: "Annotation for injecting the tool call ID."
source: "https://reference.langchain.com/python/langchain-core/tools/base/InjectedToolCallId"
category: "reference"
tags: [reference, langchain-core, tools, base, injectedtoolcallid]
---

# InjectedToolCallId

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/tools/base/InjectedToolCallId)

Annotation for injecting the tool call ID.

This annotation is used to mark a tool parameter that should receive the tool call
ID at runtime.

```python
from typing import Annotated
from langchain_core.messages import ToolMessage
from langchain_core.tools import tool, InjectedToolCallId

@tool
def foo(
    x: int, tool_call_id: Annotated[str, InjectedToolCallId]
) -> ToolMessage:
    """Return x."""
    return ToolMessage(
        str(x),
        artifact=x,
        name="foo",
        tool_call_id=tool_call_id
    )
```

## Signature

```python
InjectedToolCallId()
```

## Extends

- `InjectedToolArg`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/tools/base.py#L1756)
