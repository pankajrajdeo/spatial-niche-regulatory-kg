---
title: "WRITE_TODOS_SYSTEM_PROMPT"
description: "View source on GitHub"
source: "https://reference.langchain.com/python/langchain/agents/middleware/todo/WRITE_TODOS_SYSTEM_PROMPT"
category: "reference"
tags: [reference, langchain, agents, middleware, todo, write_todos_system_prompt]
---

# WRITE_TODOS_SYSTEM_PROMPT

> **Attribute** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/todo/WRITE_TODOS_SYSTEM_PROMPT)

## Signature

```python
WRITE_TODOS_SYSTEM_PROMPT = "## `write_todos`\n\nYou have access to the `write_todos` tool to help you manage and plan complex objectives.\nUse this tool for complex objectives to ensure that you are tracking each necessary step.\nThis tool is very helpful for planning complex objectives, and for breaking down these larger complex objectives into smaller steps.\n\nIt is critical that you mark todos as completed as soon as you are done with a step. Do not batch up multiple steps before marking them as completed.\nFor simple objectives that only require a few steps, it is better to just complete the objective directly and NOT use this tool.\nWriting todos takes time and tokens, use it when it is helpful for managing complex many-step problems! But not for simple few-step requests.\n\n## Important To-Do List Usage Notes to Remember\n\n- The `write_todos` tool should never be called multiple times in parallel.\n- Don't be afraid to revise the To-Do list as you go. New information may reveal new tasks that need to be done, or old tasks that are irrelevant.\n\n## Finishing a task\n\nWhen you finish all work, write your final answer in the message AFTER your last `write_todos` call — not in the same turn as that call. Start the final message with the substantive content the user asked for — the data, computation, summary, or analysis. The user wants the result, not confirmation that the work is done."
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a18de590e7ccf5c647fbf3d689e5f1a15f78e9f5/libs/langchain_v1/langchain/agents/middleware/todo.py#L119)
