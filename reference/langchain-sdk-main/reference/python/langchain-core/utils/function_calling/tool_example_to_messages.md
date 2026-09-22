---
title: "tool_example_to_messages"
description: "Convert an example into a list of messages that can be fed into an LLM."
source: "https://reference.langchain.com/python/langchain-core/utils/function_calling/tool_example_to_messages"
category: "reference"
tags: [reference, langchain-core, utils, function_calling, tool_example_to_messages]
---

# tool_example_to_messages

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/utils/function_calling/tool_example_to_messages)

Convert an example into a list of messages that can be fed into an LLM.

This code is an adapter that converts a single example to a list of messages
that can be fed into a chat model.

The list of messages per example by default corresponds to:

1. `HumanMessage`: contains the content from which content should be extracted.
2. `AIMessage`: contains the extracted information from the model
3. `ToolMessage`: contains confirmation to the model that the model requested a
    tool correctly.

If `ai_response` is specified, there will be a final `AIMessage` with that
response.

The `ToolMessage` is required because some chat models are hyper-optimized for
agents rather than for an extraction use case.

## Signature

```python
tool_example_to_messages(
    input: str,
    tool_calls: list[BaseModel],
    tool_outputs: list[str] | None = None,
    *,
    ai_response: str | None = None,
) -> list[BaseMessage]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `input` | `str` | Yes | The user input |
| `tool_calls` | `list[BaseModel]` | Yes | Tool calls represented as Pydantic BaseModels |
| `tool_outputs` | `list[str] \| None` | No | Tool call outputs.  Does not need to be provided.  If not provided, a placeholder value will be inserted. (default: `None`) |
| `ai_response` | `str \| None` | No | If provided, content for a final `AIMessage`. (default: `None`) |

## Returns

`list[BaseMessage]`

A list of messages

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/utils/function_calling.py#L620)
