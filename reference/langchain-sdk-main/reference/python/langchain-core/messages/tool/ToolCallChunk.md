---
title: "ToolCallChunk"
description: "A chunk of a tool call (yielded when streaming)."
source: "https://reference.langchain.com/python/langchain-core/messages/tool/ToolCallChunk"
category: "reference"
tags: [reference, langchain-core, messages, tool, toolcallchunk]
---

# ToolCallChunk

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/messages/tool/ToolCallChunk)

A chunk of a tool call (yielded when streaming).

When merging `ToolCallChunk` objects (e.g., via `AIMessageChunk.__add__`), all
string attributes are concatenated. Chunks are only merged if their values of
`index` are equal and not `None`.

Example:
```python
left_chunks = [ToolCallChunk(name="foo", args='{"a":', index=0)]
right_chunks = [ToolCallChunk(name=None, args="1}", index=0)]

(
    AIMessageChunk(content="", tool_call_chunks=left_chunks)
    + AIMessageChunk(content="", tool_call_chunks=right_chunks)
).tool_call_chunks == [ToolCallChunk(name="foo", args='{"a":1}', index=0)]
```

## Signature

```python
ToolCallChunk()
```

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    name: str | None,
    args: str | None,
    id: str | None,
    index: int | None,
    type: NotRequired[Literal['tool_call_chunk']],
)
```

| Name | Type |
|------|------|
| `name` | `str \| None` |
| `args` | `str \| None` |
| `id` | `str \| None` |
| `index` | `int \| None` |
| `type` | `NotRequired[Literal['tool_call_chunk']]` |

## Properties

- `name`
- `args`
- `id`
- `index`
- `type`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/messages/tool.py#L261)
