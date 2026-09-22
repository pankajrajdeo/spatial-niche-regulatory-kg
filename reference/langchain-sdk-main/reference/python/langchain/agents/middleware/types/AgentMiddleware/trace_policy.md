---
title: "trace_policy"
description: "Optional trace policy for this middleware's hook spans (wrap_model_call/ wrap_tool_call and the before_/after_ node hooks)."
source: "https://reference.langchain.com/python/langchain/agents/middleware/types/AgentMiddleware/trace_policy"
category: "reference"
tags: [reference, langchain, agents, middleware, types, agentmiddleware, trace_policy]
---

# trace_policy

> **Attribute** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/types/AgentMiddleware/trace_policy)

Optional trace policy for this middleware's hook spans (`wrap_model_call`/
`wrap_tool_call` and the `before_*`/`after_*` node hooks).

By default (`None`), hook spans are traced normally. Set a `TracePolicy` to shape
what they record -- e.g. `TracePolicy(process_inputs=omit_payload)` to drop the
conversation `messages`/`state` payload while keeping the span and its timing.
Messages are still captured on the inner model-call span.

## Signature

```python
trace_policy: TracePolicy | None = None
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a18de590e7ccf5c647fbf3d689e5f1a15f78e9f5/libs/langchain_v1/langchain/agents/middleware/types.py#L403)
