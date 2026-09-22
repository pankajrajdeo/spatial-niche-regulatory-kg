---
title: "filter_messages"
description: "Filter messages based on name, type or id."
source: "https://reference.langchain.com/python/langchain-core/messages/utils/filter_messages"
category: "reference"
tags: [reference, langchain-core, messages, utils, filter_messages]
---

# filter_messages

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/messages/utils/filter_messages)

Filter messages based on `name`, `type` or `id`.

## Signature

```python
filter_messages(
    messages: Iterable[MessageLikeRepresentation] | PromptValue,
    *,
    include_names: Sequence[str] | None = None,
    exclude_names: Sequence[str] | None = None,
    include_types: Sequence[str | type[BaseMessage]] | None = None,
    exclude_types: Sequence[str | type[BaseMessage]] | None = None,
    include_ids: Sequence[str] | None = None,
    exclude_ids: Sequence[str] | None = None,
    exclude_tool_calls: Sequence[str] | bool | None = None,
) -> list[BaseMessage]
```

## Description

**Example:**

```python
from langchain_core.messages import (
    filter_messages,
    AIMessage,
    HumanMessage,
    SystemMessage,
)

messages = [
    SystemMessage("you're a good assistant."),
    HumanMessage("what's your name", id="foo", name="example_user"),
    AIMessage("steve-o", id="bar", name="example_assistant"),
    HumanMessage(
        "what's your favorite color",
        id="baz",
    ),
    AIMessage(
        "silicon blue",
        id="blah",
    ),
]

filter_messages(
    messages,
    include_names=("example_user", "example_assistant"),
    include_types=("system",),
    exclude_ids=("bar",),
)
```

```python
[
    SystemMessage("you're a good assistant."),
    HumanMessage("what's your name", id="foo", name="example_user"),
]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `messages` | `Iterable[MessageLikeRepresentation] \| PromptValue` | Yes | Sequence Message-like objects to filter. |
| `include_names` | `Sequence[str] \| None` | No | Message names to include. (default: `None`) |
| `exclude_names` | `Sequence[str] \| None` | No | Messages names to exclude. (default: `None`) |
| `include_types` | `Sequence[str \| type[BaseMessage]] \| None` | No | Message types to include. Can be specified as string names (e.g. `'system'`, `'human'`, `'ai'`, ...) or as `BaseMessage` classes (e.g. `SystemMessage`, `HumanMessage`, `AIMessage`, ...). (default: `None`) |
| `exclude_types` | `Sequence[str \| type[BaseMessage]] \| None` | No | Message types to exclude. Can be specified as string names (e.g. `'system'`, `'human'`, `'ai'`, ...) or as `BaseMessage` classes (e.g. `SystemMessage`, `HumanMessage`, `AIMessage`, ...). (default: `None`) |
| `include_ids` | `Sequence[str] \| None` | No | Message IDs to include. (default: `None`) |
| `exclude_ids` | `Sequence[str] \| None` | No | Message IDs to exclude. (default: `None`) |
| `exclude_tool_calls` | `Sequence[str] \| bool \| None` | No | Tool call IDs to exclude. Can be one of the following: - `True`: All `AIMessage` objects with tool calls and all `ToolMessage`     objects will be excluded. - a sequence of tool call IDs to exclude:     - `ToolMessage` objects with the corresponding tool call ID will be         excluded.     - The `tool_calls` in the AIMessage will be updated to exclude         matching tool calls. If all `tool_calls` are filtered from an         AIMessage, the whole message is excluded. (default: `None`) |

## Returns

`list[BaseMessage]`

A list of Messages that meets at least one of the `incl_*` conditions and none

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/messages/utils.py#L856)
