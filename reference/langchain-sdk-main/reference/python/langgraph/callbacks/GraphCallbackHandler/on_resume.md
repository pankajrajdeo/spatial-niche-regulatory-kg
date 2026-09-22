---
title: "on_resume"
description: "Run when graph execution resumes from a persisted checkpoint."
source: "https://reference.langchain.com/python/langgraph/callbacks/GraphCallbackHandler/on_resume"
category: "reference"
tags: [reference, langgraph, callbacks, graphcallbackhandler, on_resume]
---

# on_resume

> **Method** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/callbacks/GraphCallbackHandler/on_resume)

Run when graph execution resumes from a persisted checkpoint.

## Signature

```python
on_resume(
    self,
    event: GraphResumeEvent,
) -> Any
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `event` | `GraphResumeEvent` | Yes | Resume lifecycle event payload. |

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/644815f9e5bc52ad8f7a5227a456227e9c3e639b/libs/langgraph/langgraph/callbacks.py#L106)
