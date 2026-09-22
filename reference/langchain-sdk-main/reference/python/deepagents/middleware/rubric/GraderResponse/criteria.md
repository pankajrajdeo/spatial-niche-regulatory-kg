---
title: "criteria"
description: "View source on GitHub"
source: "https://reference.langchain.com/python/deepagents/middleware/rubric/GraderResponse/criteria"
category: "reference"
tags: [reference, deepagents, middleware, rubric, graderresponse, criteria]
---

# criteria

> **Attribute** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/rubric/GraderResponse/criteria)

## Signature

```python
criteria: list[CriterionEval] = Field(description='Per-criterion verdicts: exactly one entry for every criterion in the rubric, in rubric order. A verdict that does not account for the whole rubric is not usable, so never omit criteria or collapse several into one. Each entry carries `passed` True/False, plus a `gap` string when failing.')
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/middleware/rubric.py#L323)
