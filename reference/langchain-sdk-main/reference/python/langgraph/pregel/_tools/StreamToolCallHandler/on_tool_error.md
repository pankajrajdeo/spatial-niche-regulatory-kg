---
title: "on_tool_error"
description: "View source on GitHub"
source: "https://reference.langchain.com/python/langgraph/pregel/_tools/StreamToolCallHandler/on_tool_error"
category: "reference"
tags: [reference, langgraph, pregel, tools, streamtoolcallhandler, on_tool_error]
---

# on_tool_error

> **Method** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/pregel/_tools/StreamToolCallHandler/on_tool_error)

## Signature

```python
on_tool_error(
    self,
    error: BaseException,
    *,
    run_id: UUID,
    parent_run_id: UUID | None = None,
    **kwargs: Any = {},
) -> Any
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/644815f9e5bc52ad8f7a5227a456227e9c3e639b/libs/langgraph/langgraph/pregel/_tools.py#L260)
