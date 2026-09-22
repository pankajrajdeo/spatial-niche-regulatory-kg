---
title: "convert_to_openai_tool"
description: "Convert a tool-like object to an OpenAI tool schema."
source: "https://reference.langchain.com/python/langchain-core/utils/function_calling/convert_to_openai_tool"
category: "reference"
tags: [reference, langchain-core, utils, function_calling, convert_to_openai_tool]
---

# convert_to_openai_tool

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/utils/function_calling/convert_to_openai_tool)

Convert a tool-like object to an OpenAI tool schema.

[OpenAI tool schema reference](https://platform.openai.com/docs/api-reference/chat/create#chat-create-tools)

## Signature

```python
convert_to_openai_tool(
    tool: Mapping[str, Any] | type[BaseModel] | Callable[..., Any] | BaseTool,
    *,
    strict: bool | None = None,
) -> dict[str, Any]
```

## Description

!!! warning "Behavior changed in `langchain-core` 0.3.16"

    `description` and `parameters` keys are now optional. Only `name` is
    required and guaranteed to be part of the output.

!!! warning "Behavior changed in `langchain-core` 0.3.44"

    Return OpenAI Responses API-style tools unchanged. This includes
    any dict with `"type"` in `"file_search"`, `"function"`,
    `"computer_use_preview"`, `"web_search_preview"`, `"apply_patch"`.

!!! warning "Behavior changed in `langchain-core` 0.3.63"

    Added support for OpenAI's image generation built-in tool.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `tool` | `Mapping[str, Any] \| type[BaseModel] \| Callable[..., Any] \| BaseTool` | Yes | Either a dictionary, a `pydantic.BaseModel` class, Python function, or `BaseTool`.  If a dictionary is passed in, it is assumed to already be a valid OpenAI function, a JSON schema with top-level `title` key specified, an Anthropic format tool, or an Amazon Bedrock Converse format tool. |
| `strict` | `bool \| None` | No | If `True`, model output is guaranteed to exactly match the JSON Schema provided in the function definition.  If `None`, `strict` argument will not be included in tool definition. (default: `None`) |

## Returns

`dict[str, Any]`

A dict version of the passed in tool which is compatible with the OpenAI
tool-calling API.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/utils/function_calling.py#L515)
