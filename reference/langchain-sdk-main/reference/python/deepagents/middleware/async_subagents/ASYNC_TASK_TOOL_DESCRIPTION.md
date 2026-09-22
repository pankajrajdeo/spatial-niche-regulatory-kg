---
title: "ASYNC_TASK_TOOL_DESCRIPTION"
description: "View source on GitHub"
source: "https://reference.langchain.com/python/deepagents/middleware/async_subagents/ASYNC_TASK_TOOL_DESCRIPTION"
category: "reference"
tags: [reference, deepagents, middleware, async_subagents, async_task_tool_description]
---

# ASYNC_TASK_TOOL_DESCRIPTION

> **Attribute** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/async_subagents/ASYNC_TASK_TOOL_DESCRIPTION)

## Signature

```python
ASYNC_TASK_TOOL_DESCRIPTION = 'Start an async subagent on a remote server. The subagent runs in the background and returns a task ID immediately.\n\nAvailable async agent types:\n{available_agents}\n\n## Usage notes:\n1. This tool launches a background task and returns immediately with a task ID. Report the task ID to the user and stop — do NOT immediately check status.\n2. Use `check_async_task` only when the user asks for a status update or result.\n3. Use `update_async_task` to send new instructions to a running task.\n4. Multiple async subagents can run concurrently — launch several and let them run in the background.\n5. The subagent runs on a remote server, so it has its own tools and capabilities.'
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/middleware/async_subagents.py#L173)
