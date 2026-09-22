---
title: "hitl_edited_tool_calls"
description: "Track tool call edits from after_model, so they can be used by wrap_tool_call."
source: "https://reference.langchain.com/python/langchain/agents/middleware/human_in_the_loop/_HumanInTheLoopState/hitl_edited_tool_calls"
category: "reference"
tags: [reference, langchain, agents, middleware, human_in_the_loop, humanintheloopstate, hitl_edited_tool_calls]
---

# hitl_edited_tool_calls

> **Attribute** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/human_in_the_loop/_HumanInTheLoopState/hitl_edited_tool_calls)

Track tool call edits from `after_model`, so they can be used by `wrap_tool_call`.

## Signature

```python
hitl_edited_tool_calls: NotRequired[Annotated[dict[str, Action], PrivateStateAttr]]
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a18de590e7ccf5c647fbf3d689e5f1a15f78e9f5/libs/langchain_v1/langchain/agents/middleware/human_in_the_loop.py#L236)
