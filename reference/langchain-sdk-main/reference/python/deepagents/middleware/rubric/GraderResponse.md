---
title: "GraderResponse"
description: "Structured output the grader sub-agent must emit."
source: "https://reference.langchain.com/python/deepagents/middleware/rubric/GraderResponse"
category: "reference"
tags: [reference, deepagents, middleware, rubric, graderresponse]
---

# GraderResponse

> **Class** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/rubric/GraderResponse)

Structured output the grader sub-agent must emit.

Passed as `response_format=GraderResponse` to `create_agent` so the
underlying provider's structured output strategy is auto-selected.

## Signature

```python
GraderResponse()
```

## Extends

- `BaseModel`

## Properties

- `result`
- `explanation`
- `criteria`

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/middleware/rubric.py#L306)
