---
title: "convert_to_openai_messages"
description: "Convert LangChain messages into OpenAI message dicts."
source: "https://reference.langchain.com/python/langchain-core/messages/utils/convert_to_openai_messages"
category: "reference"
tags: [reference, langchain-core, messages, utils, convert_to_openai_messages]
---

# convert_to_openai_messages

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/messages/utils/convert_to_openai_messages)

Convert LangChain messages into OpenAI message dicts.

## Signature

```python
convert_to_openai_messages(
    messages: MessageLikeRepresentation | Sequence[MessageLikeRepresentation],
    *,
    text_format: Literal['string', 'block'] = 'string',
    include_id: bool = False,
    pass_through_unknown_blocks: bool = True,
) -> dict[str, Any] | list[dict[str, Any]]
```

## Description

**Example:**

```python
from langchain_core.messages import (
    convert_to_openai_messages,
    AIMessage,
    SystemMessage,
    ToolMessage,
)

messages = [
    SystemMessage([{"type": "text", "text": "foo"}]),
    {
        "role": "user",
        "content": [
            {"type": "text", "text": "what's in this"},
            {
                "type": "image_url",
                "image_url": {"url": "data:image/png;base64,'/9j/4AAQSk'"},
            },
        ],
    },
    AIMessage(
        "",
        tool_calls=[
            {
                "name": "analyze",
                "args": {"baz": "buz"},
                "id": "1",
                "type": "tool_call",
            }
        ],
    ),
    ToolMessage("foobar", tool_call_id="1", name="bar"),
    {"role": "assistant", "content": "that's nice"},
]
oai_messages = convert_to_openai_messages(messages)
# -> [
#   {'role': 'system', 'content': 'foo'},
#   {'role': 'user', 'content': [{'type': 'text', 'text': 'what's in this'}, {'type': 'image_url', 'image_url': {'url': "data:image/png;base64,'/9j/4AAQSk'"}}]},
#   {'role': 'assistant', 'tool_calls': [{'type': 'function', 'id': '1','function': {'name': 'analyze', 'arguments': '{"baz": "buz"}'}}], 'content': ''},
#   {'role': 'tool', 'name': 'bar', 'content': 'foobar'},
#   {'role': 'assistant', 'content': 'that's nice'}
# ]
```

!!! version-added "Added in `langchain-core` 0.3.11"

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `messages` | `MessageLikeRepresentation \| Sequence[MessageLikeRepresentation]` | Yes | Message-like object or iterable of objects whose contents are in OpenAI, Anthropic, Bedrock Converse, or VertexAI formats. |
| `text_format` | `Literal['string', 'block']` | No | How to format string or text block contents: - `'string'`:     If a message has a string content, this is left as a string. If     a message has content blocks that are all of type `'text'`, these     are joined with a newline to make a single string. If a message has     content blocks and at least one isn't of type `'text'`, then     all blocks are left as dicts. - `'block'`:     If a message has a string content, this is turned into a list     with a single content block of type `'text'`. If a message has     content blocks these are left as is. (default: `'string'`) |
| `include_id` | `bool` | No | Whether to include message IDs in the openai messages, if they are present in the source messages. (default: `False`) |
| `pass_through_unknown_blocks` | `bool` | No | Whether to include content blocks with unknown formats in the output. If `False`, an error is raised if an unknown content block is encountered. (default: `True`) |

## Returns

`dict[str, Any] | list[dict[str, Any]]`

The return type depends on the input type:

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/messages/utils.py#L1549)
