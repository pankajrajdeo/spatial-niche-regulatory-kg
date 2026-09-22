---
title: "before_model"
description: "Inject entity-branch guidance before the model finalizes."
source: "https://reference.langchain.com/python/deepagents/profiles/harness/_nvidia_nemotron_3_ultra/EntityResolutionGuardMiddleware/before_model"
category: "reference"
tags: [reference, deepagents, profiles, harness, nvidia_nemotron_3_ultra, entityresolutionguardmiddleware, before_model]
---

# before_model

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/profiles/harness/_nvidia_nemotron_3_ultra/EntityResolutionGuardMiddleware/before_model)

Inject entity-branch guidance before the model finalizes.

## Signature

```python
before_model(
    self,
    state: AgentState[Any],
    runtime: Runtime[Any],
) -> dict[str, Any] | None
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/profiles/harness/_nvidia_nemotron_3_ultra.py#L1637)
