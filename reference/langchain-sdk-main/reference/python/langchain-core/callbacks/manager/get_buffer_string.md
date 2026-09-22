---
title: "get_buffer_string"
description: "Convert a sequence of messages to strings and concatenate them into one string."
source: "https://reference.langchain.com/python/langchain-core/callbacks/manager/get_buffer_string"
category: "reference"
tags: [reference, langchain-core, callbacks, manager, get_buffer_string]
---

# get_buffer_string

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/messages/utils/get_buffer_string)

Convert a sequence of messages to strings and concatenate them into one string.

## Signature

```python
get_buffer_string(
    messages: Sequence[BaseMessage],
    human_prefix: str = 'Human',
    ai_prefix: str = 'AI',
    *,
    system_prefix: str = 'System',
    function_prefix: str = 'Function',
    tool_prefix: str = 'Tool',
    message_separator: str = '\n',
    format: Literal['prefix', 'xml'] = 'prefix',
) -> str
```

## Description

!!! warning

    If a message is an `AIMessage` and contains both tool calls under `tool_calls`
    and a function call under `additional_kwargs["function_call"]`, only the tool
    calls will be appended to the string representation.

!!! note "XML format"

    When using `format='xml'`:

    - All messages use uniform `<message type="role">content</message>` format.
    - The `type` attribute uses `human_prefix` (lowercased) for `HumanMessage`,
        `ai_prefix` (lowercased) for `AIMessage`, `system_prefix` (lowercased)
        for `SystemMessage`, `function_prefix` (lowercased) for `FunctionMessage`,
        `tool_prefix` (lowercased) for `ToolMessage`, and the original role
        (unchanged) for `ChatMessage`.
    - Message content is escaped using `xml.sax.saxutils.escape()`.
    - Attribute values are escaped using `xml.sax.saxutils.quoteattr()`.
    - AI messages with tool calls use nested structure with `<content>` and
        `<tool_call>` elements.
    - For multi-modal content (list of content blocks), supported block types
        are: `text`, `reasoning`, `image` (URL/file_id only), `image_url`
        (OpenAI-style, URL only), `audio` (URL/file_id only), `video` (URL/file_id
        only), `text-plain`, `server_tool_call`, and `server_tool_result`.
    - Content blocks with base64-encoded data are skipped (including blocks
        with `base64` field or `data:` URLs).
    - Unknown block types are skipped.
    - Plain text document content (`text-plain`), server tool call arguments,
        and server tool result outputs are truncated to 500 characters.

**Example:**

Default prefix format:

```python
from langchain_core.messages import AIMessage, HumanMessage, get_buffer_string

messages = [
    HumanMessage(content="Hi, how are you?"),
    AIMessage(content="Good, how are you?"),
]
get_buffer_string(messages)
# -> "Human: Hi, how are you?\nAI: Good, how are you?"
```

XML format (useful when content contains role-like prefixes):

```python
messages = [
    HumanMessage(content="Example: Human: some text"),
    AIMessage(content="I see the example."),
]
get_buffer_string(messages, format="xml")
# -> '<message type="human">Example: Human: some text</message>\\n'
# -> '<message type="ai">I see the example.</message>'
```

XML format with special characters (automatically escaped):

```python
messages = [
    HumanMessage(content="Is 5 < 10 & 10 > 5?"),
]
get_buffer_string(messages, format="xml")
# -> '<message type="human">Is 5 &lt; 10 &amp; 10 &gt; 5?</message>'
```

XML format with tool calls:

```python
messages = [
    AIMessage(
        content="I'll search for that.",
        tool_calls=[
            {"id": "call_123", "name": "search", "args": {"query": "weather"}}
        ],
    ),
]
get_buffer_string(messages, format="xml")
# -> '<message type="ai">\\n'
# -> '  <content>I\\'ll search for that.</content>\\n'
# -> '  <tool_call id="call_123" name="search">'
# -> '{"query": "weather"}</tool_call>\\n'
# -> '</message>'
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `messages` | `Sequence[BaseMessage]` | Yes | Messages to be converted to strings. |
| `human_prefix` | `str` | No | The prefix to prepend to contents of `HumanMessage`s. (default: `'Human'`) |
| `ai_prefix` | `str` | No | The prefix to prepend to contents of `AIMessage`. (default: `'AI'`) |
| `system_prefix` | `str` | No | The prefix to prepend to contents of `SystemMessage`s. (default: `'System'`) |
| `function_prefix` | `str` | No | The prefix to prepend to contents of `FunctionMessage`s. (default: `'Function'`) |
| `tool_prefix` | `str` | No | The prefix to prepend to contents of `ToolMessage`s. (default: `'Tool'`) |
| `message_separator` | `str` | No | The separator to use between messages. (default: `'\n'`) |
| `format` | `Literal['prefix', 'xml']` | No | The output format. `'prefix'` uses `Role: content` format (default). For multimodal messages, only string content and `text` blocks are included; non-text blocks such as images, audio, and video are omitted.  `'xml'` uses XML-style `<message type='role'>` format with proper character escaping, which is useful when message content may contain role-like prefixes that could cause ambiguity.  Use `'xml'` when you need a structured representation of supported multimodal content blocks. (default: `'prefix'`) |

## Returns

`str`

A single string concatenation of all input messages.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/messages/utils.py#L287)
