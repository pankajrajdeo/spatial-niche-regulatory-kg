---
title: "pre_init"
description: "Optional callable invoked with the raw model spec before initialization."
source: "https://reference.langchain.com/python/deepagents/profiles/provider/provider_profiles/ProviderProfile/pre_init"
category: "reference"
tags: [reference, deepagents, profiles, provider, provider_profiles, providerprofile, pre_init]
---

# pre_init

> **Attribute** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/profiles/provider/provider_profiles/ProviderProfile/pre_init)

Optional callable invoked with the raw model spec before initialization.

Runs before `init_kwargs_factory` is invoked and before `init_chat_model`
is called; if it raises, the factory does not run and no model is
constructed. Use for side-effectful checks that must run before
`init_chat_model` (e.g. minimum-version enforcement). Raise to abort
model construction.

## Signature

```python
pre_init: Callable[[str], None] | None = None
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/profiles/provider/provider_profiles.py#L93)
