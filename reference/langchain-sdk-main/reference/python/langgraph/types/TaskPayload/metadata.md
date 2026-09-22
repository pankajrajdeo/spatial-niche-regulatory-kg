---
title: "metadata"
description: "Framework-resolved metadata associated with the task."
source: "https://reference.langchain.com/python/langgraph/types/TaskPayload/metadata"
category: "reference"
tags: [reference, langgraph, types, taskpayload, metadata]
---

# metadata

> **Attribute** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/types/TaskPayload/metadata)

Framework-resolved metadata associated with the task.

Generic dict carrier following the messages-stream pattern. Populated by
`map_debug_tasks` from `task.config["metadata"]` when non-empty, so the
same keys `stream_mode="messages"` consumers see (e.g. `lc_agent_name`,
`langgraph_node`, `langgraph_step`) are available to stream transformers.

Consumers should ignore unrecognized keys.

## Signature

```python
metadata: NotRequired[dict[str, Any]]
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/644815f9e5bc52ad8f7a5227a456227e9c3e639b/libs/langgraph/langgraph/types.py#L155)
