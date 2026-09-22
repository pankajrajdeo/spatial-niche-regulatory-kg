---
title: "wrap_model_call"
description: "Patch request messages before ChatNVIDIA serializes them."
source: "https://reference.langchain.com/python/deepagents/profiles/harness/_nvidia_nemotron_3_ultra/ChatNVIDIAMessageCompatibilityMiddleware/wrap_model_call"
category: "reference"
tags: [reference, deepagents, profiles, harness, nvidia_nemotron_3_ultra, chatnvidiamessagecompatibilitymiddleware, wrap_model_call]
---

# wrap_model_call

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/profiles/harness/_nvidia_nemotron_3_ultra/ChatNVIDIAMessageCompatibilityMiddleware/wrap_model_call)

Patch request messages before ChatNVIDIA serializes them.

## Signature

```python
wrap_model_call(
    self,
    request: ModelRequest[Any],
    handler: Callable[[ModelRequest[Any]], ModelCallResult],
) -> ModelCallResult
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/profiles/harness/_nvidia_nemotron_3_ultra.py#L651)
