---
title: "cause"
description: "Causation edge — the tool call that triggered this subagent."
source: "https://reference.langchain.com/python/langchain/agents/_subagent_transformer/AsyncSubagentRunStream/cause"
category: "reference"
tags: [reference, langchain, agents, subagent_transformer, asyncsubagentrunstream, cause]
---

# cause

> **Attribute** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/_subagent_transformer/AsyncSubagentRunStream/cause)

Causation edge — the tool call that triggered this subagent.

Returns the `LifecycleCause` recovered by the base transformer (a
`{"type": "toolCall", "tool_call_id": ...}` dict) when the originating
tool call could be joined, else `None`.

## Signature

```python
cause: LifecycleCause | None
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a18de590e7ccf5c647fbf3d689e5f1a15f78e9f5/libs/langchain_v1/langchain/agents/_subagent_transformer.py#L110)
