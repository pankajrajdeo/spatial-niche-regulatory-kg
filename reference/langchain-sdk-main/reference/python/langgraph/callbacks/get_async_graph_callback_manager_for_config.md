---
title: "get_async_graph_callback_manager_for_config"
description: "Build an async graph lifecycle callback manager from a runnable config."
source: "https://reference.langchain.com/python/langgraph/callbacks/get_async_graph_callback_manager_for_config"
category: "reference"
tags: [reference, langgraph, callbacks, get_async_graph_callback_manager_for_config]
---

# get_async_graph_callback_manager_for_config

> **Function** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/callbacks/get_async_graph_callback_manager_for_config)

Build an async graph lifecycle callback manager from a runnable config.

This helper filters `config["callbacks"]` down to handlers that inherit
from `GraphCallbackHandler` and binds the provided `run_id` onto the
returned manager.

## Signature

```python
get_async_graph_callback_manager_for_config(
    config: RunnableConfig,
    *,
    run_id: UUID | None = None,
) -> _AsyncGraphCallbackManager
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/644815f9e5bc52ad8f7a5227a456227e9c3e639b/libs/langgraph/langgraph/callbacks.py#L380)
