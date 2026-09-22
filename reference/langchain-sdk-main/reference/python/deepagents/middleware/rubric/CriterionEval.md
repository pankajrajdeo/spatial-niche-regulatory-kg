---
title: "CriterionEval"
description: "Per-criterion verdict."
source: "https://reference.langchain.com/python/deepagents/middleware/rubric/CriterionEval"
category: "reference"
tags: [reference, deepagents, middleware, rubric, criterioneval]
---

# CriterionEval

> **Attribute** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/rubric/CriterionEval)

Per-criterion verdict.

Discriminated union on `passed`: pass-verdicts have no `gap`; fail-verdicts
require one. `GraderResponse.model_validate` enforces the shape at the
trust boundary so a grader cannot emit `{passed: True, gap: ...}` or
`{passed: False}` with no gap.

## Signature

```python
CriterionEval = Annotated[CriterionPass | CriterionFail, Discriminator('passed')]
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/middleware/rubric.py#L206)
