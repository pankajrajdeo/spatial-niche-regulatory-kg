---
title: "message_log"
description: "Similar to log, this can be used to pass along extra information about what exact messages were predicted by the LLM before parsing out the (tool, tool_input)."
source: "https://reference.langchain.com/python/langchain-core/agents/AgentActionMessageLog/message_log"
category: "reference"
tags: [reference, langchain-core, agents, agentactionmessagelog, message_log]
---

# message_log

> **Attribute** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/agents/AgentActionMessageLog/message_log)

Similar to log, this can be used to pass along extra information about what exact
messages were predicted by the LLM before parsing out the `(tool, tool_input)`.

This is again useful if `(tool, tool_input)` cannot be used to fully recreate the
LLM prediction, and you need that LLM prediction (for future agent iteration).

Compared to `log`, this is useful when the underlying LLM is a chat model (and
therefore returns messages rather than a string).

## Signature

```python
message_log: Sequence[BaseMessage]
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/agents.py#L117)
