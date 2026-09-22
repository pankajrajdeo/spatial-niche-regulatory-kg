---
title: "RUBRIC_GRADER_MESSAGE_SOURCE"
description: "Tag stored on synthetic revision messages this middleware injects."
source: "https://reference.langchain.com/python/deepagents/middleware/rubric/RUBRIC_GRADER_MESSAGE_SOURCE"
category: "reference"
tags: [reference, deepagents, middleware, rubric, rubric_grader_message_source]
---

# RUBRIC_GRADER_MESSAGE_SOURCE

> **Attribute** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/rubric/RUBRIC_GRADER_MESSAGE_SOURCE)

Tag stored on synthetic revision messages this middleware injects.

The revision message is injected as a `HumanMessage` (the role the model
follows most reliably), but it carries:

- `name="rubric_grader"` -- visible at the wire on providers that round-trip
    the `name` field; ignored elsewhere.
- `additional_kwargs={"lc_source": RUBRIC_GRADER_MESSAGE_SOURCE}` -- visible
    to in-process consumers (evals, UIs, observability) so they can attribute
    the turn to the grader instead of treating it as a real user message.

This follows the same convention as `SummarizationMiddleware`, which tags
its synthetic summary messages with `lc_source="summarization"`.

## Signature

```python
RUBRIC_GRADER_MESSAGE_SOURCE = 'rubric_grader'
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/middleware/rubric.py#L124)
