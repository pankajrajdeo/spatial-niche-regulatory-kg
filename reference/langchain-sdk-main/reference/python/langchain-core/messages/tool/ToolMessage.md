---
title: "ToolMessage"
description: "Message for passing the result of executing a tool back to a model."
source: "https://reference.langchain.com/python/langchain-core/messages/tool/ToolMessage"
category: "reference"
tags: [reference, langchain-core, messages, tool, toolmessage]
---

# ToolMessage

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/messages/tool/ToolMessage)

Message for passing the result of executing a tool back to a model.

`ToolMessage` objects contain the result of a tool invocation. Typically, the result
is encoded inside the `content` field.

`tool_call_id` is used to associate the tool call request with the tool call
response. Useful in situations where a chat model is able to request multiple tool
calls in parallel.

## Signature

```python
ToolMessage(
    self,
    content: str | list[str | dict[Any, Any]] | None = None,
    content_blocks: list[types.ContentBlock] | None = None,
    **kwargs: Any = {},
)
```

## Description

**Example:**

A `ToolMessage` representing a result of `42` from a tool call with id

```python
from langchain_core.messages import ToolMessage

ToolMessage(content="42", tool_call_id="call_Jja7J89XsjrOLA5r!MEOW!SL")
```

**Example:**

A `ToolMessage` where only part of the tool output is sent to the model
and the full output is passed in to artifact.

```python
from langchain_core.messages import ToolMessage

tool_output = {
    "stdout": "From the graph we can see that the correlation between "
    "x and y is ...",
    "stderr": None,
    "artifacts": {"type": "image", "base64_data": "/9j/4gIcSU..."},
}

ToolMessage(
    content=tool_output["stdout"],
    artifact=tool_output,
    tool_call_id="call_Jja7J89XsjrOLA5r!MEOW!SL",
)
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `content` | `str \| list[str \| dict[Any, Any]] \| None` | No | The contents of the message. (default: `None`) |
| `content_blocks` | `list[types.ContentBlock] \| None` | No | Typed standard content. (default: `None`) |
| `**kwargs` | `Any` | No | Additional fields. (default: `{}`) |

## Extends

- `BaseMessage`
- `ToolOutputMixin`

## Constructors

```python
__init__(
    self,
    content: str | list[str | dict[Any, Any]] | None = None,
    content_blocks: list[types.ContentBlock] | None = None,
    **kwargs: Any = {},
) -> None
```

| Name | Type |
|------|------|
| `content` | `str \| list[str \| dict[Any, Any]] \| None` |
| `content_blocks` | `list[types.ContentBlock] \| None` |

## Properties

- `tool_call_id`
- `type`
- `artifact`
- `status`
- `additional_kwargs`
- `response_metadata`

## Methods

- [`coerce_args()`](https://reference.langchain.com/python/langchain-core/messages/tool/ToolMessage/coerce_args)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/messages/tool.py#L26)
