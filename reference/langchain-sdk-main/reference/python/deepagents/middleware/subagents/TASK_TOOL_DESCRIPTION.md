---
title: "TASK_TOOL_DESCRIPTION"
description: "View source on GitHub"
source: "https://reference.langchain.com/python/deepagents/middleware/subagents/TASK_TOOL_DESCRIPTION"
category: "reference"
tags: [reference, deepagents, middleware, subagents, task_tool_description]
---

# TASK_TOOL_DESCRIPTION

> **Attribute** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/subagents/TASK_TOOL_DESCRIPTION)

## Signature

```python
TASK_TOOL_DESCRIPTION = "Launch an ephemeral subagent to handle a complex, multi-step task.\n\nAvailable agent types and the tools they have access to:\n{available_agents}\n\nSpecify subagent_type to select the agent. Usage notes:\n- Launch multiple agents concurrently when their tasks are independent, using a single message with multiple tool calls.\n- Each invocation is stateless by default: the agent sees only the prompt you give it and returns a single final report. Put full detail in the prompt and state exactly what it should return — unless an agent type below says it inherits your conversation instead.\n- The agent's report is not shown to the user; relay a summary yourself.\n- Tell the agent whether to create content, analyze, or only research, since it can't necessarily see the user's intent unless it inherits your conversation, as noted per agent type below.\n- If an agent's description says to use it proactively, do so without waiting to be asked.\n- When only general-purpose is available, use it for any complex, context-heavy task; it has the same capabilities as the main agent."
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/middleware/subagents.py#L426)
