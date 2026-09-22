---
title: "interleave_projections"
description: "Yield (channel_name, item) tuples across multiple projections."
source: "https://reference.langchain.com/python/langgraph-sdk/_sync/stream/SyncThreadStream/interleave_projections"
category: "reference"
tags: [reference, langgraph-sdk, sync, stream, syncthreadstream, interleave_projections]
---

# interleave_projections

> **Method** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/_sync/stream/SyncThreadStream/interleave_projections)

Yield `(channel_name, item)` tuples across multiple projections.

One shared subscription drives all per-channel decoders; items arrive
in server-emit order (the SDK analog of `GraphRunStream.interleave`).

## Signature

```python
interleave_projections(
    self,
    channels: list[str],
) -> Iterator[tuple[str, Any]]
```

## Description

**Note:**

Handles and streams are yielded eagerly (before their sub-stream
completes), so items arrive interleaved in real time. To receive a
fully-resolved handle (output already populated), use the dedicated
`thread.tool_calls` / `thread.messages` projections instead.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `channels` | `list[str]` | Yes | Flat list of `"values"`, `"messages"`, `"tool_calls"`, `"subgraphs"`, and/or extension names. Built-ins yield their typed item (snapshot dict / `ChatModelStream` / `SyncToolCallHandle` / `SyncScopedStreamHandle`); an extension yields its payload dict, keyed by the bare extension name. |

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/d5f4b2aa960940effc8430165ab3604038e817af/libs/sdk-py/langgraph_sdk/_sync/stream.py#L1288)
