---
title: "ainvoke"
description: "View source on GitHub"
source: "https://reference.langchain.com/python/langgraph/pregel/protocol/PregelProtocol/ainvoke"
category: "reference"
tags: [reference, langgraph, pregel, protocol, pregelprotocol, ainvoke]
---

# ainvoke

> **Method** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/pregel/protocol/PregelProtocol/ainvoke)

## Signature

```python
ainvoke(
    self,
    input: InputT | Command | None,
    config: RunnableConfig | None = None,
    *,
    context: ContextT | None = None,
    interrupt_before: All | Sequence[str] | None = None,
    interrupt_after: All | Sequence[str] | None = None,
    version: Literal['v1', 'v2'] = 'v1',
) -> dict[str, Any] | Any
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/644815f9e5bc52ad8f7a5227a456227e9c3e639b/libs/langgraph/langgraph/pregel/protocol.py#L259)
