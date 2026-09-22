---
title: "StreamPart"
description: "A discriminated union of all v2 stream part types."
source: "https://reference.langchain.com/python/langgraph/types/StreamPart"
category: "reference"
tags: [reference, langgraph, types, streampart]
---

# StreamPart

> **Attribute** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/types/StreamPart)

A discriminated union of all v2 stream part types.

Use `part["type"]` to narrow the type:

```python
async for part in graph.astream(input, version="v2"):
    if part["type"] == "values":
        part["data"]  # OutputT — full state (pydantic/dataclass/dict)
    elif part["type"] == "messages":
        part["data"]  # tuple[BaseMessage, dict] — (message, metadata)
    elif part["type"] == "custom":
        part["data"]  # Any — user-defined
```

## Signature

```python
StreamPart = TypeAliasType('StreamPart', ValuesStreamPart[OutputT] | UpdatesStreamPart | MessagesStreamPart | CustomStreamPart | CheckpointStreamPart[StateT] | TasksStreamPart | DebugStreamPart[StateT], type_params=(StateT, OutputT))
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/644815f9e5bc52ad8f7a5227a456227e9c3e639b/libs/langgraph/langgraph/types.py#L343)
