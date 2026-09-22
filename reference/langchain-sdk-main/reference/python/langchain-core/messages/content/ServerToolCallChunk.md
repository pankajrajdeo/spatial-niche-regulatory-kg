---
title: "ServerToolCallChunk"
description: "A chunk of a server-side tool call (yielded when streaming)."
source: "https://reference.langchain.com/python/langchain-core/messages/content/ServerToolCallChunk"
category: "reference"
tags: [reference, langchain-core, messages, content, servertoolcallchunk]
---

# ServerToolCallChunk

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/messages/content/ServerToolCallChunk)

A chunk of a server-side tool call (yielded when streaming).

## Signature

```python
ServerToolCallChunk()
```

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    type: Literal['server_tool_call_chunk'],
    name: NotRequired[str],
    args: NotRequired[str],
    id: NotRequired[str],
    index: NotRequired[int | str],
    extras: NotRequired[dict[str, Any]],
)
```

| Name | Type |
|------|------|
| `type` | `Literal['server_tool_call_chunk']` |
| `name` | `NotRequired[str]` |
| `args` | `NotRequired[str]` |
| `id` | `NotRequired[str]` |
| `index` | `NotRequired[int \| str]` |
| `extras` | `NotRequired[dict[str, Any]]` |

## Properties

- `type`
- `name`
- `args`
- `id`
- `index`
- `extras`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/messages/content.py#L397)
