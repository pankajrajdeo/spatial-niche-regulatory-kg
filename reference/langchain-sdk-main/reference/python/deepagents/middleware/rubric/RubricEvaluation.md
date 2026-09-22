---
title: "RubricEvaluation"
description: "One grader evaluation, appended to _rubric_evaluations each iteration."
source: "https://reference.langchain.com/python/deepagents/middleware/rubric/RubricEvaluation"
category: "reference"
tags: [reference, deepagents, middleware, rubric, rubricevaluation]
---

# RubricEvaluation

> **Class** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/rubric/RubricEvaluation)

One grader evaluation, appended to `_rubric_evaluations` each iteration.

Consumers can read any field without guarding against absence since all
fields are always populated by `_build_evaluation` and
`_handle_grader_exception`.

## Signature

```python
RubricEvaluation()
```

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    grading_run_id: str,
    iteration: int,
    result: RubricResult,
    explanation: str,
    criteria: list[CriterionEval],
    unverified: bool,
)
```

| Name | Type |
|------|------|
| `grading_run_id` | `str` |
| `iteration` | `int` |
| `result` | `RubricResult` |
| `explanation` | `str` |
| `criteria` | `list[CriterionEval]` |
| `unverified` | `bool` |

## Properties

- `grading_run_id`
- `iteration`
- `result`
- `explanation`
- `criteria`
- `unverified`

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/middleware/rubric.py#L216)
