---
title: "get_default_model"
description: "Get the default model for Deep Agents."
source: "https://reference.langchain.com/python/deepagents/graph/get_default_model"
category: "reference"
tags: [reference, deepagents, graph, get_default_model]
---

# get_default_model

> **Function** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/graph/get_default_model)

Get the default model for Deep Agents.

!!! deprecated

    Deprecated since `0.5.3`; will be removed in `deepagents==1.0.0`.
    Construct your model explicitly (e.g.,
    `ChatAnthropic(model_name="claude-sonnet-4-6")`).

Used as a fallback when `model=None` is passed to `create_deep_agent`.

Requires `ANTHROPIC_API_KEY` to be set in the environment.

## Signature

```python
get_default_model() -> ChatAnthropic
```

## Returns

`ChatAnthropic`

`ChatAnthropic` instance configured with `claude-sonnet-4-6`.

## ⚠️ Deprecated

Deprecated since version 0.5.3. Relying on the default model is deprecated and will be removed in deepagents==1.0.0 alongside support for `model=None` in `create_deep_agent`. Construct your model explicitly (e.g., `ChatAnthropic(model_name=...)`). See https://docs.langchain.com/oss/python/deepagents/models Will be removed in version 1.0.0.

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/graph.py#L154)
