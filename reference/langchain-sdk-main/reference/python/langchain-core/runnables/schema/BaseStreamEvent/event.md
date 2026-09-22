---
title: "event"
description: "Event names are of the format: on_[runnable_type]_(start|stream|end)."
source: "https://reference.langchain.com/python/langchain-core/runnables/schema/BaseStreamEvent/event"
category: "reference"
tags: [reference, langchain-core, runnables, schema, basestreamevent, event]
---

# event

> **Attribute** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/schema/BaseStreamEvent/event)

Event names are of the format: `on_[runnable_type]_(start|stream|end)`.

Runnable types are one of:

- **llm** - used by non chat models
- **chat_model** - used by chat models
- **prompt** --  e.g., `ChatPromptTemplate`
- **tool** -- from tools defined via `@tool` decorator or inheriting
    from `Tool`/`BaseTool`
- **chain** - most `Runnable` objects are of this type

Further, the events are categorized as one of:

- **start** - when the `Runnable` starts
- **stream** - when the `Runnable` is streaming
- **end* - when the `Runnable` ends

start, stream and end are associated with slightly different `data` payload.

Please see the documentation for `EventData` for more details.

## Signature

```python
event: str
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/runnables/schema.py#L102)
