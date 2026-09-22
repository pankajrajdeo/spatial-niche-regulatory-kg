---
title: "get_state_history"
description: "View source on GitHub"
source: "https://reference.langchain.com/python/langgraph/pregel/protocol/PregelProtocol/get_state_history"
category: "reference"
tags: [reference, langgraph, pregel, protocol, pregelprotocol, get_state_history]
---

# get_state_history

> **Method** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/pregel/protocol/PregelProtocol/get_state_history)

## Signature

```python
get_state_history(
    self,
    config: RunnableConfig,
    *,
    filter: dict[str, Any] | None = None,
    before: RunnableConfig | None = None,
    limit: int | None = None,
) -> Iterator[StateSnapshot]
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/644815f9e5bc52ad8f7a5227a456227e9c3e639b/libs/langgraph/langgraph/pregel/protocol.py#L57)
