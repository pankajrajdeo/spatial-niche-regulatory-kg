---
title: "unverified"
description: "Whether a satisfied verdict was downgraded because grading was incomplete."
source: "https://reference.langchain.com/python/deepagents/middleware/rubric/RubricEvaluation/unverified"
category: "reference"
tags: [reference, deepagents, middleware, rubric, rubricevaluation, unverified]
---

# unverified

> **Attribute** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/rubric/RubricEvaluation/unverified)

Whether a `satisfied` verdict was downgraded because grading was incomplete.

True when the grader twice returned a criterion count the coverage check
rejected, and `result` was rewritten away from `satisfied` as a result.
The rewrite target is `needs_revision`. On the final iteration `result` is
then rewritten again to `max_iterations_reached` while this flag stays
True, so `(max_iterations_reached, unverified=True)` is a reachable pair.

A `needs_revision` verdict that under-reports is left alone. It claims
nothing that needs blocking, so this stays False there.

## Signature

```python
unverified: bool
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/middleware/rubric.py#L243)
