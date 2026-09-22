---
title: "before_model"
description: "Inject one-shot policy nudges before the model acts."
source: "https://reference.langchain.com/python/deepagents/profiles/harness/_nvidia_nemotron_3_ultra/NemotronPolicyNudgeMiddleware/before_model"
category: "reference"
tags: [reference, deepagents, profiles, harness, nvidia_nemotron_3_ultra, nemotronpolicynudgemiddleware, before_model]
---

# before_model

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/profiles/harness/_nvidia_nemotron_3_ultra/NemotronPolicyNudgeMiddleware/before_model)

Inject one-shot policy nudges before the model acts.

## Signature

```python
before_model(
    self,
    state: AgentState[Any],
    runtime: Runtime[Any],
) -> dict[str, Any] | None
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/profiles/harness/_nvidia_nemotron_3_ultra.py#L1344)
