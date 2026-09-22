---
title: "RubricResult"
description: "Type Alias in deepagents"
source: "https://reference.langchain.com/python/deepagents/middleware/rubric/RubricResult"
category: "reference"
tags: [reference, deepagents, middleware, rubric, rubricresult]
---

# RubricResult

> **Type Alias** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/rubric/RubricResult)

Status recorded on each evaluation.

Superset of `GraderVerdict` with two middleware-synthesized terminal
statuses the grader cannot emit itself:

- `max_iterations_reached`: the iteration cap fired on a `needs_revision`
    verdict; the agent terminates with its last response intact.
- `grader_error`: the grader sub-agent raised an exception (provider
    timeout, missing credentials, malformed structured response, etc.).

    Distinct from `failed`, which the grader returns about the *rubric*,
    not about its own machinery.

Only `needs_revision` continues the loop; every other status ends the
grading run.

## Signature

```python
RubricResult = GraderVerdict | Literal['max_iterations_reached', 'grader_error']
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/middleware/rubric.py#L75)
