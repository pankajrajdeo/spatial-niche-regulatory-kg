---
title: "compute_summarization_defaults"
description: "Compute default summarization settings based on model profile."
source: "https://reference.langchain.com/python/deepagents/middleware/summarization/compute_summarization_defaults"
category: "reference"
tags: [reference, deepagents, middleware, summarization, compute_summarization_defaults]
---

# compute_summarization_defaults

> **Function** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/summarization/compute_summarization_defaults)

Compute default summarization settings based on model profile.

## Signature

```python
compute_summarization_defaults(
    model: BaseChatModel,
) -> SummarizationDefaults
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `model` | `BaseChatModel` | Yes | A resolved chat model instance. |

## Returns

`SummarizationDefaults`

Default settings for trigger, keep, and truncate_args_settings.
If the model has a profile with `max_input_tokens`, uses
fraction-based settings. Otherwise, uses fixed token/message counts.

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/middleware/summarization.py#L262)
