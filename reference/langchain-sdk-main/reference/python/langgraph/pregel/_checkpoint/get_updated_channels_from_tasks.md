---
title: "get_updated_channels_from_tasks"
description: "Channel names written by an update_state superstep (excluding PUSH)."
source: "https://reference.langchain.com/python/langgraph/pregel/_checkpoint/get_updated_channels_from_tasks"
category: "reference"
tags: [reference, langgraph, pregel, checkpoint, get_updated_channels_from_tasks]
---

# get_updated_channels_from_tasks

> **Function** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/pregel/_checkpoint/get_updated_channels_from_tasks)

Channel names written by an update_state superstep (excluding PUSH).

## Signature

```python
get_updated_channels_from_tasks(
    run_tasks: Iterable[Any],
) -> set[str]
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/644815f9e5bc52ad8f7a5227a456227e9c3e639b/libs/langgraph/langgraph/pregel/_checkpoint.py#L74)
