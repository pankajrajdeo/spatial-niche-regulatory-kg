---
title: "system_prompt"
description: "Instructions for the subagent. Uses an empty prompt when omitted."
source: "https://reference.langchain.com/python/deepagents/middleware/subagents/SubAgent/system_prompt"
category: "reference"
tags: [reference, deepagents, middleware, subagents, subagent, system_prompt]
---

# system_prompt

> **Attribute** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/subagents/SubAgent/system_prompt)

Instructions for the subagent. Uses an empty prompt when omitted.

Under `mode="fork"` this is appended to the inherited prompt rather than
replacing it.

## Signature

```python
system_prompt: NotRequired[str]
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/middleware/subagents.py#L202)
