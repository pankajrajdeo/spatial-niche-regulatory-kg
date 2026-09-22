---
title: "rubric"
description: "Rubric middleware for self-evaluated agent iteration."
source: "https://reference.langchain.com/python/deepagents/middleware/rubric"
category: "reference"
tags: [reference, deepagents, middleware, rubric]
---

# rubric

> **Module** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/rubric)

Rubric middleware for self-evaluated agent iteration.

`RubricMiddleware` lets a caller declare *what done looks like* via a
rubric. Each time the agent would otherwise finish — i.e. the model
returns a response with no further tool calls — the middleware invokes a
separate grader sub-agent against the transcript. If the grader returns
`needs_revision`, its feedback is injected as a `HumanMessage` and the
agent loop resumes. Grading repeats until the grader returns `satisfied`
or `failed`, or `max_iterations` is reached.

## Properties

- `logger`
- `GraderVerdict`
- `RUBRIC_GRADER_MESSAGE_SOURCE`
- `GRADER_SYSTEM_PROMPT`
- `CriterionEval`

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/middleware/rubric.py)
