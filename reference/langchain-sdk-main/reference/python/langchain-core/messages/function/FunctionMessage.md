---
title: "FunctionMessage"
description: "Message for passing the result of executing a tool back to a model."
source: "https://reference.langchain.com/python/langchain-core/messages/function/FunctionMessage"
category: "reference"
tags: [reference, langchain-core, messages, function, functionmessage]
---

# FunctionMessage

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/messages/function/FunctionMessage)

Message for passing the result of executing a tool back to a model.

`FunctionMessage` are an older version of the `ToolMessage` schema, and
do not contain the `tool_call_id` field.

The `tool_call_id` field is used to associate the tool call request with the
tool call response. Useful in situations where a chat model is able
to request multiple tool calls in parallel.

## Signature

```python
FunctionMessage(
    self,
    content: str | list[str | dict[Any, Any]] | None = None,
    content_blocks: list[types.ContentBlock] | None = None,
    **kwargs: Any = {},
)
```

## Extends

- `BaseMessage`

## Properties

- `name`
- `type`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/messages/function.py#L15)
