---
title: "finalize_tool_call_chunk"
description: "Parse accumulated tool-chunk args into a finalized block."
source: "https://reference.langchain.com/python/langchain-core/language_models/chat_model_stream/finalize_tool_call_chunk"
category: "reference"
tags: [reference, langchain-core, language_models, chat_model_stream, finalize_tool_call_chunk]
---

# finalize_tool_call_chunk

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/language_models/_compat_bridge/finalize_tool_call_chunk)

Parse accumulated tool-chunk args into a finalized block.

Shared between the compat bridge's `_finalize_block` and the
`ChatModelStream` end-of-stream sweep. Parses `raw_args` as JSON:
on success builds the requested finalized type (`tool_call` or
`server_tool_call`) with provider-specific fields (`extras`)
preserved; on failure falls back to `invalid_tool_call` carrying
the raw string so downstream consumers can still introspect the
malformed payload.

## Signature

```python
finalize_tool_call_chunk(
    *,
    raw_args: str | None,
    id_: str | None,
    name: str | None,
    extras: dict[str, Any],
    finalized_type: str,
) -> FinalizedContentBlock
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `raw_args` | `str \| None` | Yes | Accumulated partial-JSON string; `None` or empty treated as `{}`. |
| `id_` | `str \| None` | Yes | Tool-call id collected across chunks. |
| `name` | `str \| None` | Yes | Tool name collected across chunks. |
| `extras` | `dict[str, Any]` | Yes | Provider-specific fields to carry onto the finalized block. Callers are responsible for having already dropped keys they don't want propagated (notably `type`, `id`, `name`, `args`, and `index` on client-side `tool_call`). |
| `finalized_type` | `str` | Yes | `"tool_call"` or `"server_tool_call"`. |

## Returns

`FinalizedContentBlock`

A `ToolCall`, `ServerToolCall`, or `InvalidToolCall` — the

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/language_models/_compat_bridge.py#L359)
