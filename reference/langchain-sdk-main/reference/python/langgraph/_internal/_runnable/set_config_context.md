---
title: "set_config_context"
description: "Set the child Runnable config + tracing context."
source: "https://reference.langchain.com/python/langgraph/_internal/_runnable/set_config_context"
category: "reference"
tags: [reference, langgraph, internal, runnable, set_config_context]
---

# set_config_context

> **Function** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/_internal/_runnable/set_config_context)

Set the child Runnable config + tracing context.

## Signature

```python
set_config_context(
    config: RunnableConfig,
    run: Any = None,
) -> Generator[Context, None, None]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `config` | `RunnableConfig` | Yes | The config to set. |

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/644815f9e5bc52ad8f7a5227a456227e9c3e639b/libs/langgraph/langgraph/_internal/_runnable.py#L126)
